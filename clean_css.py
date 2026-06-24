import os
import re

css_path = r"C:\Users\repre\Documents\Mro papeleria\css\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Fix leftover dangling selectors
css = re.sub(r'@media\s*\(min-width:\s*1025px\)\s*\{\s*\.quick-service-card:hover\s*\}', '', css)
css = re.sub(r'@media\s*\(prefers-reduced-motion:\s*reduce\)\s*\{\s*\}', '', css)

# Clean up duplicated action hover block
# Let's just remove the first instance of it since it was appended twice
css = re.sub(r'\.quick-service-card__action:hover,\s*\.quick-service-card__action:focus-visible\s*\{\s*transform:\s*translate\(2px,\s*-2px\);\s*background:\s*#07365c;\s*box-shadow:\s*0\s*10px\s*22px\s*rgba\(8,\s*52,\s*76,\s*0\.22\);\s*\}', '', css, count=1)
css = re.sub(r'\.quick-service-card__action:focus-visible\s*\{\s*outline:\s*3px\s*solid\s*#00a6c8;\s*outline-offset:\s*3px;\s*\}', '', css, count=1)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("CSS cleaned.")
