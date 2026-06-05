"""
Multilogin X + Playwright — educational sketch only.

Replace API paths and auth with your official Multilogin Local API documentation.
Do not use for unauthorized scraping or account abuse.

Keywords: multilogin playwright, multilogin x api, antidetect browser automation
"""

import os

# pip install playwright requests
# playwright install  # run once on your machine

API_BASE = os.environ.get("MLX_API_BASE", "http://127.0.0.1:35000")
PROFILE_ID = os.environ.get("MLX_PROFILE_ID", "REPLACE_WITH_PROFILE_UUID")


def start_profile() -> dict:
    """Call Multilogin Local API to start a profile — shape varies by API version."""
    import requests

    # Example only — confirm path/body in official docs:
    # POST /api/v2/profile/{id}/start  (illustrative)
    url = f"{API_BASE}/profile/start"
    payload = {"profile_id": PROFILE_ID}
    headers = {"Authorization": f"Bearer {os.environ.get('MLX_TOKEN', '')}"}

    resp = requests.post(url, json=payload, headers=headers, timeout=120)
    resp.raise_for_status()
    return resp.json()


def connect_playwright(debugger_address: str):
    """Attach Playwright to browser started by Multilogin (CDP / ws endpoint)."""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        # debugger_address format depends on API response, e.g. "127.0.0.1:9222"
        browser = p.chromium.connect_over_cdp(f"http://{debugger_address}")
        context = browser.contexts[0] if browser.contexts else browser.new_context()
        page = context.new_page()
        page.goto("https://example.com", wait_until="domcontentloaded")
        print("title:", page.title())
        browser.close()


def main():
    data = start_profile()
    # Extract port or ws URL from `data` per official response schema
    debugger = data.get("debugger_address") or data.get("port")
    if not debugger:
        raise RuntimeError("No debugger endpoint in API response — check docs")
    connect_playwright(str(debugger))


if __name__ == "__main__":
    main()
