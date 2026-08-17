#!/usr/bin/env python
"""Inject the editable text in content/*.md into the site pages.

Edit the markdown files in content/, then run:

    python build.py

(requires the `markdown` package)

Each fragment replaces the region between <!-- content:NAME --> and
<!-- /content:NAME --> markers in the page. External links (and the two
blog links) are given target="_blank" automatically.
"""
import re

import markdown

PAGES = {
    'index.html': ['about'],
    'latest-papers.html': ['paper-glow', 'paper-hankel'],
}

NEW_TAB = re.compile(r'<a href="((?:https?://|blog/|reproduce-a-paper/)[^"]+)"')
MATH = re.compile(r'\$\$.*?\$\$|\$[^$\n]+\$', re.S)


def render(name):
    """Markdown -> HTML, with TeX spans ($...$ or $$...$$) shielded from
    markdown's emphasis/underscore processing and restored verbatim
    (MathJax renders them in the browser)."""
    src = open(f'content/{name}.md').read()
    stash = []

    def shield(m):
        stash.append(m.group(0))
        return f'@@MATH{len(stash) - 1}@@'

    html = markdown.markdown(MATH.sub(shield, src))
    for i, tex in enumerate(stash):
        html = html.replace(f'@@MATH{i}@@', tex)
    return NEW_TAB.sub(
        r'<a target="_blank" rel="noopener noreferrer" href="\1"', html)


for page, names in PAGES.items():
    text = open(page).read()
    for name in names:
        begin, end = f'<!-- content:{name} -->', f'<!-- /content:{name} -->'
        region = re.compile(re.escape(begin) + r'.*?' + re.escape(end), re.S)
        if not region.search(text):
            raise SystemExit(f'{page}: markers for "{name}" not found')
        text = region.sub(lambda m: begin + '\n' + render(name) + '\n' + end,
                          text)
    open(page, 'w').write(text)
    print(f'{page}: injected {", ".join(names)}')
