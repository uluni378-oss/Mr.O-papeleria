import os
import re
import shutil

ROOT_DIR = r'C:\Users\repre\Documents\Mro papeleria'

def get_all_files():
    files_list = []
    total_size = 0
    for root, dirs, files in os.walk(ROOT_DIR):
        if '.git' in dirs: dirs.remove('.git')
        if 'node_modules' in dirs: dirs.remove('node_modules')
        if '_cleanup_quarantine' in dirs: dirs.remove('_cleanup_quarantine')
            
        for f in files:
            path = os.path.join(root, f)
            files_list.append(path)
            total_size += os.path.getsize(path)
    return files_list, total_size

files, initial_size = get_all_files()
print(f'Initial total files: {len(files)}')
print(f'Initial total size: {initial_size} bytes')

# Identify references
references = set()
for f in files:
    if f.endswith(('.html', '.css', '.js')):
        with open(f, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            # find all string literals that look like paths
            paths = re.findall(r'[\'\"\(]([a-zA-Z0-9_\-\./\\]+\.(?:jpg|jpeg|png|webp|svg|gif|ico|css|js|html|woff|woff2|ttf|json|xml|webmanifest))[\'\")]', content)
            for p in paths:
                p_norm = p.split('?')[0].split('#')[0]
                p_norm = p_norm.lstrip('./').lstrip('/')
                references.add(p_norm.lower().replace('\\', '/'))

print(f'Found {len(references)} references.')

all_images = []
for f in files:
    rel_path = os.path.relpath(f, ROOT_DIR).replace('\\', '/')
    if rel_path.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.svg', '.gif')):
        all_images.append(rel_path)

used_images = []
unused_images = []
for img in all_images:
    if any(x in img.lower() for x in ['favicon', 'og-image', 'apple-touch-icon', 'android-chrome', 'safari-pinned-tab', 'mstile']):
        used_images.append(img)
    else:
        basename = os.path.basename(img).lower()
        is_used = False
        for ref in references:
            if basename in ref:
                is_used = True
                break
        if is_used:
            used_images.append(img)
        else:
            unused_images.append(img)

print(f'Unused images: {len(unused_images)}')
for u in unused_images:
    print(f'Unused: {u}')

temp_extensions = ('.tmp', '.temp', '.bak', '.old', '.log', '.cache')
temp_files = [os.path.relpath(f, ROOT_DIR) for f in files if f.endswith(temp_extensions)]
print(f'Temp files: {temp_files}')

scripts = [os.path.relpath(f, ROOT_DIR) for f in files if f.endswith('.py') and not f.endswith('audit.py')]
print(f'Scripts: {scripts}')

# List possible duplicates or unused html
other_html = [os.path.relpath(f, ROOT_DIR) for f in files if f.endswith('.html') and os.path.basename(f) not in ('index.html', '404.html')]
print(f'Other HTML: {other_html}')

# List possible old css/js
other_css = [os.path.relpath(f, ROOT_DIR) for f in files if f.endswith('.css') and os.path.basename(f) not in ('styles.css')]
print(f'Other CSS: {other_css}')

