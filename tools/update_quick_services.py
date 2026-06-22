import os
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

project_dir = r'C:\Users\repre\Documents\Mro papeleria'
img_dir = os.path.join(project_dir, 'assets', 'img', 'servicios-rapidos')
os.makedirs(img_dir, exist_ok=True)

images = {
    "copias-blanco-negro.webp": "Professional photocopier, black and white documents stacked, sharp monochromatic print, clean commercial counter. Photorealistic, well-lit, commercial photography.",
    "copias-color.webp": "Color printer with pages coming out showing colorful charts and photos, real vibrant colors, clean commercial environment. Photorealistic, crisp.",
    "impresion-documentos.webp": "Printed PDF documents on a tidy desk with a modern computer monitor in background, school or office printing, photorealistic commercial photography.",
    "escaneo-documentos.webp": "Document placed on a flatbed scanner bed, scanning light visible, computer screen showing digital file in background, clean photorealistic.",
    "actas-nacimiento.webp": "Generic official looking certificate document being printed, blurred text, computer monitor in background, professional commercial lighting, photorealistic.",
    "curp-documento.webp": "Generic printed ID form or document, blurred fields, computer screen showing a database consultation, clean commercial photorealistic.",
    "recibo-cfe.webp": "Generic utility electricity bill being printed, blurred data, clean office environment, photorealistic commercial photography.",
    "talones-issste.webp": "Generic payroll stub or receipt document, blurred sensitive information, computer and printer in background, photorealistic.",
    "engargolado.webp": "Wire binding machine binding a document, transparent cover, black spiral ring, finished bound notebook, commercial photorealistic.",
    "enmicado.webp": "Laminating machine processing a document, shiny clear plastic lamination, clean finish, commercial photorealistic.",
    "impresion-planos.webp": "Large format printer printing an architectural blueprint, generic technical lines, roll of wide paper, photorealistic.",
    "mas-servicios.webp": "Various stationery items, a USB drive, neatly arranged folders, printed documents and a modern computer, clean desk, photorealistic commercial."
}

def download_image(filename, prompt):
    path = os.path.join(img_dir, filename)
    if os.path.exists(path):
        print(f"Already exists: {filename}")
        return
    url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote(prompt)}?width=1200&height=800&nologo=true&model=flux"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as response:
            with open(path, 'wb') as f:
                f.write(response.read())
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Failed {filename}: {e}")

print("Downloading 12 images...")
with ThreadPoolExecutor(max_workers=4) as executor:
    for filename, prompt in images.items():
        executor.submit(download_image, filename, prompt)


# HTML REPLACEMENT
html_path = os.path.join(project_dir, 'index.html')
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

