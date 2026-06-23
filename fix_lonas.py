import os
import re

base_dir = r"C:\Users\repre\Documents\Mro papeleria"
path = os.path.join(base_dir, "index.html")

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix Lonas y banners block
old_lonas = """              <article class="business-card business-design-reveal">
                <button class="business-design-preview" type="button" data-lightbox-title="Lonas y banners" aria-label="Ampliar ejemplo de lonas y banners">
                  <figure class="business-card__media">
                    <img src="./assets/img/diseno-negocios/lonas-banners-realistas.webp" alt="Lonas y banners publicitarios para un negocio local" width="1600" height="1000" loading="lazy" decoding="async">"""

new_lonas = """              <article class="business-card business-design-reveal">
                <button class="business-design-preview" type="button" data-lightbox-title="Diseño de lonas y banners" aria-label="Ampliar ejemplo de diseño de lonas y banners">
                  <figure class="business-card__media">
                    <img src="./assets/img/diseno-negocios/lonas-banners-v2.webp" alt="Computadora con diseño de lona publicitaria y archivo listo para imprimir" width="1600" height="1000" loading="lazy" decoding="async">"""

content = content.replace(old_lonas, new_lonas)
content = content.replace("<h3>Lonas y banners</h3>", "<h3>Diseño de lonas y banners</h3>")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Fix completed.")
