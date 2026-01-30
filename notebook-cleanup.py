import json
import sys

if len(sys.argv) < 2:
    print("Usage: python notebook-cleanup.py <input_file> [output_file]")
    print("Example: python notebook-cleanup.py notebook.ipynb notebook_fixed.ipynb")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2] if len(sys.argv) > 2 else input_file.replace('.ipynb', '_fixed.ipynb')

with open(input_file) as f:
    nb = json.load(f)

for cell in nb['cells']:
    if 'widgets' in cell.get('metadata', {}):
        for w in cell['metadata']['widgets'].values():
            w.setdefault('state', {})

with open(output_file, "w") as f:
    json.dump(nb, f, indent=2)

print(f"Cleaned notebook saved to: {output_file}")
