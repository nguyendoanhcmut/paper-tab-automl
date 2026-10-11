import os

path = "C:/antgravity workplace/ML/PAPER TAB AUTOML/llm_fe_papers/llm_fe/llm_fe_branches.html"
exists = os.path.exists(path)
size = os.path.getsize(path) if exists else 0
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

has_katex = "katex.min.js" in content
has_markmap = "markmap-view" in content
has_toggle = 'id="theme-toggle"' in content

print(f"Exists: {exists}")
print(f"Size: {size} bytes")
print(f"Has katex: {has_katex}")
print(f"Has markmap: {has_markmap}")
print(f"Has theme toggle: {has_toggle}")
