import os
import re

PUBLIC_DIR = r"C:\Users\repre\Documents\Mro papeleria"

def test_file_exists(rel_path):
    rel_path = rel_path.lstrip("./").lstrip("/")
    rel_path = rel_path.split("?")[0]
    rel_path = rel_path.split("#")[0]
    if not rel_path:
        return True
    
    full_path = os.path.join(PUBLIC_DIR, rel_path)
    return os.path.isfile(full_path)

html_files = ["index.html", "productos-escolares.html"]
missing = []

patterns = [
    r'src=["\']([^"\']+)["\']',
    r'href=["\']([^"\']+)["\']',
    r'poster=["\']([^"\']+)["\']',
    r'content=["\']([^"\']+)["\']' 
]

for html_file in html_files:
    path = os.path.join(PUBLIC_DIR, html_file)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    for p in patterns:
        for match in re.findall(p, content):
            if match.startswith("http") or match.startswith("data:") or match.startswith("#") or match.startswith("mailto:") or match.startswith("tel:"):
                continue
            
            # For content="", we only care if it looks like a file path
            if p.startswith('content') and not ('.' in match or '/' in match):
                continue
                
            for m in match.split(","):
                m = m.strip().split(" ")[0]
                if not test_file_exists(m):
                    missing.append((html_file, m))

css_path = os.path.join(PUBLIC_DIR, "css", "styles.css")
if os.path.isfile(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()
    for match in re.findall(r'url\(["\']?([^)"\']+)["\']?\)', css):
        if match.startswith("http") or match.startswith("data:"):
            continue
        if match.startswith("../"):
            m = match[3:]
        else:
            m = "css/" + match
        if not test_file_exists(m):
            missing.append(("styles.css", match))

if missing:
    print("Found missing files (404s) in Source:")
    for src, m in set(missing):
        print(f"  In {src}: {m}")
else:
    print("All internal links and assets exist in Source! No 404s detected.")
