import os
import re

base_dir = r"C:\Users\repre\Documents\Mro papeleria"

# 1. Update HTML
html_path = os.path.join(base_dir, "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Update Hero
html = re.sub(r'<div class="hero-copy reveal">', '<div class="hero-copy">', html)
html = re.sub(r'<p class="eyebrow">', '<p class="eyebrow hero-reveal-left" style="transition-delay: 0ms;">', html)
html = re.sub(r'<h1>TU CENTRO DE<br /><span>IMPRESI&Oacute;N Y PAPELER&Iacute;A\.</span></h1>', '<h1 class="hero-reveal-up" style="transition-delay: 100ms;">TU CENTRO DE<br /><span>IMPRESI&Oacute;N Y PAPELER&Iacute;A.</span></h1>', html)
html = re.sub(r'<h1>TU CENTRO DE<br /><span>IMPRESIN Y PAPELERA\.</span></h1>', '<h1 class="hero-reveal-up" style="transition-delay: 100ms;">TU CENTRO DE<br /><span>IMPRESI&Oacute;N Y PAPELER&Iacute;A.</span></h1>', html) # Just in case
html = re.sub(r'<p class="hero-lead">', '<p class="hero-lead hero-reveal-up" style="transition-delay: 180ms;">', html)
html = re.sub(r'<div class="actions">', '<div class="actions hero-reveal-up" style="transition-delay: 260ms;">', html)
html = re.sub(r'<figure class="hero-visual hero-photo reveal">', '<figure class="hero-visual hero-photo hero-reveal-right" style="transition-delay: 120ms;">', html)

# Some encoding issues with the h1 tag in regex could happen. Let's use a safer regex for h1.
html = re.sub(r'<h1>TU CENTRO DE<br\s*/><span>IMPRESI[^<]+PAPELER[^<]+</span></h1>', '<h1 class="hero-reveal-up" style="transition-delay: 100ms;">TU CENTRO DE<br /><span>IMPRESI&Oacute;N Y PAPELER&Iacute;A.</span></h1>', html)

# Update Mision y Vision
html = re.sub(r'<div class="mission-copy reveal"', '<div class="mission-copy"', html)
html = re.sub(r'<div class="mission-visual reveal">', '<div class="mission-visual mission-reveal-right" style="transition-delay: 140ms;">', html)

# Mision y vision internal elements
# Span eyebrow
html = re.sub(r'<span class="eyebrow" style="color: #009DBA; font-weight: 700; font-size: 0\.85rem; letter-spacing: 0\.1em; display: block; margin-bottom: 0\.5rem;">', '<span class="eyebrow mission-reveal-up" style="color: #009DBA; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.1em; display: block; margin-bottom: 0.5rem; transition-delay: 0ms;">', html)
# h2 Mision y Vision
html = re.sub(r'<h2 style="font-size: clamp\(2rem, 3vw, 2\.5rem\); color: #07365c; margin-bottom: 2rem;">Misi[^<]+Visi[^<]+</h2>', '<h2 class="mission-reveal-up" style="font-size: clamp(2rem, 3vw, 2.5rem); color: #07365c; margin-bottom: 2rem; transition-delay: 80ms;">Misi&oacute;n y Visi&oacute;n</h2>', html)
# 01 Mision
html = re.sub(r'<div class="mission-item" style="margin-bottom: 2rem; position: relative; padding-left: 3\.5rem;">', '<div class="mission-item mission-reveal-left" style="margin-bottom: 2rem; position: relative; padding-left: 3.5rem; transition-delay: 160ms;">', html)
# 02 Vision
html = re.sub(r'<div class="mission-item" style="position: relative; padding-left: 3\.5rem;">', '<div class="mission-item mission-reveal-left" style="position: relative; padding-left: 3.5rem; transition-delay: 240ms;">', html)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("HTML Updated.")


# 2. Update CSS
css_path = os.path.join(base_dir, "css", "styles.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

new_css = '''
/* --- Hero & Mission Reveal Animations --- */
.hero-reveal-left {
  opacity: 0;
  transform: translateX(-24px);
  transition: opacity 0.65s ease, transform 0.65s ease;
}

.hero-reveal-right {
  opacity: 0;
  transform: translateX(24px) scale(1.025);
  transition: opacity 0.75s ease, transform 0.75s ease;
}

.hero-reveal-up {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}

.hero-reveal-left.is-visible,
.hero-reveal-right.is-visible,
.hero-reveal-up.is-visible {
  opacity: 1;
  transform: none;
}

.mission-reveal-left {
  opacity: 0;
  transform: translateX(-22px);
  transition: opacity 0.65s ease, transform 0.65s ease;
}

.mission-reveal-right {
  opacity: 0;
  transform: translateX(22px);
  transition: opacity 0.7s ease, transform 0.7s ease;
}

.mission-reveal-up {
  opacity: 0;
  transform: translateY(18px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}

.mission-reveal-left.is-visible,
.mission-reveal-right.is-visible,
.mission-reveal-up.is-visible {
  opacity: 1;
  transform: none;
}

.mission-item span {
  display: inline-block;
  transform: scale(0.96);
  transition: transform 0.6s ease;
}
.mission-reveal-left.is-visible span {
  transform: scale(1);
}

.hero .btn {
  transition: transform 0.3s ease, box-shadow 0.3s ease, background 0.3s ease, color 0.3s ease;
}
.hero .btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
}

@media (prefers-reduced-motion: reduce) {
  .hero-reveal-left,
  .hero-reveal-right,
  .hero-reveal-up,
  .mission-reveal-left,
  .mission-reveal-right,
  .mission-reveal-up {
    opacity: 1 !important;
    transform: none !important;
    transition: none !important;
  }
  .mission-item span {
    transform: none !important;
    transition: none !important;
  }
  .hero .btn:hover {
    transform: none !important;
  }
}
'''
if '.hero-reveal-left' not in css:
    css += new_css
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css)
    print("CSS Updated.")


# 3. Update JS
js_path = os.path.join(base_dir, "js", "main.js")
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

new_js = '''
// HERO & MISSION OBSERVER
document.addEventListener("DOMContentLoaded", () => {
  const animatedElements = document.querySelectorAll(
    ".hero-reveal-left, .hero-reveal-right, .hero-reveal-up, " +
    ".mission-reveal-left, .mission-reveal-right, .mission-reveal-up"
  );

  if (animatedElements.length > 0) {
    const revealObserver = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        });
      },
      { threshold: 0.16 }
    );

    animatedElements.forEach((element) => {
      revealObserver.observe(element);
    });
  }
});
'''

if 'hero-reveal-left' not in js:
    js += new_js
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js)
    print("JS Updated.")
