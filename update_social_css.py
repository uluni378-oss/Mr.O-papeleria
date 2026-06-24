import os

css_path = r"C:\Users\repre\Documents\Mro papeleria\css\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

new_css = '''
.social-links {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.social-link {
  display: grid;
  width: 42px;
  height: 42px;
  place-items: center;
  border: 1px solid rgba(8, 47, 83, 0.16);
  border-radius: 50%;
  background: #ffffff;
  color: #082f53;
  box-shadow: 0 6px 16px rgba(8, 39, 59, 0.10);
  transition: transform 0.22s ease, background-color 0.22s ease, color 0.22s ease, box-shadow 0.22s ease;
}

.social-link svg {
  width: 21px;
  height: 21px;
}

.social-link:hover,
.social-link:focus-visible {
  transform: translateY(-2px);
  background: #00a6c8;
  color: #ffffff;
  box-shadow: 0 9px 20px rgba(8, 39, 59, 0.16);
}

.social-link:focus-visible {
  outline: 3px solid #00a6c8;
  outline-offset: 3px;
}
'''

if ".social-links {" not in css:
    with open(css_path, "a", encoding="utf-8") as f:
        f.write("\n" + new_css)
    print("CSS updated.")
else:
    print("CSS already contains .social-links.")
