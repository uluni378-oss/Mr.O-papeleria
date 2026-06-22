import os
import re
import shutil

project_dir = r'C:\Users\repre\Documents\Mro papeleria'
img_dir = os.path.join(project_dir, 'assets', 'img')
os.makedirs(img_dir, exist_ok=True)

# 1. Map existing images to the new filenames
image_map = {
    'material-escolar.webp': 'collages-escolares/collage-regreso-clases-hero.webp',
    'material-oficina.webp': 'collages-escolares/collage-organizacion.webp',
    'material-creativo.webp': 'collages-escolares/collage-pegamentos-manualidades.webp',
    'regalos-novedades.webp': 'collages-escolares/collage-colores.webp',

    'impresion-documentos.webp': 'servicios-nuevos/impresiones.webp',
    'copias-documentos.webp': 'servicios-nuevos/copias-bn.webp',
    'escaneo-documentos.webp': 'servicios-nuevos/escaneo.webp',
    'tramites-digitales.webp': 'servicios-nuevos/acta-nacimiento.webp',
    'digitalizacion-archivos.webp': 'servicios-nuevos/recibo-cfe.webp',

    'diseno-logotipos.webp': '../mro-servicios/mro_01_logotipos_mockup.webp',
    'tarjetas-presentacion.webp': '../mro-servicios/mro_02_tarjetas_presentacion.webp',
    'diseno-banners.webp': '../mro-servicios/mro_03_lonas_banners.webp',
    'diseno-redes-sociales.webp': '../mro-servicios/mro_04_redes_sociales.webp',
    'diseno-impresion.webp': '../mro-servicios/mro_05_papeleria_corporativa.webp',
    'publicidad-visual.webp': '../mro-servicios/mro_06_impresos_promocionales.webp',

    'pagina-web-informativa.webp': 'paginas-web/web-showcase-01.jpg',
    'contacto-whatsapp.webp': 'paginas-web/web-showcase-03.jpg',
    'mapa-ubicacion.webp': 'ubicacion/servicios-mro.webp',

    'atencion-cliente.webp': 'hero-papeleria.webp',
    'interior-papeleria.webp': 'temporada-escolar-realista.webp',
    
    'papeleria-general.webp': 'temporada-escolar-realista.webp' # Default fallback
}

for new_name, existing_rel_path in image_map.items():
    src = os.path.join(img_dir, existing_rel_path.replace('/', os.sep))
    dst = os.path.join(img_dir, new_name)
    if os.path.exists(src):
        shutil.copy2(src, dst)
    else:
        print(f"Warning: Source {src} not found for {new_name}")

# 2. Read and update index.html
html_path = os.path.join(project_dir, 'index.html')
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Hero Image
html = re.sub(r'<img src="\./assets/img/hero-papeleria\.webp".*?>', 
              r'<img src="./assets/img/atencion-cliente.webp" alt="Atención en Mr.O Papelería" data-fallback="./assets/img/papeleria-general.webp" />', 
              html)

# Replace Category Grid
new_categories = """<div class="category-grid">
            <article class="category-card reveal service-card">
              <figure class="category-art service-card__media"><img src="./assets/img/copias-documentos.webp" alt="Copias e impresiones" loading="lazy" data-fallback="./assets/img/papeleria-general.webp" /></figure>
              <div class="category-icon">C</div>
              <h3>Copias e impresiones</h3>
              <p>Copias, impresiones y escaneo de alta calidad.</p>
            </article>
            <article class="category-card reveal service-card">
              <figure class="category-art service-card__media"><img src="./assets/img/material-escolar.webp" alt="Papelería escolar" loading="lazy" data-fallback="./assets/img/papeleria-general.webp" /></figure>
              <div class="category-icon">P</div>
              <h3>Papelería escolar</h3>
              <p>Todo para tus clases y proyectos.</p>
            </article>
            <article class="category-card reveal service-card">
              <figure class="category-art service-card__media"><img src="./assets/img/material-oficina.webp" alt="Servicios de oficina" loading="lazy" data-fallback="./assets/img/papeleria-general.webp" /></figure>
              <div class="category-icon">O</div>
              <h3>Servicios de oficina</h3>
              <p>Material de oficina y accesorios.</p>
            </article>
            <article class="category-card reveal service-card">
              <figure class="category-art service-card__media"><img src="./assets/img/diseno-impresion.webp" alt="Diseño gráfico" loading="lazy" data-fallback="./assets/img/papeleria-general.webp" /></figure>
              <div class="category-icon">D</div>
              <h3>Diseño gráfico</h3>
              <p>Lonas, tarjetas, volantes y publicidad.</p>
            </article>
            <article class="category-card reveal service-card">
              <figure class="category-art service-card__media"><img src="./assets/img/diseno-logotipos.webp" alt="Branding e Identidad de marca" loading="lazy" data-fallback="./assets/img/papeleria-general.webp" /></figure>
              <div class="category-icon">B</div>
              <h3>Branding</h3>
              <p>Identidad de marca y logotipos.</p>
            </article>
            <article class="category-card reveal service-card">
              <figure class="category-art service-card__media"><img src="./assets/img/pagina-web-informativa.webp" alt="Diseño web" loading="lazy" data-fallback="./assets/img/papeleria-general.webp" /></figure>
              <div class="category-icon">W</div>
              <h3>Diseño web</h3>
              <p>Tu negocio en línea con diseño profesional.</p>
            </article>
          </div>"""
