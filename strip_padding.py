import os
import re

base_dir = r"C:\Users\repre\Documents\Mro papeleria"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace inline padding
html = re.sub(
    r'<section id="mision-vision" class="mission-section" style="background: #ffffff; padding: 4rem 1rem;">',
    '<section id="mision-vision" class="mission-section mission-vision section" style="background: #ffffff;">',
    html
)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Inline padding removed from HTML.")
