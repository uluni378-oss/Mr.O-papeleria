import re
import os

html_path = r'C:\Users\repre\Documents\Mro papeleria\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# 1. Update HTML: Remove data-lightbox-src and data-lightbox-alt
html_content = re.sub(r'\s*data-lightbox-src="[^"]*"', '', html_content)
html_content = re.sub(r'\s*data-lightbox-alt="[^"]*"', '', html_content)

# Add loader and error to lightbox HTML if missing
if 'image-lightbox__loader' not in html_content:
    html_content = html_content.replace('<img id="image-lightbox-img" src="" alt="">', 
'''<img id="image-lightbox-img" src="" alt="">
      <div class="image-lightbox__loader" aria-hidden="true"></div>
      <p class="image-lightbox__error" hidden>No fue posible cargar esta imagen.</p>''')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)


# 2. Update CSS
css_path = r'C:\Users\repre\Documents\Mro papeleria\css\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

if 'image-lightbox__loader' not in css_content:
    # First, let's inject the new properties to .image-lightbox__media
    new_media_styles = '''
  position: relative;
  min-width: min(900px, 90vw);
  min-height: min(560px, 72vh);
  background: linear-gradient(135deg, #0b1f31, #12334d);
'''
    css_content = css_content.replace('background: #ffffff;', new_media_styles)

    # Append the new styles to the end
    new_css = '''
.image-lightbox__loader {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 42px;
  height: 42px;
  border: 4px solid rgba(255,255,255,0.22);
  border-top-color: #00a6c8;
  border-radius: 50%;
  transform: translate(-50%, -50%);
  animation: lightbox-spin 0.8s linear infinite;
}

.image-lightbox__media img {
  position: relative;
  z-index: 1;
}

.image-lightbox__media img[src]:not([src=""]) ~ .image-lightbox__loader {
  display: none;
}

@keyframes lightbox-spin {
  to {
    transform: translate(-50%, -50%) rotate(360deg);
  }
}

.image-lightbox__error {
  position: absolute;
  inset: 0;
  display: none;
  place-items: center;
  margin: 0;
  padding: 2rem;
  color: #ffffff;
  text-align: center;
  background: #102536;
  z-index: 2;
}

.image-lightbox.has-error .image-lightbox__error {
  display: grid;
}

.image-lightbox.has-error .image-lightbox__media img {
  display: none;
}
'''
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(new_css)


# 3. Update JS
js_path = r'C:\Users\repre\Documents\Mro papeleria\js\main.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

new_open_lightbox = '''const openLightbox = (trigger) => {
  if (!lightbox || !lightboxImage || !lightboxTitle) return;

  const previewImage = trigger.querySelector("img");

  if (!previewImage) return;

  const imageSource =
    previewImage.currentSrc ||
    previewImage.getAttribute("src");

  const imageAlt =
    previewImage.getAttribute("alt") || "";

  const imageTitle =
    trigger.dataset.lightboxTitle ||
    trigger.querySelector(".web-preview__label")?.textContent?.trim() ||
    "";

  if (!imageSource) return;

  lastFocusedElement = document.activeElement;

  lightboxImage.onload = () => {
    lightbox.classList.remove("has-error");
  };

  lightboxImage.onerror = () => {
    lightbox.classList.add("has-error");
  };

  lightboxImage.src = imageSource;
  lightboxImage.alt = imageAlt;
  lightboxTitle.textContent = imageTitle;

  lightbox.classList.add("is-open");
  lightbox.setAttribute("aria-hidden", "false");
  document.body.classList.add("lightbox-open");

  const closeButton =
    lightbox.querySelector(".image-lightbox__close");

  closeButton?.focus();
};'''

old_open_lightbox_pattern = r'const openLightbox = \(trigger\) => \{[\s\S]*?closeButton\?\.focus\(\);\s*\};'
js_content = re.sub(old_open_lightbox_pattern, new_open_lightbox, js_content)

# Update closeLightbox
new_close_lightbox = '''const closeLightbox = () => {
  if (!lightbox || !lightboxImage || !lightboxTitle) return;

  lightbox.classList.remove("is-open", "has-error");
  lightbox.setAttribute("aria-hidden", "true");
  document.body.classList.remove("lightbox-open");

  lightboxImage.removeAttribute("src");
  lightboxImage.alt = "";
  lightboxTitle.textContent = "";

  lastFocusedElement?.focus();
};'''

old_close_lightbox_pattern = r'const closeLightbox = \(\) => \{[\s\S]*?lastFocusedElement\?\.focus\(\);\s*\};'
js_content = re.sub(old_close_lightbox_pattern, new_close_lightbox, js_content)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Files updated successfully.")
