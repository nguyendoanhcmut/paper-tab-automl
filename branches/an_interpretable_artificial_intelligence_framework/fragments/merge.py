import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r'C:\antgravity workplace\ML\PAPER TAB AUTOML\branche\an_interpretable_artificial_intelligence_framework'
frag_dir = os.path.join(base_dir, 'fragments')
out_path = os.path.join(base_dir, 'an_interpretable_artificial_intelligence_framework_branches.md')

with open(os.path.join(frag_dir, 'ch01_intro_and_system_branches.md'), encoding='utf-8') as f:
    ch01 = f.read()

with open(os.path.join(frag_dir, 'ch02_ml_methods_shap_opt_branches.md'), encoding='utf-8') as f:
    ch02 = f.read()

with open(os.path.join(frag_dir, 'ch03_prediction_performance_branches.md'), encoding='utf-8') as f:
    ch03 = f.read()

with open(os.path.join(frag_dir, 'ch04_process_interpretability_branches.md'), encoding='utf-8') as f:
    ch04 = f.read()

with open(os.path.join(frag_dir, 'ch05_operational_basin_perspectives_branches.md'), encoding='utf-8') as f:
    ch05 = f.read()

doc = []
doc.append('---')
doc.append('markmap:')
doc.append('  initialExpandLevel: 2')
doc.append('  maxWidth: 420')
doc.append('---')
doc.append('')
doc.append('# Khung Trí Tuệ Nhân Tạo Có Thể Diễn Giải Định Nghĩa Vùng Vận Hành MBR Xử Lý Nước Thải Bán Dẫn (An Interpretable AI Framework for Defining MBR Operational Basin)')
doc.append('')

# 1. Giới thiệu
p1_match = re.search(r'(## 1\. Giới thiệu.*)(?=## 2\.)', ch01, re.DOTALL)
if p1_match:
    doc.append(p1_match.group(1).strip())
    doc.append('')

# 2. Mô hình và phương pháp
doc.append('## 2. Mô hình và phương pháp (Models and Methods)')
doc.append('')

# Section 2.1 - 2.4 from ch01
p2_part1 = re.search(r'## 2\. Mô hình và phương pháp[^\n]*\n(.*)', ch01, re.DOTALL)
if p2_part1:
    doc.append(p2_part1.group(1).strip())
    doc.append('')

# Section 2.5 - 2.8 from ch02
p2_part2 = re.search(r'## 2\. Mô hình và phương pháp[^\n]*\n(.*)', ch02, re.DOTALL)
if p2_part2:
    doc.append(p2_part2.group(1).strip())
    doc.append('')

# 3. Kết quả và thảo luận
doc.append('## 3. Kết quả và thảo luận (Results and Discussion)')
doc.append('')

# 3.1 from ch03: change ## 3.1 to ### 3.1, ### 3.1.x to #### 3.1.x, #### 3.1.x.y to - **3.1.x.y...**
ch03_lines = ch03.strip().split('\n')
for line in ch03_lines:
    if line.startswith('## 3.1.'):
        doc.append('### ' + line[3:].strip())
    elif line.startswith('### 3.1.'):
        doc.append('#### ' + line[4:].strip())
    elif line.startswith('#### 3.1.'):
        title = line[5:].strip()
        doc.append(f'- **{title}**:')
    else:
        doc.append(line)
doc.append('')

# 3.2 from ch04: change ## 3.2 to ### 3.2, ### 3.2.x to #### 3.2.x, #### 3.2.x.y to - **3.2.x.y...**
ch04_lines = ch04.strip().split('\n')
for line in ch04_lines:
    if line.startswith('## 3.2.'):
        doc.append('### ' + line[3:].strip())
    elif line.startswith('### 3.2.'):
        doc.append('#### ' + line[4:].strip())
    elif line.startswith('#### 3.2.'):
        title = line[5:].strip()
        doc.append(f'- **{title}**:')
    else:
        doc.append(line)
doc.append('')

# In ch05: 3.3, 3.4, and 4
ch05_sec3_match = re.search(r'(## 3\.3\..*)(?=## 4\. Kết luận)', ch05, re.DOTALL)
ch05_sec4_match = re.search(r'(## 4\. Kết luận.*)', ch05, re.DOTALL)

if ch05_sec3_match:
    sec3_text = ch05_sec3_match.group(1).strip()
    for line in sec3_text.split('\n'):
        if line.startswith('## 3.3.') or line.startswith('## 3.4.'):
            doc.append('### ' + line[3:].strip())
        elif line.startswith('### 3.3.') or line.startswith('### 3.4.'):
            doc.append('#### ' + line[4:].strip())
        elif line.startswith('#### '):
            title = line[5:].strip()
            doc.append(f'- **{title}**:')
        else:
            doc.append(line)
    doc.append('')

if ch05_sec4_match:
    doc.append(ch05_sec4_match.group(1).strip())
    doc.append('')

merged_text = '\n'.join(doc)

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(merged_text)

print(f'Successfully merged into {out_path}')
print(f'Total lines: {len(merged_text.splitlines())}')
print(f'Total words: {len(merged_text.split())}')
print(f'Total bytes: {len(merged_text.encode("utf-8"))}')
