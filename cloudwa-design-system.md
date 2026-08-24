# Cloudwa — Design System & Brand Schema
> استخدم هذا الملف كـ reference في أي prompt جديد

---

## 🎨 Color Palette

```css
/* Primary Brand Colors */
--color-primary:      #7c3aed;   /* Purple 600 — CTA buttons, links, accents */
--color-primary-deep: #6b21a8;   /* Purple 700 — hover states, dark accents */
--color-primary-soft: #f4eeff;   /* Purple 50  — section backgrounds, badges */
--color-line:         #e6dbfb;   /* Purple 100 — borders, dividers */
--color-cloud:        #fdfcff;   /* Off-white  — page background */

/* Text Colors */
--color-ink:          #241a34;   /* Dark purple-black — headings, body */
--color-muted:        #6b6280;   /* Muted purple-gray — subtitles, captions */

/* Semantic (unchanged) */
--color-success:      #16a34a;
--color-warning:      #d97706;
--color-error:        #dc2626;
```

**Hex Quick Reference:**
| Role | Hex | Usage |
|------|-----|-------|
| Brand Purple | `#7c3aed` | Buttons, icons, highlights |
| Deep Purple | `#6b21a8` | Gradients end, hover |
| Soft Lavender | `#f4eeff` | Section bg, card bg |
| Purple Border | `#e6dbfb` | Dividers, card borders |
| Page BG | `#fdfcff` | Body background |
| Ink | `#241a34` | All headings + body text |
| Muted | `#6b6280` | Subtitles, descriptions |

**Brand Gradient:**
```css
background: linear-gradient(to left, #7c3aed, #6b21a8);
/* Used on: primary CTA buttons, hero cards, final CTA section */
```

---

## 🔤 Typography

### Font Families
```css
--font-heading: "El Messiri", "Tajawal", sans-serif;
--font-body:    "Tajawal", "El Messiri", sans-serif;

/* Google Fonts import */
@import url('https://fonts.googleapis.com/css2?family=El+Messiri:wght@500;600;700&family=Tajawal:wght@400;500;700;900&display=swap');
```

### Type Scale
| Element | Font | Weight | Size | Usage |
|---------|------|--------|------|-------|
| H1 | El Messiri | 700 | 40–48px (2.5–3rem) | Hero headline |
| H2 | El Messiri | 700 | 30–36px | Section titles |
| H3 | El Messiri | 700 | 20–24px | Card titles, subsections |
| Body Large | Tajawal | 400 | 18px | Hero description |
| Body | Tajawal | 400 | 16px | General text |
| Small / Caption | Tajawal | 400 | 14px | Labels, meta |
| Badge / Tag | Tajawal | 700 | 12–13px | Pills, badges |

### Heading Gradient (Signature Style)
```css
/* Applied to the accent part of H1 */
background: linear-gradient(to left, #7c3aed, #6b21a8);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
background-clip: text;
```

---

## 📐 Spacing & Layout

```css
/* Container */
max-width: 1152px; /* max-w-6xl */
padding: 0 24px;   /* px-6 */

/* Section Padding */
padding-block: 80px 112px;  /* py-20 md:py-28 */

/* Border Radius Scale */
--radius-sm:  16px;  /* small cards */
--radius-md:  24px;  /* rounded-[2rem] — service cards */
--radius-lg:  40px;  /* rounded-[2.5rem] — CTA section */
--radius-pill: 9999px; /* buttons, badges */

/* Card Padding */
padding: 32px 40px; /* p-8 md:p-10 */
```

---

## 🧩 Components

### Primary Button (CTA)
```html
<a class="btn-primary" href="...">
  تواصل معنا على واتساب
</a>

<style>
.btn-primary {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  border-radius: 9999px;
  background: linear-gradient(to left, #7c3aed, #6b21a8);
  color: #fff;
  font-family: "Tajawal", sans-serif;
  font-weight: 700;
  padding: 14px 28px;
  font-size: 16px;
  box-shadow: 0 12px 30px -10px rgba(124,58,237,.55);
  transition: opacity .2s;
  text-decoration: none;
}
.btn-primary:hover { opacity: .9; }
</style>
```

