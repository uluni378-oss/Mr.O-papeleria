import os
import re

base_dir = r"C:\Users\repre\Documents\Mro papeleria"
html_path = os.path.join(base_dir, "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove the previously added span
html = re.sub(r'\s*<span class="quick-service-whatsapp">Consultar por WhatsApp &rarr;</span>', '', html)

# 2. Refactor the cards
def refactor_card(match):
    article_attr = match.group(1)
    a_tag = match.group(2)
    inner_content = match.group(3)
    
    # Extract href and aria-label
    href_match = re.search(r'href="([^"]+)"', a_tag)
    aria_match = re.search(r'aria-label="([^"]+)"', a_tag)
    
    href = href_match.group(1) if href_match else "#"
    aria = aria_match.group(1) if aria_match else ""
    
    new_action = f'''
            <a class="quick-service-card__action" href="{href}" target="_blank" rel="noopener noreferrer" aria-label="{aria}">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <path d="M7 17 17 7"></path>
                <path d="M7 7h10v10"></path>
              </svg>
            </a>'''
            
    # We need to insert `new_action` inside `<div class="quick-service-card__content">` right before `</div>`
    # Let's use string manipulation on inner_content
    # inner_content looks like:
    # <figure ...> ... </figure>
    # <div class="quick-service-card__content">
    #   <h3>...</h3>
    #   <p>...</p>
    # </div>
    
    # Let's replace `</div>` at the end of inner_content with the action button and then `</div>`
    # We must match the LAST </div> in the inner_content.
    parts = inner_content.rsplit('</div>', 1)
    if len(parts) == 2:
        new_inner = parts[0] + new_action + '\n          </div>'
    else:
        new_inner = inner_content
        
    return f'<article {article_attr}>\n        {new_inner.strip()}\n      </article>'

pattern = r'<article ([^>]+)>\s*(<a [^>]+>)\s*(.*?)\s*</a>\s*</article>'
# Note: Since there could be other articles, we must be careful.
# The user's articles are: <article class="quick-service-card quick-reveal">
pattern = r'<article (class="quick-service-card[^"]*")>\s*(<a [^>]+>)\s*(.*?)\s*</a>\s*</article>'

html = re.sub(pattern, refactor_card, html, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)


# Update CSS
css_path = os.path.join(base_dir, "css", "styles.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# First, clean up .quick-service-whatsapp if present
css = re.sub(r'\.quick-service-whatsapp\s*\{[^}]*\}\s*', '', css)
css = re.sub(r'@media\s*\(min-width:\s*1025px\)\s*\{\s*\.quick-service-whatsapp\s*\{[^}]*\}\s*\.quick-service-card:hover\s*\.quick-service-whatsapp\s*\{[^}]*\}\s*\}\s*', '', css)

# Fix .quick-service-card__content styles to what user requested
css = re.sub(r'\.quick-service-card__content\s*\{[^}]*\}', 
             '.quick-service-card__content {\n  position: relative;\n  display: flex;\n  min-height: 150px;\n  flex-direction: column;\n  padding: 1rem 3.6rem 1rem 1rem;\n}', css)

# .quick-service-card__content h3
css = re.sub(r'\.quick-service-card__content\s*h3\s*\{[^}]*\}',
             '.quick-service-card__content h3 {\n  margin: 0 0 0.4rem;\n  color: #07365c;\n  font-size: 1rem;\n  line-height: 1.2;\n}', css)

# .quick-service-card__content p
css = re.sub(r'\.quick-service-card__content\s*p\s*\{[^}]*\}',
             '.quick-service-card__content p {\n  margin: 0;\n  color: #596b79;\n  font-size: 0.86rem;\n  line-height: 1.45;\n}', css)

# Clean up .quick-service-card cursor pointer if needed, but the user said "Mantener cursor: pointer"
# I'll just append the action styles

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
if '.quick-service-card__action' not in css:
    css += new_css

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Applied quick card refactor.")
