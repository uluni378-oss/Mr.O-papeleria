import os
p = r'C:\Users\repre\Documents\Mro papeleria\index.html'
c = open(p, encoding='utf-8').read()
c = c.replace('<img src="./assets/img/local/mision-vision-interior.webp"', '<img src="./assets/img/hero-papeleria.webp"')
open(p, 'w', encoding='utf-8').write(c)
print("Image restored")
