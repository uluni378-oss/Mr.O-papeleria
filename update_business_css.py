import os
import re

css_path = r"C:\Users\repre\Documents\Mro papeleria\css\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# I will just append the new styles directly to the bottom of the CSS file.
# The user's specification:
new_css = '''
.business-design-card {
  display: grid;
  grid-template-rows: auto minmax(3.25rem, auto);
  overflow: hidden;
  border-radius: 18px;
  background: #ffffff;
  box-shadow: 0 14px 32px rgba(8, 39, 59, 0.10);
}

.business-design-card__media {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 10;
  overflow: hidden;
  background: #edf2f4;
  margin: 0;
}

.business-design-card__media img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
}

.business-design-card__title {
  display: flex;
  min-height: 3.25rem;
  margin: 0;
  padding: 0.8rem 1rem;
  align-items: center;
  justify-content: center;
  font-family: inherit;
  font-size: clamp(0.92rem, 1vw, 1.05rem);
  font-weight: 700;
  line-height: 1.2;
  color: #082f53;
  text-align: center;
}

.business-design-preview {
  display: block;
  width: 100%;
  padding: 0;
  border: none;
  background: transparent;
  cursor: zoom-in;
}

.business-design-preview__zoom {
  position: absolute;
  top: 0.7rem;
  right: 0.7rem;
  display: grid;
  width: 2.2rem;
  height: 2.2rem;
  place-items: center;
  border-radius: 50%;
  background: rgba(6, 40, 60, 0.82);
  color: #ffffff;
  transition: transform 0.2s ease, background 0.2s ease;
}

.business-design-preview:hover .business-design-preview__zoom,
.business-design-preview:focus-visible .business-design-preview__zoom {
  transform: scale(1.05);
  background: rgba(6, 40, 60, 0.95);
}

.business-design-preview:hover img,
.business-design-preview:focus-visible img {
  transform: scale(1.035);
  filter: saturate(1.05) contrast(1.02);
  transition: transform 0.3s ease, filter 0.3s ease;
}

.business-design-card__media img {
  transition: transform 0.3s ease, filter 0.3s ease;
}
'''

if ".business-design-card__title" not in css:
    css += new_css

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)
print("CSS for business cards updated.")
