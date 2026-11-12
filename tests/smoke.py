#!/usr/bin/env python3
"""Static Razonko integrity checks, no extra dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.styles = []
        self.images = []
        self.headings = 0
        self.menus = 0
        self.mains = 0

    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        if tag == "a":
            self.links.append(attr.get("href", ""))
        if tag == "link" and attr.get("rel") == "stylesheet":
            self.styles.append(attr.get("href", ""))
        if tag == "img":
            self.images.append(attr.get("src", ""))
        if tag == "h1":
            self.headings += 1
        if tag == "details" and "mobile-menu" in attr.get("class", "").split():
            self.menus += 1
        if tag == "main":
            self.mains += 1


def resolve(page, href):
    url = urlparse(href)
    if url.scheme or url.netloc or not url.path:
        return None
    path = unquote(url.path)
    target = (page.parent / path).resolve()
    if not target.is_relative_to(ROOT):
        raise AssertionError(f"External file path in {page}: {href}")
    if target.is_dir() or path.endswith("/"):
        target /= "index.html"
    return target


def main():
    pages = list(ROOT.rglob("index.html"))
    assert len(pages) == 12, f"Expected 12 pages, found {len(pages)}"
    failures = []
    for page in pages:
        parser = Page()
        parser.feed(page.read_text(encoding="utf-8"))
        if (parser.headings, parser.mains, parser.menus) != (1, 1, 1):
            failures.append(f"{page}: missing or duplicate heading/main/mobile nav")
        expected_styles = ["styles.css", "refine.css"]
        if page == ROOT / "index.html":
            expected_styles.append("case-studies.css")
        if [Path(style).name for style in parser.styles] != expected_styles:
            failures.append(f"{page}: stylesheet order or missing case styles")
        for href in parser.links + parser.styles + parser.images:
            try:
                target = resolve(page, href)
                if target is not None and not target.is_file():
                    failures.append(f"{page}: broken link {href}")
            except AssertionError as error:
                failures.append(str(error))
    homepage = (ROOT / "index.html").read_text(encoding="utf-8")
    if homepage.count('class="case-story"') != 2:
        failures.append("Home must contain exactly two professional cases")
    if homepage.count('Esquema conceptual, no arquitectura ni captura del cliente') != 2:
        failures.append("Both conceptual diagrams must have a visible disclosure")
    if 'case-graphic case-graphic-' in homepage:
        failures.append("Old decorative illustrations have not been removed")
    assert not failures, "\n".join(failures)
    print(f"OK: {len(pages)} HTML pages, local links/assets, landmarks, case studies, disclosures and CSS order.")


if __name__ == "__main__":
    main()

