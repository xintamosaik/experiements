from bs4 import BeautifulSoup
from pathlib import Path

# Read source HTML
source_path = Path("index.src.html")
source_html = source_path.read_text(encoding="utf-8")

# Parse the HTML
soup = BeautifulSoup(source_html, "html.parser")

# Extract all <style> and <script> tags

scripts = soup.find_all("script")

# Gather CSS and JS content

js_content = "\n\n".join(script.get_text() for script in scripts)

# Remove the original <style> and <script> tags from the HTML
for tag in scripts:
    tag.decompose()

# The remaining HTML
clean_html = soup.prettify()

# Prepare output directory
output_dir = Path("dist")
output_dir.mkdir(exist_ok=True)

# Write the files
(output_dir / "index.html").write_text(clean_html, encoding="utf-8")

(output_dir / "script.js").write_text(js_content, encoding="utf-8")

# Return summary of what was extracted
{
    "html_chars": len(clean_html),
 
    "js_chars": len(js_content),
    "html_path": str(output_dir / "index.html"),

    "js_path": str(output_dir / "script.js")
}