### Secondary Button (Outline)
```html
<a class="btn-secondary" href="...">تواصل معنا</a>

<style>
.btn-secondary {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  border-radius: 9999px;
  border: 1px solid #e6dbfb;
  padding: 10px 20px;
  font-size: 14px;
  font-weight: 700;
  color: #6b21a8;
  background: transparent;
  transition: background .2s;
  text-decoration: none;
}
.btn-secondary:hover { background: #f4eeff; }
</style>
```

### Badge / Pill
```html
<span class="badge">Meta Tech Partner الرسمي</span>

<style>
.badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  border-radius: 9999px;
  background: #f4eeff;
  color: #6b21a8;
  font-size: 12px;
  font-weight: 700;
  padding: 6px 16px;
}
/* Dot accent */
.badge::before {
  content: '';
  display: block;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #7c3aed;
}
</style>
```

### Service Card (Primary — Dark)
```html
<div class="card-primary">
  <!-- gradient purple card -->
</div>

<style>
.card-primary {
  border-radius: 32px;
  background: linear-gradient(135deg, #7c3aed, #6b21a8);
  padding: 40px;
  color: #fff;
  box-shadow: 0 25px 50px -12px rgba(107,33,168,.2);
}
</style>
```

### Service Card (Secondary — White)
```html
<div class="card-secondary">...</div>

<style>
.card-secondary {
  border-radius: 32px;
  background: #fff;
  border: 1px solid #e6dbfb;
  padding: 40px;
  box-shadow: 0 20px 25px -5px rgba(107,33,168,.05);
}
</style>
```

### Icon Container
```html
<div class="icon-wrap">
  <!-- SVG Icon -->
</div>

<style>
.icon-wrap {
  width: 56px;
  height: 56px;
  border-radius: 16px;
  background: #f4eeff;
  display: flex;
  align-items: center;
  justify-content: center;
  /* Icon color: #6b21a8, size: 24px, stroke-width: 1.8 */
}
</style>
```

---

## ✨ Animations

```css
/* Floating mascot */
@keyframes float-soft {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50%       { transform: translateY(-14px) rotate(-1deg); }
}
.float-anim { animation: float-soft 6s ease-in-out infinite; }

/* Background blob drift */
@keyframes drift {
  0%   { transform: translateX(0px); }
  50%  { transform: translateX(18px); }
  100% { transform: translateX(0px); }
}
.drift-anim { animation: drift 10s ease-in-out infinite; }

/* Scroll reveal */
.reveal {
  opacity: 0;
  transform: translateY(18px);
  transition: opacity .8s ease, transform .8s ease;
}
.reveal.in { opacity: 1; transform: translateY(0); }

/* Reduced motion */
@media (prefers-reduced-motion: reduce) {
  .float-anim, .drift-anim { animation: none; }
  .reveal { opacity: 1; transform: none; transition: none; }
}
```

### Scroll Reveal JS
```javascript
const revealEls = document.querySelectorAll('.reveal');
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('in');
      io.unobserve(e.target);
    }
  });
}, { threshold: 0.15 });
revealEls.forEach(el => io.observe(el));
```

---

## 🌊 Section Dividers (Cloud SVG)

### Top → Soft Lavender
```html
<div class="relative -mt-1" aria-hidden="true">
  <svg viewBox="0 0 1440 100" class="w-full h-auto" preserveAspectRatio="none">
    <path fill="#f4eeff" d="M0,60 C240,110 480,10 720,40 C960,70 1200,110 1440,50 L1440,100 L0,100 Z"/>
  </svg>
</div>
```

### Soft Lavender → White
```html
<div class="relative bg-[#f4eeff]" aria-hidden="true">
  <svg viewBox="0 0 1440 80" class="w-full h-auto" preserveAspectRatio="none">
    <path fill="#fdfcff" d="M0,40 C240,0 480,80 720,45 C960,10 1200,60 1440,30 L1440,80 L0,80 Z"/>
  </svg>
</div>
```

---

## 📰 Blog Section — HTML Structure

