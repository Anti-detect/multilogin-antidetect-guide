# Multilogin X overview — antidetect browser profiles

**Multilogin X** is Multilogin’s current **antidetect browser** platform: many **multi-login** sessions, each with isolated storage and a coherent **browser fingerprint**.

Official pricing (partner link):  
[https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

Coupons: **`SAAS50`** (plans) · **`MIN50`** (Cloud Phone) — [details](./pricing-coupons.md)

---

## Core concepts

### Browser profile

A profile = separate user data directory + fingerprint + proxy settings. Logging into Facebook in Profile A must not leak cookies into Profile B.

### Browser fingerprint

Websites collect signals: User-Agent, screen size, WebGL vendor, canvas hash, fonts, `navigator` properties, timezone, language, etc. **Antidetect** tools tune these so each profile looks like a consistent real device, not a random mashup.

Multilogin advertises **55+ parameters**, with auto-generation based on aggregated real-device data (reduces “impossible” combinations).

### Mimic vs Stealthfox

- **Mimic** — Chromium-derived engine for Chrome-like sites.
- **Stealthfox** — Firefox-derived engine when you want non-Chromium TLS/JS behavior.

Rotating only User-Agent in normal Chrome is weak; full profile isolation is the point of **Multilogin antidetect**.

---

## Cloud Phone (mobile layer)

**Cloud Phone** runs **real Android** in the cloud for app-only platforms. Use coupon **`MIN50`** when purchasing Cloud Phone eligible plans.

Compared to desktop profiles:

| | Browser profile | Cloud Phone |
|---|-----------------|-------------|
| Best for | Web dashboards, ads managers | TikTok/IG/banking apps |
| Fingerprint | Desktop browser | Mobile hardware + apps |
| Coupon hint | **SAAS50** on plans | **MIN50** |

---

## Team & operations

- Shared folders and role-based access for agencies.
- Consistent proxy assignment per profile (residential/mobile recommended for sensitive platforms).
- Document which profile owns which account — avoids double-login bans.

---

## Automation (high level)

Multilogin X exposes a **local API** (commonly documented around port **35000**) for:

- Starting/stopping profiles
- Connecting **Selenium**, **Playwright**, or **Puppeteer** to an already launched profile

Typical GitHub searches: `multilogin playwright example`, `multilogin x api python`, `multilogin automation`.

**Practice:** automate only workflows you own; rate-limit actions; use proxies that match profile geo.

This repo does not host full bot scripts — only orientation. Official docs live on Multilogin’s site after you have a license.

---

## When Multilogin is a strong fit

- You need **both** Chromium and Firefox antidetect engines in one vendor.
- You run **web + mobile** (Cloud Phone) in one stack.
- Enterprise-style **team permissions** and long product history matter more than the cheapest per-profile dollar.

When budget dominates and you only need Chromium, compare [alternatives](./antidetect-browser-comparison.md).

---

[← Cloud Phone](./cloud-phone-guide.md) · [Download](./multilogin-download-install.md) · [Automation](./multilogin-automation.md) · [Comparison](./antidetect-browser-comparison.md) · [README](../README.md)
