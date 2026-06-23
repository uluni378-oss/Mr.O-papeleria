import os
import re

base_dir = r"C:\Users\repre\Documents\Mro papeleria"

# --- 1. HTML Update ---
index_path = os.path.join(base_dir, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Define the new cards data
cards_data = [
    {
        "id": "logotipos",
        "title": "Logotipos",
        "alt": "Proceso y aplicación de un logotipo para un negocio local",
        "img": "logotipos-realista.webp"
    },
    {
        "id": "tarjetas_presentacion",
        "title": "Tarjetas de presentación",
        "alt": "Tarjetas de presentación impresas con acabado profesional",
        "img": "tarjetas-presentacion-realistas.webp"
    },
    {
        "id": "lonas_banners",
        "title": "Lonas y banners",
        "alt": "Lonas y banners publicitarios para un negocio local",
        "img": "lonas-banners-realistas.webp"
    },
    {
        "id": "redes_sociales",
        "title": "Redes sociales",
        "alt": "Diseños coordinados para redes sociales de un negocio local",
        "img": "redes-sociales-realistas.webp"
    },
    {
        "id": "papeleria_corporativa",
        "title": "Papelería corporativa",
        "alt": "Papelería corporativa con hojas, sobres, carpetas y tarjetas",
        "img": "papeleria-corporativa-realista.webp"
    },
    {
        "id": "impresos_promocionales",
        "title": "Impresos promocionales",
        "alt": "Volantes, folletos y materiales promocionales impresos",
        "img": "impresos-promocionales-realistas.webp"
    }
]

# We will replace the entire `.business-grid` contents
grid_start_tag = '<div class="business-grid">'
grid_end_tag = '</div>\n          </div>'

start_idx = html_content.find(grid_start_tag)
if start_idx != -1:
    end_idx = html_content.find(grid_end_tag, start_idx)
    if end_idx != -1:
        new_grid_content = grid_start_tag + "\n"
        
        for data in cards_data:
            safe_title = data["title"].replace("ó", "&oacute;").replace("í", "&iacute;")
            
            card_html = f'''              <article class="business-card business-design-reveal">
                <button class="business-design-preview" type="button" data-lightbox-title="{data["title"]}" aria-label="Ampliar ejemplo de {data["title"].lower()}">
                  <figure class="business-card__media">
                    <img src="./assets/img/diseno-negocios/{data["img"]}" alt="{data["alt"]}" width="1600" height="1000" loading="lazy" decoding="async">
                    <span class="business-design-preview__zoom" aria-hidden="true">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>
                    </span>
                  </figure>
                </button>
                <h3>{safe_title}</h3>
              </article>\n'''
            new_grid_content += card_html
        
        html_content = html_content[:start_idx] + new_grid_content + "            " + html_content[end_idx:]

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html_content)

# --- 2. CSS Update ---
css_path = os.path.join(base_dir, "css", "styles.css")
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

new_css = '''
/* --- Business Design Styles --- */
.business-card__media {
  position: relative;
  aspect-ratio: 8 / 5;
  overflow: hidden;
  background: #eef2f4;
  margin: 0;
}

.business-card__media img {
  display: block;
  width: 100%;
  height: 100% !important;
  object-fit: cover !important;
  object-position: center !important;
  transition: transform 0.45s ease, filter 0.45s ease;
}

.business-card:hover .business-card__media img {
  transform: scale(1.035);
  filter: saturate(1.05) contrast(1.02);
}

.business-design-reveal {
  opacity: 0;
  transform: translateY(18px);
  transition: opacity 0.55s ease, transform 0.55s ease;
}

.business-design-reveal.is-visible {
  opacity: 1;
  transform: translateY(0);
}

@media (prefers-reduced-motion: reduce) {
  .business-design-reveal,
  .business-card,
  .business-card img {
    opacity: 1;
    transform: none;
    transition: none;
  }
}

.business-design-preview {
  display: block;
  width: 100%;
  padding: 0;
  border: 0;
  background: transparent;
  cursor: zoom-in;
}

.business-design-preview__zoom {
  position: absolute;
  top: 0.7rem;
  right: 0.7rem;
  display: grid;
  width: 2.35rem;
  height: 2.35rem;
  place-items: center;
  border-radius: 999px;
  background: rgba(4, 28, 46, 0.82);
  color: #ffffff;
  opacity: 0.85;
  backdrop-filter: blur(8px);
  transition: opacity 0.25s ease, transform 0.25s ease;
}

.business-design-preview:hover .business-design-preview__zoom,
.business-design-preview:focus-visible .business-design-preview__zoom {
  opacity: 1;
  transform: scale(1.06);
}

.business-design-preview:focus-visible {
  outline: 3px solid #00a6c8;
  outline-offset: 4px;
}
'''

if ".business-card__media" not in css_content:
    css_content += new_css

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css_content)

# --- 3. JS Update ---
js_path = os.path.join(base_dir, "js", "main.js")
with open(js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

# Update lightbox triggers selector
js_content = js_content.replace(
    'const lightboxTriggers = document.querySelectorAll(".web-preview");',
    'const lightboxTriggers = document.querySelectorAll(".web-preview, .business-design-preview");'
)

# Add observer logic if not present
if "businessDesignRevealObserver" not in js_content:
    js_observer = '''
// BUSINESS DESIGN REVEAL OBSERVER
document.addEventListener("DOMContentLoaded", () => {
  const businessRevealElements = document.querySelectorAll(".business-design-reveal");
  if(businessRevealElements.length > 0) {
    const businessRevealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: "0px 0px -40px 0px" });
    
    businessRevealElements.forEach((el, index) => {
      el.style.transitionDelay = `${index * 80}ms`;
      businessRevealObserver.observe(el);
    });
  }
});
'''
    js_content += js_observer

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print("Update completed.")
