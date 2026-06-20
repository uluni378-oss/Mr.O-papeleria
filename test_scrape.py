import requests
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

print("Testing Lumen...")
try:
    r = requests.get('https://lumen.com.mx/buscar?q=cuaderno+scribe', headers=headers, timeout=10)
    print("Status:", r.status_code)
    # look for image urls
    imgs = re.findall(r'src="(https://[^"]+\.jpg)"', r.text)
    print("Found JPGs:", len(imgs))
    if imgs:
        print("Sample:", imgs[:3])
except Exception as e:
    print("Lumen error:", e)

print("\nTesting Office Depot...")
try:
    r = requests.get('https://www.officedepot.com.mx/officedepot/en/search/?text=cuaderno+scribe', headers=headers, timeout=10)
    print("Status:", r.status_code)
except Exception as e:
    print("Office Depot error:", e)
