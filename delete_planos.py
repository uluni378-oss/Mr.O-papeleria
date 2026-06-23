import os

base_dir = r"C:\Users\repre\Documents\Mro papeleria"
html_path = os.path.join(base_dir, "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

def remove_article(html, text_to_find):
    start = 0
    while True:
        idx = html.find(text_to_find, start)
        if idx == -1:
            break
        
        # Find the start of the <article> before idx
        article_start = html.rfind('<article class="quick-service-card', 0, idx)
        
        # Find the end of the </article> after idx
        article_end = html.find('</article>', idx)
        if article_end != -1:
            article_end += len('</article>')
            
            # Also consume preceding whitespace
            while article_start > 0 and html[article_start-1] in ' \t\r\n':
                article_start -= 1
                
            html = html[:article_start] + '\n' + html[article_end:]
            # start remains 0 since html shrank
        else:
            start = idx + len(text_to_find)
            
    return html

html = remove_article(html, "Impresión de planos")
html = remove_article(html, "Impresi&oacute;n de planos")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Planos card removed safely.")
