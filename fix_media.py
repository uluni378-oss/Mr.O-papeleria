import os
import re

css_path = r"C:\Users\repre\Documents\Mro papeleria\css\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

css = re.sub(
    r'(@media \(max-width: 1100px\) \{\s*\.quick-services__container \{\s*grid-template-columns: 1fr;\s*\}\s*)\.quick-services__grid \{\s*grid-template-columns: repeat\(3, minmax\(0, 1fr\)\);\s*\}',
    r'\1.quick-service-card {\n    flex-basis: calc((100% - 2rem) / 3);\n  }',
    css
)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("CSS media query fixed.")
