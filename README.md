# Papelería MRO

Sitio corporativo multipágina para Papelería MRO, preparado para publicarse en hosting compartido mediante cPanel, FTP o administrador de archivos.

## Carpeta de producción

La versión lista para subir está en:

```text
public_html/
```

Para publicar, sube únicamente el contenido de `public_html/` dentro de la carpeta `public_html` del hosting.

No subas:

- `.git`
- `README.md`
- archivos de trabajo
- capturas o temporales
- imágenes originales no usadas
- carpetas vacías

## Archivos importantes

`public_html/` contiene:

- Páginas HTML multipágina.
- `css/styles.css`
- `js/main.js`
- `assets/img/`
- `.htaccess`
- `robots.txt`
- `sitemap.xml`

## Dominio final

Antes de publicar, cambia `dominio-final.com` por el dominio real en:

- Canonical de cada HTML.
- `public_html/robots.txt`
- `public_html/sitemap.xml`
- Open Graph si deseas usar URLs absolutas.

## Google Maps

En `public_html/contacto/index.html`, busca:

```html
<!-- Reemplazar este src por el iframe oficial de Google Maps del local -->
```

Pega el `src` oficial del iframe del local.

## UTF-8

El sitio está guardado en UTF-8 y el `.htaccess` incluye:

```apache
AddDefaultCharset UTF-8
```

Verifica que el hosting también sirva los archivos como UTF-8.

## Pruebas recomendadas

Después de subir, prueba estas URLs:

```text
https://dominio-final.com/
https://dominio-final.com/inicio/
https://dominio-final.com/nosotros/
https://dominio-final.com/servicios-digitales/
https://dominio-final.com/diseno-grafico/
https://dominio-final.com/desarrollo-web/
https://dominio-final.com/tramites/
https://dominio-final.com/preguntas-frecuentes/
https://dominio-final.com/contacto/
```

También verifica:

- Menú flotante.
- Botón de WhatsApp.
- Formulario de contacto a WhatsApp.
- Mapa en contacto.
- Acentos y caracteres en español.
- Carga de imágenes.
- Carga de CSS y JavaScript.
