import os

files_to_update = [
    r"C:\Users\repre\Documents\Mro papeleria\index.html",
    r"C:\Users\repre\Documents\Mro papeleria\public_html\index.html"
]

replacements = [
    # 1. Título principal
    ("Páginas web para negocios locales", "Páginas web para empresas y negocios"),
    
    # 2. Texto descriptivo
    ("Creamos páginas informativas para que negocios locales puedan mostrar sus servicios, ubicación y formas de contacto.", "Creamos sitios informativos claros y adaptables para presentar tus servicios, ubicación y formas de contacto."),
    
    # 3. Texto secundario inferior
    ("Sitios informativos para negocios locales.", "Sitios informativos para empresas, comercios y profesionales."),
    
    # 4. Etiquetas y atributos de ejemplos web
    ('data-lightbox-title="Negocio local"', 'data-lightbox-title="Negocio"'),
    ('aria-label="Ampliar ejemplo de página web para negocio local"', 'aria-label="Ampliar ejemplo de página web para negocio"'),
    ('alt="Página para negocio local"', 'alt="Página para negocio"'),
    ('<span class="web-showcase__label">Negocio local</span>', '<span class="web-showcase__label">Negocio</span>'),
    
    # 5. Otras apariciones sobre páginas web / diseño
    ("páginas web para negocios locales", "páginas web para empresas y negocios"),
    ("emprendedores y pequeños negocios.", "empresas, comercios y profesionales.")
]

for filepath in files_to_update:
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Update complete")
