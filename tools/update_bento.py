import os
import re
from PIL import Image, ImageDraw, ImageFilter

project_dir = r'C:\Users\repre\Documents\Mro papeleria'
out_dir = os.path.join(project_dir, 'assets', 'img', 'identidad-marca')
os.makedirs(out_dir, exist_ok=True)

# 1. Update index.html
html_path = os.path.join(project_dir, 'index.html')
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

new_section = """<section id="diseno" class="identity-showcase-section">
  <div class="container">
    <div class="identity-showcase">
      <div class="identity-showcase__intro reveal">
        <span class="eyebrow">IDENTIDAD DE MARCA</span>
        <h2>Diseño visual para negocios locales</h2>
        <p>Creamos logotipos, banners y materiales visuales para que tu negocio tenga una imagen clara, coherente y profesional.</p>
        <ul class="identity-benefits">
          <li>Imagen más reconocible</li>
          <li>Materiales coordinados</li>
          <li>Mejor presentación</li>
          <li>Diseños para impresión y medios digitales</li>
        </ul>
        <a class="btn btn--primary" href="https://wa.me/527471013037?text=Hola%2C%20quiero%20cotizar%20una%20identidad%20visual%20para%20mi%20negocio%20con%20Mr.O%20Papeler%C3%ADa." target="_blank" rel="noopener noreferrer">Cotizar identidad visual</a>
      </div>

      <div class="identity-showcase__grid">
        <article class="identity-card identity-card--featured reveal">
          <img src="./assets/img/identidad-marca/identidad-completa.webp" alt="Identidad visual completa aplicada a un negocio local" width="2000" height="1350" loading="lazy" decoding="async">
          <div class="identity-card__content">
            <h3>Identidad completa</h3>
            <p>Logotipo, colores y aplicaciones coordinadas para presentar mejor tu negocio.</p>
          </div>
          <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20cotizar%20una%20identidad%20visual%20completa%20para%20mi%20negocio." class="hidden-link" target="_blank" rel="noopener noreferrer" aria-label="Cotizar Identidad completa"></a>
        </article>

        <article class="identity-card reveal">
          <img src="./assets/img/identidad-marca/logotipo-profesional.webp" alt="Mockup profesional de diseño de logotipo para un negocio local" width="1600" height="1000" loading="lazy" decoding="async">
          <div class="identity-card__content">
            <h3>Logotipo</h3>
            <p>Una imagen clara y reconocible para identificar tu negocio.</p>
          </div>
          <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20cotizar%20el%20dise%C3%B1o%20de%20un%20logotipo%20para%20mi%20negocio." class="hidden-link" target="_blank" rel="noopener noreferrer" aria-label="Cotizar Logotipo"></a>
        </article>

        <article class="identity-card reveal">
          <img src="./assets/img/identidad-marca/banners-redes.webp" alt="Diseños coordinados para promociones, avisos y publicaciones" width="1600" height="1000" loading="lazy" decoding="async">
          <div class="identity-card__content">
            <h3>Banners y redes</h3>
            <p>Diseños coordinados para promociones, avisos y publicaciones.</p>
          </div>
          <a href="https://wa.me/527471013037?text=Hola%2C%20necesito%20banners%20y%20dise%C3%B1os%20para%20redes%20sociales." class="hidden-link" target="_blank" rel="noopener noreferrer" aria-label="Cotizar Banners y redes"></a>
        </article>

        <article class="identity-card reveal">
          <img src="./assets/img/identidad-marca/tarjetas-profesionales.webp" alt="Tarjetas de presentación profesionales para un negocio local" width="1600" height="1000" loading="lazy" decoding="async">
          <div class="identity-card__content">
            <h3>Tarjetas de presentación</h3>
            <p>Una forma profesional de compartir tus datos y servicios.</p>
          </div>
          <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20cotizar%20tarjetas%20de%20presentaci%C3%B3n." class="hidden-link" target="_blank" rel="noopener noreferrer" aria-label="Cotizar Tarjetas de presentación"></a>
        </article>

        <article class="identity-card reveal">
          <img src="./assets/img/identidad-marca/papeleria-comercial.webp" alt="Papelería comercial con hoja membretada, sobre, carpeta y tarjeta" width="1600" height="1000" loading="lazy" decoding="async">
          <div class="identity-card__content">
            <h3>Papelería comercial</h3>
            <p>Formatos y documentos que mantienen una imagen uniforme.</p>
          </div>
          <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20cotizar%20papeler%C3%ADa%20comercial%20para%20mi%20negocio." class="hidden-link" target="_blank" rel="noopener noreferrer" aria-label="Cotizar Papelería comercial"></a>
        </article>

        <article class="identity-card reveal">
          <img src="./assets/img/identidad-marca/material-promocional.webp" alt="Material promocional impreso para un negocio local" width="1600" height="1000" loading="lazy" decoding="async">
          <div class="identity-card__content">
            <h3>Material promocional</h3>
            <p>Piezas impresas para comunicar y promocionar tu negocio.</p>
          </div>
          <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20cotizar%20material%20promocional." class="hidden-link" target="_blank" rel="noopener noreferrer" aria-label="Cotizar Material promocional"></a>
        </article>
      </div>
    </div>
  </div>
</section>"""

