import os

project_dir = r'C:\Users\repre\Documents\Mro papeleria'

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
        <article class="web-showcase__item">
          <img src="./assets/img/paginas-web/web-showcase-01.jpg" alt="Diseño profesional de página web y panel administrativo" loading="lazy">
        </article>
        <article class="web-showcase__item">
          <img src="./assets/img/paginas-web/web-showcase-02.jpg" alt="Diseño web de productos y comercio electrónico" loading="lazy">
        </article>
        <article class="web-showcase__item">
          <img src="./assets/img/paginas-web/web-showcase-03.jpg" alt="Interfaces modernas para negocios digitales" loading="lazy">
        </article>
        <article class="web-showcase__item">
          <img src="./assets/img/paginas-web/web-showcase-04.jpg" alt="Diseño web profesional con paneles y catálogo" loading="lazy">
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

<section id="ubicacion" class="location-section">
  <div class="location-strip">
    <div class="location-strip__image">
      <img src="./assets/img/ubicacion/servicios-mro.webp" alt="Servicios de papelería, impresión y material escolar" loading="lazy">
    </div>

    <div class="location-copy" style="padding: 2.5rem 1.5rem; display: flex; flex-direction: column; justify-content: center;">
      <span class="location-kicker eyebrow">MR.O PAPELERÍA</span>
      <h2 style="font-size: clamp(1.8rem, 2.5vw, 2.2rem); margin-block: 0.5rem 1rem; color: #07365c; line-height: 1.1;">Soluciones para escuela y oficina</h2>
      <p style="color: #526677; font-size: 1rem; line-height: 1.5;">Copias, impresiones, trámites y material escolar con atención clara, rápida y confiable.</p>
    </div>

    <div class="location-address" style="padding: 2.5rem 1.5rem; display: flex; flex-direction: column; justify-content: center;">
      <h2 style="font-size: 1.2rem; margin-bottom: 1rem; color: #07365c;">VISÍTANOS</h2>
      <p style="color: #526677; font-size: 0.95rem; margin-bottom: 1rem; line-height: 1.5;">
        <strong>Blvd. Vicente Guerrero 8L</strong><br>
        Col. Salubridad<br>
        Chilpancingo, Guerrero
      </p>
      <div class="location-actions" style="display: flex; flex-direction: column; gap: 0.75rem;">
        <a href="https://www.google.com/maps/search/?api=1&query=Mr.O+Papelería+Chilpancingo" class="btn btn--secondary" target="_blank" rel="noopener">Cómo llegar</a>
        <a href="https://wa.me/527471013037" class="btn btn--primary" target="_blank" rel="noopener">Escríbenos por WhatsApp</a>
      </div>
    </div>

    <div class="location-strip__map">
      <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d7609.343237255719!2d-99.48879372510295!3d17.523182298879448!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x85cbebc852234447%3A0xa6099a0e6eae5589!2sMr%20O%20Papeleria!5e0!3m2!1ses!2smx!4v1781898514373!5m2!1ses!2smx" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Ubicación de Mr.O Papelería"></iframe>
    </div>
  </div>
</section>

</main>

<a class="whatsapp-float" href="https://wa.me/527471013037" target="_blank" rel="noopener noreferrer" aria-label="Contactar a Mr.O Papelería por WhatsApp" data-whatsapp data-message="Hola, necesito enviar archivos para impresión o hacer una consulta general.">WA</a>

<footer class="site-footer" id="contacto">
  <div class="site-footer__container">
    <div class="footer-brand">
      <img src="./assets/img/logo-mro.jpg" alt="Logotipo de Mr.O Papelería" style="max-width: 150px; margin-bottom:1rem; border-radius: 8px;">
      <p style="color: rgba(255,255,255,0.8); font-size: 0.95rem;">Todo para escuela, oficina y negocios locales.</p>
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
    <div class="footer-attention">
      <h3>Atención rápida y personalizada</h3>
      <p style="color: rgba(255,255,255,0.75); font-size: 0.95rem;">Lunes a Sábado<br>8:00 am - 8:00 pm</p>
    </div>
  </div>
  <div class="footer-bottom" style="text-align:center; padding-block: 1.5rem; border-top: 1px solid rgba(255,255,255,0.1); width: min(1180px, calc(100% - 2rem)); margin-inline: auto;">
    <small style="color: rgba(255,255,255,0.6); font-size: 13px;">© <span data-current-year></span> Mr.O Papelería. Escuela &amp; Oficina en Chilpancingo.</small>
  </div>
