import re

html_template = '''      <section class="products-showcase" aria-labelledby="productos-temporada">
        <span class="products-kicker">TEMPORADA ESCOLAR</span>
        <h2 id="productos-temporada">Marcas y productos escolares</h2>
        <p>Una selección de cuadernos, escritura, dibujo, organización y material escolar de marcas reconocidas.</p>
        <p><small>Conoce algunas de las marcas y líneas que podemos manejar. Modelos, colores y disponibilidad pueden variar.</small></p>

        <div class="filter-container">
          <button class="filter-btn active" data-filter="all">Todos</button>
          <button class="filter-btn" data-filter="cuadernos">Cuadernos</button>
          <button class="filter-btn" data-filter="escritura">Escritura</button>
          <button class="filter-btn" data-filter="colores">Colores</button>
          <button class="filter-btn" data-filter="geometria">Geometría</button>
          <button class="filter-btn" data-filter="pegamentos">Pegamentos</button>
          <button class="filter-btn" data-filter="organizacion">Organización</button>
          <button class="filter-btn" data-filter="mochilas">Mochilas</button>
        </div>

        <div class="products-grid">
{cards}
        </div>
      </section>'''

products = [
    ('cuadernos', 'scribe-cuaderno-profesional.webp', 'Cuaderno profesional Scribe', 'Scribe', 'Cuaderno profesional', 'Cuadernos y libretas', 'cuaderno profesional Scribe'),
    ('cuadernos', 'norma-cuaderno-profesional.webp', 'Cuaderno profesional Norma', 'Norma', 'Cuaderno profesional', 'Cuadernos y libretas', 'cuaderno profesional Norma'),
    ('cuadernos', 'estrella-libreta-francesa.webp', 'Libreta francesa Estrella', 'Estrella', 'Libreta francesa', 'Cuadernos y libretas', 'libreta francesa Estrella'),
    ('cuadernos', 'scribe-libreta-italiana.webp', 'Libreta italiana Scribe', 'Scribe', 'Libreta italiana', 'Cuadernos y libretas', 'libreta italiana Scribe'),
    ('escritura', 'bic-cristal.webp', 'Bolígrafo BIC Cristal', 'BIC', 'Bolígrafo Cristal', 'Escritura', 'bolígrafo BIC Cristal'),
    ('escritura', 'papermate-kilometrico.webp', 'Bolígrafo Paper Mate Kilométrico', 'Paper Mate', 'Bolígrafo Kilométrico', 'Escritura', 'bolígrafo Paper Mate Kilométrico'),
    ('escritura', 'dixon-lapiz-grafito.webp', 'Lápiz de grafito Dixon', 'Dixon', 'Lápiz de grafito', 'Escritura', 'lápices de grafito Dixon'),
    ('colores', 'crayola-colores-24.webp', 'Colores Crayola 24 piezas', 'Crayola', 'Caja de colores', 'Colores y dibujo', 'colores Crayola'),
    ('colores', 'faber-castell-colores.webp', 'Colores Faber-Castell 24 piezas', 'Faber-Castell', 'Caja de colores', 'Colores y dibujo', 'colores Faber-Castell'),
    ('colores', 'norma-colores-24.webp', 'Colores Norma 24 piezas', 'Norma', 'Caja de colores', 'Colores y dibujo', 'colores Norma'),
    ('colores', 'maped-color-peps.webp', 'Colores Maped Color Peps', 'Maped', 'Colores Color Peps', 'Colores y dibujo', 'colores Maped Color Peps'),
    ('escritura', 'sharpie-marcador.webp', 'Marcador permanente Sharpie', 'Sharpie', 'Marcador permanente', 'Marcadores', 'marcador permanente Sharpie'),
    ('escritura', 'stabilo-marcatextos.webp', 'Marcatextos Stabilo Boss', 'Stabilo', 'Marcatextos Boss', 'Marcadores', 'marcatextos Stabilo Boss'),
    ('geometria', 'maped-geometria.webp', 'Juego de geometría Maped', 'Maped', 'Juego de geometría', 'Geometría y accesorios', 'juego de geometría Maped'),
    ('geometria', 'barrilito-compas.webp', 'Compás escolar Barrilito', 'Barrilito', 'Compás escolar', 'Geometría y accesorios', 'compás Barrilito'),
    ('geometria', 'pelikan-tijeras.webp', 'Tijeras escolares Pelikan', 'Pelikan', 'Tijeras escolares', 'Corte y manualidades', 'tijeras escolares Pelikan'),
    ('pegamentos', 'pritt-pegamento.webp', 'Pegamento en barra Pritt', 'Pritt', 'Pegamento en barra', 'Pegamentos', 'pegamento en barra Pritt'),
    ('pegamentos', 'resistol-850.webp', 'Pegamento blanco Resistol 850', 'Resistol', 'Pegamento blanco 850', 'Pegamentos', 'pegamento Resistol 850'),
    ('organizacion', 'norma-carpeta.webp', 'Carpeta escolar Norma', 'Norma', 'Carpeta escolar', 'Organización', 'carpeta escolar Norma'),
    ('organizacion', 'wilson-jones-archivador.webp', 'Archivador Wilson Jones', 'Wilson Jones', 'Folder / Archivador', 'Organización', 'archivador Wilson Jones'),
    ('mochilas', 'chenson-mochila.webp', 'Mochila escolar Chenson', 'Chenson', 'Mochila escolar', 'Mochilas y estuches', 'mochila Chenson')
]

cards_html = []
for cat, img, alt, brand, title, p_cat, wa in products:
    url_wa = "https://wa.me/527471013037?text=Hola,%20quiero%20consultar%20la%20disponibilidad%20del%20producto%20" + wa.replace(" ", "%20")
    cards_html.append(f'''          <article class="product-card" data-category="{cat}">
            <div class="product-card-image">
              <img src="./assets/img/productos-reales/{img}" alt="{alt}" loading="lazy">
            </div>
            <div class="product-card-content">
              <span class="product-brand">{brand}</span>
              <h3>{title}</h3>
              <p class="product-category">{p_cat}</p>
              <a href="{url_wa}" target="_blank" rel="noopener">Consultar disponibilidad</a>
            </div>
          </article>''')

replacement = html_template.replace('{cards}', '\n'.join(cards_html))

with open('productos-escolares.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the section using regex
pattern = re.compile(r'<section class="products-showcase" aria-labelledby="productos-temporada">.*?</section>', re.DOTALL)
new_content = pattern.sub(replacement, content)

with open('productos-escolares.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Done!')
