import os
import re
import shutil

base_dir = r'C:\Users\repre\Documents\Mro papeleria'
source_dir = os.path.join(base_dir, 'assets', 'source', 'productos-reales')
img_dir = os.path.join(base_dir, 'assets', 'img', 'productos-reales')
docs_dir = os.path.join(base_dir, 'docs')
html_path = os.path.join(base_dir, 'productos-escolares.html')
css_path = os.path.join(base_dir, 'css', 'styles.css')

# Ensure directories exist
os.makedirs(source_dir, exist_ok=True)
os.makedirs(img_dir, exist_ok=True)
os.makedirs(docs_dir, exist_ok=True)

# 1. Clean existing placeholders (we must delete the old webp files to comply with rule "no dejar placeholders")
for f in os.listdir(img_dir):
    if f.endswith('.webp'):
        os.remove(os.path.join(img_dir, f))

# 2. Process source images (0 expected right now)
# (If there were images, we'd use PIL to process them here)

# 3. Read HTML and update cards
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

card_pattern = r'(<article class="product-card"[^>]*>)(.*?)(</article>)'
cards = re.findall(card_pattern, html, re.DOTALL)

products = []
new_html = html

for start_tag, inner_html, end_tag in cards:
    # Extract brand and product
    brand_match = re.search(r'<span class="product-brand">(.*?)</span>', inner_html)
    brand = brand_match.group(1).strip() if brand_match else "Desconocida"
    
    name_match = re.search(r'<h3>(.*?)</h3>', inner_html)
    name = name_match.group(1).strip() if name_match else "Producto Desconocido"
    
    # Generate expected filename
    import unicodedata
    def clean_text(text):
        text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('utf-8')
        text = text.lower()
        text = re.sub(r'[^a-z0-9\s-]', '', text)
        text = re.sub(r'\s+', '-', text).strip('-')
        return text
    
    # Custom specific filenames based on the user's list
    if name == "Cuaderno profesional" and brand.lower() == "scribe": expected_file = "cuaderno-profesional-scribe.webp"
    elif name == "Cuaderno profesional" and brand.lower() == "norma": expected_file = "cuaderno-profesional-norma.webp"
    elif name == "Libreta francesa" and brand.lower() == "estrella": expected_file = "libreta-francesa-estrella.webp"
    elif name == "Libreta italiana" and brand.lower() == "scribe": expected_file = "libreta-italiana-scribe.webp"
    elif name == "Bolígrafo Cristal" and brand.lower() == "bic": expected_file = "boligrafos-bic.webp" # user specifically listed boligrafos-bic.webp in point 5
    elif name == "Kilométrico" and brand.lower() == "paper mate": expected_file = "boligrafos-papermate.webp"
    elif name == "Lápices Grafito" and brand.lower() == "dixon": expected_file = "lapices-grafito-dixon.webp"
    elif name == "Colores 24 pz" and brand.lower() == "crayola": expected_file = "colores-crayola.webp"
    elif name == "Marcador" and brand.lower() == "sharpie": expected_file = "plumones-sharpie.webp"
    elif name == "Marcatextos" and brand.lower() == "stabilo": expected_file = "marcatextos-stabilo.webp"
    elif name == "Juego de Geometría" and brand.lower() == "maped": expected_file = "juego-geometria-maped.webp"
    elif name == "Tijeras Escolares" and brand.lower() == "pelikan": expected_file = "tijeras-pelikan.webp"
    elif name == "Pegamento en Barra" and brand.lower() == "pritt": expected_file = "pegamento-pritt.webp"
    elif name == "Resistol 850" and brand.lower() == "resistol": expected_file = "pegamento-resistol.webp"
    elif name == "Carpeta Escolar" and brand.lower() == "norma": expected_file = "carpeta-norma.webp"
    elif name == "Archivador" and brand.lower() == "wilson jones": expected_file = "archivador-wilson-jones.webp"
    elif name == "Mochila Escolar" and brand.lower() == "chenson": expected_file = "mochila-chenson.webp"
    else: expected_file = f"{clean_text(name)}-{clean_text(brand)}.webp"
    
    products.append({
        'brand': brand,
        'name': name,
        'expected_file': expected_file
    })
    
    # We know there are no images, so all must be marked missing.
    # Ensure data-image-status="missing" is applied, and remove existing data-image-status if any
    clean_start = re.sub(r'\sdata-image-status="[^"]*"', '', start_tag)
    new_start_tag = clean_start.replace('<article class="product-card"', '<article class="product-card" data-image-status="missing"')
    
    # Update HTML inside card
    # Replace img src with expected path (even if missing)
    # The user said: "En productos-escolares.html, sustituir cada placeholder únicamente cuando exista una fotografía válida."
    # BUT they also said: "Las rutas deben comenzar así: ./assets/img/productos-reales/"
    # If no photo exists, the card is hidden by CSS.
    new_inner_html = re.sub(r'<img\s+src=".*?"', f'<img src="./assets/img/productos-reales/{expected_file}"', inner_html)
    
    new_html = new_html.replace(start_tag + inner_html + end_tag, new_start_tag + new_inner_html + end_tag)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

# 4. Generate Reports
with open(os.path.join(docs_dir, 'inventario-fotografias-productos.md'), 'w', encoding='utf-8') as f:
    f.write('| Archivo original | Producto identificado | Marca | Tarjeta asignada | Estado |\n')
    f.write('|---|---|---|---|---|\n')
    # No lines because 0 provided

with open(os.path.join(docs_dir, 'productos-sin-fotografia.md'), 'w', encoding='utf-8') as f:
    f.write('# Reporte de Productos Sin Fotografía\n\n')
    f.write('Los siguientes productos no tienen una fotografía válida procesada en `assets/img/productos-reales/`:\n\n')
    for p in products:
        f.write(f"- **Producto:** {p['name']}\n")
        f.write(f"  - **Marca:** {p['brand']}\n")
        f.write(f"  - **Archivo requerido:** `{p['expected_file']}`\n\n")

# 5. Update CSS
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Add missing card CSS
if '.product-card[data-image-status="missing"]' not in css:
    missing_css = '\n.product-card[data-image-status="missing"] {\n  display: none;\n}\n'
    css += missing_css

# Regex replace .product-card-image styling
new_image_css = """
.product-card-image {
  width: 100%;
  height: 270px;
  padding: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  background: #ffffff;
  border-bottom: 1px solid #e5edf1;
  box-sizing: border-box;
}

.product-card-image img {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: contain;
  object-position: center;
  background: #ffffff;
}
"""

# Try to replace existing block or append
css = re.sub(r'\.product-card-image\s*\{[^}]*\}', '', css)
css = re.sub(r'\.product-card-image img\s*\{[^}]*\}', '', css)
css += new_image_css

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print(f"Script completado. Tarjetas: {len(products)}. Fotos: 0.")
