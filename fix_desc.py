import os

base_dir = r"C:\Users\repre\Documents\Mro papeleria"
path = os.path.join(base_dir, "productos-escolares.html")

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix description manually
old_desc = '<meta name="description" content="Productos escolares de temporada en Mr.O Papelería: cuadernos, lápices, colores, mochilas, cartulinas, manualidades y material para tareas." />'
new_desc = '<meta name="description" content="Conoce las categorías de productos escolares, material de oficina y artículos creativos que puedes encontrar en Mr.O Papelería, Chilpancingo.">'

if old_desc in content:
    content = content.replace(old_desc, new_desc)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Description fixed.")
