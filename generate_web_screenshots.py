import asyncio
from playwright.async_api import async_playwright
import os

html_templates = {
    'web-consultorio': """
    <!DOCTYPE html>
    <html lang="es">
    <head><meta charset="utf-8"><style>
    body { font-family: 'Inter', sans-serif; margin: 0; padding: 0; background: #fdfdfd; color: #333; }
    header { background: #009DBA; color: white; padding: 1.5rem 4rem; display: flex; justify-content: space-between; align-items: center; }
    header h1 { margin: 0; font-size: 1.8rem; }
    nav { display: flex; gap: 2rem; font-weight: 500; font-size: 1.1rem; }
    .hero { display: flex; padding: 5rem 4rem; background: #e0f4f8; align-items: center; justify-content: space-between; gap: 4rem; }
    .hero-content { max-width: 50%; }
    .hero h2 { font-size: 3.5rem; color: #07365c; margin-bottom: 1.5rem; line-height: 1.1; }
    .hero p { font-size: 1.4rem; line-height: 1.6; color: #555; margin-bottom: 2rem; }
    .btn { background: #25D366; color: white; padding: 1rem 2rem; border-radius: 6px; text-decoration: none; font-weight: bold; display: inline-block; font-size: 1.2rem; }
    .services { padding: 4rem 4rem; }
    .services h3 { font-size: 2.5rem; color: #07365c; margin-bottom: 3rem; text-align: center; }
    .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2.5rem; }
    .card { background: white; padding: 2.5rem; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-top: 6px solid #009DBA; }
    .card h4 { font-size: 1.5rem; margin: 0 0 1rem; color: #07365c; }
    .card p { font-size: 1.1rem; color: #666; line-height: 1.5; }
    </style></head>
    <body>
    <header><h1>Dra. Mariana López | Dentista</h1><nav><span>Inicio</span><span>Servicios</span><span>Horario</span><span>Ubicación</span></nav></header>
    <div class="hero">
        <div class="hero-content">
            <h2>Cuidado dental integral y especializado</h2>
            <p>Atención profesional para ti y tu familia. Ubicados en el centro de la ciudad, con tecnología moderna y trato amable.</p>
            <a href="#" class="btn">Agendar cita por WhatsApp</a>
        </div>
        <div style="flex:1; height: 400px; background: #ccc; border-radius: 16px; overflow: hidden;"><img src="https://images.unsplash.com/photo-1606811841689-23dfddce3e95?auto=format&fit=crop&w=800&q=80" style="width: 100%; height: 100%; object-fit: cover;"></div>
    </div>
    <div class="services">
        <h3>Nuestros Servicios</h3>
        <div class="grid">
            <div class="card"><h4>Limpieza Dental</h4><p>Prevención, diagnóstico y limpieza profunda para una sonrisa saludable.</p></div>
            <div class="card"><h4>Ortodoncia</h4><p>Alineación perfecta con brackets o alineadores invisibles de última generación.</p></div>
            <div class="card"><h4>Implantes y Prótesis</h4><p>Restauración dental segura, duradera y con acabados altamente estéticos.</p></div>
        </div>
    </div>
    </body></html>
    """,
    
    'web-negocio-local': """
    <!DOCTYPE html>
    <html lang="es">
    <head><meta charset="utf-8"><style>
    body { font-family: 'Helvetica Neue', sans-serif; margin: 0; padding: 0; background: #fff; color: #222; }
    header { background: #fff; padding: 1.5rem 4rem; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #eaeaea; }
    header h1 { margin: 0; font-size: 2rem; font-weight: 800; text-transform: uppercase; letter-spacing: 2px; }
    nav { display: flex; gap: 3rem; font-weight: 600; font-size: 1rem; text-transform: uppercase; letter-spacing: 1px; }
    .hero { position: relative; height: 600px; display: flex; align-items: center; justify-content: center; text-align: center; color: white; }
    .hero::before { content: ''; position: absolute; inset: 0; background: url('https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=1600&q=80') center/cover; filter: brightness(0.5); z-index: -1; }
    .hero h2 { font-size: 4.5rem; margin-bottom: 1.5rem; font-weight: 800; letter-spacing: -1px; }
    .hero p { font-size: 1.4rem; max-width: 700px; margin: 0 auto 2.5rem; line-height: 1.5; }
    .btn { background: #e63946; color: white; padding: 1.2rem 2.5rem; text-decoration: none; font-weight: bold; font-size: 1.2rem; border-radius: 50px; text-transform: uppercase; letter-spacing: 1px; }
    .info { display: flex; padding: 4rem; gap: 4rem; background: #f8f9fa; }
    .info-box { flex: 1; text-align: center; padding: 3rem 2rem; background: white; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.04); border: 1px solid #eee; }
    .info-box h3 { font-size: 1.6rem; margin: 0 0 1rem; color: #e63946; }
    .info-box p { font-size: 1.2rem; color: #555; margin: 0; }
    </style></head>
    <body>
    <header><h1>Rústico Café</h1><nav><span>Menú</span><span>Galería</span><span>Ubicación</span><span>Contacto</span></nav></header>
    <div class="hero">
        <div>
            <h2>Tu café de especialidad</h2>
            <p>El mejor café orgánico de la región, pan recién horneado y postres artesanales. Un espacio perfecto para relajarte o trabajar en el corazón de la ciudad.</p>
            <a href="#" class="btn">Menú y Pedidos por WhatsApp</a>
        </div>
    </div>
    <div class="info">
        <div class="info-box"><h3>📍 Ubicación</h3><p>Av. Principal 123, Colonia Centro.<br>A dos cuadras del parque.</p></div>
        <div class="info-box"><h3>🕒 Horario</h3><p>Lunes a Sábado: 8:00 am - 9:00 pm<br>Domingos: Cerrado</p></div>
        <div class="info-box"><h3>📱 Contacto</h3><p>Tel: 555-0192<br>WA: 555-0192</p></div>
    </div>
    </body></html>
    """,
    
    'web-profesionista': """
    <!DOCTYPE html>
    <html lang="es">
    <head><meta charset="utf-8"><style>
    body { font-family: 'Roboto', sans-serif; margin: 0; padding: 0; background: #111; color: #eee; }
    header { padding: 3rem 5rem; display: flex; justify-content: space-between; align-items: center; }
    header h1 { margin: 0; font-size: 1.8rem; font-weight: 300; letter-spacing: 4px; }
    nav { display: flex; gap: 3rem; font-size: 1.1rem; letter-spacing: 1px; font-weight: 300; }
    .hero { display: flex; padding: 2rem 5rem 5rem; align-items: center; gap: 5rem; }
    .hero-content { flex: 1; }
    .hero h2 { font-size: 4.5rem; color: #fff; margin-bottom: 1.5rem; line-height: 1.1; font-weight: 700; }
    .hero p { font-size: 1.4rem; line-height: 1.7; color: #aaa; margin-bottom: 3rem; }
    .btn { background: #fff; color: #111; padding: 1.2rem 2.5rem; text-decoration: none; font-weight: bold; border-radius: 2px; font-size: 1.2rem; }
    .btn-outline { background: transparent; color: white; border: 1px solid white; margin-left: 1.5rem; }
    .hero-img { flex: 1; height: 600px; background: url('https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=800&q=80') center/cover; filter: grayscale(100%); }
    </style></head>
    <body>
    <header><h1>ROBERTO LUNA | ARQUITECTURA</h1><nav><span>Proyectos</span><span>Estudio</span><span>Contacto</span></nav></header>
    <div class="hero">
        <div class="hero-content">
            <h2>Diseño de espacios funcionales y estéticos</h2>
            <p>Arquitecto independiente con más de 10 años de experiencia en proyectos residenciales y comerciales. Transformando ideas en realidades habitables y sostenibles.</p>
            <div>
                <a href="#" class="btn">Ver Proyectos</a>
                <a href="#" class="btn btn-outline">Contacto Directo</a>
            </div>
        </div>
        <div class="hero-img"></div>
    </div>
    </body></html>
    """,
    
    'web-comercio': """
    <!DOCTYPE html>
    <html lang="es">
    <head><meta charset="utf-8"><style>
    body { font-family: 'Segoe UI', sans-serif; margin: 0; padding: 0; background: #fafafa; color: #333; }
    header { background: #FFD166; padding: 1.5rem 4rem; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
    header h1 { margin: 0; font-size: 2.2rem; color: #118AB2; font-weight: 900; }
    nav { display: flex; gap: 2rem; font-weight: bold; color: #118AB2; font-size: 1.2rem; }
    .banner { background: #118AB2; color: white; padding: 4rem; text-align: center; }
    .banner h2 { font-size: 3.5rem; margin: 0 0 1rem; font-weight: 800; }
    .banner p { font-size: 1.4rem; max-width: 800px; margin: 0 auto 2rem; }
    .btn { background: #FFD166; color: #118AB2; padding: 1rem 2.5rem; border-radius: 50px; text-decoration: none; font-weight: 800; font-size: 1.2rem; }
    .grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem; padding: 3rem 4rem; }
    .item { background: white; border-radius: 12px; padding: 1.5rem; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }
    .item img { width: 100%; height: 200px; object-fit: cover; border-radius: 8px; margin-bottom: 1.5rem; }
    .item h4 { margin: 0 0 0.5rem; color: #118AB2; font-size: 1.4rem; }
    .item p { color: #666; margin: 0; font-size: 1.1rem; }
    </style></head>
    <body>
    <header><h1>Mueblería Hogar Feliz</h1><nav><span>Salas</span><span>Comedores</span><span>Recámaras</span><span>Contacto</span></nav></header>
    <div class="banner">
        <h2>Renueva tu hogar esta temporada</h2>
        <p>Visita nuestra tienda física y descubre los mejores muebles al mejor precio. ¡Menciona nuestra página web y obtén envío local gratis en todas tus compras!</p>
        <a href="#" class="btn">📍 Ver Ubicación de Tienda</a>
    </div>
    <div class="grid">
        <div class="item"><img src="https://images.unsplash.com/photo-1555041469-a586c61ea9bc?auto=format&fit=crop&w=400&q=80"><h4>Sillas de diseño</h4><p>Variedad de estilos</p></div>
        <div class="item"><img src="https://images.unsplash.com/photo-1540574163026-643ea20ade25?auto=format&fit=crop&w=400&q=80"><h4>Sofás cómodos</h4><p>Para toda la familia</p></div>
        <div class="item"><img src="https://images.unsplash.com/photo-1595526114035-0d45ed16cfbf?auto=format&fit=crop&w=400&q=80"><h4>Mesas de centro</h4><p>Acabados de primera</p></div>
        <div class="item"><img src="https://images.unsplash.com/photo-1505693314120-0d443867091c?auto=format&fit=crop&w=400&q=80"><h4>Decoración</h4><p>Detalles únicos</p></div>
    </div>
    </body></html>
    """
}

async def generate():
    from PIL import Image
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for name, html in html_templates.items():
            page = await browser.new_page(viewport={'width': 1600, 'height': 1000})
            await page.set_content(html, wait_until='networkidle')
            path_jpg = os.path.join('assets', 'img', 'paginas-web', f'{name}.jpg')
            path_webp = os.path.join('assets', 'img', 'paginas-web', f'{name}.webp')
            await page.screenshot(path=path_jpg, type='jpeg', quality=90)
            print(f"Generated {name}.jpg")
            img = Image.open(path_jpg)
            img.save(path_webp, 'webp', quality=90)
            os.remove(path_jpg)
            print(f"Converted {name}.webp")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(generate())
