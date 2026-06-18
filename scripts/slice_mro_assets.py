from pathlib import Path
import shutil

from PIL import Image, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "source" / "mro-assets-originales.png"
REFERENCE = ROOT / "assets" / "img" / "reference" / "mro-assets-originales.png"


ASSETS = [
    ("assets/img/hero-papeleria.webp", (0, 0, 610, 315), (1200, 620)),
    ("assets/img/escuela.webp", (612, 0, 245, 265), (600, 420)),
    ("assets/img/oficina.webp", (858, 0, 150, 265), (600, 420)),
    ("assets/img/copias-impresiones.webp", (1008, 0, 185, 265), (600, 420)),
    ("assets/img/tramites.webp", (1193, 0, 170, 265), (600, 420)),
    ("assets/img/diseno-grafico.webp", (1363, 0, 173, 265), (600, 420)),
    ("assets/img/paginas-web.webp", (0, 716, 510, 195), (600, 420)),
    ("assets/img/temporada-escolar.webp", (0, 318, 745, 205), (1400, 380)),
    ("assets/img/servicios/copias-bn.webp", (754, 270, 98, 75), (420, 260)),
    ("assets/img/servicios/copias-color.webp", (886, 270, 96, 75), (420, 260)),
    ("assets/img/servicios/impresiones.webp", (1015, 270, 96, 75), (420, 260)),
    ("assets/img/servicios/escaneo.webp", (1145, 270, 96, 75), (420, 260)),
    ("assets/img/servicios/actas.webp", (1274, 270, 99, 75), (420, 260)),
    ("assets/img/servicios/curp.webp", (1407, 270, 102, 75), (420, 260)),
    ("assets/img/servicios/recibo-cfe.webp", (754, 398, 98, 75), (420, 260)),
    ("assets/img/servicios/talones-issste.webp", (886, 398, 96, 75), (420, 260)),
    ("assets/img/servicios/engargolado.webp", (1015, 398, 96, 75), (420, 260)),
    ("assets/img/servicios/enmicado.webp", (1145, 398, 96, 75), (420, 260)),
    ("assets/img/servicios/planos.webp", (1274, 398, 99, 75), (420, 260)),
    ("assets/img/servicios/mas-servicios.webp", (1407, 398, 102, 75), (420, 260)),
    ("assets/img/negocios/logotipos.webp", (207, 520, 195, 168), (600, 360)),
    ("assets/img/negocios/tarjetas.webp", (403, 520, 193, 168), (600, 360)),
    ("assets/img/negocios/lonas.webp", (597, 520, 245, 168), (600, 360)),
    ("assets/img/negocios/redes.webp", (843, 520, 215, 168), (600, 360)),
    ("assets/img/negocios/papeleria-corporativa.webp", (1295, 914, 241, 110), (600, 360)),
    ("assets/img/paginas-web-mockup.webp", (0, 716, 510, 195), (900, 450)),
    ("assets/img/personaje-mro.webp", (675, 715, 205, 205), (700, 700)),
    ("assets/img/mapa-mro.webp", (1065, 825, 470, 95), (900, 360)),
    ("assets/img/fachada-mro.webp", (1270, 520, 266, 305), (700, 700)),
    ("assets/img/tienda-interior.webp", (0, 914, 215, 110), (900, 450)),
    ("assets/img/utiles-apoyo.webp", (215, 914, 330, 110), (900, 450)),
    ("assets/img/impresora-apoyo.webp", (545, 914, 185, 110), (700, 450)),
]


def crop_resize(image: Image.Image, box, size) -> Image.Image:
    x, y, width, height = box
    crop = image.crop((x, y, x + width, y + height))
    resized = crop.resize(size, Image.Resampling.LANCZOS)
    return resized.filter(ImageFilter.UnsharpMask(radius=0.8, percent=80, threshold=3))


def main() -> None:
    if not SOURCE.exists():
        raise FileNotFoundError(f"No existe la imagen fuente: {SOURCE}")

    image = Image.open(SOURCE).convert("RGB")

    REFERENCE.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SOURCE, REFERENCE)

    for relative_path, box, size in ASSETS:
        output = ROOT / relative_path
        output.parent.mkdir(parents=True, exist_ok=True)
        asset = crop_resize(image, box, size)
        asset.save(output, "WEBP", quality=92, method=6)
        print(f"ok {relative_path} {size[0]}x{size[1]}")


if __name__ == "__main__":
    main()
