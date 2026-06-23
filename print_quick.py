import re
h = open('C:\\Users\\repre\\Documents\\Mro papeleria\\index.html', encoding='utf-8').read()
m = re.search(r'(<section class="quick-services">.*?</section>)', h, re.DOTALL)
if m:
    print(m.group(1)[:2000])
else:
    print("Not found")
