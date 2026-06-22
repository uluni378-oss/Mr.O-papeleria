from duckduckgo_search import DDGS
import json

try:
    with DDGS() as ddgs:
        results = list(ddgs.images("Cuaderno profesional Scribe site:officedepot.com.mx", max_results=3))
        print("Office Depot:", json.dumps(results, indent=2))
        
        if not results:
            results2 = list(ddgs.images("Cuaderno profesional Scribe site:walmart.com.mx", max_results=3))
            print("Walmart:", json.dumps(results2, indent=2))
            
except Exception as e:
    print(f"Error: {e}")
