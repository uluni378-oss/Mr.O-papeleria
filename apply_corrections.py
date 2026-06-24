import os
import re

base_dir = r"C:\Users\repre\Documents\Mro papeleria"
html_path = os.path.join(base_dir, "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Hero principal
html = html.replace('Papelería, copias e impresiones al instante. Además, impulsamos tu negocio con diseño gráfico, branding y páginas web.',
                    'Papelería, copias, impresiones y trámites digitales con atención directa. También creamos logotipos, piezas gráficas y páginas web para negocios locales.')
# Encode fallback just in case
html = html.replace('Papeler&iacute;a, copias e impresiones al instante. Adem&aacute;s, impulsamos tu negocio con dise&ntilde;o gr&aacute;fico, branding y p&aacute;ginas web.',
                    'Papeler&iacute;a, copias, impresiones y tr&aacute;mites digitales con atenci&oacute;n directa. Tambi&eacute;n creamos logotipos, piezas gr&aacute;ficas y p&aacute;ginas web para negocios locales.')
# Some more robust regex for the hero
html = re.sub(r'<p class="hero-lead hero-reveal-up"[^>]*>Papeler[^<]+</p>',
              '<p class="hero-lead hero-reveal-up" style="transition-delay: 180ms;">Papelería, copias, impresiones y trámites digitales con atención directa. También creamos logotipos, piezas gráficas y páginas web para negocios locales.</p>', html)

html = html.replace('<a class="btn btn--ghost" href="#servicios">Ver servicios</a>',
                    '<a class="btn btn--ghost" href="#ubicacion">Cómo llegar</a>')


# 2. Categoría Diseño para negocios
html = html.replace('Logotipo, tarjetas, banners y mockups profesionales',
                    'Logotipo, tarjetas, banners y aplicaciones visuales para presentar tu negocio')
html = html.replace('Logotipos, tarjetas y mockups profesionales.',
                    'Logotipos, tarjetas y aplicaciones visuales para presentar tu negocio.')


# 3. Diseño de lonas y banners
html = html.replace('<h3>Diseño de lonas y banners</h3>',
                    '<h3>Diseño de lonas y banners</h3>\n                <p class="business-card__desc">Creamos el diseño y entregamos el archivo digital listo para imprimir con el proveedor de tu preferencia.</p>')
html = html.replace('<h3>Dise&ntilde;o de lonas y banners</h3>',
                    '<h3>Dise&ntilde;o de lonas y banners</h3>\n                <p class="business-card__desc">Creamos el dise&ntilde;o y entregamos el archivo digital listo para imprimir con el proveedor de tu preferencia.</p>')

# 4. Nota general de diseño para negocios
note_html = '\n          <div class="business-design-note" style="text-align: center; margin-top: 2rem; color: #526677; font-size: 0.95rem;">\n            <p>Entregamos archivos digitales listos para impresión. La producción de lonas y formatos de gran tamaño se realiza con el proveedor que el cliente elija.</p>\n          </div>'
html = html.replace('            </div>\n          </div>\n        </div>\n      </section>',
                    '            </div>\n          </div>' + note_html + '\n        </div>\n      </section>')


# 5. Servicios rápidos WhatsApp text
def replace_quick(match):
    return match.group(1) + '\n            <span class="quick-service-whatsapp">Consultar por WhatsApp &rarr;</span>\n          ' + match.group(2)

html = re.sub(r'(<div class="quick-service-card__content">\s*<h3>.*?</h3>\s*<p>.*?</p>)\s*(</div>)', replace_quick, html)


with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)


# CSS Updates
css_path = os.path.join(base_dir, "css", "styles.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

new_css = '''
.business-card__desc {
  color: #526677;
  font-size: 0.95rem;
  line-height: 1.5;
  margin-top: 0.5rem;
}

.quick-service-whatsapp {
  display: none;
}
@media (min-width: 1025px) {
  .quick-service-whatsapp {
    display: inline-block;
    margin-top: 0.75rem;
    color: #009dba;
    font-size: 0.85rem;
    font-weight: 600;
    transition: transform 0.3s ease;
  }
  .quick-service-card:hover .quick-service-whatsapp {
    transform: translateX(4px);
  }
}
'''
if '.quick-service-whatsapp' not in css:
    css += new_css
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css)

print("Updates successful.")