html = re.sub(r'<section id="diseno" class="business-branding">.*?</section>', new_section, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update CSS
css_path = os.path.join(project_dir, 'css', 'styles.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Remove old .business-branding
css = re.sub(r'\.business-branding\s*\{[^}]*\}', '', css)
css = re.sub(r'\.business-branding__layout\s*\{[^}]*\}', '', css)
css = re.sub(r'\.business-branding__intro\s*\{[^}]*\}', '', css)
css = re.sub(r'\.business-branding__grid\s*\{[^}]*\}', '', css)
css = re.sub(r'\.brand-service-card\s*\{[^}]*\}', '', css)
css = re.sub(r'\.brand-service-card:hover\s*\{[^}]*\}', '', css)
css = re.sub(r'\.brand-service-card .hidden-link\s*\{[^}]*\}', '', css)
css = re.sub(r'\.brand-service-card__media\s*\{[^}]*\}', '', css)
css = re.sub(r'\.brand-service-card__media img\s*\{[^}]*\}', '', css)
css = re.sub(r'\.brand-service-card:hover \.brand-service-card__media img\s*\{[^}]*\}', '', css)
css = re.sub(r'\.brand-service-card__body\s*\{[^}]*\}', '', css)
css = re.sub(r'\.brand-service-card__body h3\s*\{[^}]*\}', '', css)
css = re.sub(r'\.brand-service-card__body p\s*\{[^}]*\}', '', css)

new_css = """
/* Bento Grid Branding Section */
.identity-showcase-section {
  background:
    radial-gradient(circle at 90% 5%, rgba(0, 166, 200, 0.18), transparent 30%),
    radial-gradient(circle at 10% 95%, rgba(247, 178, 26, 0.10), transparent 28%),
    linear-gradient(180deg, #f8fbfd 0%, #edf4f7 100%);
  position: relative;
}

.identity-showcase-section::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image: linear-gradient(rgba(0, 0, 0, 0.02) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0, 0, 0, 0.02) 1px, transparent 1px);
  background-size: 40px 40px;
  pointer-events: none;
}

.identity-showcase {
  display: grid;
  grid-template-columns: minmax(260px, 0.75fr) minmax(0, 1.8fr);
  gap: clamp(2rem, 5vw, 5rem);
  align-items: start;
  padding-block: clamp(3rem, 6vw, 6rem);
  position: relative;
  z-index: 2;
}

.identity-showcase__intro {
  position: sticky;
  top: 7rem;
}

.eyebrow {
  display: inline-block;
  font-size: 0.85rem;
  font-weight: 800;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: #009DBA;
  margin-bottom: 0.75rem;
}

.identity-showcase__intro h2 {
  font-size: clamp(2rem, 3.5vw, 2.5rem);
  color: #07365c;
  margin-bottom: 1rem;
  line-height: 1.15;
}

.identity-showcase__intro p {
  font-size: 1.1rem;
  color: #526677;
  margin-bottom: 1.5rem;
  line-height: 1.6;
}

.identity-benefits {
  list-style: none;
  padding: 0;
  margin: 0 0 2.5rem 0;
}

.identity-benefits li {
  position: relative;
  padding-left: 1.5rem;
  margin-bottom: 0.75rem;
  color: #3b4c5c;
  font-weight: 500;
}

.identity-benefits li::before {
  content: "✓";
  position: absolute;
  left: 0;
  color: #009DBA;
  font-weight: bold;
}

.identity-showcase__grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  grid-auto-rows: minmax(220px, auto);
  gap: 1.25rem;
}

.identity-card--featured {
  grid-row: span 2;
}

.identity-card {
  position: relative;
  overflow: hidden;
  min-height: 250px;
  border-radius: 24px;
  background: #0b2135;
  box-shadow: 0 24px 65px rgba(8, 38, 58, 0.16);
  transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.4s ease;
}

.identity-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 30px 75px rgba(8, 38, 58, 0.25);
}

.identity-card img {
  width: 100%;
  height: 100%;
  min-height: inherit;
  display: block;
  object-fit: cover;
  object-position: center;
  transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1);
}

.identity-card:hover img {
  transform: scale(1.035);
}

.identity-card::after {
  content: "";
  position: absolute;
  inset: 40% 0 0;
  background: linear-gradient(180deg, rgba(5, 25, 40, 0), rgba(5, 25, 40, 0.88));
  pointer-events: none;
}

.identity-card__content {
  position: absolute;
  z-index: 2;
  left: 1.25rem;
  right: 1.25rem;
  bottom: 1.2rem;
  color: #ffffff;
  pointer-events: none;
}

.identity-card__content h3 {
  margin: 0 0 0.35rem;
  font-size: clamp(1.1rem, 2vw, 1.55rem);
  font-weight: 700;
  text-shadow: 0 2px 4px rgba(0,0,0,0.5);
}

.identity-card__content p {
  margin: 0;
  max-width: 35ch;
  color: rgba(255, 255, 255, 0.84);
  line-height: 1.45;
  font-size: 0.95rem;
  text-shadow: 0 1px 3px rgba(0,0,0,0.5);
}

.identity-card .hidden-link {
  position: absolute;
  inset: 0;
  z-index: 10;
}

@media (max-width: 960px) {
  .identity-showcase {
    grid-template-columns: 1fr;
  }
  .identity-showcase__intro {
    position: static;
  }
}

@media (max-width: 640px) {
  .identity-showcase__grid {
    grid-template-columns: 1fr;
  }
  .identity-card--featured {
    grid-row: auto;
  }
  .identity-card {
    min-height: 300px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .identity-card, .identity-card img {
    transition: none;
  }
  .identity-card:hover, .identity-card:hover img {
    transform: none;
  }
}
"""

if "identity-showcase-section" not in css:
    css += '\n' + new_css
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

# Update main.js
js_path = os.path.join(project_dir, 'js', 'main.js')
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()
js = js.replace('.brand-service-card', '.identity-card')
with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

# 3. Generate high fidelity mockups
BG_COLOR = (242, 244, 246, 255) # Light gray
BRAND_PRIMARY = (0, 157, 186, 255) # Turquesa
BRAND_SECONDARY = (247, 178, 26, 255) # Amarillo
BRAND_DARK = (11, 33, 53, 255) # Azul oscuro
PAPER_COLOR = (255, 255, 255, 255)
SHADOW_COLOR = (0, 0, 0, 45)

def create_shadow(size, offset, radius, opacity=45):
    shadow = Image.new('RGBA', (size[0] + radius*6, size[1] + radius*6), (0,0,0,0))
    draw = ImageDraw.Draw(shadow)
    draw.rectangle([radius*3, radius*3, radius*3+size[0], radius*3+size[1]], fill=(0,0,0,opacity))
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius))
    return shadow, (offset[0]-radius*3, offset[1]-radius*3)

