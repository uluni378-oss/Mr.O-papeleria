import os
from PIL import Image, ImageDraw, ImageFilter

project_dir = r'C:\Users\repre\Documents\Mro papeleria'
out_dir = os.path.join(project_dir, 'assets', 'img', 'identidad-marca')
os.makedirs(out_dir, exist_ok=True)

W, H = 1600, 1000

def create_shadow(size, offset, radius, opacity=100):
    shadow = Image.new('RGBA', (size[0] + radius*4, size[1] + radius*4), (0,0,0,0))
    draw = ImageDraw.Draw(shadow)
    draw.rectangle([radius*2, radius*2, radius*2+size[0], radius*2+size[1]], fill=(0,0,0,opacity))
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius))
    return shadow, (offset[0]-radius*2, offset[1]-radius*2)

def draw_card(img, position, size, radius=10, fill=(255,255,255), shadow_radius=25, shadow_offset=(0,20), shadow_opacity=40):
    shadow, sh_pos = create_shadow(size, (position[0]+shadow_offset[0], position[1]+shadow_offset[1]), shadow_radius, shadow_opacity)
    img.alpha_composite(shadow, sh_pos)
    card = Image.new('RGBA', size, (0,0,0,0))
    draw = ImageDraw.Draw(card)
    if radius > 0:
        draw.rounded_rectangle([0, 0, size[0], size[1]], radius=radius, fill=fill)
    else:
        draw.rectangle([0, 0, size[0], size[1]], fill=fill)
    img.alpha_composite(card, position)
    return card

def draw_mock_text(draw, position, width, lines, color=(220, 225, 230, 255), line_height=12):
    for i in range(lines):
        # Vary width slightly for a realistic text block look
        w = width if i < lines - 1 else int(width * 0.7)
        draw.rounded_rectangle([position[0], position[1] + i*(line_height+8), position[0] + w, position[1] + i*(line_height+8) + line_height], radius=4, fill=color)

def get_base():
    # Warm gray studio background
    return Image.new('RGBA', (W, H), color=(235, 238, 240, 255))

# 1. Logotipo
img1 = get_base()
draw_card(img1, (400, 150), (800, 700), radius=5, fill=(255,255,255,255))
draw1 = ImageDraw.Draw(img1)
# Grid
for i in range(400, 1200, 50):
    draw1.line([(i, 150), (i, 850)], fill=(0,0,0, 10), width=1)
for i in range(150, 850, 50):
    draw1.line([(400, i), (1200, i)], fill=(0,0,0, 10), width=1)
# Logo
draw1.ellipse([700, 350, 900, 550], fill=(0, 157, 186, 255))
draw1.polygon([(800, 450), (950, 400), (850, 600)], fill=(250, 186, 43, 255))
draw_mock_text(draw1, (700, 700), 200, 2, color=(150, 160, 170, 255))
# Pencil
draw_card(img1, (1100, 200), (15, 500), radius=5, fill=(50,50,50,255), shadow_radius=10, shadow_offset=(5,10))
img1.convert('RGB').save(os.path.join(out_dir, 'identidad-logotipo.webp'), 'WEBP', quality=90)

# 2. Tarjetas de presentación
img2 = get_base()
draw_card(img2, (500, 250), (500, 300), radius=15, fill=(250, 186, 43, 255)) # Back
draw_card(img2, (650, 450), (500, 300), radius=15, fill=(255,255,255, 255)) # Front
draw2 = ImageDraw.Draw(img2)
draw2.ellipse([700, 550, 780, 630], fill=(0, 157, 186, 255)) # Logo on front
draw_mock_text(draw2, (830, 560), 250, 3, color=(150, 160, 170, 255))
img2.convert('RGB').save(os.path.join(out_dir, 'identidad-tarjetas.webp'), 'WEBP', quality=90)

# 3. Banners
img3 = get_base()
draw_card(img3, (250, 150), (450, 700), radius=0, fill=(255,255,255,255)) # Roll-up
draw3 = ImageDraw.Draw(img3)
draw3.rectangle([250, 150, 700, 400], fill=(0, 157, 186, 255)) # Roll-up top image
draw_mock_text(draw3, (300, 450), 300, 4)

draw_card(img3, (800, 300), (600, 300), radius=0, fill=(255,255,255, 255)) # Web banner
draw3.rectangle([800, 300, 1100, 600], fill=(250, 186, 43, 255)) # Banner img
draw_mock_text(draw3, (1150, 400), 200, 4)
img3.convert('RGB').save(os.path.join(out_dir, 'identidad-banners.webp'), 'WEBP', quality=90)

# 4. Redes sociales
img4 = get_base()
# Left phone
draw_card(img4, (250, 250), (350, 500), radius=35, fill=(40,45,50, 255)) 
draw_card(img4, (270, 270), (310, 460), radius=20, fill=(255,255,255, 255))
draw_card(img4, (290, 300), (270, 270), radius=10, fill=(0, 157, 186, 255), shadow_opacity=0)
draw4 = ImageDraw.Draw(img4)
draw_mock_text(draw4, (290, 600), 270, 2)

# Center tablet
draw_card(img4, (700, 200), (600, 600), radius=35, fill=(40,45,50, 255))
draw_card(img4, (730, 230), (540, 540), radius=15, fill=(255,255,255, 255))
draw_card(img4, (760, 260), (480, 350), radius=10, fill=(250, 186, 43, 255), shadow_opacity=0)
draw_mock_text(draw4, (760, 650), 480, 2)
img4.convert('RGB').save(os.path.join(out_dir, 'identidad-redes.webp'), 'WEBP', quality=90)

# 5. Papelería comercial
img5 = get_base()
draw_card(img5, (300, 100), (500, 750), radius=0, fill=(255,255,255,255)) # Letterhead
draw5 = ImageDraw.Draw(img5)
draw5.ellipse([350, 150, 400, 200], fill=(0, 157, 186, 255))
draw_mock_text(draw5, (350, 250), 400, 15)

draw_card(img5, (900, 200), (500, 250), radius=0, fill=(245,245,245,255)) # Envelope
draw5.ellipse([950, 250, 1000, 300], fill=(0, 157, 186, 255))

draw_card(img5, (950, 600), (400, 200), radius=5, fill=(250, 186, 43, 255)) # Card
draw5.ellipse([1000, 650, 1050, 700], fill=(255,255,255, 255))
draw_mock_text(draw5, (1100, 650), 200, 3, color=(255,255,255,200))
img5.convert('RGB').save(os.path.join(out_dir, 'identidad-papeleria.webp'), 'WEBP', quality=90)

# 6. Material promocional
img6 = get_base()
draw_card(img6, (400, 150), (250, 700), radius=0, fill=(250,250,250,255)) # Tri-fold 1
draw_card(img6, (650, 150), (250, 700), radius=0, fill=(255,255,255,255)) # Tri-fold 2
draw_card(img6, (900, 150), (250, 700), radius=0, fill=(245,245,245,255)) # Tri-fold 3
draw6 = ImageDraw.Draw(img6)
draw6.rectangle([650, 150, 900, 450], fill=(0, 157, 186, 255))
draw_mock_text(draw6, (680, 500), 190, 8)

draw_card(img6, (300, 450), (450, 300), radius=5, fill=(250, 186, 43, 255)) # Flyer
draw6.ellipse([350, 500, 420, 570], fill=(255,255,255, 255))
draw_mock_text(draw6, (450, 500), 250, 5, color=(255,255,255,200))
img6.convert('RGB').save(os.path.join(out_dir, 'identidad-promocional.webp'), 'WEBP', quality=90)

print("High-quality clay mockups successfully generated.")