html = re.sub(r'<div class="category-grid">.*?</div>\s*</div>\s*</section>', new_categories + '\n        </div>\n      </section>', html, flags=re.DOTALL)

# Replace Business Grid
new_business = """<div class="business-grid">
              <article class="business-card service-card">
                <figure class="service-card__media"><img src="./assets/img/diseno-logotipos.webp" width="640" height="420" loading="lazy" alt="Logotipos" data-fallback="./assets/img/papeleria-general.webp" /></figure>
                <h3>Logotipos</h3>
              </article>

              <article class="business-card service-card">
                <figure class="service-card__media"><img src="./assets/img/tarjetas-presentacion.webp" width="640" height="420" loading="lazy" alt="Tarjetas de presentación" data-fallback="./assets/img/papeleria-general.webp" /></figure>
                <h3>Tarjetas de presentación</h3>
              </article>

              <article class="business-card service-card">
                <figure class="service-card__media"><img src="./assets/img/diseno-banners.webp" width="640" height="420" loading="lazy" alt="Lonas y banners" data-fallback="./assets/img/papeleria-general.webp" /></figure>
                <h3>Lonas y banners</h3>
              </article>

              <article class="business-card service-card">
                <figure class="service-card__media"><img src="./assets/img/diseno-redes-sociales.webp" width="640" height="420" loading="lazy" alt="Redes sociales" data-fallback="./assets/img/papeleria-general.webp" /></figure>
                <h3>Redes sociales</h3>
              </article>

              <article class="business-card service-card">
                <figure class="service-card__media"><img src="./assets/img/diseno-impresion.webp" width="640" height="420" loading="lazy" alt="Papelería corporativa" data-fallback="./assets/img/papeleria-general.webp" /></figure>
                <h3>Papelería corporativa</h3>
              </article>

              <article class="business-card service-card">
                <figure class="service-card__media"><img src="./assets/img/publicidad-visual.webp" width="640" height="420" loading="lazy" alt="Impresos promocionales" data-fallback="./assets/img/papeleria-general.webp" /></figure>
                <h3>Impresos promocionales</h3>
              </article>
            </div>"""
html = re.sub(r'<div class="business-grid">.*?</div>\s*</div>\s*</div>\s*</section>', new_business + '\n          </div>\n        </div>\n      </section>', html, flags=re.DOTALL)

# Replace Web Showcase Grid
new_web = """<div class="web-gallery">
            <article class="web-gallery-card service-card">
              <figure class="service-card__media"><img src="./assets/img/pagina-web-informativa.webp" alt="Página web informativa" loading="lazy" data-fallback="./assets/img/papeleria-general.webp" /></figure>
            </article>

            <article class="web-gallery-card service-card">
              <figure class="service-card__media"><img src="./assets/img/contacto-whatsapp.webp" alt="Botón de WhatsApp y contacto" loading="lazy" data-fallback="./assets/img/papeleria-general.webp" /></figure>
            </article>

            <article class="web-gallery-card service-card">
              <figure class="service-card__media"><img src="./assets/img/mapa-ubicacion.webp" alt="Mapa y ubicación" loading="lazy" data-fallback="./assets/img/papeleria-general.webp" /></figure>
            </article>
          </div>"""
html = re.sub(r'<div class="web-gallery">.*?</div>', new_web, html, flags=re.DOTALL)

# Replace Location image
html = re.sub(r'<div class="location-visual">\s*<img\s*src="\./assets/img/ubicacion/servicios-mro\.webp".*?>\s*</div>',
              r'<div class="location-visual service-card"><figure class="service-card__media"><img src="./assets/img/interior-papeleria.webp" alt="Interior de la papelería" loading="lazy" data-fallback="./assets/img/papeleria-general.webp"></figure></div>',
              html, flags=re.DOTALL)

# Write updated HTML
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# 3. Add CSS
css_path = os.path.join(project_dir, 'css', 'styles.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

new_css = """
/* Service Card Global Styles */
.service-card__media {
  aspect-ratio: 16 / 9;
  overflow: hidden;
  background: #111827;
  margin: 0;
  padding: 0;
  display: block;
  border-radius: 12px;
}

.service-card__media img {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
  object-position: center;
  transition:
    transform 0.45s ease,
    filter 0.45s ease;
}

.service-card:hover .service-card__media img {
  transform: scale(1.035);
  filter: saturate(1.06);
}

/* Fixes for category cards that used category-art before */
.category-card .service-card__media {
  margin-bottom: 20px;
  border-radius: 12px;
}

/* Fixes for business cards that had raw imgs before */
.business-card .service-card__media {
  margin-bottom: 20px;
}
.business-card > img {
  display: none; /* In case old raw img tag leaked */
}

/* Web Showcase */
.web-gallery {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-bottom: 40px;
}

@media (max-width: 900px) {
  .web-gallery {
    grid-template-columns: 1fr;
  }
}
"""

if "service-card__media" not in css:
    css += '\n' + new_css
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

# 4. Add JS Fallback Handler
js_path = os.path.join(project_dir, 'js', 'main.js')
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

fallback_js = """
// Fallback for missing images
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('img[data-fallback]').forEach(img => {
    img.addEventListener('error', function() {
      const fallbackSrc = this.getAttribute('data-fallback');
      if (fallbackSrc && this.src !== fallbackSrc && !this.src.includes(fallbackSrc)) {
        this.src = fallbackSrc;
      }
    });
  });
});
"""

if "data-fallback" not in js:
    js += '\n' + fallback_js
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js)

print("HTML, CSS, JS, and image copies updated successfully.")
