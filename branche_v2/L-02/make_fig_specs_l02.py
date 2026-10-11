import os
import json

output_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\mbr_opcond_survey\branches_v2\L-02"
figures_manifest_path = os.path.join(output_dir, "figures_manifest.json")

with open(figures_manifest_path, "r", encoding="utf-8") as f:
    fm = json.load(f)

figures = fm.get("figures", [])

specs = []
for fig in figures:
    fid = fig["id"]
    ftype = fig.get("figure_type", "figure")
    fnum = fig.get("figure_number") or fig.get("number") or "1"
    caption = fig.get("caption", "")
    rel_path = fig.get("rel_path")
    abs_path = fig.get("abs_path")
    out_file = os.path.join(output_dir, "fragments", f"_fig_{fid}.md")
    
    is_table = (ftype == "table")
    prefix = "Bảng" if is_table else "Hình"
    
    prompt = f"""You are figure_driller for {fid}.
Parameters:
- output_dir: {output_dir}
- figure_id: {fid}
- figure_number: {fnum}
- figure_type: {ftype}
- rel_paths: ["{rel_path}"]
- abs_paths: ["{abs_path}"]
- caption: "{caption}"
- indent: 4
- output_language: vi
- output_file: {out_file}

Instructions:
1. Open image with view_file: `{abs_path}`.
2. Read the image carefully to extract exact numbers, axes, labels, trends, or table rows/columns.
3. Write an evidence block (maximum 10 lines, exactly 4-space indent) to `{out_file}`.
   The block MUST start with:
    * **{prefix} {fnum}.** Tiêu đề ngắn gọn mô tả {prefix.lower()} (tối đa 12 từ)
      * <img src="{rel_path}" alt="{prefix} {fnum}" />
      * **{prefix} này chứng minh điều gì**
        * [Phân tích ngắn gọn 1-2 gạch đầu dòng về phát hiện chính từ hình/bảng]
      * **Từ đâu mà thấy được**
        * [Chỉ rõ vị trí trực quan: trục tọa độ Ox, Oy, hàng/cột, xu hướng hoặc giá trị cụ thể quan sát được]
4. Write empty JSON [] to `{out_file}.conflicts.json`.
5. Send to parent: Figure {fnum} done. Type: {ftype}. Lines: N."""

    specs.append({
        "Model": "flash",
        "Prompt": prompt,
        "Role": f"Figure Driller {fid}",
        "TypeName": "figure_driller",
        "Workspace": "inherit",
        "scope": fid
    })

specs_file = os.path.join(output_dir, "fig_subagents.json")
with open(specs_file, "w", encoding="utf-8") as f:
    json.dump(specs, f, indent=2, ensure_ascii=False)

print(f"Generated {len(specs)} figure specs in {specs_file}")
