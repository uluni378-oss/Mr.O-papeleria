import os

base_dir = r"C:\Users\repre\Documents\Mro papeleria"
html_path = os.path.join(base_dir, "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

json_old = '"url": "https://uluni378-oss.github.io/Mr.O-papeleria/"\n  }'
json_new = '"url": "https://uluni378-oss.github.io/Mr.O-papeleria/",\n    "sameAs": [\n      "https://www.facebook.com/MrOPapeleria",\n      "https://www.instagram.com/mr.opapeleria/"\n    ]\n  }'
html = html.replace(json_old, json_new)

footer_old = '<a href="https://www.facebook.com/MrOPapeleria" target="_blank" rel="noopener">Facebook</a>\n      <span>Instagram</span>'

footer_new = '''<div class="footer-social" style="display: flex; gap: 1rem; margin-top: 0.5rem; align-items: center;">
        <a href="https://www.facebook.com/MrOPapeleria" target="_blank" rel="noopener noreferrer" aria-label="Visitar Facebook de Mr.O Papelería" style="color: rgba(255,255,255,0.75); transition: color 0.3s ease; display: flex; align-items: center; justify-content: center;" onmouseover="this.style.color='#ffffff'" onmouseout="this.style.color='rgba(255,255,255,0.75)'">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>
        </a>
        <a href="https://www.instagram.com/mr.opapeleria/" target="_blank" rel="noopener noreferrer" aria-label="Visitar Instagram de Mr.O Papelería" style="color: rgba(255,255,255,0.75); transition: color 0.3s ease; display: flex; align-items: center; justify-content: center;" onmouseover="this.style.color='#ffffff'" onmouseout="this.style.color='rgba(255,255,255,0.75)'">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
        </a>
      </div>'''

html = html.replace(footer_old, footer_new)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Social links updated.")
