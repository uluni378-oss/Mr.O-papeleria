import re

html_path = r'C:\Users\repre\Documents\Mro papeleria\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace articles
def replace_article(match):
    label_text = match.group(1)
    img_src = match.group(2)
    img_alt = match.group(3)
    
    return f'''<article class="web-showcase__item web-reveal-stagger">
          <button class="web-preview" type="button" data-lightbox-src="{img_src}" data-lightbox-alt="{img_alt}" data-lightbox-title="{label_text}" aria-label="Ampliar ejemplo de página web para {label_text.lower()}">
            <img src="{img_src}" alt="{img_alt}" loading="lazy">
            <span class="web-showcase__label">{label_text}</span>
            <span class="web-preview__zoom" aria-hidden="true">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>
            </span>
          </button>
        </article>'''

pattern = r'<article class="web-showcase__item web-reveal-stagger">\s*<span class="web-showcase__label">([^<]+)</span>\s*<img src="([^"]+)" alt="([^"]+)" loading="lazy">\s*</article>'

content = re.sub(pattern, replace_article, content)

# Add Lightbox HTML before </body>
lightbox_html = '''
<div class="image-lightbox" id="image-lightbox" role="dialog" aria-modal="true" aria-labelledby="image-lightbox-title" aria-hidden="true">
  <div class="image-lightbox__backdrop" data-lightbox-close></div>
  <div class="image-lightbox__dialog">
    <button class="image-lightbox__close" type="button" aria-label="Cerrar imagen ampliada" data-lightbox-close>
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
    </button>
    <div class="image-lightbox__media">
      <img id="image-lightbox-img" src="" alt="">
    </div>
    <p class="image-lightbox__title" id="image-lightbox-title"></p>
  </div>
</div>
'''

if 'id="image-lightbox"' not in content:
    content = content.replace('</body>', f'{lightbox_html}\n  </body>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('HTML updated.')
