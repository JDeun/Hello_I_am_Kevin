#!/usr/bin/env python3
"""Keep the parts of the profile that need no judgement.

Two blocks are generated, both from the arXiv API and nothing else: the papers
table and the badge counting them. Adding a paper to arXiv is the only action
required to see it here -- there is no description to write, no ordering to pick,
nothing to decide. That is the whole test for what belongs in this script.

Everything else is written by hand, on purpose. The open-source table carries
one-line descriptions, a deliberate order, and each project's own release caveat
("pre-field alpha", "before signed release"). Those are judgements, and a
judgement encoded as a string inside a generator is a config file pretending to
be a program: the day a project ships 1.0, you would edit Python instead of
editing the page. So the table stays prose, and `--audit` simply reports when a
version printed there no longer matches PyPI or GitHub. The machine says what
drifted; a person decides what to say about it.

Every source is PUBLIC -- arXiv, PyPI, the GitHub REST API. The career ledger
behind these projects is a private vault holding confidential entries, and
nothing here reads it, so automation has no path to leak one onto a public page.

Fails closed. If a call fails, the file is left exactly as it is and the exit
code is non-zero: a stale table is recoverable, a silently emptied one reads as
though the work never happened.

  (no flags)  rewrite the generated blocks
  --check     report whether they would change, write nothing (for CI)
  --audit     report versions in the hand-written table that no longer match
"""
from __future__ import annotations

import functools
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OWNER = "JDeun"
ARXIV_AUTHOR = "Cho, Yong-eun"
UA = {"User-Agent": "JDeun-profile-updater"}

# Badge palette, taken from the header banner gradient so the badges read as one set
# rather than three clashing brand colours. The sponsor badge is deliberately the
# only exception (teal) -- everything else being uniform is what makes it read as
# the call to action. Keep this in sync with the hand-written badges in the READMEs.
BADGE_LABEL_COLOR = "0f172a"
BADGE_ACCENT_COLOR = "1d4ed8"

# Audit only. Deliberately just identifiers -- no prose, no ordering, no status.
# Anything describing a project belongs in the README, where a human edits it.
AUDITED = {
    "SchemaRouter": "schemarouter",
    "Helm": "helm-agent-ops",
    "local_context": None,
}


class FetchError(RuntimeError):
    pass


def _headers(url: str) -> dict:
    h = dict(UA)
    # Unauthenticated github.com allows 60 requests an hour. The workflow's
    # built-in GITHUB_TOKEN raises that to 1000 and needs no setup.
    token = os.environ.get("GITHUB_TOKEN")
    if token and url.startswith("https://api.github.com"):
        h["Authorization"] = f"Bearer {token}"
    return h


def _get(url: str, parse: str = "json"):
    req = urllib.request.Request(url, headers=_headers(url))
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            raw = r.read()
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise FetchError(f"{url}: {exc}") from exc
    return json.loads(raw) if parse == "json" else raw


@functools.lru_cache(maxsize=None)
def arxiv_entries() -> tuple[tuple[str, str, str], ...]:
    url = ("http://export.arxiv.org/api/query?" + urllib.parse.urlencode({
        "search_query": f'au:"{ARXIV_AUTHOR}"', "max_results": "40",
        "sortBy": "submittedDate", "sortOrder": "descending"}))
    ns = {"a": "http://www.w3.org/2005/Atom"}
    try:
        root = ET.fromstring(_get(url, parse="raw"))
    except ET.ParseError as exc:
        raise FetchError(f"arXiv returned unparseable XML: {exc}") from exc
    entries = root.findall("a:entry", ns)
    if not entries:
        raise FetchError("arXiv returned no entries -- refusing to blank the table")
    return tuple(
        (" ".join(e.find("a:title", ns).text.split()),
         e.find("a:id", ns).text.rsplit("/", 1)[1].split("v")[0],
         e.find("a:published", ns).text[:7])
        for e in entries
    )


def papers_block(lang: str) -> str:
    head = (["| Paper | arXiv | Date |", "|---|---|---|"] if lang == "en"
            else ["| 논문 | arXiv | 시점 |", "|---|---|---|"])
    rows = [f"| **{t}** | [{i}](https://arxiv.org/abs/{i}) | {d} |"
            for t, i, d in arxiv_entries()]
    return "\n".join(head + rows)


def arxiv_badge(lang: str, count: int) -> str:
    # The count lives here rather than in the prose because it is derived data: a
    # fourth paper used to update the table while leaving a hardcoded "3" in the
    # badge, which is the stale-number failure this script exists to prevent.
    label = f"{count} sole-author papers" if lang == "en" else f"단독저자 {count}편"
    quoted = urllib.parse.quote(label).replace("-", "--")
    return (
        '    <a href="https://arxiv.org/search/?searchtype=author&query=Yong-eun+Cho" target="_blank">\n'
        f'      <img src="https://img.shields.io/badge/arXiv-{quoted}-{BADGE_ACCENT_COLOR}'
        f'?style=for-the-badge&labelColor={BADGE_LABEL_COLOR}&logo=arxiv&logoColor=white" alt="arXiv" />\n'
        "    </a>"
    )


def replace_block(text: str, name: str, body: str) -> str:
    start, end = f"<!-- {name} starts -->", f"<!-- {name} ends -->"
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    if not pattern.search(text):
        raise FetchError(f"marker pair '{name}' not found")
    return pattern.sub(f"{start}\n{body}\n{end}", text)


def live_version(repo: str, pypi: str | None) -> str:
    if pypi:
        return _get(f"https://pypi.org/pypi/{pypi}/json")["info"]["version"]
    rels = _get(f"https://api.github.com/repos/{OWNER}/{repo}/releases?per_page=1")
    return rels[0]["tag_name"].lstrip("v") if rels else ""


def audit() -> int:
    """Report versions the page claims that the world no longer agrees with."""
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    drift = []
    for repo, pypi in AUDITED.items():
        row = next((ln for ln in text.splitlines() if f"/{repo})" in ln and ln.startswith("|")), None)
        if row is None:
            drift.append(f"{repo}: no row found in README.md")
            continue
        claimed = re.search(r"\*\*v([0-9][^*]*)\*\*", row)
        live = live_version(repo, pypi)
        if not claimed:
            drift.append(f"{repo}: row states no version, live is {live}")
        elif claimed.group(1) != live:
            drift.append(f"{repo}: README says v{claimed.group(1)}, live is v{live}")
    if drift:
        print("version drift -- update the table by hand:", file=sys.stderr)
        for d in drift:
            print(f"  {d}", file=sys.stderr)
        return 1
    print("versions match")
    return 0


def main(argv: list[str]) -> int:
    try:
        if "--audit" in argv:
            return audit()
        check = "--check" in argv
        n = len(arxiv_entries())
        blocks = {lang: {"papers": papers_block(lang), "arxiv-badge": arxiv_badge(lang, n)}
                  for lang in ("en", "ko")}
    except FetchError as exc:
        print(f"aborted, files untouched: {exc}", file=sys.stderr)
        return 1

    changed = []
    for lang, fname in (("en", "README.md"), ("ko", "README.ko.md")):
        path = ROOT / fname
        before = path.read_text(encoding="utf-8")
        after = before
        for name, body in blocks[lang].items():
            after = replace_block(after, name, body)
        if after != before:
            changed.append(fname)
            if not check:
                path.write_text(after, encoding="utf-8")

    if check:
        print("stale: " + ", ".join(changed) if changed else "up to date")
        return 1 if changed else 0
    print("updated: " + ", ".join(changed) if changed else "already up to date")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
