import os
import re

html_path = r"C:\Users\repre\Documents\Mro papeleria\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

titles = [
    "Logotipos",
    "Tarjetas de presentación",
    "Diseño de lonas y banners",
    "Redes sociales",
    "Papelería para negocios",
    "Diseños promocionales para impresión"
]

images = []
pattern = r'<article class="business-card[^>]*>.*?<img src="([^"]+)" alt="([^"]+)".*?</article>'
matches = re.finditer(pattern, html, flags=re.DOTALL)
for match in matches:
    images.append({"src": match.group(1), "alt": match.group(2)})

print(f"Found {len(images)} images")

if len(images) == 6:
    new_cards = []
    for i in range(6):
        title = titles[i]
        src = images[i]["src"]
        alt = images[i]["alt"]
        
        card_html = f'''<article class="business-design-card business-design-reveal">
                <button class="business-design-preview" type="button" data-lightbox-title="{title}" aria-label="Ampliar ejemplo de {title.lower()}">
                  <figure class="business-design-card__media">
                    <img src="{src}" alt="{alt}" loading="lazy" decoding="async">
                    <span class="business-design-preview__zoom" aria-hidden="true">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>
                    </span>
                  </figure>
                </button>
                <h3 class="business-design-card__title">{title}</h3>
              </article>'''
        new_cards.append(card_html)
        
    grid_content = "\n              ".join(new_cards)
    
    grid_pattern = r'(<div class="business-grid">).*?(</div>\s*</div>\s*<div class="business-design-note")'
    
    html = re.sub(grid_pattern, r'\1\n              ' + grid_content + r'\n            \2', html, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print("HTML for business cards updated.")
