import os
import urllib.request
import re

project_dir = r'C:\Users\repre\Documents\Mro papeleria'

# 1. Ensure directories exist and download images
img_web_dir = os.path.join(project_dir, 'assets', 'img', 'paginas-web')
img_local_dir = os.path.join(project_dir, 'assets', 'img', 'local')
os.makedirs(img_web_dir, exist_ok=True)
os.makedirs(img_local_dir, exist_ok=True)

def download_pollinations(prompt, filepath):
    url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote(prompt)}?width=1600&height=1000&nologo=true&model=flux"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Downloaded: {filepath}")
    except Exception as e:
        print(f"Failed {filepath}: {e}")

download_pollinations("photorealistic mockup of a modern business website displayed on a sleek laptop on a wooden desk, natural lighting, 50mm lens", os.path.join(img_web_dir, 'web-escritorio.webp'))
download_pollinations("photorealistic mockup of responsive web design showing the same website on a laptop monitor, tablet, and smartphone on a modern desk", os.path.join(img_web_dir, 'web-responsive.webp'))
download_pollinations("photorealistic mockup of a local business website on an iMac, showing services and map location, clean modern desk", os.path.join(img_web_dir, 'web-negocio-local.webp'))
download_pollinations("photorealistic interior of a modern stationery store showing a clean service counter and organized office supplies, natural lighting, bright commercial photography", os.path.join(img_local_dir, 'interior-mro.webp'))


# 2. Update HTML
html_path = os.path.join(project_dir, 'index.html')
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

