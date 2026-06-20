import os
import re

base_dir = r'C:\Users\repre\Documents\Mro papeleria'
html_path = os.path.join(base_dir, 'productos-escolares.html')
css_path = os.path.join(base_dir, 'css', 'styles.css')

new_main = """<main id="contenido-principal" class="school-catalog">

  <section class="school-catalog-hero">
    <div class="school-catalog-hero-bg">
      <img
        src="./assets/img/collages-escolares/collage-regreso-clases-hero.webp"
        alt=""
        aria-hidden="true"
      >
    </div>

    <div class="school-catalog-hero-overlay"></div>

    <div class="school-catalog-hero-inner">
      <span>TEMPORADA ESCOLAR</span>

      <h1>Todo para el regreso a clases</h1>

      <p>
        Conoce una selección de útiles, materiales escolares y productos para
        oficina. Modelos y presentaciones sujetos a disponibilidad.
      </p>

      <div class="school-catalog-actions">
        <a
          href="https://wa.me/527471013037?text=Hola,%20quiero%20consultar%20productos%20escolares."
          target="_blank"
          rel="noopener"
          class="catalog-button catalog-button-primary"
        >
          Consultar disponibilidad
        </a>

        <a
          href="./index.html#papeleria"
          class="catalog-button catalog-button-secondary"
        >
          Volver al inicio
        </a>
      </div>
    </div>
  </section>

  <section class="school-categories">
    <div class="school-categories-heading">
      <span>MOSTRARIO</span>

      <h2>Productos escolares y de oficina</h2>

      <p>
        Encuentra diferentes opciones para clases, tareas, proyectos,
        organización y trabajo.
      </p>
    </div>

    <div class="school-category-grid">

      <article class="school-category-card">
        <div class="school-category-image">
          <img
            src="./assets/img/collages-escolares/collage-cuadernos.webp"
            alt="Cuadernos, libretas, folders y separadores"
            loading="lazy"
          >
        </div>

        <div class="school-category-content">
          <h3>Cuadernos y libretas</h3>

          <p>
            Cuadernos profesionales, libretas, hojas, folders y separadores.
          </p>

          <a
            href="https://wa.me/527471013037?text=Hola,%20quiero%20consultar%20cuadernos%20y%20libretas."
            target="_blank"
            rel="noopener"
          >
            Consultar productos
          </a>
        </div>
      </article>

      <article class="school-category-card">
        <div class="school-category-image">
          <img
            src="./assets/img/collages-escolares/collage-escritura.webp"
            alt="Lápices, bolígrafos, marcatextos y material de escritura"
            loading="lazy"
          >
        </div>

        <div class="school-category-content">
          <h3>Escritura</h3>

          <p>
            Lápices, bolígrafos, portaminas, marcatextos y correctores.
          </p>

          <a
            href="https://wa.me/527471013037?text=Hola,%20quiero%20consultar%20productos%20de%20escritura."
            target="_blank"
            rel="noopener"
          >
            Consultar productos
          </a>
        </div>
      </article>

      <article class="school-category-card">
        <div class="school-category-image">
          <img
            src="./assets/img/collages-escolares/collage-colores.webp"
            alt="Colores, plumones, crayones y acuarelas"
            loading="lazy"
          >
        </div>

        <div class="school-category-content">
          <h3>Colores y dibujo</h3>

          <p>
            Colores, plumones, crayones, acuarelas y material para dibujo.
          </p>

          <a
            href="https://wa.me/527471013037?text=Hola,%20quiero%20consultar%20colores%20y%20material%20de%20dibujo."
            target="_blank"
            rel="noopener"
          >
            Consultar productos
          </a>
        </div>
      </article>

      <article class="school-category-card">
        <div class="school-category-image">
          <img
            src="./assets/img/collages-escolares/collage-geometria.webp"
            alt="Reglas, escuadras, transportadores y compases"
            loading="lazy"
          >
        </div>

        <div class="school-category-content">
          <h3>Geometría</h3>

          <p>
            Reglas, escuadras, transportadores, compases y juegos geométricos.
          </p>

          <a
            href="https://wa.me/527471013037?text=Hola,%20quiero%20consultar%20material%20de%20geometría."
            target="_blank"
            rel="noopener"
          >
            Consultar productos
          </a>
        </div>
      </article>

      <article class="school-category-card">
        <div class="school-category-image">
          <img
            src="./assets/img/collages-escolares/collage-pegamentos-manualidades.webp"
            alt="Pegamentos, tijeras y materiales para manualidades"
            loading="lazy"
          >
        </div>

        <div class="school-category-content">
          <h3>Pegamentos y manualidades</h3>

          <p>
            Pegamentos, tijeras, cartulinas, foamy, plastilina y papel de colores.
          </p>

          <a
            href="https://wa.me/527471013037?text=Hola,%20quiero%20consultar%20material%20para%20manualidades."
            target="_blank"
            rel="noopener"
          >
            Consultar productos
          </a>
        </div>
      </article>

      <article class="school-category-card">
        <div class="school-category-image">
          <img
            src="./assets/img/collages-escolares/collage-organizacion.webp"
            alt="Carpetas, folders, separadores y etiquetas"
            loading="lazy"
          >
        </div>

        <div class="school-category-content">
          <h3>Organización</h3>

          <p>
            Carpetas, folders, separadores, etiquetas y accesorios de archivo.
          </p>

          <a
            href="https://wa.me/527471013037?text=Hola,%20quiero%20consultar%20productos%20de%20organización."
            target="_blank"
            rel="noopener"
          >
            Consultar productos
          </a>
        </div>
      </article>

      <article class="school-category-card">
        <div class="school-category-image">
          <img
            src="./assets/img/collages-escolares/collage-mochilas-estuches.webp"
            alt="Mochilas, estuches y accesorios escolares"
            loading="lazy"
          >
        </div>

        <div class="school-category-content">
          <h3>Mochilas y estuches</h3>

          <p>
            Mochilas, estuches, loncheras y accesorios para el regreso a clases.
          </p>

          <a
            href="https://wa.me/527471013037?text=Hola,%20quiero%20consultar%20mochilas%20y%20estuches."
            target="_blank"
            rel="noopener"
          >
            Consultar productos
          </a>
        </div>
      </article>

      <article class="school-category-card">
        <div class="school-category-image">
          <img
            src="./assets/img/collages-escolares/collage-impresion-oficina.webp"
            alt="Impresiones, engargolados y material de oficina"
            loading="lazy"
          >
        </div>

        <div class="school-category-content">
          <h3>Impresión y oficina</h3>

          <p>
            Papel, impresiones, engargolados, enmicados y material de oficina.
          </p>

          <a
            href="https://wa.me/527471013037?text=Hola,%20quiero%20consultar%20servicios%20de%20impresión%20y%20oficina."
            target="_blank"
            rel="noopener"
          >
            Consultar productos
          </a>
        </div>
      </article>

    </div>
  </section>

</main>"""

