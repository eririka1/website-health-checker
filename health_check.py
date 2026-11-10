
import sys
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

website = sys.argv[1] if len(sys.argv) > 1 else "https://example.com"

print(f"Checking {website}")

try:
    with urlopen(website, timeout=5) as response:
        print("Status: UP")
        print(f"HTTP code: {response.status}")

except (HTTPError, URLError, ValueError) as error:
    print("Status: DOWN")
    print(f"Error: {error}")
    sys.exit(1)
