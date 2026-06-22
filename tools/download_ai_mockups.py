import os
import urllib.request

project_dir = r'C:\Users\repre\Documents\Mro papeleria'
out_dir = os.path.join(project_dir, 'assets', 'img', 'identidad-marca')

def download_pollinations(prompt, filename, w=1600, h=1100):
    url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote(prompt)}?width={w}&height={h}&nologo=true&model=flux"
    path = os.path.join(out_dir, filename)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(path, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Failed {filename}: {e}")

# 1. Identidad completa
download_pollinations("photorealistic high-end corporate identity branding mockup on wooden studio table, showing letterhead, business cards, tablet with website, smartphone, paper envelope. natural soft lighting, depth of field, minimalist, professional, no text, 50mm lens", "identidad-completa-realista.webp", 2000, 1500)

# 2. Logotipo
download_pollinations("photorealistic sketchbook with pencil drawings of a minimalist logo next to printed logo on premium textured paper card, metal ruler, mechanical pencil, wooden desk, soft studio lighting, macro photography", "logotipo-realista.webp")

# 3. Banners y redes
download_pollinations("photorealistic mockup showing a modern laptop, a smartphone and a tablet on a sleek desk, displaying consistent brand design colors, natural window lighting, premium office environment, sharp focus", "banners-redes-realista.webp")

# 4. Tarjetas de presentacion
download_pollinations("macro photography of a stack of premium thick business cards with textured matte paper and subtle spot UV gloss on a concrete table, beautiful natural lighting, deep shadows, 50mm lens", "tarjetas-presentacion-realistas.webp")

# 5. Papeleria comercial
download_pollinations("photorealistic corporate stationery mockup set on an elegant cream surface, showing letterhead, folder, envelope, notebook, and clips. clean composition, top down angle 45 degrees, realistic paper texture, soft shadows", "papeleria-comercial-realista.webp")

# 6. Material promocional
download_pollinations("photorealistic mockup of printed promotional materials, tri-fold brochure, flyer, small poster and tags on a concrete surface, sharp print quality, natural lighting, commercial product photography", "material-promocional-realista.webp")

print("All images generated via Pollinations AI.")
