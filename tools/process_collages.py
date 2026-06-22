import os
from PIL import Image

brain_dir = r'C:\Users\repre\.gemini\antigravity\brain\5b257ddd-d9e5-494e-ae71-70e682d3015a'
project_dir = r'C:\Users\repre\Documents\Mro papeleria'
out_dir = os.path.join(project_dir, 'assets', 'img', 'collages-escolares')
os.makedirs(out_dir, exist_ok=True)

images = [
    ('collage_cuadernos_1781981867994.png', 'collage-cuadernos.webp', (1600, 1100)),
    ('collage_escritura_1781981877949.png', 'collage-escritura.webp', (1600, 1100)),
    ('collage_colores_1781981885943.png', 'collage-colores.webp', (1600, 1100)),
    ('collage_geometria_1781981895613.png', 'collage-geometria.webp', (1600, 1100)),
    ('collage_pegamentos_1781981903009.png', 'collage-pegamentos-manualidades.webp', (1600, 1100)),
    ('collage_organizacion_1781981910541.png', 'collage-organizacion.webp', (1600, 1100)),
    ('collage_mochilas_1781981919909.png', 'collage-mochilas-estuches.webp', (1600, 1100)),
    ('collage_impresion_1781981928099.png', 'collage-impresion-oficina.webp', (1600, 1100)),
    ('collage_hero_1781981937106.png', 'collage-regreso-clases-hero.webp', (1920, 850))
]

def crop_center(img, target_width, target_height):
    width, height = img.size
    aspect_ratio = target_width / target_height
    img_ratio = width / height

    if img_ratio > aspect_ratio:
        new_width = int(aspect_ratio * height)
        offset = (width - new_width) / 2
        img = img.crop((offset, 0, width - offset, height))
    else:
        new_height = int(width / aspect_ratio)
        offset = (height - new_height) / 2
        img = img.crop((0, offset, width, height - offset))
    
    return img.resize((target_width, target_height), Image.Resampling.LANCZOS)

for src_name, dst_name, size in images:
    src_path = os.path.join(brain_dir, src_name)
    dst_path = os.path.join(out_dir, dst_name)
    if os.path.exists(src_path):
        with Image.open(src_path) as img:
            img = crop_center(img, size[0], size[1])
            img.save(dst_path, 'WEBP', quality=90)
            print(f'Saved {dst_name}')
    else:
        print(f'Error: Not found {src_path}')