# Read HTML
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace main
html = re.sub(r'<main[^>]*>.*?</main>', new_main, html, flags=re.DOTALL)

# Write HTML
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)


# Read CSS
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Delete old broken filters and missing CSS
css = re.sub(r'\.product-card\[data-image-status="missing"\]\s*\{\s*display:\s*none;\s*\}', '', css)
css = re.sub(r'\.product-card-image\s*\{[^}]*\}', '', css)
css = re.sub(r'\.product-card-image img\s*\{[^}]*\}', '', css)
css = re.sub(r'\.products-grid\s*\{[^}]*\}', '', css)
css = re.sub(r'\.product-card\s*\{[^}]*\}', '', css)

# Append new CSS
new_css = """
.school-catalog {
  background: #F4F8FA;
}

.school-catalog-hero {
  position: relative;
  min-height: 470px;
  overflow: hidden;
  background: #061B2E;
  color: #ffffff;
}

.school-catalog-hero-bg {
  position: absolute;
  inset: 0;
}

.school-catalog-hero-bg img {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
  object-position: center right;
}

.school-catalog-hero-overlay {
  position: absolute;
  inset: 0;
  background:
    linear-gradient(
      90deg,
      rgba(6, 27, 46, 0.98) 0%,
      rgba(6, 27, 46, 0.88) 36%,
      rgba(6, 27, 46, 0.35) 70%,
      rgba(6, 27, 46, 0.12) 100%
    );
}

.school-catalog-hero-inner {
  position: relative;
  z-index: 2;
  width: min(100%, 1280px);
  min-height: 470px;
  margin: 0 auto;
  padding: 64px 46px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.school-catalog-hero-inner > span,
.school-categories-heading > span {
  color: #00A6C8;
  font-size: 12px;
  line-height: 1.2;
  font-weight: 900;
  letter-spacing: 0.11em;
}

.school-catalog-hero h1 {
  max-width: 680px;
  margin: 14px 0 20px;
  font-size: clamp(48px, 6vw, 82px);
  line-height: 0.94;
  font-weight: 900;
  letter-spacing: -0.045em;
}

.school-catalog-hero p {
  max-width: 570px;
  margin: 0 0 28px;
  font-size: 18px;
  line-height: 1.5;
}

.school-catalog-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
}

.catalog-button {
  display: inline-flex;
  min-height: 48px;
  padding: 0 26px;
  align-items: center;
  justify-content: center;
  border-radius: 999px;
  text-decoration: none;
  font-size: 15px;
  font-weight: 900;
}

.catalog-button-primary {
  background: #009DBA;
  color: #ffffff;
}

.catalog-button-secondary {
  background: #ffffff;
  color: #061B2E;
}

.school-categories {
  width: min(100%, 1280px);
  margin: 0 auto;
  padding: 66px 40px 84px;
}

.school-categories-heading {
  max-width: 780px;
  margin-bottom: 38px;
}

.school-categories-heading h2 {
  margin: 12px 0 14px;
  color: #061B2E;
  font-size: clamp(38px, 5vw, 62px);
  line-height: 0.98;
  font-weight: 900;
  letter-spacing: -0.035em;
}

.school-categories-heading p {
  margin: 0;
  max-width: 680px;
  color: #314756;
  font-size: 17px;
  line-height: 1.5;
}

.school-category-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 28px;
}

.school-category-card {
  overflow: hidden;
  border-radius: 20px;
  background: #ffffff;
  box-shadow: 0 12px 34px rgba(6, 27, 46, 0.09);
  transition:
    transform 200ms ease,
    box-shadow 200ms ease;
}

.school-category-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 44px rgba(6, 27, 46, 0.14);
}

.school-category-image {
  height: 320px;
  overflow: hidden;
  background: #E6EEF2;
}

.school-category-image img {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
  object-position: center;
  transition: transform 400ms ease;
}

.school-category-card:hover img {
  transform: scale(1.025);
}

.school-category-content {
  padding: 24px 26px 28px;
}

.school-category-content h3 {
  margin: 0 0 10px;
  color: #061B2E;
  font-size: 25px;
  line-height: 1.15;
  font-weight: 900;
}

.school-category-content p {
  margin: 0 0 20px;
  color: #456070;
  font-size: 15px;
  line-height: 1.5;
}

.school-category-content a {
  color: #003B73;
  font-size: 14px;
  font-weight: 900;
  text-decoration: none;
}

.school-category-content a:hover {
  color: #009DBA;
}

@media (max-width: 800px) {
  .school-category-grid {
    grid-template-columns: 1fr;
  }

  .school-category-image {
    height: 290px;
  }
}

@media (max-width: 560px) {
  .school-catalog-hero-inner {
    padding: 48px 20px;
  }

  .school-catalog-hero h1 {
    font-size: 48px;
  }

  .school-categories {
    padding: 50px 18px 70px;
  }

  .school-category-image {
    height: 240px;
  }
}
"""
css += new_css

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Remove the JS filters
js_path = os.path.join(base_dir, 'js', 'main.js')
if os.path.exists(js_path):
    with open(js_path, 'r', encoding='utf-8') as f:
        js = f.read()
    js = re.sub(r'// =============================================\n// PRODUCTOS ESCOLARES.*$', '', js, flags=re.DOTALL)
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js)

print("HTML, CSS y JS actualizados.")
