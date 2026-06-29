import os

# Tarea 1: index.html
index_path = r"C:\Users\repre\Documents\Mro papeleria\index.html"
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Identidad de marca -> Trámites y documentos
# Original:
# <h3>Identidad de marca</h3>
# <p>Identidad de marca y logotipos.</p>
index_content = index_content.replace(
    "<h3>Identidad de marca</h3>\n              <p>Identidad de marca y logotipos.</p>",
    "<h3>Trámites y documentos</h3>\n              <p>Apoyo en trámites digitales básicos.</p>"
)

# Páginas web -> Copias e impresiones
# Original:
# <h3>Páginas web</h3>
# <p>Tu negocio en línea con diseño profesional.</p>
index_content = index_content.replace(
    "<h3>Páginas web</h3>\n              <p>Tu negocio en línea con diseño profesional.</p>",
    "<h3>Copias e impresiones</h3>\n              <p>Servicios de impresión documental y copiado.</p>"
)

# Tarea 3: index.html
# Footer navigation
# Original:
# <a href="#paginas-web">Páginas web</a>
# Wait, let's look at the nav block in the footer:
# <nav aria-label="Servicios">
#   <h3>Servicios</h3>
#   ...
#   <a href="#paginas-web">Páginas web</a>
# </nav>
# I will just replace the specific text in the footer.
# Let's find the specific block to avoid replacing the header link if possible. Or maybe replace all if they are the same?
# "Busca el enlace de texto que dice 'Páginas web'. Sustituye ese texto exacto por 'Diseño para negocios'."
# Let's just replace `<a href="#paginas-web">Páginas web</a>` with `<a href="#paginas-web">Diseño para negocios</a>` where it is inside `<nav aria-label="Servicios">`.

import re
nav_pattern = r'(<nav aria-label="Servicios">.*?</nav>)'
def nav_repl(match):
    nav_block = match.group(1)
    nav_block = nav_block.replace('>Páginas web</a>', '>Diseño para negocios</a>')
    return nav_block

index_content = re.sub(nav_pattern, nav_repl, index_content, flags=re.DOTALL)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_content)

# Tarea 2: productos-escolares.html
prod_path = r"C:\Users\repre\Documents\Mro papeleria\productos-escolares.html"
with open(prod_path, 'r', encoding='utf-8') as f:
    prod_content = f.read()

# Replace H1 and add subtitle
# Original:
# <h1>Todo para el regreso a clases</h1>
prod_content = prod_content.replace(
    "<h1>Todo para el regreso a clases</h1>",
    "<h1>Artículos Escolares y Material de Oficina</h1>\n        <p class=\"hero-lead hero-reveal-up\" style=\"transition-delay: 150ms; font-size: 1.25rem; font-weight: 500; color: #07365c; margin-top: 1rem;\">Todo para el regreso a clases.</p>"
)

with open(prod_path, 'w', encoding='utf-8') as f:
    f.write(prod_content)

print("Modificaciones aplicadas exitosamente.")
