import os
import re

html_path = r"C:\Users\repre\Documents\Mro papeleria\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Update JSON-LD to add sameAs if it doesn't exist
json_ld_pattern = r'("url":\s*"https://uluni378-oss.github.io/Mr.O-papeleria/")(\s*\})'
if '"sameAs"' not in html:
    html = re.sub(json_ld_pattern, r'\1,\n    "sameAs": [\n      "https://www.facebook.com/MrOPapeleria",\n      "https://www.instagram.com/mr.opapeleria/"\n    ]\2', html)

# Replace the social links in the footer
# Old footer block looks something like:
#      <a href="https://www.facebook.com/MrOPapeleria" target="_blank" rel="noopener">Facebook</a>
#      <span>Instagram</span>
social_replacement = '''      <div style="margin-top: 1rem;">
        <span style="display: block; font-size: 0.85rem; color: rgba(255,255,255,0.7); margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.5px;">Síguenos</span>
        <div class="social-links">
          <a class="social-link social-link--facebook" href="https://www.facebook.com/MrOPapeleria" target="_blank" rel="noopener noreferrer" aria-label="Visitar Facebook de Mr.O Papelería" title="Facebook">
            <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
              <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.469h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.469h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
            </svg>
          </a>
          <a class="social-link social-link--instagram" href="https://www.instagram.com/mr.opapeleria/" target="_blank" rel="noopener noreferrer" aria-label="Visitar Instagram de Mr.O Papelería" title="Instagram">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
              <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
              <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
            </svg>
          </a>
        </div>
      </div>'''

old_links_pattern = r'<a href="https://www.facebook.com/MrOPapeleria"[^>]*>Facebook</a>\s*<span>Instagram</span>'
html = re.sub(old_links_pattern, social_replacement, html)

# Just in case they are slightly different:
old_links_pattern2 = r'<a href="https://www.facebook.com/MrOPapeleria"[^>]*>Facebook</a>\s*<a[^>]*>Instagram</a>'
html = re.sub(old_links_pattern2, social_replacement, html)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("HTML updated.")
