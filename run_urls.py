import subprocess
from pathlib import Path

urls = [line.strip() for line in Path("urls.txt").read_text().splitlines() if line.strip()]

# Run in chunks so macOS shell/argv limits never bite you
CHUNK_SIZE = 30

for i in range(0, len(urls), CHUNK_SIZE):
    chunk = urls[i:i+CHUNK_SIZE]
    print(f"\nRunning chunk {i//CHUNK_SIZE + 1} ({len(chunk)} URLs)...")
    subprocess.run(["python3", "main.py", *chunk], check=False)
