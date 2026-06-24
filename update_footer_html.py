import os
import re

html_path = r"C:\Users\repre\Documents\Mro papeleria\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# The block to replace:
# <div class="social-links"> ... </div>
social_replacement = '''<div class="footer-social-links">
  <a
    class="footer-social-link"
    href="https://www.facebook.com/MrOPapeleria"
    target="_blank"
    rel="noopener noreferrer"
    aria-label="Visitar Facebook de Mr.O Papelería"
  >
    <svg
      class="footer-social-link__icon"
      viewBox="0 0 24 24"
      fill="currentColor"
      aria-hidden="true"
    >
      <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.469h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.469h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
    </svg>
    <span>Facebook</span>
  </a>

  <a
    class="footer-social-link"
    href="https://www.instagram.com/mr.opapeleria/"
    target="_blank"
    rel="noopener noreferrer"
    aria-label="Visitar Instagram de Mr.O Papelería"
  >
    <svg
      class="footer-social-link__icon"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="1.9"
      stroke-linecap="round"
      stroke-linejoin="round"
      aria-hidden="true"
    >
      <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
      <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
      <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
    </svg>
    <span>Instagram</span>
  </a>
</div>'''

# Replace `<div class="social-links">...</div>` with the new HTML
# Since it's multiline, we can use a regex that matches `<div class="social-links">` up to its closing tag.
# Let's match from `<div class="social-links">` to the closing `</div>` that aligns with it.
pattern = r'<div class="social-links">.*?</div>\s*</div>'
html = re.sub(r'<div class="social-links">.*?</a>\s*</div>', social_replacement, html, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print("HTML for footer social links updated.")
