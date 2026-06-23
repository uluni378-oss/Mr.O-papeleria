import os
import re

base_dir = r"C:\Users\repre\Documents\Mro papeleria"

# 1. Update CSS
css_path = os.path.join(base_dir, "css", "styles.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Replace padding in .location-section
css = re.sub(
    r'\.location-section\s*\{\s*padding-block:\s*clamp\(.*?\);\s*\}',
    '.location-section {\n  height: auto;\n  min-height: 0;\n  margin-top: 0;\n  padding-top: clamp(2.5rem, 4vw, 4rem);\n  padding-bottom: clamp(3rem, 5vw, 5.5rem);\n}',
    css
)

# Replace padding in .web-section
css = re.sub(
    r'\.web-section\s*\{\s*padding-block:\s*clamp\(.*?\);\s*overflow:\s*hidden;\s*\}',
    '.web-section {\n  height: auto;\n  min-height: 0;\n  padding-top: clamp(3rem, 5vw, 5.5rem);\n  padding-bottom: clamp(2.5rem, 4vw, 4rem);\n  margin-bottom: 0;\n  overflow: hidden;\n}',
    css
)

# Add location-header styles if not present
if '.location-header' not in css:
    css += '''
.location-header {
  text-align: center;
  margin-bottom: clamp(1.5rem, 3vw, 2.5rem);
}
.location-header__badge {
  display: inline-block;
  background: rgba(0, 157, 186, 0.1);
  color: #009dba;
  font-size: 0.85rem;
  font-weight: 800;
  letter-spacing: 0.1em;
  padding: 0.5rem 1.25rem;
  border-radius: 100px;
  text-transform: uppercase;
}
'''
with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)


# 2. Update HTML
html_path = os.path.join(base_dir, "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Add the badge inside location-section
badge_html = '''<div class="location-header">
    <span class="location-header__badge">UBICACIÓN Y ATENCIÓN DIRECTA</span>
  </div>
  <div class="location-strip">'''

html = re.sub(r'<div class="location-strip">', badge_html, html, count=1)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Spacing fixed and badge added.")
