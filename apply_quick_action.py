import os
import re

base_dir = r"C:\Users\repre\Documents\Mro papeleria"
html_path = os.path.join(base_dir, "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace the specific span with the new button
old_span = r'\s*<span class="quick-service-whatsapp">Consultar por WhatsApp &rarr;</span>'
new_action_btn = '''
            <span class="quick-service-card__action" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M7 17 17 7"></path>
                <path d="M7 7h10v10"></path>
              </svg>
            </span>'''

# First remove all old span
html = re.sub(old_span, '', html)

# Then insert new action button
html = re.sub(r'(<div class="quick-service-card__content">\s*<h3>.*?</h3>\s*<p>.*?</p>)\s*(</div>)', 
              r'\1' + new_action_btn + '\n          \2', html, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

css_path = os.path.join(base_dir, "css", "styles.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Remove old quick-service-whatsapp rules
css = re.sub(r'\.quick-service-whatsapp\s*\{[^}]*\}\s*', '', css)
css = re.sub(r'@media\s*\(min-width:\s*1025px\)\s*\{\s*\.quick-service-whatsapp\s*\{[^}]*\}\s*\.quick-service-card:hover\s*\.quick-service-whatsapp\s*\{[^}]*\}\s*\}\s*', '', css)

# Update padding in .quick-service-card__content
css = re.sub(r'(\.quick-service-card__content\s*\{[^}]*?)padding:\s*1rem;([^}]*\})', r'\1padding: 1rem 3.75rem 1rem 1rem;\2', css)

# Add new CSS rules
new_css = '''
.quick-service-card:focus-visible {
  outline: 3px solid #00a6c8;
  outline-offset: 4px;
}

.quick-service-card__action {
  position: absolute;
  right: 1rem;
  bottom: 1rem;
  display: grid;
  width: 2.4rem;
  height: 2.4rem;
  place-items: center;
  border-radius: 50%;
  background: #00a6c8;
  color: #ffffff;
  box-shadow: 0 8px 20px rgba(8, 52, 76, 0.16);
  transition:
    transform 0.25s ease,
    background-color 0.25s ease,
    box-shadow 0.25s ease;
}

.quick-service-card__action svg {
  width: 1.15rem;
  height: 1.15rem;
}

.quick-service-card:hover .quick-service-card__action,
.quick-service-card:focus-visible .quick-service-card__action {
  transform: translate(2px, -2px);
  background: #07365c;
  box-shadow: 0 10px 24px rgba(8, 52, 76, 0.22);
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

print("Applied Quick Service button updates.")
