# Hướng dẫn Multilogin — trình duyệt antidetect (tiếng Việt)

Repo: **multilogin-antidetect-guide** — tài liệu độc lập do cộng đồng [Anti-detect](https://github.com/Anti-detect) duy trì, **không phải** website chính thức của Multilogin.

**Ngôn ngữ khác:** [English](../../README.md) · [中文](../zh/README.md) · [Русский](../ru/README.md) · [Bahasa Indonesia](../id/README.md) · [Português](../pt/README.md) · [ไทย](../th/README.md)

---

## Giá & mã giảm giá

| Mã | Áp dụng |
|----|---------|
| **SAAS50** | Gói Multilogin (khách mới, tùy điều kiện checkout) |
| **MIN50** | **Cloud Phone** (Android thật trên cloud) |

**Link đối tác (pricing):**  
[https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

Nhập mã ở bước thanh toán trước khi trả tiền.

---

## Multilogin là gì?

**Multilogin** là **trình duyệt antidetect** / **multi-login**: mỗi **profile** tách cookies, cache và **vân tay trình duyệt** (canvas, WebGL, font, múi giờ…) để quản lý nhiều tài khoản (ads, TMĐT, social, agency) mà không “dính” chéo.

**Multilogin X** là phiên bản hiện tại: team, API local, tích hợp **Selenium / Playwright / Puppeteer**.

### Mimic & Stealthfox

| Engine | Nền | Ghi chú |
|--------|-----|---------|
| **Mimic** | Chromium | Giống Chrome, dùng cho đa số web |
| **Stealthfox** | Firefox | Đa dạng hóa so với chỉ dùng Chromium |

### Cloud Phone

Chạy **app Android thật** trên cloud (TikTok, Instagram, app ngân hàng…). Dùng mã **MIN50** khi mua gói có Cloud Phone.  
Chi tiết tiếng Anh: [cloud-phone-guide.md](../cloud-phone-guide.md)

---

## Tải & cài đặt (chính thức)

1. Mua / trial qua [link pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) ở trên.  
2. Đăng nhập dashboard khách hàng trên multilogin.com.  
3. Tải **Multilogin X** đúng bản installer từ dashboard.  
4. **Không** cài bản “crack / free full” từ GitHub lạ.

Hướng dẫn đầy đủ: [multilogin-download-install.md](../multilogin-download-install.md)

---

## So sánh nhanh

| | Multilogin | AdsPower / GoLogin / Dolphin |
|---|------------|------------------------------|
| 2 engine (Chrome + Firefox) | Có | Hầu hết chỉ Chromium |
| Cloud Phone | Có | Hạn chế hoặc khác sản phẩm |
| Giá | Cao hơn | Thường rẻ hơn / có free tier |

Bảng chi tiết: [antidetect-browser-comparison.md](../antidetect-browser-comparison.md)

---

## Automation (dev)

Luồng cơ bản: script → **Local API** (thường cổng 35000) → mở profile → Playwright/Selenium gắn vào browser đó.

Xem: [multilogin-automation.md](../multilogin-automation.md) · [examples/](../../examples/)

---

## Mục lục tiếng Anh (đầy đủ hơn)

| Tài liệu | Nội dung |
|----------|----------|
| [pricing-coupons.md](../pricing-coupons.md) | Mã **SAAS50**, **MIN50** |
| [getting-started.md](../getting-started.md) | Checklist tuần đầu |
| [faq.md](../faq.md) | FAQ mở rộng |
| [README.md](../../README.md) | Trang chính repo |

---

## Từ khóa tìm trên GitHub

`multilogin` · `multilogin-x` · `antidetect browser` · `trình duyệt antidetect` · `multilogin playwright` · `cloud phone` · `browser fingerprint`

---

**Mua & nhập mã →** [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

English: [README](../../README.md)
