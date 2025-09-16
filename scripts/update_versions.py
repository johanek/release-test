#!/usr/bin/env python3
import sys
import re
from pathlib import Path

if len(sys.argv) != 2:
    print("Usage: update_versions.py <version>")
    sys.exit(1)

version = sys.argv[1]

# update README.md
readme_file = Path("README.md")
readme_text = readme_file.read_text()

readme_text_new = re.sub(
  r"(version:)\s+([0-9]+\.[0-9]+\.[0-9]+)",
  rf"\1 {version}",
  readme_text
)

readme_file.write_text(readme_text_new)
print(f"Updated {readme_file} to version {version}")
