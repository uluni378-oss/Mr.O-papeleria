import os
import re

base_dir = r"C:\Users\repre\Documents\Mro papeleria"

def update_html():
    html_path = os.path.join(base_dir, "index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    icons = {
        "C": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>',
        "M": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10a4 4 0 0 1 4-4h8a4 4 0 0 1 4 4v10a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V10Z"></path><path d="M9 6V4a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2"></path><path d="M8 22v-6a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v6"></path></svg>',
        "A": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>',
        "T": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19l7-7 3 3-7 7-3-3z"></path><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"></path><path d="M2 2l7.586 7.586"></path><circle cx="11" cy="11" r="2"></circle></svg>',
        "D": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"></path><line x1="7" y1="7" x2="7.01" y2="7"></line></svg>',
        "W": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg>'
    }
    
    titles = {
        "C": "Copias e impresiones",
        "M": "Material escolar",
        "A": "Artículos de oficina",
        "T": "Diseño para negocios",
        "D": "Identidad de marca",
        "W": "Páginas web"
    }

    zoom_icon = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>'

    def replacer(match):
        img_src = match.group(1)
        alt_text = match.group(2)
        letter = match.group(3)
        
        title = titles.get(letter, "Imagen")
        
        button_html = f'''<button class="category-preview" type="button" data-lightbox-title="{title}" aria-label="Ampliar imagen de {title.lower()}">
                <figure class="category-art__media" style="margin:0; width: 100%; height: 100%;">
                  <img src="{img_src}" alt="{alt_text}" loading="lazy" decoding="async" />
                  <span class="category-preview__zoom" aria-hidden="true">{zoom_icon}</span>
                </figure>
              </button>'''
        
        icon_html = f'<div class="category-icon" aria-hidden="true">{icons.get(letter, "")}</div>'
        
        return f'{button_html}\n              {icon_html}'

    pattern = r'<div class="category-art">\s*<img src="([^"]+)" alt="([^"]+)"[^>]*>\s*</div>\s*<div class="category-icon">([CMATDW])</div>'
    content = re.sub(pattern, replacer, content)

    # Add staggered delays to <article class="category-card reveal">
    def add_delay(match):
        nonlocal delay_count
        if delay_count < 6:
            delay_ms = delay_count * 70
            delay_count += 1
            return f'<article class="category-card reveal" style="transition-delay: {delay_ms}ms;">'
        return match.group(0)
        
    delay_count = 0
    content = re.sub(r'<article class="category-card reveal">', add_delay, content)

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    update_html()
    print("Update 3 HTML applied safely.")
