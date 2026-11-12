from datetime import datetime, timezone
from time import perf_counter
import sys
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

website = sys.argv[1] if len(sys.argv) > 1 else "https://example.com"

print(f"Checking {website}")
print(f"Checked at: {datetime.now(timezone.utc).isoformat(timespec='seconds')}")
start_time = perf_counter()

try:
    with urlopen(website, timeout=5) as response:
        response_time = perf_counter() - start_time

        print("Status: UP")
        print(f"HTTP code: {response.status}")
        print(f"Response time: {response_time:.2f} seconds")

except (HTTPError, URLError, ValueError) as error:
    print("Status: DOWN")
    print(f"Error: {error}")
    sys.exit(1)
