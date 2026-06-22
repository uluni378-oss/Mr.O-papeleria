import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def fetch_unsplash_photo(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
        html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
        # Extract og:image
        match = re.search(r'<meta property="og:image" content="(https://images\.unsplash\.com/[^"]+)"', html)
        if match:
            base_url = match.group(1).split('?')[0] # remove query params
            final_url = base_url + "?w=1600&h=1100&fit=crop&q=88&fm=webp"
            return final_url
    except Exception as e:
        print(f"Failed {url}: {e}")
    return None

test_url = "https://unsplash.com/photos/a-stack-of-business-cards-sitting-on-top-of-a-table-aXwQ4bWzHqY"
print("Image URL:", fetch_unsplash_photo(test_url))
