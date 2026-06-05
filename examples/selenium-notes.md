# Multilogin + Selenium notes

Educational checklist for **`multilogin selenium`** / **`multilogin webdriver`**.

---

## Steps

1. Start **Multilogin X** and log in.
2. Start profile via **Local API** (same as Playwright flow).
3. Read API response for WebDriver URL or debugger port.
4. Attach Selenium:

```python
# Illustrative — endpoint comes from Multilogin API response
from selenium import webdriver

options = webdriver.ChromeOptions()
options.debugger_address = "127.0.0.1:9222"  # example port
driver = webdriver.Chrome(options=options)
driver.get("https://example.com")
```

5. Stop profile via API when done.

---

## Python deps

```bash
pip install selenium requests
```

Use official chromedriver pairing only if Multilogin docs require it; often you attach to an **already running** browser instead of launching vanilla Chrome.

---

## Links

- [multilogin-automation.md](../docs/multilogin-automation.md)
- [playwright_connect.example.py](./playwright_connect.example.py)
- [Pricing + SAAS50](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
