import os
import re

base_dir = r"C:\Users\repre\Documents\Mro papeleria"
html_path = os.path.join(base_dir, "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Remove the action buttons from HTML
action_btn_pattern = r'\s*<a class="quick-service-card__action"[^>]*>.*?</a>'
html = re.sub(action_btn_pattern, '', html, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

css_path = os.path.join(base_dir, "css", "styles.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Remove all action styles
css = re.sub(r'\.quick-service-card__action\s*\{[^}]*\}\s*', '', css)
css = re.sub(r'\.quick-service-card__action\s*svg\s*\{[^}]*\}\s*', '', css)
css = re.sub(r'\.quick-service-card__action:hover,\s*\.quick-service-card__action:focus-visible\s*\{[^}]*\}\s*', '', css)
css = re.sub(r'\.quick-service-card__action:focus-visible\s*\{[^}]*\}\s*', '', css)
css = re.sub(r'\.quick-service-card:focus-visible\s*\{[^}]*\}\s*', '', css)

# Revert content styling
css = re.sub(r'\.quick-service-card__content\s*\{\s*position:\s*relative;\s*display:\s*flex;\s*min-height:\s*145px;\s*flex-direction:\s*column;\s*padding:\s*1rem\s*3\.25rem\s*1rem\s*1rem;\s*\}',
             '.quick-service-card__content {\n  position: relative;\n  display: block;\n  min-height: auto;\n  padding: 1rem;\n}', css)

# Revert .quick-service-card__content h3 padding 
# Not required according to prompt, just padding of content div needs to be restored.

# Enforce cursor: default on the card
new_cursor_rule = '''
.quick-service-card {
  cursor: default !important;
}
'''
if "cursor: default !important;" not in css:
    css += new_cursor_rule

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Removed buttons and fixed styles securely.")
