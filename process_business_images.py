import os
import glob
from PIL import Image

output_dir = r"C:\Users\repre\Documents\Mro papeleria\assets\img\diseno-negocios"
os.makedirs(output_dir, exist_ok=True)

images = [
    ("logotipos_realista", "logotipos-realista.webp"),
    ("tarjetas_presentacion", "tarjetas-presentacion-realistas.webp"),
    ("lonas_banners", "lonas-banners-realistas.webp"),
    ("redes_sociales", "redes-sociales-realistas.webp"),
    ("papeleria_corporativa", "papeleria-corporativa-realista.webp"),
    ("impresos_promocionales", "impresos-promocionales-realistas.webp"),
]

artifact_dir = r"C:\Users\repre\.gemini\antigravity\brain\5b257ddd-d9e5-494e-ae71-70e682d3015a"

for prefix, out_name in images:
    # Find the most recent generated image matching the prefix
    pattern = os.path.join(artifact_dir, f"{prefix}*.png")
    matches = glob.glob(pattern)
    if not matches:
        print(f"No image found for {prefix}")
        continue
    
    # Sort by modification time to get the newest one
    matches.sort(key=os.path.getmtime, reverse=True)
    latest_img = matches[0]
    
    img = Image.open(latest_img).convert("RGB")
    
    # Resize and crop to exactly 1600x1000 (8:5 ratio)
    target_ratio = 1600 / 1000
    w, h = img.size
    current_ratio = w / h
    
    if current_ratio > target_ratio:
        # Image is too wide, crop width
        new_w = int(target_ratio * h)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    elif current_ratio < target_ratio:
        # Image is too tall, crop height
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        img = img.crop((0, top, w, top + new_h))
        
    img = img.resize((1600, 1000), Image.Resampling.LANCZOS)
    
    out_path = os.path.join(output_dir, out_name)
    img.save(out_path, "WEBP", quality=88, icc_profile=img.info.get("icc_profile"))
    print(f"Saved {out_name}")

