# -*- coding: utf-8 -*-
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

path = r"C:\antgravity workplace\ML\PAPER TAB AUTOML\branche\machine_learning_for_membrane_bioreactor\fragments\ch05_ung_dung_du_doan_tac_nghen_mang_branches.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

lines = text.split("\n")
print(f"Total lines: {len(lines)}")

semicolons = []
for i, l in enumerate(lines):
    if ";" in l:
        semicolons.append((i+1, l))

print(f"Semicolons found: {len(semicolons)}")
for num, line in semicolons:
    print(f"  Line {num}: {line}")

headings = [(i+1, l) for i, l in enumerate(lines) if l.strip().startswith("#")]
print(f"Headings found: {len(headings)}")
for h in headings:
    print(f"  Line {h[0]}: {h[1]}")

long_sentences = []
for i, line in enumerate(lines):
    s = line.strip()
    if s.startswith("- ") or s.startswith("  - "):
        content = re.sub(r"^\s*-\s*", "", s)
        clean_content = re.sub(r"\$\$.*?\$\$", "MATH", content)
        clean_content = re.sub(r"\$.*?\$", "MATH", clean_content)
        parts = re.split(r"(?<=[.!?])\s+", clean_content)
        for p in parts:
            words = p.strip().split()
            if len(words) > 25:
                long_sentences.append((i+1, len(words), p))

print(f"Long sentences (>25 words): {len(long_sentences)}")
for l in long_sentences:
    print(f"  Line {l[0]} ({l[1]} words): {l[2]}")
