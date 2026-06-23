import re
h = open('C:\\Users\\repre\\Documents\\Mro papeleria\\index.html', encoding='utf-8').read()

m = re.search(r'(<section class="hero" id="inicio">.*?</section>)', h, re.DOTALL)
if m:
    print("--- HERO ---")
    print(m.group(1)[:1000])

m2 = re.search(r'(<section id="mision-vision".*?</section>)', h, re.DOTALL)
if m2:
    print("--- MISION ---")
    print(m2.group(1)[:1500])
