import os
import re

base_dir = r"C:\Users\repre\Documents\Mro papeleria"
html_path = os.path.join(base_dir, "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Fix the accidental replace in .categories
bad_replace = '<p class="eyebrow hero-reveal-left" style="transition-delay: 0ms;">Servicios principales</p>'
good_replace = '<p class="eyebrow">Servicios principales</p>'
html = html.replace(bad_replace, good_replace)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Accidental replacement fixed.")
