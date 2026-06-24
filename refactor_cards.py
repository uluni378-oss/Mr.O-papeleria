import os
import re

html_path = r"C:\Users\repre\Documents\Mro papeleria\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# I will find each quick-service-card and refactor it.
# Structure:
# <article class="quick-service-card quick-reveal">
#   <a href="URL" target="_blank" rel="noopener noreferrer" aria-label="LABEL">
#     <figure ...> ... </figure>
#     <div class="quick-service-card__content">
#       <h3>...</h3>
#       <p>...</p>
#       <span class="quick-service-card__action" aria-hidden="true">
#         <svg ...> ... </svg>
#       </span>
#     </div>
#   </a>
# </article>

def refactor_card(match):
    article_tag = match.group(1)
    a_tag = match.group(2)
    href_match = re.search(r'href="([^"]+)"', a_tag)
    aria_match = re.search(r'aria-label="([^"]+)"', a_tag)
    
    href = href_match.group(1) if href_match else "#"
    aria = aria_match.group(1) if aria_match else ""
    
    figure_content = match.group(3)
    content_div = match.group(4)
    h3_content = match.group(5)
    p_content = match.group(6)
    
    # We drop the old span with SVG and recreate it as an <a> tag
    new_action = f'''
            <a class="quick-service-card__action" href="{href}" target="_blank" rel="noopener noreferrer" aria-label="{aria}">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <path d="M7 17 17 7"></path>
                <path d="M7 7h10v10"></path>
              </svg>
            </a>'''
            
    # Assemble new card
    new_card = f'''{article_tag}
          {figure_content}
          <div class="quick-service-card__content">
            {h3_content}
            {p_content}{new_action}
          </div>
      </article>'''
    
    return new_card

pattern = r'(<article class="quick-service-card[^>]*>)\s*(<a [^>]+>)\s*(<figure class="quick-service-card__media">.*?</figure>)\s*(<div class="quick-service-card__content">)\s*(<h3>.*?</h3>)\s*(<p>.*?</p>).*?</div>\s*</a>\s*</article>'

html = re.sub(pattern, refactor_card, html, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print("HTML refactored.")
