import os
import re

css_path = r"C:\Users\repre\Documents\Mro papeleria\css\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# First remove my recently added .quick-service-card__action rules
css = re.sub(r'\.quick-service-card:focus-visible\s*\{[^}]*\}\s*', '', css)
css = re.sub(r'\.quick-service-card__action\s*\{[^}]*\}\s*', '', css)
css = re.sub(r'\.quick-service-card__action\s*svg\s*\{[^}]*\}\s*', '', css)
css = re.sub(r'\.quick-service-card:hover\s*\.quick-service-card__action,\s*\.quick-service-card:focus-visible\s*\.quick-service-card__action\s*\{[^}]*\}\s*', '', css)
css = re.sub(r'@media\s*\(prefers-reduced-motion:\s*reduce\)\s*\{\s*\.quick-service-card__action\s*\{[^}]*\}\s*\}\s*', '', css)

# Fix .quick-service-card__content styles to what user requested
# The user wants:
# .quick-service-card__content {
#   position: relative;
#   display: flex;
#   min-height: 150px;
#   flex-direction: column;
#   padding: 1rem 3.6rem 1rem 1rem;
# }
css = re.sub(r'\.quick-service-card__content\s*\{[^}]*\}', 
             '.quick-service-card__content {\n  position: relative;\n  display: flex;\n  min-height: 150px;\n  flex-direction: column;\n  padding: 1rem 3.6rem 1rem 1rem;\n}', css)

# .quick-service-card__content h3
css = re.sub(r'\.quick-service-card__content\s*h3\s*\{[^}]*\}',
             '.quick-service-card__content h3 {\n  margin: 0 0 0.4rem;\n  color: #07365c;\n  font-size: 1rem;\n  line-height: 1.2;\n}', css)

# .quick-service-card__content p
css = re.sub(r'\.quick-service-card__content\s*p\s*\{[^}]*\}',
             '.quick-service-card__content p {\n  margin: 0;\n  color: #596b79;\n  font-size: 0.86rem;\n  line-height: 1.45;\n}', css)

# Append new action styles
new_css = '''
.quick-service-card__action {
  position: absolute;
  right: 1rem;
  bottom: 1rem;
  display: grid;
  width: 2.35rem;
  height: 2.35rem;
  place-items: center;
  border-radius: 50%;
  background: #00a6c8;
  color: #ffffff;
  box-shadow: 0 8px 18px rgba(8, 52, 76, 0.16);
  transition:
    transform 0.25s ease,
    background-color 0.25s ease,
    box-shadow 0.25s ease;
}

.quick-service-card__action svg {
  width: 1.1rem;
  height: 1.1rem;
}

.quick-service-card__action:hover,
.quick-service-card__action:focus-visible {
  transform: translate(2px, -2px);
  background: #07365c;
  box-shadow: 0 10px 22px rgba(8, 52, 76, 0.22);
}

.quick-service-card__action:focus-visible {
  outline: 3px solid #00a6c8;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .quick-service-card__action {
    transform: none;
    transition: none;
  }
}
'''
css += new_css

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)
print("CSS updated.")
