import re
import os

def update_index(filepath):
    if not os.path.exists(filepath):
        print(f"No existe {filepath}")
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the new grid HTML
    new_grid_html = """          <div class="category-grid">
            <a href="#servicios" class="category-card category-card-reveal" style="text-decoration: none; color: inherit;">
              <div class="category-art"><img src="./assets/img/servicios-principales/copias-impresiones.webp" alt="Copiadora, impresora y documentos en escritorio limpio" width="800" height="600" loading="lazy" decoding="async" /></div>
              <div class="category-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg></div>
              <h3>Copias e impresiones</h3>
              <p>Copias, impresiones y escaneo de alta calidad.</p>
            </a>
            
            <a href="productos-escolares.html" class="category-card category-card-reveal" style="text-decoration: none; color: inherit;">
              <div class="category-art"><img src="./assets/img/servicios-principales/material-escolar.webp" alt="Cuadernos, lápices, colores y mochilas organizadas" width="800" height="600" loading="lazy" decoding="async" /></div>
              <div class="category-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path><path d="M10 2v20"></path></svg></div>
              <h3>Material escolar</h3>
              <p>Todo para tus clases y proyectos.</p>
            </a>
            
            <a href="productos-escolares.html" class="category-card category-card-reveal" style="text-decoration: none; color: inherit;">
              <div class="category-art"><img src="./assets/img/servicios-principales/articulos-oficina.webp" alt="Folders, carpetas, hojas y bolígrafos corporativos" width="800" height="600" loading="lazy" decoding="async" /></div>
              <div class="category-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg></div>
              <h3>Artículos de oficina</h3>
              <p>Material de oficina y accesorios.</p>
            </a>
            
            <a href="#servicios" class="category-card category-card-reveal" style="text-decoration: none; color: inherit;">
              <div class="category-art"><img src="./assets/img/servicios-principales/tramites-documentos.webp" alt="Computadora e impresora para trámites y documentos" width="800" height="600" loading="lazy" decoding="async" /></div>
              <div class="category-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"></path><line x1="7" y1="7" x2="7.01" y2="7"></line></svg></div>
              <h3>Trámites y documentos</h3>
              <p>Apoyo en trámites digitales básicos.</p>
            </a>
            
            <a href="#servicios" class="category-card category-card-reveal" style="text-decoration: none; color: inherit;">
              <div class="category-art"><img src="./assets/img/servicios-rapidos/engargolado.webp" alt="Trabajos de engargolado y enmicado" width="800" height="600" loading="lazy" decoding="async" /></div>
              <div class="category-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg></div>
              <h3>Engargolado y enmicado</h3>
              <p>Acabados de protección y presentación.</p>
            </a>
            
            <a href="#diseno" class="category-card category-card-reveal" style="text-decoration: none; color: inherit;">
              <div class="category-art"><img src="./assets/img/servicios-principales/diseno-negocios.webp" alt="Logotipo, tarjetas, banners y aplicaciones visuales para presentar tu negocio" width="800" height="600" loading="lazy" decoding="async" /></div>
              <div class="category-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19l7-7 3 3-7 7-3-3z"></path><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"></path><path d="M2 2l7.586 7.586"></path><circle cx="11" cy="11" r="2"></circle></svg></div>
              <h3>Diseño para negocios</h3>
              <p>Logotipos, tarjetas y aplicaciones visuales para presentar tu negocio.</p>
            </a>
          </div>"""

    # Replace the category-grid block using regex
    pattern = r'<div class="category-grid">.*?</div>\s*</div>\s*</section>'
    
    # We need to make sure we don't accidentally swallow too much.
    # We will search specifically for the <div class="category-grid"> block and replace its contents.
    grid_pattern = re.compile(r'<div class="category-grid">[\s\S]*?</div>\s*</div>\s*</section>', re.IGNORECASE)
    
    replacement = new_grid_html + "\n        </div>\n      </section>"
    
    content = grid_pattern.sub(replacement, content, count=1)
    
    # Footer link replacement:
    # <nav aria-label="Servicios">
    #   ...
    #   <a href="#paginas-web">Páginas web</a>
    
    footer_pattern = re.compile(r'(<nav aria-label="Servicios">[\s\S]*?)<a href="#paginas-web"[^>]*>P.ginas web</a>([\s\S]*?</nav>)')
    content = footer_pattern.sub(r'\1<a href="#diseno">Diseño para negocios</a>\2', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def update_productos(filepath):
    if not os.path.exists(filepath):
        print(f"No existe {filepath}")
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to replace the H1
    h1_pattern = re.compile(r'<h1>Todo para el regreso a clases</h1>')
    replacement = '<h1>Artículos escolares y material de oficina</h1>\n        <p class="hero-lead hero-reveal-up" style="transition-delay: 150ms; font-size: 1.25rem; font-weight: 500; color: #07365c; margin-top: 1rem;">Todo para el regreso a clases</p>'
    
    content = h1_pattern.sub(replacement, content, count=1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Apply to root
update_index(r"C:\Users\repre\Documents\Mro papeleria\index.html")
update_productos(r"C:\Users\repre\Documents\Mro papeleria\productos-escolares.html")

# Apply to public_html
update_index(r"C:\Users\repre\Documents\Mro papeleria\public_html\index.html")
update_productos(r"C:\Users\repre\Documents\Mro papeleria\public_html\productos-escolares.html")

print("Correcciones aplicadas en ambos entornos.")