def draw_card(img, position, size, radius=0, fill=PAPER_COLOR, shadow_radius=30, shadow_offset=(0,20), shadow_opacity=40):
    shadow, sh_pos = create_shadow(size, (position[0]+shadow_offset[0], position[1]+shadow_offset[1]), shadow_radius, shadow_opacity)
    img.alpha_composite(shadow, sh_pos)
    card = Image.new('RGBA', size, (0,0,0,0))
    draw = ImageDraw.Draw(card)
    if radius > 0:
        draw.rounded_rectangle([0, 0, size[0], size[1]], radius=radius, fill=fill)
    else:
        draw.rectangle([0, 0, size[0], size[1]], fill=fill)
    img.alpha_composite(card, position)
    return card

def draw_luma_logo(img, center, size):
    draw = ImageDraw.Draw(img)
    s = size // 2
    x, y = center
    draw.ellipse([x-s, y-s, x+s, y+s], fill=BRAND_PRIMARY)
    draw.polygon([(x, y-s), (x+s, y), (x, y+s)], fill=BRAND_SECONDARY)
    draw.rectangle([x-s//2, y+s+20, x+s//2, y+s+35], fill=BRAND_DARK)

def draw_lines(img, position, width, count, line_h=8, gap=12, color=(200,205,210,255)):
    draw = ImageDraw.Draw(img)
    x, y = position
    for i in range(count):
        w = width if i < count - 1 else int(width * 0.6)
        draw.rounded_rectangle([x, y + i*(line_h+gap), x + w, y + i*(line_h+gap) + line_h], radius=line_h//2, fill=color)

def get_base(size):
    return Image.new('RGBA', size, color=BG_COLOR)

# 1. Identidad completa (2000 x 1350)
img1 = get_base((2000, 1350))
draw_card(img1, (200, 150), (600, 400), radius=10, fill=BRAND_DARK)
draw_luma_logo(img1, (500, 300), 120)
draw_card(img1, (950, 100), (550, 800), fill=PAPER_COLOR)
draw_luma_logo(img1, (1225, 300), 80)
draw_lines(img1, (1050, 450), 350, 12)
draw_card(img1, (300, 650), (450, 280), radius=15, fill=BRAND_PRIMARY)
draw_card(img1, (450, 800), (450, 280), radius=15, fill=PAPER_COLOR)
draw_luma_logo(img1, (675, 940), 60)
draw_card(img1, (1550, 400), (350, 750), radius=45, fill=(30,30,30,255))
draw_card(img1, (1570, 420), (310, 710), radius=30, fill=PAPER_COLOR)
draw_card(img1, (1590, 450), (270, 270), radius=15, fill=BRAND_SECONDARY, shadow_opacity=0)
draw_luma_logo(img1, (1725, 585), 60)
draw_lines(img1, (1590, 750), 250, 3)
img1.convert('RGB').save(os.path.join(out_dir, 'identidad-completa.webp'), 'WEBP', quality=90)

# 2. Logotipo (1600 x 1000)
img2 = get_base((1600, 1000))
draw_card(img2, (200, 150), (700, 700), fill=PAPER_COLOR)
draw2 = ImageDraw.Draw(img2)
for i in range(200, 900, 50): draw2.line([(i, 150), (i, 850)], fill=(0,0,0, 15), width=2)
for i in range(150, 850, 50): draw2.line([(200, i), (900, i)], fill=(0,0,0, 15), width=2)
draw2.ellipse([450, 350, 650, 550], outline=BRAND_DARK, width=4)
draw2.polygon([(550, 350), (750, 450), (550, 550)], outline=BRAND_DARK, width=4)
draw_card(img2, (1000, 200), (300, 150), radius=10, fill=BRAND_PRIMARY)
draw_card(img2, (1000, 400), (300, 150), radius=10, fill=BRAND_SECONDARY)
draw_card(img2, (1000, 600), (300, 150), radius=10, fill=BRAND_DARK)
draw_card(img2, (1150, 700), (400, 400), radius=20, fill=PAPER_COLOR)
draw_luma_logo(img2, (1350, 900), 100)
img2.convert('RGB').save(os.path.join(out_dir, 'logotipo-profesional.webp'), 'WEBP', quality=90)

# 3. Banners y redes (1600 x 1000)
img3 = get_base((1600, 1000))
draw_card(img3, (200, 200), (800, 550), radius=30, fill=(30,30,30,255))
draw_card(img3, (230, 230), (740, 490), radius=15, fill=PAPER_COLOR)
draw_card(img3, (230, 230), (740, 300), radius=0, fill=BRAND_PRIMARY, shadow_opacity=0)
draw_luma_logo(img3, (600, 380), 80)
draw_lines(img3, (300, 580), 600, 4)
draw_card(img3, (1100, 150), (350, 750), radius=45, fill=(30,30,30,255))
draw_card(img3, (1120, 170), (310, 710), radius=25, fill=PAPER_COLOR)
draw_card(img3, (1140, 200), (270, 350), radius=15, fill=BRAND_SECONDARY, shadow_opacity=0)
draw_luma_logo(img3, (1275, 375), 80)
draw_lines(img3, (1140, 600), 250, 5)
img3.convert('RGB').save(os.path.join(out_dir, 'banners-redes.webp'), 'WEBP', quality=90)

# 4. Tarjetas de presentación (1600 x 1000)
img4 = get_base((1600, 1000))
draw_card(img4, (400, 200), (500, 320), radius=15, fill=BRAND_DARK)
draw_luma_logo(img4, (650, 360), 80)
draw_card(img4, (700, 450), (500, 320), radius=15, fill=PAPER_COLOR)
draw_luma_logo(img4, (800, 610), 60)
draw_lines(img4, (900, 550), 250, 4)
img4.convert('RGB').save(os.path.join(out_dir, 'tarjetas-profesionales.webp'), 'WEBP', quality=90)

# 5. Papelería comercial (1600 x 1000)
img5 = get_base((1600, 1000))
draw_card(img5, (200, 100), (600, 800), radius=10, fill=BRAND_DARK)
draw_luma_logo(img5, (500, 500), 150)
draw_card(img5, (850, 150), (550, 750), fill=PAPER_COLOR)
draw_luma_logo(img5, (1125, 300), 80)
draw_lines(img5, (950, 450), 350, 15)
draw_card(img5, (300, 650), (500, 250), fill=(245,245,245,255))
draw_luma_logo(img5, (400, 775), 50)
img5.convert('RGB').save(os.path.join(out_dir, 'papeleria-comercial.webp'), 'WEBP', quality=90)

# 6. Material promocional (1600 x 1000)
img6 = get_base((1600, 1000))
draw_card(img6, (300, 150), (280, 700), fill=(250,250,250,255))
draw_card(img6, (580, 150), (280, 700), fill=PAPER_COLOR)
draw_card(img6, (860, 150), (280, 700), fill=(245,245,245,255))
draw_card(img6, (580, 150), (280, 400), radius=0, fill=BRAND_PRIMARY, shadow_opacity=0)
draw_luma_logo(img6, (720, 350), 80)
draw_lines(img6, (620, 600), 200, 6)
draw_card(img6, (1000, 400), (400, 500), fill=BRAND_SECONDARY)
draw_luma_logo(img6, (1200, 650), 100)
img6.convert('RGB').save(os.path.join(out_dir, 'material-promocional.webp'), 'WEBP', quality=90)

# Clean up old images
old_images = ['identidad-logotipo.webp', 'identidad-tarjetas.webp', 'identidad-banners.webp', 'identidad-redes.webp', 'identidad-papeleria.webp', 'identidad-promocional.webp']
for old in old_images:
    try:
        os.remove(os.path.join(out_dir, old))
    except:
        pass

print("Bento grid and high-quality mockups updated.")
