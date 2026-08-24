import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_gradient(width, height, start_color, end_color):
    """Creates a horizontal linear gradient image."""
    base = Image.new('RGBA', (width, height), start_color)
    top = Image.new('RGBA', (width, height), end_color)
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        for x in range(width):
            mask_data.append(int(255 * (x / width)))
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

def get_arabic_font(size):
    paths = [
        '/System/Library/Fonts/SFArabic.ttf',
        '/System/Library/Fonts/GeezaPro.ttc',
        '/System/Library/Fonts/Supplemental/Arial.ttf',
        '/System/Library/Fonts/Helvetica.ttc'
    ]
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()

def get_latin_font(size, bold=True):
    paths = [
        '/System/Library/Fonts/SFNS.ttf',
        '/System/Library/Fonts/SFCamera.ttf',
        '/System/Library/Fonts/Supplemental/Arial Bold.ttf',
        '/System/Library/Fonts/Supplemental/Arial.ttf'
    ]
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()

def generate_favicons():
    print("Generating Favicons...")
    # 512x512 Master Favicon
    size = 512
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Rounded purple square background
    grad = create_gradient(size, size, (124, 58, 237, 255), (107, 33, 168, 255))
    mask = Image.new('L', (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([20, 20, size-20, size-20], radius=110, fill=255)
    
    img.paste(grad, (0, 0), mask)
    
    # Draw Cw text in the center
    font = get_latin_font(230, bold=True)
    draw = ImageDraw.Draw(img)
    text = "Cw"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    tx = (size - tw) // 2 - bbox[0]
    ty = (size - th) // 2 - bbox[1] - 10
    draw.text((tx, ty), text, fill=(255, 255, 255, 255), font=font)
    
    # Save standard formats
    img.save('favicon.png', 'PNG')
    img.resize((180, 180), Image.Resampling.LANCZOS).save('apple-touch-icon.png', 'PNG')
    
    ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
    img.save('favicon.ico', format='ICO', sizes=ico_sizes)
    print("Favicons generated successfully.")

def generate_logo():
    print("Generating Logo...")
    w, h = 800, 240
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    
    # Icon (160x160)
    icon_size = 160
    icon_img = Image.new('RGBA', (icon_size, icon_size), (0, 0, 0, 0))
    grad = create_gradient(icon_size, icon_size, (124, 58, 237, 255), (107, 33, 168, 255))
    mask = Image.new('L', (icon_size, icon_size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([0, 0, icon_size, icon_size], radius=38, fill=255)
    icon_img.paste(grad, (0, 0), mask)
    
    font_cw = get_latin_font(75, bold=True)
    icon_draw = ImageDraw.Draw(icon_img)
    text = "Cw"
    bbox = icon_draw.textbbox((0, 0), text, font=font_cw)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    tx = (icon_size - tw) // 2 - bbox[0]
    ty = (icon_size - th) // 2 - bbox[1] - 4
    icon_draw.text((tx, ty), text, fill=(255, 255, 255, 255), font=font_cw)
    
    img.paste(icon_img, (40, (h - icon_size) // 2), icon_img)
    
    # Text "Cloudwa"
    draw = ImageDraw.Draw(img)
    font_title = get_latin_font(85, bold=True)
    draw.text((230, 55), "Cloudwa", fill=(36, 26, 52, 255), font=font_title)
    
    # Subtitle
    font_sub = get_latin_font(28, bold=False)
    draw.text((235, 145), "Meta Tech Partner • WhatsApp API", fill=(107, 98, 128, 255), font=font_sub)
    
    img.save('logo.png', 'PNG')
    print("Logo generated successfully.")

def generate_og_image():
    print("Generating OG Image (1200x630)...")
    w, h = 1200, 630
    
    # Background: off-white to soft purple gradient
    bg = Image.new('RGBA', (w, h), (253, 252, 255, 255))
    draw = ImageDraw.Draw(bg)
    
    # Subtle purple radial glow circles in background
    glow = Image.new('RGBA', (600, 600), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    glow_draw.ellipse([50, 50, 550, 550], fill=(244, 238, 255, 220))
    glow = glow.filter(ImageFilter.GaussianBlur(50))
    bg.paste(glow, (-100, -100), glow)
    bg.paste(glow, (w - 450, h - 450), glow)
    
    # Right side: Mascot
    if os.path.exists('cloudwa-mascot.png'):
        mascot = Image.open('cloudwa-mascot.png').convert('RGBA')
        mascot_w = 400
        mascot_h = int(mascot.height * (mascot_w / mascot.width))
        mascot_resized = mascot.resize((mascot_w, mascot_h), Image.Resampling.LANCZOS)
        
        # Mascot shadow
        shadow = Image.new('RGBA', (mascot_w, 40), (0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(shadow)
        shadow_draw.ellipse([30, 5, mascot_w - 30, 35], fill=(107, 33, 168, 60))
        shadow = shadow.filter(ImageFilter.GaussianBlur(12))
        
        bg.paste(shadow, (720, 510), shadow)
        bg.paste(mascot_resized, (720, 90), mascot_resized)
    
    # Left side: Brand, Badge, Titles
    # Logo pill
    badge = Image.new('RGBA', (320, 48), (0, 0, 0, 0))
    badge_draw = ImageDraw.Draw(badge)
    badge_draw.rounded_rectangle([0, 0, 320, 48], radius=24, fill=(244, 238, 255, 255))
    badge_draw.ellipse([18, 19, 28, 29], fill=(124, 58, 237, 255))
    font_badge = get_latin_font(20, bold=True)
    badge_draw.text((38, 12), "Meta Tech Partner الرسمي", fill=(107, 33, 168, 255), font=get_arabic_font(20))
    bg.paste(badge, (80, 80), badge)
    
    # Brand Name
    font_brand = get_latin_font(72, bold=True)
    draw.text((80, 150), "Cloudwa", fill=(36, 26, 52, 255), font=font_brand)
    
    # Heading text in Arabic
    font_h1 = get_arabic_font(44)
    draw.text((80, 240), "واتساب بيزنس API الرسمي", fill=(124, 58, 237, 255), font=font_h1)
    
    font_h2 = get_arabic_font(34)
    draw.text((80, 305), "وحلول الأتمتة الموثوقة للشركات", fill=(36, 26, 52, 255), font=font_h2)
    
    # Subtitle
    font_desc = get_arabic_font(24)
    draw.text((80, 385), "• شريك Meta الرسمي لواتساب بيزنس", fill=(107, 98, 128, 255), font=font_desc)
    draw.text((80, 425), "• رسائل جماعية وخدمة عملاء وربط CRM", fill=(107, 98, 128, 255), font=font_desc)
    draw.text((80, 465), "• خبرة +5 سنوات — مدعومين من AQuadic", fill=(107, 98, 128, 255), font=font_desc)
    
    # CTA badge
    cta = Image.new('RGBA', (260, 56), (0, 0, 0, 0))
    cta_grad = create_gradient(260, 56, (124, 58, 237, 255), (107, 33, 168, 255))
    cta_mask = Image.new('L', (260, 56), 0)
    cta_mask_draw = ImageDraw.Draw(cta_mask)
    cta_mask_draw.rounded_rectangle([0, 0, 260, 56], radius=28, fill=255)
    cta.paste(cta_grad, (0, 0), cta_mask)
    cta_draw = ImageDraw.Draw(cta)
    cta_draw.text((45, 14), "cloudwa.net", fill=(255, 255, 255, 255), font=get_latin_font(26, bold=True))
    bg.paste(cta, (80, 520), cta)
    
    # Convert RGBA to RGB for JPEG
    rgb_img = Image.new('RGB', (w, h), (255, 255, 255))
    rgb_img.paste(bg, (0, 0), bg)
    rgb_img.save('og-image.jpg', 'JPEG', quality=95)
    print("OG Image generated successfully.")

def generate_blog_heroes():
    print("Generating Blog Hero images...")
    posts = [
        {
            "slug": "farq-whatsapp-api-rasmi-wa-atamata",
            "cat": "واتساب API",
            "title": "الفرق بين واتساب API الرسمي وحل الأتمتة",
            "bg_color": ((124, 58, 237), (107, 33, 168)),
            "accent": (244, 238, 255)
        },
        {
            "slug": "roi-whatsapp-campaigns",
            "cat": "ماركتينج",
            "title": "إزاي تقيس ROI حملاتك على واتساب؟",
            "bg_color": ((79, 70, 229), (124, 58, 237)),
            "accent": (238, 242, 255)
        },
        {
            "slug": "5-akhtaa-bulk-whatsapp",
            "cat": "نصائح",
            "title": "أكتر 5 أخطاء في البلك ماسج وكيف تتجنبها",
            "bg_color": ((217, 119, 6), (180, 83, 9)),
            "accent": (254, 243, 199)
        },
        {
            "slug": "chatbot-whatsapp-meta-waqt",
            "cat": "أتمتة",
            "title": "شات بوت واتساب: متى يفيد ومتى يضر؟",
            "bg_color": ((107, 33, 168), (76, 29, 149)),
            "accent": (244, 238, 255)
        },
        {
            "slug": "meta-updates-whatsapp-2025",
            "cat": "تحديثات",
            "title": "تحديثات Meta على واتساب بيزنس في 2025",
            "bg_color": ((37, 99, 235), (29, 78, 216)),
            "accent": (219, 234, 254)
        },
        {
            "slug": "rabt-whatsapp-bil-nizam",
            "cat": "تقني",
            "title": "دليل ربط واتساب بيزنس API بأنظمة الشركات",
            "bg_color": ((13, 148, 136), (15, 118, 110)),
            "accent": (204, 251, 241)
        }
    ]
    
    w, h = 800, 450
    for p in posts:
        dir_path = os.path.join("blog", p["slug"])
        os.makedirs(dir_path, exist_ok=True)
        
        img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        grad = create_gradient(w, h, p["bg_color"][0] + (255,), p["bg_color"][1] + (255,))
        img.paste(grad, (0, 0))
        
        # Decorative circular pattern
        pattern = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        pat_draw = ImageDraw.Draw(pattern)
        pat_draw.ellipse([w-250, -100, w+150, 300], outline=(255, 255, 255, 30), width=3)
        pat_draw.ellipse([w-320, -150, w+220, 390], outline=(255, 255, 255, 20), width=2)
        pat_draw.ellipse([-80, h-200, 220, h+100], fill=(255, 255, 255, 15))
        img.paste(pattern, (0, 0), pattern)
        
        draw = ImageDraw.Draw(img)
        
        # Category Tag
        cat_w = 120
        tag = Image.new('RGBA', (cat_w, 36), (0, 0, 0, 0))
        tag_draw = ImageDraw.Draw(tag)
        tag_draw.rounded_rectangle([0, 0, cat_w, 36], radius=18, fill=p["accent"] + (240,))
        tag_draw.text((20, 8), p["cat"], fill=p["bg_color"][1] + (255,), font=get_arabic_font(18))
        img.paste(tag, (50, 50), tag)
        
        # Cloudwa Brand Mark
        draw.text((w - 160, 55), "Cloudwa", fill=(255, 255, 255, 200), font=get_latin_font(24, bold=True))
        
        # Title text
        font_title = get_arabic_font(36)
        # Split text into 2 lines if needed
        words = p["title"].split(" ")
        if len(words) > 4:
            line1 = " ".join(words[:4])
            line2 = " ".join(words[4:])
            draw.text((50, 180), line1, fill=(255, 255, 255, 255), font=font_title)
            draw.text((50, 240), line2, fill=(255, 255, 255, 255), font=font_title)
        else:
            draw.text((50, 200), p["title"], fill=(255, 255, 255, 255), font=font_title)
        
        # Footer in card
        font_foot = get_arabic_font(20)
        draw.text((50, 360), "Cloudwa Blog — أسرار وحلول واتساب بيزنس", fill=(255, 255, 255, 190), font=font_foot)
        
        out_path = os.path.join(dir_path, "hero.webp")
        img.save(out_path, "WEBP", quality=90)
        print(f"Generated: {out_path}")

if __name__ == '__main__':
    generate_favicons()
    generate_logo()
    generate_og_image()
    generate_blog_heroes()
    print("All assets generated successfully!")
