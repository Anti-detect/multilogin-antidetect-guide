# Multilogin automation — API, Playwright, Selenium

Orientation for **`multilogin automation`**, **`multilogin x api`**, **`multilogin playwright`**, **`multilogin selenium`** searches.

Requires a valid Multilogin license and the desktop app running.

**Pricing / coupons:** [partner link](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · **SAAS50** · **MIN50** (Cloud Phone)

---

## Architecture (typical)

```
Your script (Python/Node)
    → HTTP Local API (often localhost:35000)
        → Multilogin X launches profile
            → Browser exposes debugger port
                → Playwright / Selenium attaches
```

Exact endpoints and payloads change — always read **official Multilogin API docs** inside your subscription.

---

## Workflow

1. Start Multilogin X and sign in.
2. Enable **Local API** in settings (if your plan includes it).
3. `POST` / equivalent to **start profile** with `profile_id` + optional proxy flags.
4. Read response for **browser debug port** or WebDriver endpoint.
5. Connect automation library to that endpoint — **not** a fresh generic Chrome.
6. On finish: stop profile via API to free resources.

---

## Playwright (concept)

See [examples/playwright_connect.example.py](../examples/playwright_connect.example.py) for a **pseudocode-shaped** template. Replace URLs and tokens with values from your official API reference.

Keywords: `multilogin playwright python`, `multilogin connect playwright`, `antidetect playwright`.

---

## Selenium (concept)

Same pattern: start profile through API → attach to returned driver/port.  
Keywords: `multilogin selenium`, `multilogin webdriver`.

---

## Puppeteer / Node

Node clients call the same Local API with `fetch`/`axios`, then `puppeteer.connect({ browserURL })`.  
Keywords: `multilogin puppeteer`, `multilogin node api`.

---

## Practices that reduce bans

- One profile per platform account; persistent cookies.
- Residential/mobile proxy aligned with profile timezone.
- Human-like delays; avoid 24/7 robotic patterns on consumer sites.
- Comply with site ToS and applicable law.

---

## What this repo includes

| Path | Content |
|------|---------|
| [examples/](../examples/) | Educational stubs, not production bots |
| [multilogin-x-overview.md](./multilogin-x-overview.md) | Profiles & fingerprints |
| [getting-started.md](./getting-started.md) | Week-1 checklist |

We do **not** distribute account-farming kits or bypass-only malware.

---

[← Examples](../examples/README.md) · [README](../README.md)
