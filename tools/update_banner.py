import os
import re
import urllib.request
from PIL import Image
from io import BytesIO

project_dir = r'C:\Users\repre\Documents\Mro papeleria'

# 1. Download images
url_desktop = "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=1920&h=700&fit=crop&q=80"
url_mobile = "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=900&h=1000&fit=crop&q=80"

desk_path = os.path.join(project_dir, 'assets', 'img', 'temporada-escolar-realista.webp')
mob_path = os.path.join(project_dir, 'assets', 'img', 'temporada-escolar-realista-mobile.webp')

try:
    req = urllib.request.Request(url_desktop, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        img = Image.open(BytesIO(response.read()))
        img.save(desk_path, format="WEBP", quality=85)
    
    req_m = urllib.request.Request(url_mobile, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req_m) as response:
        img_m = Image.open(BytesIO(response.read()))
        img_m.save(mob_path, format="WEBP", quality=85)
except Exception as e:
    print("Error downloading images:", e)
    # Create simple placeholders if download fails
    Image.new('RGB', (1920, 700), color='#1e3a5f').save(desk_path, format="WEBP")
    Image.new('RGB', (900, 1000), color='#1e3a5f').save(mob_path, format="WEBP")

# 2. Update HTML
html_path = os.path.join(project_dir, 'index.html')
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

new_section = """<section class="school-season-banner" id="papeleria">
  <picture class="school-season-banner__picture">
    <source
      media="(max-width: 700px)"
      srcset="./assets/img/temporada-escolar-realista-mobile.webp"
    >
    <img
      src="./assets/img/temporada-escolar-realista.webp"
      alt="Cuadernos, lápices, colores y útiles para la temporada escolar"
      width="1920"
      height="700"
      loading="eager"
      fetchpriority="high"
    >
  </picture>

  <div class="school-season-overlay" aria-hidden="true"></div>

  <div class="school-season-inner">
    <div class="school-season-copy reveal">
      <h2><span>TEMPORADA</span><br>ESCOLAR</h2>
      <p>Encuentra todo para este regreso a clases.</p>
      <a href="./productos-escolares.html" class="school-season-button">Ver productos</a>
    </div>

    <ul class="school-season-list reveal">
      <li>Cuadernos</li>
      <li>Colores</li>
      <li>Lápices</li>
      <li>Mochilas</li>
      <li>Cartulinas</li>
      <li>Y mucho más...</li>
    </ul>
  </div>
</section>"""

html = re.sub(r'<section class="school-season" id="papeleria">.*?</section>', new_section, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# 3. Update CSS
css_path = os.path.join(project_dir, 'css', 'styles.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Remove old .school-season rules
css = re.sub(r'\.school-season\s*\{[^}]*\}', '', css)
css = re.sub(r'\.school-season-bg\s*\{[^}]*\}', '', css)
css = re.sub(r'\.school-season-overlay\s*\{[^}]*\}', '', css)
css = re.sub(r'\.school-season-inner\s*\{[^}]*\}', '', css)
css = re.sub(r'\.school-season-list\s*\{[^}]*\}', '', css)
css = re.sub(r'\.season-grid\s*\{[^}]*\}', '', css)
css = re.sub(r'\.season-copy\s*\{[^}]*\}', '', css)
css = re.sub(r'\.season-title\s*\{[^}]*\}', '', css)
css = re.sub(r'\.season-collage\s*\{[^}]*\}', '', css)
css = re.sub(r'\.season-collage\s*>\s*\*\s*\{[^}]*\}', '', css)
css = re.sub(r'\.season-book\s*\{[^}]*\}', '', css)
css = re.sub(r'\.season-pencil\s*\{[^}]*\}', '', css)
css = re.sub(r'\.season-colors\s*\{[^}]*\}', '', css)
css = re.sub(r'\.season-colors\s*>\s*div\s*\{[^}]*\}', '', css)

# Wait, the user didn't mention .school-season-button styles, I should keep existing styles for buttons if they were separate or add them if they were deleted.
# Let me preserve .school-season-button if it existed. It seems it wasn't strictly deleted above.
# Actually I need to make sure I don't delete styles that weren't specifically requested to be replaced, but adding the new requested styles.

new_css = """
.school-season-banner {
  position: relative;
  min-height: clamp(390px, 36vw, 560px);
  overflow: hidden;
  color: #ffffff;
  background: #051c30;
}

.school-season-banner__picture,
.school-season-banner__picture img {
  width: 100%;
  height: 100%;
}

.school-season-banner__picture {
  position: absolute;
  inset: 0;
  overflow: hidden;
}

.school-season-banner__picture img {
  display: block;
  object-fit: cover;
  object-position: 62% center;
}

.school-season-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    90deg,
    rgba(5, 28, 48, 0.96) 0%,
    rgba(5, 28, 48, 0.80) 32%,
    rgba(5, 28, 48, 0.25) 65%,
    rgba(5, 28, 48, 0.08) 100%
  );
  z-index: 1;
}

.school-season-inner {
  position: relative;
  z-index: 2;
  width: min(100% - 32px, 1180px);
  margin: 0 auto;
  min-height: clamp(390px, 36vw, 560px);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 30px;
  padding: 40px 0;
}

.school-season-copy {
  max-width: 500px;
}

.school-season-copy h2 {
  font-size: clamp(2.7rem, 5.6vw, 5.1rem);
  font-weight: 900;
  line-height: 0.9;
  margin-bottom: 16px;
}

.school-season-copy p {
  font-size: 1.18rem;
  margin-bottom: 24px;
  color: rgba(255, 255, 255, 0.85);
}

.school-season-button {
  display: inline-flex;
  min-height: 48px;
  padding: 13px 26px;
  align-items: center;
  justify-content: center;
  border-radius: 999px;
  background: #ffc400;
  color: #061b2e;
  text-decoration: none;
  font-size: 15px;
  font-weight: 900;
  transition: transform 180ms ease, box-shadow 180ms ease;
}

.school-season-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.2);
}

.school-season-list {
  background: rgba(7, 35, 55, 0.72);
  border: 1px solid rgba(255, 255, 255, 0.22);
  backdrop-filter: blur(12px);
  box-shadow: 0 18px 45px rgba(0, 0, 0, 0.30);
  border-radius: 20px;
  padding: 30px 40px;
  list-style: none;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.school-season-list li {
  font-size: 1.1rem;
  font-weight: 600;
  position: relative;
  padding-left: 20px;
}

.school-season-list li::before {
  content: "•";
  position: absolute;
  left: 0;
  color: #009dba;
  font-size: 1.5rem;
  line-height: 1;
  top: -2px;
}

@media (max-width: 900px) {
  .school-season-banner {
    min-height: 520px;
  }
  .school-season-inner {
    min-height: 520px;
  }
}

@media (max-width: 700px) {
  .school-season-banner__picture img {
    object-position: center;
  }
  
  .school-season-overlay {
    background: linear-gradient(
      180deg,
      rgba(5, 28, 48, 0.92) 0%,
      rgba(5, 28, 48, 0.85) 40%,
      rgba(5, 28, 48, 0.30) 100%
    );
  }

  .school-season-inner {
    flex-direction: column;
    justify-content: flex-start;
    padding: 50px 0;
  }

  .school-season-copy {
    text-align: center;
  }
  
  .school-season-list {
    align-self: center;
    width: 100%;
    max-width: 400px;
  }
}
"""

css = css + '\n' + new_css

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Update script completed successfully.")
