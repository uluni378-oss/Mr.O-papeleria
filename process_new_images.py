import os
import glob
from PIL import Image

base_dir = r"C:\Users\repre\Documents\Mro papeleria\assets\img"
artifact_dir = r"C:\Users\repre\.gemini\antigravity\brain\5b257ddd-d9e5-494e-ae71-70e682d3015a"

tasks = [
    # (prefix, out_dir, out_name, target_width, target_height)
    ("mro_og_image", "social", "mro-papeleria-og.webp", 1200, 630),
    ("srv_copias", "servicios-principales", "copias-impresiones.webp", 800, 600),
    ("srv_escuela", "servicios-principales", "material-escolar.webp", 800, 600),
    ("srv_oficina", "servicios-principales", "articulos-oficina.webp", 800, 600),
    ("srv_tramites", "servicios-principales", "tramites-documentos.webp", 800, 600),
    ("srv_diseno", "servicios-principales", "diseno-negocios.webp", 800, 600),
    ("srv_web", "servicios-principales", "paginas-web.webp", 800, 600),
    ("banner_escolar", "papeleria", "banner-escolar-realista.webp", 1920, 800),
]

for prefix, folder, out_name, tw, th in tasks:
    out_dir = os.path.join(base_dir, folder)
    os.makedirs(out_dir, exist_ok=True)
    
    pattern = os.path.join(artifact_dir, f"{prefix}*.png")
    matches = glob.glob(pattern)
    if not matches:
        print(f"No image found for {prefix}")
        continue
    
    matches.sort(key=os.path.getmtime, reverse=True)
    latest_img = matches[0]
    
    try:
        img = Image.open(latest_img).convert("RGB")
        w, h = img.size
        
        target_ratio = tw / th
        current_ratio = w / h
        
        if current_ratio > target_ratio:
            new_w = int(target_ratio * h)
            left = (w - new_w) // 2
            img = img.crop((left, 0, left + new_w, h))
        elif current_ratio < target_ratio:
            new_h = int(w / target_ratio)
            top = (h - new_h) // 2
            img = img.crop((0, top, w, top + new_h))
            
        img = img.resize((tw, th), Image.Resampling.LANCZOS)
        out_path = os.path.join(out_dir, out_name)
        img.save(out_path, "WEBP", quality=88, icc_profile=img.info.get("icc_profile"))
        print(f"Saved {out_path}")
    except Exception as e:
        print(f"Error processing {prefix}: {e}")
