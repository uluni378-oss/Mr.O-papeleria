import os
import shutil
import json
import re

ROOT_DIR = r'C:\Users\repre\Documents\Mro papeleria'
QUARANTINE_DIR = os.path.join(ROOT_DIR, '_cleanup_quarantine')
TOOLS_DIR = os.path.join(ROOT_DIR, 'tools')
DOCS_DIR = os.path.join(ROOT_DIR, 'docs')
SOURCE_ASSETS_DIR = os.path.join(ROOT_DIR, 'source-assets')

for d in [QUARANTINE_DIR, TOOLS_DIR, DOCS_DIR, SOURCE_ASSETS_DIR]:
    os.makedirs(d, exist_ok=True)

# Add quarantine to .gitignore
gitignore_path = os.path.join(ROOT_DIR, '.gitignore')
if os.path.exists(gitignore_path):
    with open(gitignore_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if '_cleanup_quarantine/' not in content:
        with open(gitignore_path, 'a', encoding='utf-8') as f:
            f.write('\n_cleanup_quarantine/\n')
else:
    with open(gitignore_path, 'w', encoding='utf-8') as f:
        f.write('_cleanup_quarantine/\n')

def get_all_files():
    files_list = []
    total_size = 0
    for root, dirs, files in os.walk(ROOT_DIR):
        dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '_cleanup_quarantine', 'tools', 'docs', 'source-assets']]
        for f in files:
            path = os.path.join(root, f)
            files_list.append(path)
            total_size += os.path.getsize(path)
    return files_list, total_size

files_before, size_before = get_all_files()

# Identify references
references = set()
for f in files_before:
    if f.endswith(('.html', '.css', '.js', '.json', '.xml', '.md', '.webmanifest')):
        with open(f, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            paths = re.findall(r'[\'\"\(]([a-zA-Z0-9_\-\./\\]+\.(?:jpg|jpeg|png|webp|svg|gif|ico|css|js|html|woff|woff2|ttf|json|xml|webmanifest))[\'\")]', content)
            for p in paths:
                p_norm = p.split('?')[0].split('#')[0]
                p_norm = p_norm.lstrip('./').lstrip('/')
                references.add(p_norm.lower().replace('\\', '/'))

used_images = []
unused_images = []
all_images = [f for f in files_before if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.svg', '.gif'))]

for img_path in all_images:
    rel_path = os.path.relpath(img_path, ROOT_DIR).replace('\\', '/')
    if any(x in rel_path.lower() for x in ['favicon', 'og-image', 'apple-touch-icon', 'android-chrome', 'safari-pinned-tab', 'mstile']):
        used_images.append(img_path)
    else:
        basename = os.path.basename(rel_path).lower()
        is_used = False
        for ref in references:
            if basename in ref:
                is_used = True
                break
        if is_used:
            used_images.append(img_path)
        else:
            unused_images.append(img_path)

# Find duplicates
import hashlib
def file_hash(filepath):
    h = hashlib.md5()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

hashes = {}
duplicates = []
for f in files_before:
    # only check images and html/css for duplicates
    if f.endswith(('.jpg', '.jpeg', '.png', '.webp', '.svg', '.html', '.css')):
        fh = file_hash(f)
        if fh in hashes:
            # duplicate found
            duplicates.append(f)
        else:
            hashes[fh] = f

moved_files = []

def move_file(src, dest_dir):
    rel = os.path.relpath(src, ROOT_DIR)
    dest = os.path.join(dest_dir, rel) if dest_dir == QUARANTINE_DIR else os.path.join(dest_dir, os.path.basename(src))
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.move(src, dest)
    moved_files.append((rel, dest_dir))

# Move unused images
real_photos_keywords = ['interior', 'equipo', 'local']
for img in unused_images:
    basename = os.path.basename(img).lower()
    is_real = any(k in img.lower() for k in real_photos_keywords)
    if is_real:
        move_file(img, SOURCE_ASSETS_DIR)
    else:
        move_file(img, QUARANTINE_DIR)

# Move temp files
temp_exts = ('.tmp', '.temp', '.bak', '.old', '.log', '.cache')
temp_files = [f for f in files_before if f.endswith(temp_exts)]
for t in temp_files:
    move_file(t, QUARANTINE_DIR)

# Move scripts
scripts = [f for f in files_before if f.endswith('.py') and os.path.basename(f) not in ('generate_web_screenshots.py',)]
for s in scripts:
    move_file(s, TOOLS_DIR)

# Move docs/notes (txt, md) except README.md and cleanup-report.md
notes = [f for f in files_before if f.endswith(('.txt', '.md')) and os.path.basename(f) not in ('README.md', 'cleanup-report.md')]
for n in notes:
    move_file(n, DOCS_DIR)

# Move unused HTML / old CSS
other_html = [f for f in files_before if f.endswith('.html') and os.path.basename(f) not in ('index.html', '404.html')]
for h in other_html:
    move_file(h, QUARANTINE_DIR)

other_css = [f for f in files_before if f.endswith('.css') and os.path.basename(f) not in ('styles.css',)]
for c in other_css:
    move_file(c, QUARANTINE_DIR)

# Re-calculate size
files_after, size_after = get_all_files()

report = {
    'total_files_before': len(files_before),
    'size_before_bytes': size_before,
    'total_files_after': len(files_after),
    'size_after_bytes': size_after,
    'moved': moved_files,
    'duplicates': [os.path.relpath(d, ROOT_DIR) for d in duplicates]
}

with open(os.path.join(ROOT_DIR, 'cleanup-report.json'), 'w') as f:
    json.dump(report, f, indent=2)

print("Cleanup script executed successfully.")