new_html = """<section class="quick-services">
  <div class="quick-services__container">
    <div class="quick-services__intro">
      <span class="quick-kicker eyebrow" style="font-weight: 700; color: #009DBA; display: block; margin-bottom: 0.5rem; letter-spacing: 0.1em; font-size: 0.85rem;">IMPRESIÓN Y DOCUMENTOS</span>
      <h2 style="font-size: clamp(2.2rem, 3.5vw, 3rem); color: #07365c; line-height: 1.1; margin-bottom: 1rem;">Servicios rápidos</h2>
      <p style="color: #526677; font-size: 1.05rem; line-height: 1.5; margin-bottom: 1.5rem;">Resuelve en un solo lugar tus copias, impresiones, escaneos, documentos y acabados para escuela, trabajo o trámites.</p>
      
      <ul style="list-style: none; padding: 0; margin: 0 0 2rem; color: #526677; font-size: 0.95rem;">
        <li style="margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;"><span style="color: #009DBA;">✓</span> Atención directa.</li>
        <li style="margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;"><span style="color: #009DBA;">✓</span> Archivos desde tu celular.</li>
        <li style="margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;"><span style="color: #009DBA;">✓</span> Servicios para escuela, trabajo y trámites.</li>
      </ul>

      <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20consultar%20un%20servicio%20de%20impresi%C3%B3n%20o%20documentos%20en%20Mr.O%20Papeler%C3%ADa." class="btn btn--primary quick-services__cta" target="_blank" rel="noopener noreferrer">Consultar servicio</a>
    </div>

    <div class="quick-services__grid">
      <article class="quick-service-card quick-reveal">
        <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20consultar%20el%20servicio%20de%20copias%20en%20blanco%20y%20negro." target="_blank" rel="noopener noreferrer" aria-label="Consultar copias en blanco y negro por WhatsApp">
          <figure class="quick-service-card__media">
            <img src="./assets/img/servicios-rapidos/copias-blanco-negro.webp" alt="Copias de documentos en blanco y negro" width="1200" height="800" loading="lazy" decoding="async">
          </figure>
          <div class="quick-service-card__content">
            <h3>Copias B/N</h3>
            <p>Documentos claros para escuela, trabajo o trámites.</p>
          </div>
        </a>
      </article>

      <article class="quick-service-card quick-reveal">
        <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20consultar%20el%20servicio%20de%20copias%20a%20color." target="_blank" rel="noopener noreferrer" aria-label="Consultar copias a color por WhatsApp">
          <figure class="quick-service-card__media">
            <img src="./assets/img/servicios-rapidos/copias-color.webp" alt="Copias a color" width="1200" height="800" loading="lazy" decoding="async">
          </figure>
          <div class="quick-service-card__content">
            <h3>Copias a color</h3>
            <p>Copias con color uniforme y buena presentación.</p>
          </div>
        </a>
      </article>

      <article class="quick-service-card quick-reveal">
        <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20imprimir%20unos%20documentos." target="_blank" rel="noopener noreferrer" aria-label="Consultar impresiones por WhatsApp">
          <figure class="quick-service-card__media">
            <img src="./assets/img/servicios-rapidos/impresion-documentos.webp" alt="Impresiones" width="1200" height="800" loading="lazy" decoding="async">
          </figure>
          <div class="quick-service-card__content">
            <h3>Impresiones</h3>
            <p>Imprime archivos escolares, laborales o personales.</p>
          </div>
        </a>
      </article>

      <article class="quick-service-card quick-reveal">
        <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20consultar%20el%20servicio%20de%20escaneo." target="_blank" rel="noopener noreferrer" aria-label="Consultar escaneo por WhatsApp">
          <figure class="quick-service-card__media">
            <img src="./assets/img/servicios-rapidos/escaneo-documentos.webp" alt="Escaneo de documentos" width="1200" height="800" loading="lazy" decoding="async">
          </figure>
          <div class="quick-service-card__content">
            <h3>Escaneo</h3>
            <p>Convierte tus documentos físicos en archivos digitales.</p>
          </div>
        </a>
      </article>

      <article class="quick-service-card quick-reveal">
        <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20informaci%C3%B3n%20para%20consultar%20o%20imprimir%20un%20acta%20de%20nacimiento." target="_blank" rel="noopener noreferrer" aria-label="Consultar actas de nacimiento por WhatsApp">
          <figure class="quick-service-card__media">
            <img src="./assets/img/servicios-rapidos/actas-nacimiento.webp" alt="Actas de nacimiento" width="1200" height="800" loading="lazy" decoding="async">
          </figure>
          <div class="quick-service-card__content">
            <h3>Actas de nacimiento</h3>
            <p>Apoyo para consultar e imprimir actas de nacimiento.</p>
          </div>
        </a>
      </article>

      <article class="quick-service-card quick-reveal">
        <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20consultar%20o%20imprimir%20una%20CURP." target="_blank" rel="noopener noreferrer" aria-label="Consultar CURP por WhatsApp">
          <figure class="quick-service-card__media">
            <img src="./assets/img/servicios-rapidos/curp-documento.webp" alt="CURP" width="1200" height="800" loading="lazy" decoding="async">
          </figure>
          <div class="quick-service-card__content">
            <h3>CURP</h3>
            <p>Consulta e impresión de CURP.</p>
          </div>
        </a>
      </article>

      <article class="quick-service-card quick-reveal">
        <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20consultar%20o%20imprimir%20un%20recibo%20CFE." target="_blank" rel="noopener noreferrer" aria-label="Consultar recibo CFE por WhatsApp">
          <figure class="quick-service-card__media">
            <img src="./assets/img/servicios-rapidos/recibo-cfe.webp" alt="Recibos CFE" width="1200" height="800" loading="lazy" decoding="async">
          </figure>
          <div class="quick-service-card__content">
            <h3>Recibo CFE</h3>
            <p>Consulta e impresión de recibos de energía.</p>
          </div>
        </a>
      </article>

      <article class="quick-service-card quick-reveal">
        <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20consultar%20el%20servicio%20de%20impresi%C3%B3n%20de%20talones%20ISSSTE." target="_blank" rel="noopener noreferrer" aria-label="Consultar talones ISSSTE por WhatsApp">
          <figure class="quick-service-card__media">
            <img src="./assets/img/servicios-rapidos/talones-issste.webp" alt="Talones ISSSTE" width="1200" height="800" loading="lazy" decoding="async">
          </figure>
          <div class="quick-service-card__content">
            <h3>Talones ISSSTE</h3>
            <p>Apoyo para consultar e imprimir talones ISSSTE.</p>
          </div>
        </a>
      </article>

      <article class="quick-service-card quick-reveal">
        <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20consultar%20el%20servicio%20de%20engargolado." target="_blank" rel="noopener noreferrer" aria-label="Consultar engargolado por WhatsApp">
          <figure class="quick-service-card__media">
            <img src="./assets/img/servicios-rapidos/engargolado.webp" alt="Engargolado" width="1200" height="800" loading="lazy" decoding="async">
          </figure>
          <div class="quick-service-card__content">
            <h3>Engargolado</h3>
            <p>Presentación ordenada para trabajos y documentos.</p>
          </div>
        </a>
      </article>

      <article class="quick-service-card quick-reveal">
        <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20consultar%20el%20servicio%20de%20enmicado." target="_blank" rel="noopener noreferrer" aria-label="Consultar enmicado por WhatsApp">
          <figure class="quick-service-card__media">
            <img src="./assets/img/servicios-rapidos/enmicado.webp" alt="Enmicado" width="1200" height="800" loading="lazy" decoding="async">
          </figure>
          <div class="quick-service-card__content">
            <h3>Enmicado</h3>
            <p>Protege credenciales, avisos y documentos.</p>
          </div>
        </a>
      </article>

      <article class="quick-service-card quick-reveal">
        <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20consultar%20el%20servicio%20de%20impresi%C3%B3n%20de%20planos." target="_blank" rel="noopener noreferrer" aria-label="Consultar impresión de planos por WhatsApp">
          <figure class="quick-service-card__media">
            <img src="./assets/img/servicios-rapidos/impresion-planos.webp" alt="Impresión de planos" width="1200" height="800" loading="lazy" decoding="async">
          </figure>
          <div class="quick-service-card__content">
            <h3>Impresión de planos</h3>
            <p>Impresión de planos y documentos de formato amplio.</p>
          </div>
        </a>
      </article>

      <article class="quick-service-card quick-reveal">
        <a href="https://wa.me/527471013037?text=Hola%2C%20necesito%20un%20servicio%20adicional%20y%20quiero%20saber%20si%20pueden%20ayudarme." target="_blank" rel="noopener noreferrer" aria-label="Consultar más servicios por WhatsApp">
          <figure class="quick-service-card__media">
            <img src="./assets/img/servicios-rapidos/mas-servicios.webp" alt="Más servicios documentales" width="1200" height="800" loading="lazy" decoding="async">
          </figure>
          <div class="quick-service-card__content">
            <h3>Más servicios</h3>
            <p>Consulta disponibilidad para otras necesidades documentales.</p>
          </div>
        </a>
      </article>
    </div>
  </div>
</section>"""

