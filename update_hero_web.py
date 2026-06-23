import os
import re

base_dir = r'C:\Users\repre\Documents\Mro papeleria'
index_path = os.path.join(base_dir, 'index.html')

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Corregir textos de Páginas Web
content = content.replace(
    'Creamos sitios informativos claros y responsivos para mostrar tus servicios, ubicación y formas de contacto.</p>',
    'Creamos sitios informativos claros y adaptables para presentar tus servicios, ubicación y formas de contacto.</p>'
)

content = content.replace(
    'Sitios de presentación empresarial. No tiendas en línea.</p>',
    'Sitios informativos para negocios locales.</p>'
)

# 2. Corregir beneficios de Páginas Web
content = content.replace('<div class="web-benefit">Secciones claras de servicios.</div>', '<div class="web-benefit">Secciones claras para tus servicios.</div>')
content = content.replace('<div class="web-benefit">WhatsApp y ubicación.</div>', '<div class="web-benefit">WhatsApp, ubicación y datos de contacto.</div>')
content = content.replace('<div class="web-benefit">Optimización básica para búsqueda local.</div>', '<div class="web-benefit">Presencia digital clara y profesional.</div>')

# 3. Sustituir imagen principal del hero
old_img_pattern = r'<img src="\./assets/img/hero-papeleria\.webp"[^>]*>'
new_img_tag = '<img src="./assets/img/hero-mro-papeleria.webp" alt="Útiles escolares, libreta, lápices y estuche de Mr.O Papelería" width="1792" height="1024" loading="eager" decoding="async" fetchpriority="high">'
content = re.sub(old_img_pattern, new_img_tag, content)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Update CSS
css_path = os.path.join(base_dir, 'css', 'styles.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Modify .hero-photo img block
old_css_img = '''.hero-photo img {
  width: 100%;
  aspect-ratio: 1200 / 620;
  height: auto;
  object-fit: contain;
}'''

new_css_img = '''.hero-photo img {
  display: block;
  width: 100%;
  aspect-ratio: 1200 / 620;
  height: 100%;
  object-fit: cover;
  object-position: 48% 50%;
}'''

if old_css_img in css_content:
    css_content = css_content.replace(old_css_img, new_css_img)
else:
    # If indentation is different, we use regex
    css_content = re.sub(
        r'\.hero-photo img\s*\{\s*width:\s*100%;\s*aspect-ratio:\s*1200\s*/\s*620;\s*height:\s*auto;\s*object-fit:\s*contain;\s*\}',
        new_css_img,
        css_content
    )

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Update completed.")
