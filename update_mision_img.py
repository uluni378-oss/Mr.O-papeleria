import os
import shutil
import re

artifact_path = r'C:\Users\repre\.gemini\antigravity\brain\5b257ddd-d9e5-494e-ae71-70e682d3015a\media__1782235760555.jpg'
dest_dir = r'C:\Users\repre\Documents\Mro papeleria\assets\img\mision-vision'
dest_path = os.path.join(dest_dir, 'mision-vision-integral.png')

os.makedirs(dest_dir, exist_ok=True)
shutil.copy2(artifact_path, dest_path)
print(f'Image copied to {dest_path}')

# HTML Update
index_path = r'C:\Users\repre\Documents\Mro papeleria\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace inline styles with classes in HTML
# <div class="mission-grid" style="...">
html = re.sub(
    r'<div class="mission-grid" style="display: grid; gap: 3rem; grid-template-columns: repeat\(auto-fit, minmax\(300px, 1fr\)\); align-items: center;">',
    '<div class="mission-grid">',
    html
)

# <div class="mission-visual reveal" style="...">
old_visual_div = r'<div class="mission-visual reveal" style="border-radius: 16px; overflow: hidden; box-shadow: 0 10px 28px rgba\(0,0,0,0\.08\); aspect-ratio: 4/3;">'
new_visual_div = '<div class="mission-visual reveal">'
html = re.sub(old_visual_div, new_visual_div, html)

# Replace the img tag
old_img = r'<img src="\./assets/img/hero-papeleria\.webp" alt="Mostrador e interior de Mr\.O Papelería en Chilpancingo" width="800" height="600" loading="lazy" decoding="async" style="width: 100%; height: 100%; object-fit: cover; display: block;">'
new_img = '''<img
                src="./assets/img/mision-vision/mision-vision-integral.png"
                alt="Misión y visión de Mr.O Papelería: apoyo escolar, servicios digitales, trámites y soluciones para negocios"
                width="1024"
                height="1024"
                loading="lazy"
                decoding="async"
              >'''
html = re.sub(old_img, new_img, html)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('HTML updated.')

# CSS Update
css_path = r'C:\Users\repre\Documents\Mro papeleria\css\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

new_css = '''
/* --- Misión y Visión Styles --- */
.mission-grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(360px, 470px);
  gap: clamp(2rem, 5vw, 5rem);
  align-items: center;
}

.mission-visual {
  display: grid;
  place-items: center;
  width: 100%;
  max-width: 470px;
  margin-inline: auto;
  overflow: hidden;
  border-radius: 22px;
  background: #f3eadb;
  box-shadow: 0 20px 48px rgba(8, 39, 59, 0.12);
}

.mission-visual img {
  display: block;
  width: 100%;
  height: auto;
  aspect-ratio: 1 / 1;
  object-fit: contain;
  object-position: center;
}

@media (max-width: 900px) {
  .mission-grid {
    grid-template-columns: 1fr;
  }

  .mission-visual {
    width: min(100%, 520px);
  }
}

@media (max-width: 520px) {
  .mission-visual {
    width: 100%;
    border-radius: 16px;
  }
}
'''

if ".mission-grid {" not in css:
    css += new_css
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print('CSS updated.')
else:
    print('CSS already contains .mission-grid')