new_html_bottom = """<section id="paginas-web" class="web-section">
  <div class="web-section__container">
    <div class="web-section__layout">
      <div class="web-showcase-copy">
        <span class="web-kicker eyebrow">SOLUCIONES DIGITALES</span>
        <h2>Páginas web</h2>
        <p>Creamos sitios web modernos, rápidos y adaptados a tu negocio.</p>
        <a href="https://wa.me/527471013037?text=Hola%2C%20quiero%20cotizar%20una%20p%C3%A1gina%20web." class="btn btn--primary web-cta" target="_blank" rel="noopener noreferrer" style="margin-top:1.5rem; display:inline-block;">Solicitar página web</a>
      </div>

      <div class="web-showcase">
        <article class="web-showcase__main">
          <img src="./assets/img/paginas-web/web-escritorio.webp" alt="Página web empresarial en escritorio" loading="lazy">
        </article>
        <article>
          <img src="./assets/img/paginas-web/web-responsive.webp" alt="Diseño web responsivo en múltiples dispositivos" loading="lazy">
        </article>
        <article>
          <img src="./assets/img/paginas-web/web-negocio-local.webp" alt="Página informativa para negocio local" loading="lazy">
        </article>
      </div>

      <div class="web-benefits">
        <div class="web-benefit">Diseño responsivo</div>
        <div class="web-benefit">Rápido y seguro</div>
        <div class="web-benefit">Fácil de administrar</div>
        <div class="web-benefit">Soporte incluido</div>
      </div>
    </div>
  </div>
</section>

<section id="ubicacion" class="location-contact">
  <div class="location-contact__container">
    <div class="location-contact__layout">
      <div class="location-contact__left">
        <span class="location-kicker eyebrow">MR.O PAPELERÍA</span>
        <h2>Soluciones para escuela y oficina</h2>
        <p>Copias, impresiones, trámites y material escolar con atención clara, rápida y confiable.</p>
        
        <img src="./assets/img/local/interior-mro.webp" alt="Interior de Mr.O Papelería" style="width: 100%; border-radius: 22px; margin-block: 1.5rem; max-height: 280px; object-fit: cover;">
        
        <div class="location-address">
          <h3>VISÍTANOS</h3>
          <p>
            <strong>Blvd. Vicente Guerrero 8L</strong><br>
            Col. Salubridad<br>
            Chilpancingo, Guerrero
          </p>
          <p>Lunes a Sábado: 8:00 am - 8:00 pm</p>
  
          <div class="location-actions" style="display:flex; gap:1rem; flex-wrap:wrap; margin-top:1.5rem;">
            <a href="https://www.google.com/maps/search/?api=1&query=Mr.O+Papelería+Chilpancingo" class="btn btn--secondary" target="_blank" rel="noopener">Cómo llegar</a>
            <a href="https://wa.me/527471013037" class="btn btn--primary" target="_blank" rel="noopener">Escríbenos por WhatsApp</a>
          </div>
        </div>
      </div>
  
      <div class="location-contact__right">
        <div class="location-map">
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d7609.343237255719!2d-99.48879372510295!3d17.523182298879448!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x85cbebc852234447%3A0xa6099a0e6eae5589!2sMr%20O%20Papeleria!5e0!3m2!1ses!2smx!4v1781898514373!5m2!1ses!2smx" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Ubicación de Mr.O Papelería"></iframe>
        </div>
      </div>
    </div>
  </div>
</section>

</main>

<a class="whatsapp-float" href="https://wa.me/527471013037" target="_blank" rel="noopener noreferrer" aria-label="Contactar a Mr.O Papelería por WhatsApp" data-whatsapp data-message="Hola, necesito enviar archivos para impresión o hacer una consulta general.">WA</a>

<footer class="site-footer" id="contacto">
  <div class="site-footer__container">
    <div class="footer-brand">
      <img src="./assets/img/logo-mro.jpg" alt="Logotipo de Mr.O Papelería" style="max-width: 150px; margin-bottom:1rem; border-radius: 8px;">
      <p style="color: rgba(255,255,255,0.8);">Todo para escuela, oficina y negocios locales.</p>
    </div>
    <nav aria-label="Enlaces principales">
      <h3>Enlaces</h3>
      <a href="#inicio">Inicio</a>
      <a href="#servicios">Servicios</a>
      <a href="#papeleria">Papelería</a>
      <a href="#diseno">Diseño para negocios</a>
      <a href="#paginas-web">Páginas web</a>
      <a href="#ubicacion">Ubicación</a>
      <a href="#contacto">Contacto</a>
    </nav>
    <nav aria-label="Servicios">
      <h3>Servicios</h3>
      <a href="#servicios">Copias e impresiones</a>
      <a href="#servicios">Trámites</a>
      <a href="#papeleria">Material escolar</a>
      <a href="#papeleria">Oficina</a>
      <a href="#diseno">Diseño gráfico</a>
      <a href="#paginas-web">Páginas web</a>
    </nav>
    <div class="footer-contact">
      <h3>Contacto</h3>
      <a href="https://wa.me/527471013037" target="_blank" rel="noopener noreferrer" data-whatsapp data-message="Hola, me gustaría hacer una consulta.">747 101 3037</a>
      <a href="tel:+527471013037">Llamar: 747 101 3037</a>
      <a href="mailto:mropapeleria@gmail.com">mropapeleria@gmail.com</a>
      <a href="https://www.facebook.com/MrOPapeleria" target="_blank" rel="noopener">Facebook</a>
      <span>Instagram</span>
    </div>
  </div>
  <div class="footer-bottom" style="text-align:center; padding-block: 1.5rem; border-top: 1px solid rgba(255,255,255,0.1); width: min(1180px, calc(100% - 3rem)); margin-inline: auto;">
    <small style="color: rgba(255,255,255,0.6);">© <span data-current-year></span> Mr.O Papelería. Escuela &amp; Oficina en Chilpancingo.</small>
  </div>
</footer>"""

start_idx = html.find('<section id="paginas-web"')
end_idx = html.find('</footer>') + len('</footer>')

if start_idx != -1 and end_idx != -1:
    html = html[:start_idx] + new_html_bottom + html[end_idx:]
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("HTML bottom updated safely.")
else:
    print("Could not find section boundaries.")


