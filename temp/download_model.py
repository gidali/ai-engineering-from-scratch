

from huggingface_hub import hf_hub_download
from pathlib import Path

path = hf_hub_download(
      repo_id="sentence-transformers/all-MiniLM-L6-v2",
      filename="config.json")
size = Path(path).stat().st_size
print(f"Cached at: {path}")
print(f"Size: {size:,} bytes")
