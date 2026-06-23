import os
import re

base_dir = r"C:\Users\repre\Documents\Mro papeleria"

# 1. Update HTML
index_path = os.path.join(base_dir, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace('class="category-card reveal"', 'class="category-card category-card-reveal"')

svgs = {
    "C": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>',
    "M": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path><path d="M10 2v20"></path></svg>',
    "A": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>',
    "T": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19l7-7 3 3-7 7-3-3z"></path><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"></path><path d="M2 2l7.586 7.586"></path><circle cx="11" cy="11" r="2"></circle></svg>',
    "D": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"></path><line x1="7" y1="7" x2="7.01" y2="7"></line></svg>',
    "W": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg>'
}

def replace_icon(m):
    letter = m.group(1)
    svg = svgs.get(letter, letter)
    return f'<div class="category-icon" aria-hidden="true">{svg}</div>'

html = re.sub(r'<div class="category-icon">([CMATDW])</div>', replace_icon, html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)


# 2. Update CSS
css_path = os.path.join(base_dir, "css", "styles.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Replace padding-block of .section
css = re.sub(r'\.section \{\s*padding-block:.*?;?\s*\}', '.section {\n  padding-block: clamp(3rem, 5vw, 5.5rem);\n}', css)

# Fix excessive spacing rules, avoid 100vh on anything except hero if it's there
css = re.sub(r'min-height:\s*100vh;', 'min-height: 0;', css)
css = re.sub(r'\.hero \{\s*min-height:\s*0;', '.hero {\n  min-height: 100vh;', css) # Restore hero

# Find and replace excessive margins/paddings 
css = re.sub(r'margin-top:\s*6rem;', 'margin-top: clamp(2.5rem, 4vw, 4rem);', css)
css = re.sub(r'margin-bottom:\s*6rem;', 'margin-bottom: clamp(2.5rem, 4vw, 4rem);', css)

# Remove any padding-block: 8rem;
css = re.sub(r'padding-block:\s*8rem;', 'padding-block: clamp(3rem, 5vw, 5.5rem);', css)

# Insert the new requested rules
new_css = '''
.category-card__icon {
  display: grid;
  width: 48px;
  height: 48px;
  place-items: center;
  border: 4px solid #ffffff;
  border-radius: 50%;
  background: #00a6c8;
  color: #ffffff;
  box-shadow: 0 8px 20px rgba(7, 54, 92, 0.16);
}
.category-card__icon svg {
  width: 24px;
  height: 24px;
}

.category-icon {
  display: grid !important;
  place-items: center;
}
.category-icon svg {
  width: 24px;
  height: 24px;
}

.category-card-reveal {
  opacity: 0;
  transform: translateY(16px);
  transition: opacity 0.52s ease, transform 0.52s ease;
}

.category-card-reveal.is-visible {
  opacity: 1;
  transform: translateY(0);
}

.category-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.category-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 18px 38px rgba(8, 39, 59, 0.14);
}

.category-card:hover img {
  transform: scale(1.025);
}

@media (prefers-reduced-motion: reduce) {
  .category-card-reveal,
  .category-card,
  .category-card img {
    opacity: 1;
    transform: none;
    transition: none;
  }
}

.mission-vision {
  padding-bottom: clamp(2.5rem, 4vw, 4rem);
}
.categories {
  padding-top: clamp(2rem, 3vw, 3rem);
  padding-bottom: clamp(2.5rem, 4vw, 4rem);
}
.school-season {
  margin-top: 0;
}

@media (max-width: 700px) {
  .section {
    padding-block: 2.75rem;
  }
  .section--compact {
    padding-block: 2rem;
  }
}
'''
if '.category-card-reveal' not in css:
    css += new_css

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

# 3. Update JS
js_path = os.path.join(base_dir, "js", "main.js")
with open(js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

new_js = '''
// CATEGORY CARDS REVEAL OBSERVER
document.addEventListener("DOMContentLoaded", () => {
  const categoryCards = document.querySelectorAll(".category-card-reveal");
  if(categoryCards.length > 0) {
    const categoryObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.15, rootMargin: "0px 0px -40px 0px" });

    categoryCards.forEach((card, index) => {
      card.style.transitionDelay = `${index * 65}ms`;
      categoryObserver.observe(card);
    });
  }
});
'''

if 'categoryObserver' not in js_content:
    js_content += new_js
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js_content)

print("Update completed.")
