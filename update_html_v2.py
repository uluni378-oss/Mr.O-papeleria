import os
import re

base_dir = r"C:\Users\repre\Documents\Mro papeleria"
path = os.path.join(base_dir, "index.html")

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Misión y Visión
mision_old = "Facilitar a estudiantes, trabajadores, familias y pequeños negocios de Chilpancingo el acceso a productos de papelería, impresión, copias, trámites y apoyo digital, mediante una atención directa, soluciones claras y servicios confiables en un solo lugar."
mision_new = "Resolver necesidades de papelería, impresión, copias, trámites y apoyo digital para estudiantes, familias, trabajadores y pequeños negocios de Chilpancingo, con atención directa y servicios confiables."
content = content.replace(mision_old, mision_new)

vision_old = "Consolidar a Mr.O Papelería como una papelería local de referencia en Chilpancingo, reconocida por integrar escuela, oficina y servicios documentales con soluciones visuales y digitales, y crecer gradualmente hacia una atención más amplia para negocios y clientes mayoristas."
vision_new = "Consolidar a Mr.O Papelería como una referencia local en escuela, oficina y servicios documentales, ampliando gradualmente la atención a negocios y clientes mayoristas."
content = content.replace(vision_old, vision_new)

img_mision_old = '<img src="./assets/img/hero-papeleria.webp" alt="Mostrador e interior de Mr.O Papelería en Chilpancingo"'
img_mision_new = '<img src="./assets/img/local/mision-vision-interior.webp" alt="Mostrador e interior de Mr.O Papelería en Chilpancingo"'
content = content.replace(img_mision_old, img_mision_new)

# 2. Impresión de planos -> Digitalización de archivos
planos_old = """<article class="quick-card reveal">
              <img src="./assets/img/servicios-rapidos/impresion-planos.webp" alt="Impresión de planos" loading="lazy" />
              <h3>Impresión de planos</h3>
              <p>Formatos amplios en blanco y negro o color.</p>
            </article>"""
planos_new = """<article class="quick-card reveal">
              <img src="./assets/img/servicios-rapidos/digitalizacion.webp" alt="Digitalización de archivos y escáner" loading="lazy" />
              <h3>Digitalización de archivos</h3>
              <p>Conversión de documentos físicos a archivos digitales para guardar, compartir o respaldar.</p>
            </article>"""
if planos_old in content:
    content = content.replace(planos_old, planos_new)
else:
    # try regex just in case
    content = re.sub(r'<article class="quick-card reveal">\s*<img src="\./assets/img/servicios-rapidos/impresion-planos\.webp"[^>]+>\s*<h3>Impresión de planos</h3>\s*<p>[^<]+</p>\s*</article>', planos_new, content)


# 3. Diseño para negocios
content = content.replace("Cotizar branding", "Consultar diseño visual")

list_old = "Logotipo &middot; Colores de marca &middot; Papeler&iacute;a &middot; Redes sociales &middot; Material promocional"
list_new = "Logotipo &middot; Colores de marca &middot; Tarjetas &middot; Redes sociales &middot; Papelería para negocios &middot; Diseños listos para impresión"
content = content.replace(list_old, list_new)

# Lonas y banners
lonas_old = """<div class="business-card reveal">
            <div class="business-art">
              <img src="./assets/img/diseno-negocios/lonas-banners.png" alt="Lonas y banners" class="business-design-preview" loading="lazy" />
            </div>
            <h3>Lonas y banners</h3>
            <p>Diseños atractivos para exteriores e interiores que captan la atención.</p>
          </div>"""
lonas_new = """<div class="business-card reveal">
            <div class="business-art">
              <img src="./assets/img/diseno-negocios/lonas-banners-v2.webp" alt="Diseño de lonas y banners" class="business-design-preview" loading="lazy" />
            </div>
            <h3>Diseño de lonas y banners</h3>
            <p>Creamos el diseño y entregamos el archivo listo para imprimir con el proveedor de tu confianza.</p>
          </div>"""
if lonas_old in content:
    content = content.replace(lonas_old, lonas_new)
else:
    content = re.sub(r'<div class="business-card reveal">\s*<div class="business-art">\s*<img src="\./assets/img/diseno-negocios/lonas-banners\.(?:webp|png)" alt="Lonas y banners" class="business-design-preview" loading="lazy" />\s*</div>\s*<h3>Lonas y banners</h3>\s*<p>Diseños atractivos para exteriores e interiores que captan la atención.</p>\s*</div>', lonas_new, content)


# Papelería corporativa -> Papelería para negocios
content = content.replace("<h3>Papelería corporativa</h3>", "<h3>Papelería para negocios</h3>")

# Impresos promocionales -> Diseños promocionales para impresión
content = content.replace("<h3>Impresos promocionales</h3>", "<h3>Diseños promocionales para impresión</h3>")

# Add disclaimer below cards
if "business-disclaimer" not in content:
    disclaimer = '\n        <p class="business-disclaimer" style="text-align: center; font-size: 0.9rem; color: #526677; margin-top: 2rem;">Entregamos archivos digitales listos para impresión. La producción de lonas y otros formatos de gran tamaño se realiza con el proveedor que el cliente elija.</p>\n      </section>'
    content = content.replace('      </section>\n\n      <!-- PÁGINAS WEB -->', disclaimer + '\n\n      <!-- PÁGINAS WEB -->')

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Update completed.")
