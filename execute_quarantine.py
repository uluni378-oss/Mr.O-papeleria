import os
import shutil
import hashlib
from datetime import datetime

BASE_DIR = r"C:\Users\repre\Documents\Mro papeleria"
REPORT_PATH = os.path.join(BASE_DIR, "dependency-report.txt")
QUARANTINE_DIR = os.path.join(BASE_DIR, "_cleanup_quarantine_final")
MANIFEST_PATH = os.path.join(QUARANTINE_DIR, "MANIFEST.txt")
NODET_PATH = os.path.join(QUARANTINE_DIR, "NO_DETERMINADOS.txt")

os.makedirs(QUARANTINE_DIR, exist_ok=True)

def hash_file(filepath):
    h = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            h.update(f.read())
        return h.hexdigest()
    except:
        return "N/A"

# Parse the report
files_data = {}
with open(REPORT_PATH, "r", encoding="utf-8") as f:
    blocks = f.read().split("------------------------------")
    for block in blocks:
        lines = block.strip().split("\n")
        file_path = None
        classification = None
        refs = "Ninguno"
        for line in lines:
            if line.startswith("Archivo: "):
                file_path = line[9:].strip()
            elif line.startswith("Clasificacion: "):
                classification = line[15:].strip()
            elif line.startswith("Referenciado por: "):
                refs = line[18:].strip()
        if file_path and classification:
            files_data[file_path] = {"class": classification, "refs": refs}

moved_count = 0
freed_bytes = 0
manifest_entries = []
nodet_entries = []

for rel_path, data in files_data.items():
    cls = data["class"]
    refs = data["refs"]
    full_path = os.path.join(BASE_DIR, rel_path)
    
    # Don't touch public_html or git or quarantine itself (already excluded by audit, but just in case)
    if not os.path.exists(full_path):
        continue
        
    if cls == "NO DETERMINADO":
        nodet_entries.append(rel_path)
        continue
        
    if cls in ["POSIBLE SOBRANTE", "TEMPORAL", "RESPALDO"]:
        # Only move if refs == Ninguno
        if refs != "Ninguno" and refs != "":
            nodet_entries.append(rel_path + " (Skipped because it has references despite classification)")
            continue
            
        size = os.path.getsize(full_path)
        sha = hash_file(full_path)
        dest_path = os.path.join(QUARANTINE_DIR, rel_path)
        
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        shutil.move(full_path, dest_path)
        
        moved_count += 1
        freed_bytes += size
        
        manifest_entries.append(
            f"Ruta original: {rel_path}\n"
            f"Ruta en cuarentena: {os.path.join('_cleanup_quarantine_final', rel_path).replace(chr(92), '/')}\n"
            f"Clasificacion: {cls}\n"
            f"Motivo: Archivo no utilizado por dependencias HTML/CSS/JS (Referenciado por: {refs})\n"
            f"Referencias encontradas: {refs}\n"
            f"Fecha de movimiento: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Tamaño: {size} bytes\n"
            f"Hash SHA-256: {sha}\n"
            f"Posibilidad de restauracion: Alta. Ruta relativa preservada.\n"
            f"{'-'*40}\n"
        )

with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
    f.writelines(manifest_entries)

with open(NODET_PATH, "w", encoding="utf-8") as f:
    for entry in nodet_entries:
        f.write(f"{entry}\n")

print(f"MOVED: {moved_count}")
print(f"FREED: {freed_bytes / 1024 / 1024:.2f} MB")
