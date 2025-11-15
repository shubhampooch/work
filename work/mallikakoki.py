# mk.py
from urllib.parse import urlparse
import webbrowser

# Example URL (you can change this)
url = "/work"

# Parse the URL
parsed = urlparse(url)

# Capture the scheme
ak = parsed.scheme

# If there is no scheme (like http or https), open it as-is
if not ak:
    full_url = parsed.path
else:
    full_url = f"{ak}://{parsed.netloc or parsed.path}"

print(f"Opening URL: {full_url}")
webbrowser.open(full_url)
