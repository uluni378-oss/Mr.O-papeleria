import os
import re

project_dir = r'C:\Users\repre\Documents\Mro papeleria'

# 1. Update index.html
html_path = os.path.join(project_dir, 'index.html')
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('identidad-completa.webp', 'identidad-completa-realista.webp')
html = html.replace('logotipo-profesional.webp', 'logotipo-realista.webp')
html = html.replace('banners-redes.webp', 'banners-redes-realista.webp')
html = html.replace('tarjetas-profesionales.webp', 'tarjetas-presentacion-realistas.webp')
html = html.replace('papeleria-comercial.webp', 'papeleria-comercial-realista.webp')
html = html.replace('material-promocional.webp', 'material-promocional-realista.webp')

# Update alt texts
html = html.replace('alt="Identidad visual completa aplicada a un negocio local"', 'alt="Presentación fotorrealista de identidad visual completa para un negocio local"')
html = html.replace('alt="Mockup profesional de diseño de logotipo para un negocio local"', 'alt="Bocetos y presentación profesional de un logotipo para negocio local"')
html = html.replace('alt="Diseños coordinados para promociones, avisos y publicaciones"', 'alt="Mockups realistas de banners y publicaciones digitales para un negocio local"')
html = html.replace('alt="Tarjetas de presentación profesionales para un negocio local"', 'alt="Tarjetas de presentación impresas con acabado profesional"')
html = html.replace('alt="Papelería comercial con hoja membretada, sobre, carpeta y tarjeta"', 'alt="Papelería comercial con hojas, sobres, carpetas y tarjetas coordinadas"')
html = html.replace('alt="Material promocional impreso para un negocio local"', 'alt="Volantes, folletos, carteles y material promocional impreso"')

# Add specific modifiers to article classes
html = html.replace('<article class="identity-card identity-card--featured reveal">', '<article class="identity-card identity-card--featured identity-card--complete reveal">')
html = html.replace('<article class="identity-card reveal">\n          <img src="./assets/img/identidad-marca/logotipo-realista.webp"', '<article class="identity-card identity-card--logo reveal">\n          <img src="./assets/img/identidad-marca/logotipo-realista.webp"')
html = html.replace('<article class="identity-card reveal">\n          <img src="./assets/img/identidad-marca/banners-redes-realista.webp"', '<article class="identity-card identity-card--digital reveal">\n          <img src="./assets/img/identidad-marca/banners-redes-realista.webp"')
html = html.replace('<article class="identity-card reveal">\n          <img src="./assets/img/identidad-marca/tarjetas-presentacion-realistas.webp"', '<article class="identity-card identity-card--cards reveal">\n          <img src="./assets/img/identidad-marca/tarjetas-presentacion-realistas.webp"')
html = html.replace('<article class="identity-card reveal">\n          <img src="./assets/img/identidad-marca/papeleria-comercial-realista.webp"', '<article class="identity-card identity-card--stationery reveal">\n          <img src="./assets/img/identidad-marca/papeleria-comercial-realista.webp"')
html = html.replace('<article class="identity-card reveal">\n          <img src="./assets/img/identidad-marca/material-promocional-realista.webp"', '<article class="identity-card identity-card--promo reveal">\n          <img src="./assets/img/identidad-marca/material-promocional-realista.webp"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update CSS
css_path = os.path.join(project_dir, 'css', 'styles.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace identity-card base
old_card = """.identity-card {
  position: relative;
  overflow: hidden;
  min-height: 250px;
  border-radius: 24px;
  background: #0b2135;
  box-shadow: 0 24px 65px rgba(8, 38, 58, 0.16);
  transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.4s ease;
}"""
new_card = """.identity-card {
  position: relative;
  overflow: hidden;
  min-height: 250px;
  border-radius: 22px;
  background: #dfe7eb;
  box-shadow: 0 22px 58px rgba(8, 37, 58, 0.18);
  transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.4s ease;
}"""
css = css.replace(old_card, new_card)

old_img = """.identity-card img {
  width: 100%;
  height: 100%;
  min-height: inherit;
  display: block;
  object-fit: cover;
  object-position: center;
  transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1);
}"""
new_img = """.identity-card img {
  width: 100%;
  height: 100%;
  min-height: inherit;
  display: block;
  object-fit: cover;
  object-position: center;
  filter: saturate(1.03) contrast(1.02);
  transition: transform 0.55s ease, filter 0.55s ease;
}"""
css = css.replace(old_img, new_img)

old_hover_img = """.identity-card:hover img {
  transform: scale(1.035);
}"""
new_hover_img = """.identity-card:hover img {
  transform: scale(1.035);
  filter: saturate(1.08) contrast(1.04);
}"""
css = css.replace(old_hover_img, new_hover_img)

old_after = """.identity-card::after {
  content: "";
  position: absolute;
  inset: 40% 0 0;
  background: linear-gradient(180deg, rgba(5, 25, 40, 0), rgba(5, 25, 40, 0.88));
  pointer-events: none;
}"""
new_after = """.identity-card::after {
  content: "";
  position: absolute;
  inset: 45% 0 0;
  background: linear-gradient(180deg, rgba(5, 25, 40, 0), rgba(5, 25, 40, 0.88) 78%, rgba(5, 25, 40, 0.96) 100%);
  pointer-events: none;
}"""
css = css.replace(old_after, new_after)

# Add specific framing classes
specific_classes = """
.identity-card--complete img { object-position: 50% 50%; }
.identity-card--logo img { object-position: 52% 48%; }
.identity-card--digital img { object-position: 55% 50%; }
.identity-card--cards img { object-position: 50% 55%; }
.identity-card--stationery img { object-position: 50% 48%; }
.identity-card--promo img { object-position: 50% 52%; }
"""

if ".identity-card--complete img" not in css:
    css += specific_classes

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("HTML and CSS successfully updated.")
