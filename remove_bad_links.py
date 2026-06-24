import os
import re

html_path = r"C:\Users\repre\Documents\Mro papeleria\public_html\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

html = re.sub(r'<link rel="stylesheet" href="./css/location\.css">\s*', '', html)
html = re.sub(r'<link rel="stylesheet" href="./css/ux-improvements\.css">\s*', '', html)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Removed missing CSS links from public_html/index.html")
