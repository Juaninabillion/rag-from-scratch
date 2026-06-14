"""
Ingestion pipeline for the Google SRE Book.
Downloads chapters as HTML, cleans them, saves as markdown with metadata.
"""

import httpx
import json
from pathlib import Path
from bs4 import BeautifulSoup
from markdownify import markdownify as md


# Base URL for the SRE book
BASE_URL = "https://sre.google/sre-book"

# Output directory
DATA_DIR = Path("data")

def get_chapter_urls() -> list[dict]:
    """Fetch the table of contents and extract chapter URLs + titles."""
    url = f"{BASE_URL}/table-of-contents/"
    response = httpx.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    chapters = []
    # The TOC page has links to each chapter
    for link in soup.select("a[href]"):
        href = link.get("href", "")
        title = link.get_text(strip=True)

        # Filter to only chapter links (they start with /sre-book/)
        if href.startswith("/sre-book/") and href != "/sre-book/table-of-contents/":
            full_url = f"https://sre.google{href}"
            if full_url not in [c["url"] for c in chapters] and title:
                chapters.append({"title": title, "url": full_url})

    return chapters

def download_chapter(chapter: dict, index: int) -> None:
    """Download a single chapter, clean it, and save as markdown + metadata."""
    print(f"  [{index}] Downloading: {chapter['title']}")

    response = httpx.get(chapter["url"], follow_redirects=True)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # The main content is inside the article or main tag
    # We try a few selectors since page structure can vary
    content = (
        soup.find("article")
        or soup.find("main")
        or soup.find("div", class_="content")
    )

    if not content:
        print(f"  ⚠ Could not find content for: {chapter['title']}")
        return

    # Remove nav, footer, sidebar elements we don't want
    for tag in content.find_all(["nav", "footer", "aside", "script", "style"]):
        tag.decompose()

    # Convert the clean HTML to markdown
    markdown_text = md(str(content), heading_style="ATX", strip=["img"])

    # Clean up excessive blank lines
    lines = markdown_text.splitlines()
    cleaned_lines = []
    blank_count = 0
    for line in lines:
        if line.strip() == "":
            blank_count += 1
            if blank_count <= 2:
                cleaned_lines.append(line)
        else:
            blank_count = 0
            cleaned_lines.append(line)

    markdown_text = "\n".join(cleaned_lines).strip()

    # Create a safe filename from the URL
    slug = chapter["url"].rstrip("/").split("/")[-1]
    filename = f"{index:02d}_{slug}"

    # Save the markdown
    md_path = DATA_DIR / f"{filename}.md"
    md_path.write_text(markdown_text, encoding="utf-8")

    # Save metadata alongside it
    metadata = {
        "title": chapter["title"],
        "url": chapter["url"],
        "chapter_index": index,
        "filename": f"{filename}.md",
    }
    meta_path = DATA_DIR / f"{filename}.json"
    meta_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")


def main():
    """Run the full ingestion pipeline."""
    print("Starting SRE Book ingestion...\n")

    # Create the data directory if it doesn't exist
    DATA_DIR.mkdir(exist_ok=True)

    # Step 1: Get all chapter URLs from the table of contents
    print("Fetching table of contents...")
    chapters = get_chapter_urls()
    print(f"Found {len(chapters)} chapters.\n")

    # Step 2: Download and convert each chapter
    print("Downloading chapters...")
    for i, chapter in enumerate(chapters, start=1):
        try:
            download_chapter(chapter, i)
        except Exception as e:
            print(f"  ✗ Failed on '{chapter['title']}': {e}")

    # Step 3: Summary
    md_files = list(DATA_DIR.glob("*.md"))
    json_files = list(DATA_DIR.glob("*.json"))
    print(f"\nDone! {len(md_files)} markdown files, {len(json_files)} metadata files in {DATA_DIR}/")


if __name__ == "__main__":
    main()