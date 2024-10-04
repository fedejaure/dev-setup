"""This module modifies GitHub-style Markdown links in MkDocs pages."""

import re

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page


def on_page_markdown(
    markdown: str, *, page: Page, config: MkDocsConfig, files: Files
) -> str | None:
    """Transforms GitHub-style markdown links to this site MkDocs-compatible format."""
    # Define a regex to match GitHub-style markdown links
    github_link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\.md\)")

    def replace_md_link(match):
        link_text = match.group(1)
        link_target = match.group(2)

        # Customize the replacement logic
        # Adjust the link to work for MkDocs
        return f"[{link_text}]({link_target.lower()}.md)"

    # Replace all matches in the page's markdown
    modified_markdown = re.sub(github_link_pattern, replace_md_link, markdown)

    return modified_markdown
