import os
import re

project_dir = r'C:\Users\repre\Documents\Mro papeleria'

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
        <article class="identity-card identity-card--featured identity-card--complete reveal">
          <img src="./assets/img/identidad-marca/identidad-completa-realista.webp" alt="Presentación fotorrealista de identidad visual completa para un negocio local" width="2000" height="1500" loading="lazy" decoding="async">
          <div class="identity-card__content">
            <h3>Identidad completa</h3>
            <p>Logotipo, colores y aplicaciones coordinadas para presentar mejor tu negocio.</p>
          </div>
          <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20cotizar%20una%20identidad%20visual%20completa%20para%20mi%20negocio." class="hidden-link" target="_blank" rel="noopener noreferrer" aria-label="Cotizar Identidad completa"></a>
        </article>

        <article class="identity-card identity-card--logo reveal">
          <img src="./assets/img/identidad-marca/logotipo-realista.webp" alt="Bocetos y presentación profesional de un logotipo para negocio local" width="1600" height="1100" loading="lazy" decoding="async">
          <div class="identity-card__content">
            <h3>Logotipo</h3>
            <p>Una imagen clara y reconocible para identificar tu negocio.</p>
          </div>
          <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20cotizar%20el%20dise%C3%B1o%20de%20un%20logotipo%20para%20mi%20negocio." class="hidden-link" target="_blank" rel="noopener noreferrer" aria-label="Cotizar Logotipo"></a>
        </article>

        <article class="identity-card identity-card--digital reveal">
          <img src="./assets/img/identidad-marca/banners-redes-realista.webp" alt="Mockups realistas de banners y publicaciones digitales para un negocio local" width="1600" height="1100" loading="lazy" decoding="async">
          <div class="identity-card__content">
            <h3>Banners y redes</h3>
            <p>Diseños coordinados para promociones, avisos y publicaciones.</p>
          </div>
          <a href="https://wa.me/527471013037?text=Hola%2C%20necesito%20banners%20y%20dise%C3%B1os%20para%20redes%20sociales." class="hidden-link" target="_blank" rel="noopener noreferrer" aria-label="Cotizar Banners y redes"></a>
        </article>

        <article class="identity-card identity-card--cards reveal">
          <img src="./assets/img/identidad-marca/tarjetas-presentacion-realistas.webp" alt="Tarjetas de presentación impresas con acabado profesional" width="1600" height="1100" loading="lazy" decoding="async">
          <div class="identity-card__content">
            <h3>Tarjetas de presentación</h3>
            <p>Una forma profesional de compartir tus datos y servicios.</p>
          </div>
          <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20cotizar%20tarjetas%20de%20presentaci%C3%B3n." class="hidden-link" target="_blank" rel="noopener noreferrer" aria-label="Cotizar Tarjetas de presentación"></a>
        </article>

        <article class="identity-card identity-card--stationery reveal">
          <img src="./assets/img/identidad-marca/papeleria-comercial-realista.webp" alt="Papelería comercial con hojas, sobres, carpetas y tarjetas coordinadas" width="1600" height="1100" loading="lazy" decoding="async">
          <div class="identity-card__content">
            <h3>Papelería comercial</h3>
            <p>Formatos y documentos que mantienen una imagen uniforme.</p>
          </div>
          <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20cotizar%20papeler%C3%ADa%20comercial%20para%20mi%20negocio." class="hidden-link" target="_blank" rel="noopener noreferrer" aria-label="Cotizar Papelería comercial"></a>
        </article>

        <article class="identity-card identity-card--promo reveal">
          <img src="./assets/img/identidad-marca/material-promocional-realista.webp" alt="Volantes, folletos, carteles y material promocional impreso" width="1600" height="1100" loading="lazy" decoding="async">
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

# Find the exact bounds of the diseno section to safely replace it
start_idx = html.find('<section id="diseno" class="business-branding">')
if start_idx != -1:
    end_idx = html.find('</section>', start_idx) + len('</section>')
    html = html[:start_idx] + new_section + html[end_idx:]
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("HTML updated securely.")
else:
    print("Could not find diseno section in HTML.")

# 2. Update CSS safely
css_path = os.path.join(project_dir, 'css', 'styles.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

new_css = """
/* Bento Grid Branding Section (New Photorealistic Layout) */
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
  border-radius: 22px;
  background: #dfe7eb;
  box-shadow: 0 22px 58px rgba(8, 37, 58, 0.18);
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
  filter: saturate(1.03) contrast(1.02);
  transition: transform 0.55s ease, filter 0.55s ease;
}

.identity-card:hover img {
  transform: scale(1.035);
  filter: saturate(1.08) contrast(1.04);
}

.identity-card::after {
  content: "";
  position: absolute;
  inset: 45% 0 0;
  background: linear-gradient(180deg, rgba(5, 25, 40, 0), rgba(5, 25, 40, 0.88) 78%, rgba(5, 25, 40, 0.96) 100%);
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

/* Individual Image Framing */
.identity-card--complete img { object-position: 50% 50%; }
.identity-card--logo img { object-position: 52% 48%; }
.identity-card--digital img { object-position: 55% 50%; }
.identity-card--cards img { object-position: 50% 55%; }
.identity-card--stationery img { object-position: 50% 48%; }
.identity-card--promo img { object-position: 50% 52%; }

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

if ".identity-showcase-section" not in css:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write("\n" + new_css)
    print("CSS updated securely.")
else:
    print("CSS already contains the new styles.")
