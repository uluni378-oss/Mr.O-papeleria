import os
import re

base_dir = r"C:\Users\repre\Documents\Mro papeleria"

def update_index():
    path = os.path.join(base_dir, "index.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Title and description
    content = re.sub(r'<title>.*?</title>', '<title>Mr.O Papelería | Escuela, oficina e impresiones en Chilpancingo</title>', content, count=1, flags=re.IGNORECASE|re.DOTALL)
    content = re.sub(r'<meta\s+name="description"\s+content="[^"]*"\s*>', '<meta name="description" content="Papelería en Chilpancingo con artículos escolares y de oficina, copias, impresiones, escaneo, trámites digitales básicos y atención por WhatsApp.">', content, count=1, flags=re.IGNORECASE)

    # Canonical and OG
    og_tags = """
  <link rel="canonical" href="https://uluni378-oss.github.io/Mr.O-papeleria/">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="es_MX">
  <meta property="og:title" content="Mr.O Papelería | Escuela, oficina e impresiones en Chilpancingo">
  <meta property="og:description" content="Papelería en Chilpancingo con artículos escolares y de oficina, copias, impresiones, escaneo, trámites digitales básicos y atención por WhatsApp.">
  <meta property="og:url" content="https://uluni378-oss.github.io/Mr.O-papeleria/">
  <meta property="og:image" content="https://uluni378-oss.github.io/Mr.O-papeleria/assets/img/social/mro-papeleria-og.webp">
"""
    if 'rel="canonical"' not in content:
        content = content.replace('</title>', '</title>\n' + og_tags)

    # Schema
    new_schema = """{
    "@context": "https://schema.org",
    "@type": "Store",
    "name": "Mr.O Papelería",
    "description": "Papelería para escuela y oficina con servicios de impresión, copias, trámites digitales y apoyo documental.",
    "telephone": "+52 747 101 3037",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Blvd. Vicente Guerrero 8L",
      "addressLocality": "Chilpancingo de los Bravo",
      "addressRegion": "Guerrero",
      "addressCountry": "MX"
    },
    "areaServed": "Chilpancingo, Guerrero",
    "url": "https://uluni378-oss.github.io/Mr.O-papeleria/"
  }"""
    content = re.sub(r'<script type="application/ld\+json">.*?</script>', '<script type="application/ld+json">\n  ' + new_schema + '\n  </script>', content, count=1, flags=re.IGNORECASE|re.DOTALL)

    # Mision y Vision
    mision_html = """
      <section id="mision-vision" class="mission-section" style="background: #ffffff; padding: 4rem 1rem;">
        <div class="container" style="max-width: 1000px; margin: 0 auto;">
          <div class="mission-grid" style="display: grid; gap: 3rem; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); align-items: center;">
            <div class="mission-copy reveal" style="display: flex; flex-direction: column; justify-content: center;">
              <span class="eyebrow" style="color: #009DBA; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.1em; display: block; margin-bottom: 0.5rem;">LO QUE HACEMOS HOY Y HACIA DÓNDE VAMOS</span>
              <h2 style="font-size: clamp(2rem, 3vw, 2.5rem); color: #07365c; margin-bottom: 2rem;">Misión y Visión</h2>
              
              <div class="mission-item" style="margin-bottom: 2rem; position: relative; padding-left: 3.5rem;">
                <span aria-hidden="true" style="position: absolute; left: 0; top: -5px; font-size: 2.2rem; font-weight: 900; color: #e6eef2; line-height: 1;">01</span>
                <h3 style="font-size: 1.25rem; color: #061b2e; margin-bottom: 0.5rem;">Misión</h3>
                <p style="color: #526677; font-size: 1.05rem; line-height: 1.6; margin: 0;">Facilitar a estudiantes, trabajadores, familias y pequeños negocios de Chilpancingo el acceso a productos de papelería, impresión, copias, trámites y apoyo digital, mediante una atención directa, soluciones claras y servicios confiables en un solo lugar.</p>
              </div>

              <div class="mission-item" style="position: relative; padding-left: 3.5rem;">
                <span aria-hidden="true" style="position: absolute; left: 0; top: -5px; font-size: 2.2rem; font-weight: 900; color: #e6eef2; line-height: 1;">02</span>
                <h3 style="font-size: 1.25rem; color: #061b2e; margin-bottom: 0.5rem;">Visión</h3>
                <p style="color: #526677; font-size: 1.05rem; line-height: 1.6; margin: 0;">Consolidar a Mr.O Papelería como una papelería local de referencia en Chilpancingo, reconocida por integrar escuela, oficina y servicios documentales con soluciones visuales y digitales, y crecer gradualmente hacia una atención más amplia para negocios y clientes mayoristas.</p>
              </div>
            </div>
            
            <div class="mission-visual reveal" style="border-radius: 16px; overflow: hidden; box-shadow: 0 10px 28px rgba(0,0,0,0.08); aspect-ratio: 4/3;">
              <img src="./assets/img/hero-papeleria.webp" alt="Mostrador e interior de Mr.O Papelería en Chilpancingo" width="800" height="600" loading="lazy" decoding="async" style="width: 100%; height: 100%; object-fit: cover; display: block;">
            </div>
          </div>
        </div>
      </section>
"""
    if "mision-vision" not in content:
        content = content.replace('</section>\n\n      <section class="section categories" id="servicios">', '</section>\n' + mision_html + '\n      <section class="section categories" id="servicios">')

    # Servicios Principales Images
    # 1. Copias e impresiones
    content = re.sub(r'<img src="\./assets/img/copias-impresiones\.webp"[^>]+>', '<img src="./assets/img/servicios-principales/copias-impresiones.webp" alt="Copiadora, impresora y documentos en escritorio limpio" width="800" height="600" loading="lazy" decoding="async" />', content)
    # 2. Material escolar
    content = re.sub(r'<img src="\./assets/img/escuela\.webp"[^>]+>', '<img src="./assets/img/servicios-principales/material-escolar.webp" alt="Cuadernos, lápices, colores y mochilas organizadas" width="800" height="600" loading="lazy" decoding="async" />', content)
    # 3. Oficina
    content = re.sub(r'<img src="\./assets/img/oficina\.webp"[^>]+>', '<img src="./assets/img/servicios-principales/articulos-oficina.webp" alt="Folders, carpetas, hojas y bolígrafos corporativos" width="800" height="600" loading="lazy" decoding="async" />', content)
    # 4. Trámites
    content = re.sub(r'<img src="\./assets/img/tramites\.webp"[^>]+>', '<img src="./assets/img/servicios-principales/tramites-documentos.webp" alt="Computadora e impresora para trámites y documentos" width="800" height="600" loading="lazy" decoding="async" />', content)
    # 5. Diseño grafico -> Identidad
    content = re.sub(r'<img src="\./assets/img/diseno-grafico\.webp"[^>]+>', '<img src="./assets/img/servicios-principales/diseno-negocios.webp" alt="Logotipo, tarjetas, banners y mockups profesionales" width="800" height="600" loading="lazy" decoding="async" />', content)
    # 6. Páginas web
    content = re.sub(r'<img src="\./assets/img/paginas-web\.webp"[^>]+>', '<img src="./assets/img/servicios-principales/paginas-web.webp" alt="Diseños completos de páginas web en dispositivos móviles" width="800" height="600" loading="lazy" decoding="async" />', content)

    # Fix headings in servicios principales
    content = content.replace('<h3>Trámites</h3>\n              <p>Trámites digitales y documentos.</p>', '<h3>Trámites y documentos</h3>\n              <p>Trámites digitales y servicios documentales.</p>')
    content = content.replace('<h3>Diseño gráfico</h3>\n              <p>Lonas, tarjetas, volantes y publicidad.</p>', '<h3>Diseño para negocios</h3>\n              <p>Logotipos, tarjetas y mockups profesionales.</p>')
    content = content.replace('<h3>Branding</h3>', '<h3>Identidad de marca</h3>')
    
    # Wait, the current categories are: Copias, Papeleria escolar, Servicios de oficina, Diseño grafico, Branding, Diseño web.
    # We need to change the titles of the cards:
    # 1. Copias e impresiones (already correct)
    # 2. Papelería escolar -> Material escolar
    content = content.replace('<h3>Papelería escolar</h3>', '<h3>Material escolar</h3>')
    # 3. Servicios de oficina -> Artículos de oficina
    content = content.replace('<h3>Servicios de oficina</h3>', '<h3>Artículos de oficina</h3>')
    # 4. Diseño gráfico -> Trámites y documentos
    content = content.replace('<h3>Diseño gráfico</h3>\n              <p>Lonas, tarjetas, volantes y publicidad.</p>', '<h3>Trámites y documentos</h3>\n              <p>Gestión de documentos y trámites digitales básicos.</p>')
    # 5. Branding -> Diseño para negocios
    content = content.replace('<h3>Branding</h3>\n              <p>Identidad de marca y logotipos.</p>', '<h3>Diseño para negocios</h3>\n              <p>Identidad visual, logotipos y material corporativo.</p>')
    # 6. Diseño web -> Páginas web
    content = content.replace('<h3>Diseño web</h3>', '<h3>Páginas web</h3>')

    # Fix icons texts
    content = content.replace('<div class="category-icon">D</div>', '<div class="category-icon">T</div>') # Trámites
    content = content.replace('<div class="category-icon">B</div>', '<div class="category-icon">D</div>') # Diseño
    content = content.replace('<div class="category-icon">P</div>', '<div class="category-icon">M</div>') # Material
    content = content.replace('<div class="category-icon">O</div>', '<div class="category-icon">A</div>') # Articulos

    # Replace SVG Banner escolar with WebP Banner
    content = content.replace('<img src="./assets/img/temporada-escolar-fondo.svg" alt="" />', '<img src="./assets/img/papeleria/banner-escolar-realista.webp" alt="Cuadernos, lápices y material escolar organizado" width="1920" height="800" loading="lazy" decoding="async" />')

    # Replace Branding text
    content = content.replace('<span class="section-kicker">BRANDING</span>', '<span class="section-kicker">IDENTIDAD DE MARCA</span>')

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def update_productos_escolares():
    path = os.path.join(base_dir, "productos-escolares.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # SEO tags
    content = re.sub(r'<title>.*?</title>', '<title>Productos escolares y de oficina | Mr.O Papelería</title>', content, count=1, flags=re.IGNORECASE|re.DOTALL)
    content = re.sub(r'<meta\s+name="description"\s+content="[^"]*"\s*>', '<meta name="description" content="Conoce las categorías de productos escolares, material de oficina y artículos creativos que puedes encontrar en Mr.O Papelería, Chilpancingo.">', content, count=1, flags=re.IGNORECASE)

    # Canonical and OG
    og_tags = """
    <link rel="canonical" href="https://uluni378-oss.github.io/Mr.O-papeleria/productos-escolares.html">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="es_MX">
    <meta property="og:title" content="Productos escolares y de oficina | Mr.O Papelería">
    <meta property="og:description" content="Conoce las categorías de productos escolares, material de oficina y artículos creativos que puedes encontrar en Mr.O Papelería, Chilpancingo.">
    <meta property="og:url" content="https://uluni378-oss.github.io/Mr.O-papeleria/productos-escolares.html">
    <meta property="og:image" content="https://uluni378-oss.github.io/Mr.O-papeleria/assets/img/social/mro-papeleria-og.webp">
"""
    if 'rel="canonical"' not in content:
        # Remove old og tags
        content = re.sub(r'<meta property="og:.*?".*?>\n', '', content, flags=re.IGNORECASE)
        content = content.replace('</title>', '</title>' + og_tags)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def update_sitemap_and_robots():
    sitemap_path = os.path.join(base_dir, "sitemap.xml")
    sitemap = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://uluni378-oss.github.io/Mr.O-papeleria/</loc></url>
  <url><loc>https://uluni378-oss.github.io/Mr.O-papeleria/productos-escolares.html</loc></url>
</urlset>"""
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap)
        
    robots_path = os.path.join(base_dir, "robots.txt")
    robots = """User-agent: *
Allow: /

Sitemap: https://uluni378-oss.github.io/Mr.O-papeleria/sitemap.xml"""
    with open(robots_path, "w", encoding="utf-8") as f:
        f.write(robots)

if __name__ == "__main__":
    update_index()
    update_productos_escolares()
    update_sitemap_and_robots()
    print("SEO and content updated successfully.")
