import os
import re
import urllib.request
from PIL import Image, ImageDraw
from io import BytesIO

project_dir = r'C:\Users\repre\Documents\Mro papeleria'
out_dir = os.path.join(project_dir, 'assets', 'img', 'identidad-marca')
os.makedirs(out_dir, exist_ok=True)

queries = [
    ('identidad-logotipo.webp', 'logo,sketch,design'),
    ('identidad-tarjetas.webp', 'business,cards,mockup'),
    ('identidad-banners.webp', 'advertising,banner,mockup'),
    ('identidad-redes.webp', 'smartphone,social,media'),
    ('identidad-papeleria.webp', 'branding,stationery,mockup'),
    ('identidad-promocional.webp', 'flyers,print,design')
]

for filename, query in queries:
    path = os.path.join(out_dir, filename)
    url = f"https://loremflickr.com/1600/1000/{query}/all"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            img = Image.open(BytesIO(response.read()))
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img = img.resize((1600, 1000), Image.Resampling.LANCZOS)
            img.save(path, format='WEBP', quality=88)
            print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
        img = Image.new('RGB', (1600, 1000), color='#E9F0F4')
        draw = ImageDraw.Draw(img)
        draw.rectangle([300, 200, 1300, 800], fill='#FFFFFF', outline='#D0D9DF', width=2)
        draw.rectangle([400, 300, 1200, 700], fill='#F4F7F9')
        img.save(path, format='WEBP', quality=88)

# Update HTML
html_path = os.path.join(project_dir, 'index.html')
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

new_section = """<section id="diseno" class="business-branding">
        <div class="container business-branding__layout">
          <div class="business-branding__intro reveal">
            <span class="section-kicker">IDENTIDAD DE MARCA</span>
            <h2>Diseño visual para negocios locales</h2>
            <p>Creamos logotipos, banners y piezas visuales para que tu negocio tenga una imagen clara, coherente y profesional.</p>
            <p class="business-services" style="margin-bottom: 2rem; color: #526677; font-weight: 500;">Logotipo &middot; Colores de marca &middot; Banners &middot; Tarjetas &middot; Redes sociales &middot; Material impreso</p>
            <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20cotizar%20una%20identidad%20visual%20para%20mi%20negocio%20con%20Mr.O%20Papeler%C3%ADa." target="_blank" rel="noopener noreferrer" class="btn btn--primary">Cotizar identidad visual</a>
          </div>

          <div class="business-branding__grid">
            <article class="brand-service-card reveal">
              <figure class="brand-service-card__media">
                <img
                  src="./assets/img/identidad-marca/identidad-logotipo.webp"
                  alt="Mockup profesional de diseño de logotipo para un negocio local"
                  width="1600"
                  height="1000"
                  loading="lazy"
                  decoding="async"
                >
              </figure>
              <div class="brand-service-card__body">
                <h3>Logotipo</h3>
                <p>Una imagen clara y reconocible para presentar mejor tu negocio.</p>
              </div>
              <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20informaci%C3%B3n%20para%20dise%C3%B1ar%20el%20logotipo%20de%20mi%20negocio." class="hidden-link" target="_blank" rel="noopener noreferrer" aria-label="Cotizar Logotipo"></a>
            </article>

            <article class="brand-service-card reveal">
              <figure class="brand-service-card__media">
                <img
                  src="./assets/img/identidad-marca/identidad-tarjetas.webp"
                  alt="Tarjetas de presentación impresas"
                  width="1600"
                  height="1000"
                  loading="lazy"
                  decoding="async"
                >
              </figure>
              <div class="brand-service-card__body">
                <h3>Tarjetas de presentación</h3>
                <p>Diseño limpio para compartir tus datos y servicios con confianza.</p>
              </div>
              <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20cotizar%20tarjetas%20de%20presentaci%C3%B3n." class="hidden-link" target="_blank" rel="noopener noreferrer" aria-label="Cotizar Tarjetas"></a>
            </article>

            <article class="brand-service-card reveal">
              <figure class="brand-service-card__media">
                <img
                  src="./assets/img/identidad-marca/identidad-banners.webp"
                  alt="Mockup de banners comerciales"
                  width="1600"
                  height="1000"
                  loading="lazy"
                  decoding="async"
                >
              </figure>
              <div class="brand-service-card__body">
                <h3>Banners</h3>
                <p>Piezas visuales para promociones, anuncios y comunicación de tu negocio.</p>
              </div>
              <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20cotizar%20un%20banner%20para%20mi%20negocio." class="hidden-link" target="_blank" rel="noopener noreferrer" aria-label="Cotizar Banners"></a>
            </article>

            <article class="brand-service-card reveal">
              <figure class="brand-service-card__media">
                <img
                  src="./assets/img/identidad-marca/identidad-redes.webp"
                  alt="Publicaciones para redes sociales"
                  width="1600"
                  height="1000"
                  loading="lazy"
                  decoding="async"
                >
              </figure>
              <div class="brand-service-card__body">
                <h3>Redes sociales</h3>
                <p>Diseños coordinados para promociones, avisos y servicios.</p>
              </div>
              <a href="https://wa.me/527471013037?text=Hola%2C%20necesito%20dise%C3%B1os%20para%20las%20redes%20sociales%20de%20mi%20negocio." class="hidden-link" target="_blank" rel="noopener noreferrer" aria-label="Cotizar Redes sociales"></a>
            </article>

            <article class="brand-service-card reveal">
              <figure class="brand-service-card__media">
                <img
                  src="./assets/img/identidad-marca/identidad-papeleria.webp"
                  alt="Mockup fotorrealista de papelería para negocio"
                  width="1600"
                  height="1000"
                  loading="lazy"
                  decoding="async"
                >
              </figure>
              <div class="brand-service-card__body">
                <h3>Papelería comercial</h3>
                <p>Formatos y materiales que mantienen una imagen coherente.</p>
              </div>
              <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20informaci%C3%B3n%20sobre%20papeler%C3%ADa%20comercial%20con%20la%20imagen%20de%20mi%20negocio." class="hidden-link" target="_blank" rel="noopener noreferrer" aria-label="Cotizar Papelería"></a>
            </article>

            <article class="brand-service-card reveal">
              <figure class="brand-service-card__media">
                <img
                  src="./assets/img/identidad-marca/identidad-promocional.webp"
                  alt="Material promocional"
                  width="1600"
                  height="1000"
                  loading="lazy"
                  decoding="async"
                >
              </figure>
              <div class="brand-service-card__body">
                <h3>Material promocional</h3>
                <p>Volantes, anuncios y piezas impresas para dar a conocer tu negocio.</p>
              </div>
              <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20cotizar%20material%20promocional%20para%20mi%20negocio." class="hidden-link" target="_blank" rel="noopener noreferrer" aria-label="Cotizar Material"></a>
            </article>
          </div>
        </div>
      </section>"""

