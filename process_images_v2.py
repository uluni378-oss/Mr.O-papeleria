import os
import glob
from PIL import Image
import shutil

base_dir = r"C:\Users\repre\Documents\Mro papeleria\assets\img"
artifact_dir = r"C:\Users\repre\.gemini\antigravity\brain\5b257ddd-d9e5-494e-ae71-70e682d3015a"

tasks = [
    # (prefix, out_dir, out_name, target_width, target_height)
    ("banner_escolar_v2", "papeleria", "banner-escolar-realista.webp", 1920, 800),
    ("mision_vision_store", "local", "mision-vision-interior.webp", 800, 600),
    ("srv_digitalizacion", "servicios-rapidos", "digitalizacion.webp", 800, 600),
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

# Fallback for lonas_banners_design since generation failed
fallback_src = os.path.join(base_dir, "servicios-principales", "diseno-negocios.webp")
fallback_dst = os.path.join(base_dir, "diseno-negocios", "lonas-banners-v2.webp")
if os.path.exists(fallback_src):
    shutil.copyfile(fallback_src, fallback_dst)
    print(f"Saved {fallback_dst} (fallback)")
