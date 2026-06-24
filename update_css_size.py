import os
import re

css_path = r"C:\Users\repre\Documents\Mro papeleria\css\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# First, remove existing .quick-service-card__action blocks and related
css = re.sub(r'\.quick-service-card__action\s*\{[^}]*\}\s*', '', css)
css = re.sub(r'\.quick-service-card__action\s*svg\s*\{[^}]*\}\s*', '', css)
css = re.sub(r'\.quick-service-card__action:hover,\s*\.quick-service-card__action:focus-visible\s*\{[^}]*\}\s*', '', css)
css = re.sub(r'\.quick-service-card__action:focus-visible\s*\{[^}]*\}\s*', '', css)
css = re.sub(r'@media\s*\(prefers-reduced-motion:\s*reduce\)\s*\{\s*\.quick-service-card__action\s*\{[^}]*\}\s*\}\s*', '', css)

# Fix .quick-service-card__content styles to what user requested
css = re.sub(r'\.quick-service-card__content\s*\{[^}]*\}', 
             '.quick-service-card__content {\n  position: relative;\n  display: flex;\n  min-height: 145px;\n  flex-direction: column;\n  padding: 1rem 3.25rem 1rem 1rem;\n}', css)

# Append new action styles
new_css = '''
.quick-service-card__action {
  position: absolute;
  right: 0.85rem;
  bottom: 0.85rem;
  display: grid;
  width: 32px;
  height: 32px;
  min-width: 32px;
  min-height: 32px;
  aspect-ratio: 1 / 1;
  place-items: center;
  padding: 0;
  border: 0;
  border-radius: 50%;
  flex: 0 0 32px;
  align-self: auto;
  background: #00a6c8;
  color: #ffffff;
  box-shadow: 0 5px 12px rgba(8, 52, 76, 0.14);
  cursor: pointer;
  transition:
    transform 0.2s ease,
    background-color 0.2s ease,
    box-shadow 0.2s ease;
}

.quick-service-card__action svg {
  display: block;
  width: 14px;
  height: 14px;
  flex: none;
}

.quick-service-card__action:hover,
.quick-service-card__action:focus-visible {
  transform: translate(1px, -1px);
  background: #07365c;
  box-shadow: 0 7px 16px rgba(8, 52, 76, 0.2);
}

.quick-service-card__action:focus-visible {
  outline: 2px solid #00a6c8;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .quick-service-card__action {
    transform: none;
    transition: none;
  }
}
'''
if '.quick-service-card__action' not in css:
    css += new_css

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("CSS sizing updated.")
