import os
import urllib.request
import urllib.parse
import time

project_dir = r'C:\Users\repre\Documents\Mro papeleria'
img_dir = os.path.join(project_dir, 'assets', 'img', 'servicios-rapidos')
os.makedirs(img_dir, exist_ok=True)

images = {
    "copias-blanco-negro.webp": "Professional photocopier, black and white documents stacked, sharp monochromatic print, clean commercial counter. Photorealistic, well-lit, commercial photography.",
    "copias-color.webp": "Color printer with pages coming out showing colorful charts and photos, real vibrant colors, clean commercial environment. Photorealistic, crisp.",
    "impresion-documentos.webp": "Printed PDF documents on a tidy desk with a modern computer monitor in background, school or office printing, photorealistic commercial photography.",
    "escaneo-documentos.webp": "Document placed on a flatbed scanner bed, scanning light visible, computer screen showing digital file in background, clean photorealistic.",
    "actas-nacimiento.webp": "Generic official looking certificate document being printed, blurred text, computer monitor in background, professional commercial lighting, photorealistic.",
    "curp-documento.webp": "Generic printed ID form or document, blurred fields, computer screen showing a database consultation, clean commercial photorealistic.",
    "recibo-cfe.webp": "Generic utility electricity bill being printed, blurred data, clean office environment, photorealistic commercial photography.",
    "talones-issste.webp": "Generic payroll stub or receipt document, blurred sensitive information, computer and printer in background, photorealistic.",
    "engargolado.webp": "Wire binding machine binding a document, transparent cover, black spiral ring, finished bound notebook, commercial photorealistic.",
    "enmicado.webp": "Laminating machine processing a document, shiny clear plastic lamination, clean finish, commercial photorealistic.",
    "impresion-planos.webp": "Large format printer printing an architectural blueprint, generic technical lines, roll of wide paper, photorealistic.",
    "mas-servicios.webp": "Various stationery items, a USB drive, neatly arranged folders, printed documents and a modern computer, clean desk, photorealistic commercial."
}

def download_image(filename, prompt):
    path = os.path.join(img_dir, filename)
    if os.path.exists(path) and os.path.getsize(path) > 10000:
        print(f"Already exists: {filename}")
        return True
        
    url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote(prompt)}?width=1200&height=800&nologo=true&model=flux"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as response:
            with open(path, 'wb') as f:
                f.write(response.read())
        print(f"Downloaded: {filename}")
        return True
    except Exception as e:
        print(f"Failed {filename}: {e}")
        return False

print("Retrying downloads sequentially...")
for filename, prompt in images.items():
    success = download_image(filename, prompt)
    if not success:
        time.sleep(2)
        print("Retrying once more...")
        download_image(filename, prompt)
    time.sleep(1) # wait between requests