</footer>"""

start_idx = html.find('<section id="paginas-web"')
end_idx = html.find('</footer>') + len('</footer>')

if start_idx != -1 and end_idx != -1:
    html = html[:start_idx] + new_html_bottom + html[end_idx:]
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("HTML restored safely.")
else:
    print("Could not find section boundaries in HTML.")


# Update CSS
css_path = os.path.join(project_dir, 'css', 'styles.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Remove the refactored block
css_split = css.split('/* ------------------------------------- */\n/* REFACTORED BOTTOM SECTIONS */')
if len(css_split) > 1:
    css = css_split[0]

new_css = """
/* ------------------------------------- */
/* REFACTORED BOTTOM SECTIONS */
/* ------------------------------------- */

.web-section__container {
  width: min(1180px, calc(100% - 2rem));
  margin-inline: auto;
}

.web-section,
.location-section {
  padding-block: clamp(4rem, 7vw, 7rem);
}

.web-section__layout {
  display: grid;
  grid-template-columns: minmax(220px, 0.7fr) minmax(500px, 1.45fr) minmax(220px, 0.65fr);
  gap: clamp(2rem, 4vw, 4rem);
  align-items: center;
}

.web-showcase {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}

.web-showcase__item {
  aspect-ratio: 16 / 10;
  overflow: hidden;
  border-radius: 14px;
}

.web-showcase__item img {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
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

.location-strip {
  width: min(1180px, calc(100% - 2rem));
  margin-inline: auto;
  display: grid;
  grid-template-columns: minmax(230px, 1fr) minmax(220px, 0.8fr) minmax(230px, 0.8fr) minmax(300px, 1.2fr);
  align-items: stretch;
  overflow: hidden;
  border-radius: 20px;
  background: #ffffff;
  box-shadow: 0 20px 55px rgba(8, 37, 58, 0.12);
}

.location-strip__image img {
  width: 100%;
  height: 100%;
  min-height: 310px;
  display: block;
  object-fit: cover;
  object-position: center;
}

.location-strip__map {
  min-height: 310px;
  overflow: hidden;
}

.location-strip__map iframe,
.location-strip__map img {
  width: 100%;
  height: 100%;
  min-height: 310px;
  display: block;
  border: 0;
  object-fit: cover;
}

.site-footer {
  background: #0b2135;
  color: #fff;
}

.site-footer__container {
  width: min(1180px, calc(100% - 2rem));
  margin-inline: auto;
  display: grid;
  grid-template-columns: minmax(220px, 1.2fr) repeat(4, minmax(130px, 0.7fr));
  gap: 2rem;
  padding-block: 2.25rem;
}

.site-footer h3 {
  color: #fff;
  font-size: 1.15rem;
  margin-bottom: 1.2rem;
  font-weight: 600;
}

.site-footer nav a,
.footer-contact a,
.footer-contact span,
.footer-attention p {
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

.web-section p {
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
  .location-strip {
    grid-template-columns: 1fr 1fr;
  }
  .location-strip__image img {
    height: 100%;
  }
  .site-footer__container {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 700px) {
  .web-section__layout,
  .location-strip,
  .site-footer__container {
    grid-template-columns: 1fr;
  }
  .web-showcase {
    grid-template-columns: 1fr;
  }
  .web-benefits {
    grid-template-columns: 1fr;
  }
  .location-strip__image img,
  .location-strip__map iframe {
    min-height: 250px;
  }
}
"""

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css + new_css)
print("CSS restored safely.")