html = re.sub(r'<section id="diseno" class="business-design-section">.*?</section>', new_section, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# Update CSS
css_path = os.path.join(project_dir, 'css', 'styles.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Remove old .business-design-section rules if possible
css = re.sub(r'\.business-design-section\s*\{[^}]*\}', '', css)
css = re.sub(r'\.business-design-inner\s*\{[^}]*\}', '', css)
css = re.sub(r'\.business-copy\s*\{[^}]*\}', '', css)
css = re.sub(r'\.business-assets\s*\{[^}]*\}', '', css)
css = re.sub(r'\.business-grid\s*\{[^}]*\}', '', css)
css = re.sub(r'\.business-card\s*\{[^}]*\}', '', css)
css = re.sub(r'\.business-card\s*>\s*img\s*\{[^}]*\}', '', css)
css = re.sub(r'\.business-description\s*\{[^}]*\}', '', css)
css = re.sub(r'\.btn-business\s*\{[^}]*\}', '', css)

new_css = """
/* Branding Section */
.business-branding {
  padding-block: clamp(3rem, 6vw, 6rem);
  background:
    radial-gradient(circle at 85% 15%, rgba(0, 166, 200, 0.11), transparent 30%),
    linear-gradient(180deg, #f7fafc 0%, #eef4f7 100%);
}

.business-branding__layout {
  display: grid;
  grid-template-columns: minmax(260px, 0.75fr) minmax(0, 1.75fr);
  gap: clamp(2rem, 5vw, 5rem);
  align-items: start;
}

.business-branding__intro {
  position: sticky;
  top: 7rem;
}

.business-branding__grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1.1rem;
}

.brand-service-card {
  position: relative;
  overflow: hidden;
  border-radius: 20px;
  background: #ffffff;
  border: 1px solid rgba(12, 52, 78, 0.10);
  box-shadow: 0 18px 45px rgba(9, 41, 61, 0.05);
  transition:
    transform 0.45s ease,
    box-shadow 0.45s ease;
}

.brand-service-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 26px 60px rgba(9, 41, 61, 0.12);
}

.brand-service-card .hidden-link {
  position: absolute;
  inset: 0;
  z-index: 10;
}

.brand-service-card__media {
  aspect-ratio: 8 / 5;
  overflow: hidden;
  background: #e9f0f4;
  margin: 0;
}

.brand-service-card__media img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1);
}

.brand-service-card:hover .brand-service-card__media img {
  transform: scale(1.035);
}

.brand-service-card__body {
  padding: 1.25rem 1.2rem 1.4rem;
}

.brand-service-card__body h3 {
  margin: 0 0 0.4rem;
  color: #07365c;
  font-size: clamp(1.05rem, 1.5vw, 1.15rem);
  font-weight: 800;
}

.brand-service-card__body p {
  margin: 0;
  color: #526677;
  font-size: 0.95rem;
  line-height: 1.45;
}

@media (max-width: 1024px) {
  .business-branding__layout {
    grid-template-columns: 1fr;
  }

  .business-branding__intro {
    position: static;
  }

  .business-branding__grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 640px) {
  .business-branding__grid {
    grid-template-columns: 1fr;
  }

  .brand-service-card__media {
    aspect-ratio: 16 / 10;
  }
}

@media (prefers-reduced-motion: reduce) {
  .brand-service-card {
    transition: none;
  }
  .brand-service-card:hover {
    transform: none;
    box-shadow: 0 18px 45px rgba(9, 41, 61, 0.05);
  }
  .brand-service-card__media img {
    transition: none;
  }
  .brand-service-card:hover .brand-service-card__media img {
    transform: none;
  }
}
"""

if "business-branding" not in css:
    css += '\n' + new_css
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

# Update JS to observe .brand-service-card
js_path = os.path.join(project_dir, 'js', 'main.js')
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace('.business-card', '.brand-service-card')
with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated branding section.")