import re
# Regex to find <section class="section quick-services"> ... </section>
pattern = re.compile(r'<section class="section quick-services">.*?</section>', re.DOTALL)
if pattern.search(html):
    html = pattern.sub(new_html, html)
else:
    # try another match
    print("Could not find quick-services with regex.")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("HTML updated.")


# CSS APPEND
css_path = os.path.join(project_dir, 'css', 'styles.css')
with open(css_path, 'a', encoding='utf-8') as f:
    f.write("""
/* ------------------------------------- */
/* QUICK SERVICES REFACTOR */
/* ------------------------------------- */

.quick-services {
  position: relative;
  padding-block: clamp(3.5rem, 6vw, 6.5rem);
  background: radial-gradient(circle at 90% 10%, rgba(0, 166, 200, 0.11), transparent 28%), linear-gradient(180deg, #ffffff 0%, #f1f6f8 100%);
}

.quick-services__container {
  width: min(1240px, calc(100% - 2.5rem));
  margin-inline: auto;
  display: grid;
  grid-template-columns: minmax(240px, 0.7fr) minmax(0, 2fr);
  gap: clamp(2rem, 4vw, 4.5rem);
  align-items: start;
}

.quick-services__grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 1rem;
}

.quick-service-card {
  overflow: hidden;
  min-width: 0;
  border-radius: 18px;
  background: #ffffff;
  border: 1px solid rgba(7, 54, 92, 0.10);
  box-shadow: 0 14px 36px rgba(8, 39, 59, 0.10);
  transition: transform 0.35s ease, box-shadow 0.35s ease, border-color 0.35s ease;
}

.quick-service-card:hover {
  transform: translateY(-5px);
  border-color: rgba(0, 166, 200, 0.34);
  box-shadow: 0 22px 48px rgba(8, 39, 59, 0.17);
}

.quick-service-card a {
  display: block;
  height: 100%;
  color: inherit;
  text-decoration: none;
}

.quick-service-card__media {
  aspect-ratio: 3 / 2;
  overflow: hidden;
  background: #dfe8ec;
}

.quick-service-card__media img {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
  object-position: center;
  transition: transform 0.5s ease, filter 0.5s ease;
}

.quick-service-card:hover img {
  transform: scale(1.04);
  filter: saturate(1.06) contrast(1.02);
}

.quick-service-card__content {
  position: relative;
  padding: 1rem;
}

.quick-service-card__content h3 {
  margin: 0 0 0.3rem;
  color: #07365c;
  font-size: 1rem;
  line-height: 1.2;
}

.quick-service-card__content p {
  margin: 0;
  color: #596b79;
  font-size: 0.86rem;
  line-height: 1.45;
}

.quick-reveal {
  opacity: 0;
  transform: translateY(18px);
  transition: opacity 0.55s ease, transform 0.55s ease;
}

.quick-reveal.is-visible {
  opacity: 1;
  transform: translateY(0);
}

@media (prefers-reduced-motion: reduce) {
  .quick-reveal,
  .quick-service-card,
  .quick-service-card img {
    transition: none;
    transform: none;
    opacity: 1;
  }
}

@media (max-width: 1100px) {
  .quick-services__container {
    grid-template-columns: 1fr;
  }
  .quick-services__grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}

@media (max-width: 760px) {
  .quick-services__grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 480px) {
  .quick-services__grid {
    grid-template-columns: 1fr;
  }
  .quick-services__cta {
    width: 100%;
    justify-content: center;
  }
}
""")
print("CSS appended.")

# JS APPEND
js_path = os.path.join(project_dir, 'js', 'main.js')
if os.path.exists(js_path):
    with open(js_path, 'r', encoding='utf-8') as f:
        js = f.read()
    if 'quickServiceElements' not in js:
        with open(js_path, 'a', encoding='utf-8') as f:
            f.write("""

// QUICK SERVICES REVEAL OBSERVER
document.addEventListener("DOMContentLoaded", () => {
  const quickServiceElements = document.querySelectorAll(".quick-reveal");
  if(quickServiceElements.length > 0) {
    const quickServiceObserver = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        });
      },
      { threshold: 0.15 }
    );

    quickServiceElements.forEach((element, index) => {
      element.style.transitionDelay = `${index * 70}ms`;
      quickServiceObserver.observe(element);
    });
  }
});
""")
        print("JS appended.")
else:
    print("js/main.js not found.")