```html
<!-- Blog Post Card -->
<article class="blog-card">
  <a href="/blog/[slug]">
    <div class="blog-img">
      <img src="..." alt="..." loading="lazy">
      <span class="blog-cat">واتساب API</span>
    </div>
    <div class="blog-body">
      <div class="blog-meta">
        <span>12 يناير 2025</span>
        <span>•</span>
        <span>5 دقائق قراءة</span>
      </div>
      <h3 class="blog-title">عنوان المقالة هنا</h3>
      <p class="blog-excerpt">وصف مختصر للمحتوى في سطرين...</p>
      <span class="blog-read-more">اقرأ المقالة ←</span>
    </div>
  </a>
</article>

<style>
.blog-card {
  border-radius: 24px;
  background: #fff;
  border: 1px solid #e6dbfb;
  overflow: hidden;
  transition: box-shadow .3s, transform .3s;
}
.blog-card:hover {
  box-shadow: 0 20px 40px -10px rgba(107,33,168,.15);
  transform: translateY(-4px);
}
.blog-img { position: relative; aspect-ratio: 16/9; overflow: hidden; }
.blog-img img { width: 100%; height: 100%; object-fit: cover; }
.blog-cat {
  position: absolute; top: 12px; right: 12px;
  background: #7c3aed; color: #fff;
  font-size: 12px; font-weight: 700;
  padding: 4px 12px; border-radius: 9999px;
}
.blog-body { padding: 24px; }
.blog-meta { font-size: 13px; color: #6b6280; display: flex; gap: 8px; margin-bottom: 12px; }
.blog-title { font-family: "El Messiri", sans-serif; font-weight: 700; font-size: 18px; color: #241a34; margin-bottom: 10px; line-height: 1.5; }
.blog-excerpt { font-size: 14px; color: #6b6280; line-height: 1.8; margin-bottom: 16px; }
.blog-read-more { font-size: 14px; font-weight: 700; color: #7c3aed; }
</style>
```

---

## 🔍 SEO — On-Page Essentials

```html
<head>
  <!-- Primary Meta -->
  <title>عنوان المقالة — Cloudwa | واتساب بيزنس API</title>
  <meta name="description" content="وصف من 150-160 حرف يتضمن الكلمة المفتاحية الرئيسية"/>
  <meta name="robots" content="index, follow"/>
  <link rel="canonical" href="https://cloudwa.net/blog/[slug]"/>

  <!-- Open Graph (Facebook / WhatsApp preview) -->
  <meta property="og:type"        content="article"/>
  <meta property="og:title"       content="عنوان المقالة"/>
  <meta property="og:description" content="وصف قصير"/>
  <meta property="og:image"       content="https://cloudwa.net/blog/[slug]/og-image.jpg"/>
  <!-- OG Image: 1200×630px -->
  <meta property="og:url"         content="https://cloudwa.net/blog/[slug]"/>
  <meta property="og:site_name"   content="Cloudwa"/>
  <meta property="og:locale"      content="ar_EG"/>

  <!-- Twitter Card -->
  <meta name="twitter:card"        content="summary_large_image"/>
  <meta name="twitter:title"       content="عنوان المقالة"/>
  <meta name="twitter:description" content="وصف قصير"/>
  <meta name="twitter:image"       content="https://cloudwa.net/blog/[slug]/og-image.jpg"/>

  <!-- Article Schema (JSON-LD) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "عنوان المقالة",
    "description": "وصف المقالة",
    "image": "https://cloudwa.net/blog/[slug]/og-image.jpg",
    "datePublished": "2025-01-12T08:00:00+02:00",
    "dateModified": "2025-01-12T08:00:00+02:00",
    "author": {
      "@type": "Organization",
      "name": "Cloudwa",
      "url": "https://cloudwa.net"
    },
    "publisher": {
      "@type": "Organization",
      "name": "Cloudwa",
      "logo": {
        "@type": "ImageObject",
        "url": "https://cloudwa.net/logo.png"
      }
    },
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": "https://cloudwa.net/blog/[slug]"
    }
  }
  </script>

  <!-- BreadcrumbList Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "name": "الرئيسية", "item": "https://cloudwa.net" },
      { "@type": "ListItem", "position": 2, "name": "المدونة",  "item": "https://cloudwa.net/blog" },
      { "@type": "ListItem", "position": 3, "name": "عنوان المقالة" }
    ]
  }
  </script>
</head>
```

---

## 📊 Tracking Pixels

