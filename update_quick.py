import os
import re

base_dir = r"C:\Users\repre\Documents\Mro papeleria"

# 1. HTML Update
html_path = os.path.join(base_dir, "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Match the <article> containing "Impresión de planos"
# Use re.DOTALL to match across lines
html = re.sub(r'<article class="quick-service-card quick-reveal"[^>]*>.*?Impresi&oacute;n de planos.*?</article>', '', html, flags=re.DOTALL)
html = re.sub(r'<article class="quick-service-card quick-reveal"[^>]*>.*?Impresi[oó]n de planos.*?</article>', '', html, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)


# 2. CSS Update
css_path = os.path.join(base_dir, "css", "styles.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Update .quick-services__grid
css = re.sub(
    r'\.quick-services__grid\s*\{\s*display:\s*grid;\s*grid-template-columns:\s*repeat\(4,\s*minmax\(0,\s*1fr\)\);\s*gap:\s*1rem;\s*\}',
    '.quick-services__grid {\n  display: flex;\n  flex-wrap: wrap;\n  justify-content: center;\n  gap: 1rem;\n}',
    css
)

# Update .quick-service-card to add flex basis
css = re.sub(
    r'\.quick-service-card\s*\{(\s*overflow:\s*hidden;\s*min-width:\s*0;)',
    r'.quick-service-card {\n  flex: 0 1 calc((100% - 3rem) / 4);\1',
    css
)

# Update media query 1100px
css = re.sub(
    r'@media \(max-width: 1100px\) \{\s*\.quick-services__grid \{\s*grid-template-columns: repeat\(3, minmax\(0, 1fr\)\);\s*\}\s*\}',
    '@media (max-width: 1100px) {\n  .quick-service-card {\n    flex-basis: calc((100% - 2rem) / 3);\n  }\n}',
    css
)

# Update media query 760px
css = re.sub(
    r'@media \(max-width: 760px\) \{\s*\.quick-services__grid \{\s*grid-template-columns: repeat\(2, minmax\(0, 1fr\)\);\s*\}\s*\}',
    '@media (max-width: 760px) {\n  .quick-service-card {\n    flex-basis: calc((100% - 1rem) / 2);\n  }\n}',
    css
)

# Update media query 480px
# Note: 480px also has .quick-services__cta { width: 100%; justify-content: center; }
css = re.sub(
    r'@media \(max-width: 480px\) \{\s*\.quick-services__grid \{\s*grid-template-columns: 1fr;\s*\}',
    '@media (max-width: 480px) {\n  .quick-service-card {\n    flex-basis: 100%;\n  }',
    css
)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Update completed.")