# 3. Update CSS
css_path = os.path.join(project_dir, 'css', 'styles.css')
with open(css_path, 'a', encoding='utf-8') as f:
    f.write("""
/* ------------------------------------- */
/* REFACTORED BOTTOM SECTIONS */
/* ------------------------------------- */

.web-section__container,
.location-contact__container,
.site-footer__container {
  width: min(1180px, calc(100% - 3rem));
  margin-inline: auto;
}

.web-section,
.location-contact {
  padding-block: clamp(4rem, 7vw, 7rem);
}

.web-section__layout {
  display: grid;
  grid-template-columns: minmax(240px, 0.75fr) minmax(520px, 1.55fr) minmax(220px, 0.65fr);
  gap: clamp(2rem, 4vw, 4rem);
  align-items: center;
}

.web-showcase {
  display: grid;
  grid-template-columns: 1.25fr 0.9fr;
  grid-template-rows: repeat(2, minmax(180px, 1fr));
  gap: 1.25rem;
}

.web-showcase__main {
  grid-row: 1 / 3;
}

.web-showcase img {
  width: 100%;
  height: 100%;
  min-height: 190px;
  display: block;
  object-fit: cover;
  border-radius: 18px;
  box-shadow: 0 12px 30px rgba(0,0,0,0.08);
}

.web-benefits {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.web-benefit {
  min-height: 52px;
  padding: 0.9rem 1.15rem;
  font-size: 0.98rem;
  background: #f1f5f9;
  border-radius: 12px;
  display: flex;
  align-items: center;
  color: #334155;
  font-weight: 500;
  border-left: 4px solid #009DBA;
}

.location-contact__layout {
  display: grid;
  grid-template-columns: minmax(330px, 0.85fr) minmax(520px, 1.35fr);
  gap: clamp(2rem, 5vw, 4rem);
  align-items: stretch;
}

.location-map {
  min-height: 430px;
  height: 100%;
  overflow: hidden;
  border-radius: 22px;
  box-shadow: 0 16px 40px rgba(0,0,0,0.1);
}

.location-map iframe {
  width: 100%;
  height: 100%;
  min-height: 430px;
  border: 0;
  display: block;
}

.location-address h3 {
  font-size: 1.25rem;
  color: #0f172a;
  margin-bottom: 0.75rem;
}

.location-address p {
  color: #475569;
  margin-bottom: 0.5rem;
}

.site-footer {
  background: #0b2135;
  color: #fff;
}

.site-footer__container {
  display: grid;
  grid-template-columns: 1.2fr repeat(3, minmax(150px, 0.7fr));
  gap: clamp(2rem, 4vw, 3rem);
  padding-block: 4rem 2.5rem;
}

.site-footer h3 {
  color: #fff;
  font-size: 1.15rem;
  margin-bottom: 1.2rem;
  font-weight: 600;
}

.site-footer nav a,
.footer-contact a,
.footer-contact span {
  display: block;
  color: rgba(255,255,255,0.75);
  text-decoration: none;
  margin-bottom: 0.75rem;
  transition: color 0.3s ease;
  font-size: 1rem;
}

.site-footer nav a:hover,
.footer-contact a:hover {
  color: #F7B21A;
}

/* Fix scales */
.web-section h2 {
  font-size: clamp(2.4rem, 4.5vw, 4.6rem);
  color: #0f172a;
  margin-bottom: 1rem;
  line-height: 1.1;
}

.location-contact h2 {
  font-size: clamp(2rem, 3.5vw, 3.4rem);
  color: #0f172a;
  margin-bottom: 1.25rem;
  line-height: 1.15;
}

.web-section p,
.location-contact p {
  font-size: clamp(0.98rem, 1.2vw, 1.1rem);
  color: #475569;
  line-height: 1.6;
}

/* Responsive */
@media (max-width: 1000px) {
  .web-section__layout {
    grid-template-columns: 1fr 1.4fr;
  }
  .web-benefits {
    grid-column: 1 / -1;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 800px) {
  .site-footer__container {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 700px) {
  .web-section__layout,
  .location-contact__layout,
  .site-footer__container {
    grid-template-columns: 1fr;
  }
  .web-showcase {
    grid-template-columns: 1fr;
    grid-template-rows: auto;
  }
  .web-showcase__main {
    grid-row: auto;
  }
  .web-benefits {
    grid-template-columns: 1fr;
  }
  .location-map {
    min-height: 350px;
  }
  .location-map iframe {
    min-height: 350px;
  }
}
""")
print("CSS appended securely.")
