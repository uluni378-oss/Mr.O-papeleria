import re

css_path = r"C:\Users\repre\Documents\Mro papeleria\css\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Fix the broken media query
css = re.sub(r'@media\s*\(min-width:\s*1025px\)\s*\{\s*\.quick-service-card:hover\s*\}', '', css)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)
print("CSS fixed.")
