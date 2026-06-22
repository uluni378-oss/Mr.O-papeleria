import os
import re
import shutil

base_dir = r'C:\Users\repre\Documents\Mro papeleria'
quarantine_dir = os.path.join(base_dir, '_cleanup_quarantine')

# 1. Rename images folder
old_img_dir = os.path.join(base_dir, 'assets', 'img', 'collages-escolares')
new_img_dir = os.path.join(base_dir, 'assets', 'img', 'productos-escolares')
if os.path.exists(old_img_dir) and not os.path.exists(new_img_dir):
    os.rename(old_img_dir, new_img_dir)

# 2. Restore and modify HTML
src_html = os.path.join(quarantine_dir, 'productos-escolares.html')
dst_html = os.path.join(base_dir, 'productos-escolares.html')

with open(src_html, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Update paths and classes
html_content = html_content.replace('collages-escolares', 'productos-escolares')
html_content = html_content.replace('ux-improvements.css', 'productos-escolares.css')
html_content = html_content.replace('class="school-products-page"', 'class="productos-escolares-page"')
html_content = html_content.replace('href="./index.html#inicio"', 'href="./index.html"')
html_content = html_content.replace('href="./index.html#papeleria"\n          class="catalog-button catalog-button-secondary"\n        >\n          Volver al inicio', 'href="./index.html"\n          class="catalog-button catalog-button-secondary"\n        >\n          Volver a Mr.O Papelería')
# Ensure single-line replacements in case the spacing is different
html_content = re.sub(r'href="\./index\.html#papeleria"[^>]*>\s*Volver al inicio', 'href="./index.html" class="catalog-button catalog-button-secondary">Volver a Mr.O Papelería', html_content)


with open(dst_html, 'w', encoding='utf-8') as f:
    f.write(html_content)

# 3. Restore CSS
src_css = os.path.join(quarantine_dir, 'css', 'ux-improvements.css')
dst_css = os.path.join(base_dir, 'css', 'productos-escolares.css')

with open(src_css, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Encapsulate under .productos-escolares-page where safe
new_css = []
for block in css_content.split('}'):
    block = block.strip()
    if not block:
        continue
    if block.startswith('@media'):
        new_css.append(block + '}')
        continue
    
    parts = block.split('{')
    if len(parts) == 2:
        selectors = parts[0].strip().split(',')
        new_selectors = []
        for sel in selectors:
            sel = sel.strip()
            # Do not encapsulate body or generic layout things that might break, but prompt requested to encapsulate
            # Since it's a separate file, it only affects the subpage anyway. We will prepend just for compliance.
            if sel.startswith('/*') or sel.startswith('@'):
                new_selectors.append(sel)
            else:
                new_selectors.append('.productos-escolares-page ' + sel)
        new_css.append(', '.join(new_selectors) + ' { ' + parts[1] + '}')

with open(dst_css, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_css))

# 4. Update index.html button
index_path = os.path.join(base_dir, 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    index_html = f.read()

index_html = re.sub(r'<a href="#papeleria" class="school-season-button">Ver papelería</a>', '<a href="./productos-escolares.html" class="school-season-button">Ver productos</a>', index_html)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Restoration successful.")