### Facebook Pixel
```html
<!-- Facebook Pixel — ضع في <head> -->
<script>
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}
(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');

fbq('init', 'YOUR_PIXEL_ID');   // ← ضع Pixel ID هنا
fbq('track', 'PageView');
</script>
<noscript>
  <img height="1" width="1" style="display:none"
    src="https://www.facebook.com/tr?id=YOUR_PIXEL_ID&ev=PageView&noscript=1"/>
</noscript>

<!-- Custom Events — اضبطهم على أزرار CTA -->
<script>
// عند ضغط زر "تواصل معنا"
fbq('track', 'Contact');

// عند قراءة مقال كامل (70% scroll)
fbq('track', 'ViewContent', {
  content_name: 'Blog Article',
  content_category: 'WhatsApp Business'
});

// Lead إذا كان فيه فورم
fbq('track', 'Lead');
</script>
```

### TikTok Pixel
```html
<!-- TikTok Pixel — ضع في <head> -->
<script>
!function (w, d, t) {
  w.TiktokAnalyticsObject=t;var ttq=w[t]=w[t]||[];ttq.methods=["page","track",
  "identify","instances","debug","on","off","once","ready","alias","group",
  "enableCookie","disableCookie","holdConsent","revokeConsent","grantConsent"];
  ttq.setAndDefer=function(t,e){t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}};
  for(var i=0;i<ttq.methods.length;i++)ttq.setAndDefer(ttq,ttq.methods[i]);
  ttq.instance=function(t){for(var e=ttq._i[t]||[],n=0;n<ttq.methods.length;n++)ttq.setAndDefer(e,ttq.methods[n]);return e};
  ttq.load=function(e,n){var r="https://analytics.tiktok.com/i18n/pixel/events.js",o=n&&n.partner;
  ttq._i=ttq._i||{};ttq._i[e]=[];ttq._i[e]._u=r;ttq._t=ttq._t||{};ttq._t[e]=+new Date;
  ttq._o=ttq._o||{};ttq._o[e]=n||{};n=document.createElement("script");
  n.type="text/javascript";n.async=!0;n.src=r+"?sdkid="+e+"&lib="+t;
  e=document.getElementsByTagName("script")[0];e.parentNode.insertBefore(n,e)};
  ttq.load('YOUR_TIKTOK_PIXEL_ID');  // ← ضع TikTok Pixel ID هنا
  ttq.page();
}(window, document, 'ttq');
</script>

<!-- Custom TikTok Events -->
<script>
// عند ضغط CTA
ttq.track('Contact');

// عند مشاهدة صفحة مقال
ttq.track('ViewContent', {
  content_name: 'Blog Article',
  content_type: 'article'
});
</script>
```

### Google Firebase / Analytics (GA4)
```html
<!-- Google tag (gtag.js) — ضع في <head> -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');   // ← ضع Measurement ID هنا
</script>

<!-- Custom GA4 Events -->
<script>
// CTA Click
gtag('event', 'cta_click', {
  event_category: 'engagement',
  event_label: 'whatsapp_contact',
  value: 1
});

// Blog Article Read (اتحسب بـ scroll depth)
gtag('event', 'article_read', {
  event_category: 'blog',
  event_label: document.title
});

// Scroll depth tracking — 25%, 50%, 75%, 100%
const depths = [25, 50, 75, 100];
const fired = new Set();
window.addEventListener('scroll', () => {
  const pct = Math.round(
    (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100
  );
  depths.forEach(d => {
    if (pct >= d && !fired.has(d)) {
      fired.add(d);
      gtag('event', 'scroll', { percent_scrolled: d });
    }
  });
});
</script>
```

---

## 📁 File Naming Convention (Blog)

```
/blog/
  index.html                    ← قائمة المقالات
  [category]/
    [slug]/
      index.html                ← المقالة
      og-image.jpg              ← 1200×630px
      hero.webp                 ← 1600×900px
```

**Slug format:** `whatsapp-api-vs-automation-ar` (Arabic content, Latin slug for URLs)

---

## 🎯 Brand Voice (للمحتوى)

- **اللهجة:** مصري محترم — مش رسمي جداً، مش عامي جداً
- **النبرة:** واثق، بسيط، عملي — "بنحل مشاكل حقيقية"
- **تجنب:** الكلام التقني الزيادة في العناوين، المبالغة في الوعود
- **استخدم:** أمثلة واقعية، أرقام، قصص عملاء

---

*Generated for Cloudwa — Powered by AQuadic*
