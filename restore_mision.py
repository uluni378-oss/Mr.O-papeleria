import os

base_dir = r"C:\Users\repre\Documents\Mro papeleria"
path = os.path.join(base_dir, "index.html")

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

mision_wrong = "Resolver necesidades de papelería, impresión, copias, trámites y apoyo digital para estudiantes, familias, trabajadores y pequeños negocios de Chilpancingo, con atención directa y servicios confiables."
mision_correct = "Facilitar a estudiantes, trabajadores, familias y pequeños negocios de Chilpancingo el acceso a productos de papelería, impresión, copias, trámites y apoyo digital, mediante una atención directa, soluciones claras y servicios confiables en un solo lugar."

vision_wrong = "Consolidar a Mr.O Papelería como una referencia local en escuela, oficina y servicios documentales, ampliando gradualmente la atención a negocios y clientes mayoristas."
vision_correct = "Consolidar a Mr.O Papelería como una papelería local de referencia en Chilpancingo, reconocida por integrar escuela, oficina y servicios documentales con soluciones visuales y digitales, y crecer gradualmente hacia una atención más amplia para negocios y clientes mayoristas."

content = content.replace(mision_wrong, mision_correct)
content = content.replace(vision_wrong, vision_correct)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Mision y Vision restored to correct text.")
