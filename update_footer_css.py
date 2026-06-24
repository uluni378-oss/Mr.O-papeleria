import os

css_path = r"C:\Users\repre\Documents\Mro papeleria\css\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

new_css = '''
.footer-social-links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.65rem;
  margin-top: 0.75rem;
}

.footer-social-link {
  display: inline-flex;
  min-height: 42px;
  padding: 0.65rem 0.9rem;
  align-items: center;
  gap: 0.55rem;
  border: 1px solid rgba(255, 255, 255, 0.28);
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.08);
  color: #ffffff;
  font-size: 0.92rem;
  font-weight: 700;
  line-height: 1;
  text-decoration: none;
  transition: transform 0.22s ease, background-color 0.22s ease, border-color 0.22s ease, box-shadow 0.22s ease;
}

.footer-social-link__icon {
  width: 20px;
  height: 20px;
  flex: 0 0 20px;
}

.footer-social-link:hover,
.footer-social-link:focus-visible {
  transform: translateY(-2px);
  border-color: #00a6c8;
  background: #00a6c8;
  color: #ffffff;
  box-shadow: 0 8px 20px rgba(0, 166, 200, 0.22);
}

.footer-social-link:focus-visible {
  outline: 3px solid rgba(255, 255, 255, 0.85);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .footer-social-link {
    transform: none;
    transition: none;
  }
}
'''

if ".footer-social-links {" not in css:
    with open(css_path, "a", encoding="utf-8") as f:
        f.write("\n" + new_css)
    print("CSS updated.")
else:
    print("CSS already contains .footer-social-links.")
