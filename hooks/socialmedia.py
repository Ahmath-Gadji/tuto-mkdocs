import re
import urllib.parse
from textwrap import dedent

x_intent = "https://x.com/intent/tweet"
fb_sharer = "https://www.facebook.com/sharer/sharer.php"
include = re.compile(r"blog/.*")


def on_page_markdown(markdown, **kwargs):
    page = kwargs["page"]
    config = kwargs["config"]

    if not include.match(page.url):
        return markdown

    # Use site_url if configured, otherwise use a placeholder or local URL
    base_url = getattr(config, "site_url", None)
    if base_url is None:
        base_url = "https://example.com/"
    if not base_url.endswith("/"):
        base_url += "/"

    page_url = base_url + page.url
    page_title = urllib.parse.quote(page.title + "\n")

    return markdown + dedent(f"""

    <div style="text-align: center;">
    <h2 style="font-weight: bold; text-decoration: underline;">Share this post!</h2>
    <p>
    <a href="{x_intent}?text={page_title}&url={page_url}" class="md-button">
    Share on <span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg></span>
    </a>
    <a href="{fb_sharer}?u={page_url}" class="md-button">
    Share on <span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg></span>
    </a>
    </p>
    </div>
    """)
