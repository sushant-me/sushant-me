"""Fail if a release link in the profile README is not the latest release.

The README points each tool at its current release. That went stale silently
twice: mcp-nameguard and trajectorycheck each had a release cut afterwards and
the profile kept linking the superseded one. A profile that understates the work
is a small thing, but it is the kind of small thing nobody notices, which is
exactly what a check is for.

Reads the README, asks the API for each repository's latest release, and fails
on any of three disagreements: the visible label, the tag in the URL, or either
of those against the release that actually exists.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"
OWNER = "sushant-me"

# [v1.2.3](https://github.com/sushant-me/<repo>/releases/tag/v1.2.3)
LINK = re.compile(
    r"\[(v[0-9][0-9.]*)\]\("
    r"https://github\.com/" + re.escape(OWNER) + r"/([A-Za-z0-9_.-]+)/releases/tag/(v[0-9][0-9.]*)\)"
)


def latest_release(repo: str, token: str | None) -> str | None:
    url = f"https://api.github.com/repos/{OWNER}/{repo}/releases/latest"
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "profile-link-check",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)["tag_name"]
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return None  # no releases at all
        raise


def main() -> int:
    text = README.read_text(encoding="utf-8")
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    links = LINK.findall(text)

    if not links:
        print("no release links found - expected at least one")
        return 1

    problems = []
    for label, repo, url_tag in links:
        actual = latest_release(repo, token)
        if label != url_tag:
            problems.append(
                f"{repo}: the label says {label} but the URL points at {url_tag}"
            )
        if actual is None:
            problems.append(f"{repo}: no releases exist, but the README links {url_tag}")
        elif url_tag != actual:
            problems.append(
                f"{repo}: README links {url_tag}, but the latest release is {actual}"
            )
        else:
            print(f"ok  {repo}: {label}")

    for problem in problems:
        print(f"FAIL  {problem}")

    if problems:
        print(
            "\nUpdate the link, or cut the release the README already promises."
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
