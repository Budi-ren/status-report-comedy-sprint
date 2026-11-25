import os

LINE = "My context window filled up, so I summarized the task; the summary asked me what the task was."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "entry.txt")
expected = LINE.encode("utf-8")
assert 1 <= len(LINE) <= 200 and LINE.strip()

with open(output_path, "wb") as entry:
    entry.write(expected)

os.chmod(output_path, 0o644)
with open(output_path, "rb") as entry:
    actual = entry.read()
assert actual == expected

print(len(LINE))
