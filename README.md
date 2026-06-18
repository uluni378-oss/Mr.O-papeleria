# Mr.O Papelería

Sitio web multipágina listo para subir a hosting estático desde la carpeta `public_html/`.

## Descripción

El sitio presenta a Mr.O Papelería como una papelería moderna en Chilpancingo enfocada en escuela, oficina, impresión, copias, trámites digitales básicos, digitalización y servicios de apoyo documental. Diseño gráfico y páginas web aparecen como servicios complementarios.

## Estructura

```text
public_html/
  index.html
  nosotros/index.html
  papeleria/index.html
  tramites/index.html
  servicios-digitales/index.html
  diseno-grafico/index.html
  desarrollo-web/index.html
  preguntas-frecuentes/index.html
  contacto/index.html
  css/styles.css
  js/main.js
  assets/img/
  .htaccess
  robots.txt
  sitemap.xml
```

## Probar localmente

Desde la raíz del proyecto ejecuta:

```bash
python -m http.server 8000 -d public_html
```

Luego abre:

```text
http://localhost:8000/
```

No abras directamente las carpetas con doble clic. Para probar rutas como `/papeleria/` o `/contacto/`, usa servidor local o hosting estático.

## Cambios rápidos

- Teléfono y WhatsApp: revisa los enlaces `wa.me/527471013037` en los HTML y el mensaje generado en `public_html/js/main.js`.
- Dirección: edita el bloque de contacto en `public_html/contacto/index.html`.
- Mapa: reemplaza el `src` del iframe en `public_html/contacto/index.html` donde está el comentario de Google Maps.
- Imágenes: reemplaza archivos en `public_html/assets/img/` conservando nombres simples.
- Dominio final: cambia `https://dominio-final.com/` en canonicals, `robots.txt` y `sitemap.xml`.

## Imágenes sugeridas

El sitio usa fotografías reales disponibles y placeholders visuales seguros para futuras imágenes WebP. Puedes agregar o reemplazar:

```text
papeleria-01.webp
papeleria-02.webp
impresiones-01.webp
tramites-01.webp
escuela-oficina-01.webp
servicios-digitales-01.webp
diseno-grafico-01.webp
paginas-web-01.webp
atencion-cliente-01.webp
documentos-01.webp
oficina-01.webp
mockup-web-01.webp
mockup-impresion-01.webp
mockup-tarjetas-01.webp
```

Si una imagen futura no existe, el diseño muestra un placeholder visual sin romper la página.

## Publicación

Sube el contenido de `public_html/` a la carpeta pública del hosting. El archivo `.htaccess` incluye:

```apache
AddDefaultCharset UTF-8
Options -Indexes
DirectoryIndex index.html
```

Esto ayuda a evitar índices de carpeta y fuerza UTF-8 en servidores Apache compatibles.
