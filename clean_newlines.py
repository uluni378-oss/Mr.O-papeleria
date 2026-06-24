import os
import re

css_path = r"C:\Users\repre\Documents\Mro papeleria\css\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Fix the dangling media query and extra newlines
css = re.sub(r'@media\s*\(prefers-reduced-motion:\s*reduce\)\s*\{\s*\}', '', css)
css = re.sub(r'\n{3,}', '\n\n', css)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("CSS extra newlines cleaned.")
