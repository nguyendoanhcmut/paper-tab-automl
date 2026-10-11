import json
import os

output_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\mbr_opcond_survey\branches_v2\L-01"
manifest_path = os.path.join(output_dir, "L-01_scout_manifest.json")
with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

context_pack = manifest.get("global_context_pack", "")
rt = manifest.get("routing_table", [])

subagents = []
for entry in rt:
    cid = entry["chunk_id"]
    title = entry["title"]
    lvl = entry["start_heading_level"]
    figs = entry.get("figure_ids", [])
    src_file = entry["section_text_file"]
    frag_file = os.path.join(output_dir, entry["fragment_file"])
    
    extra = ""
    if cid == "ch07":
        extra = "\nNote: Drill lines covering 6 Conclusion, Impact Statement, and Reproducibility Statement. Skip References."
        
    prompt = f"""You are branch_driller for chunk {cid}: {title}.
Read-scope rule: Read only this prompt, your parameter files, and script outputs. Do not open other skill files. Do not lint JSON.

Parameters:
- section_text_file: {src_file}
- section_title: {title}
- start_level: {lvl}
- max_heading_level: 4
- drill_threshold_words: 800
- figures_manifest: {output_dir}\\figures_manifest.json
- assigned_figures: {json.dumps(figs)}
- exercises: []
- domain: general
- rule_index: []
- global_context_pack: {context_pack}
- output_file: {frag_file}
- output_dir: {output_dir}
- output_language: vi{extra}

Follow procedure in system prompt:
1. Write the spine and claim bullets in Vietnamese. Keep technical terms as written. Wrap numbers/formulas in KaTeX.
2. For each assigned figure:
   - Identify the claim bullet in your fragment that states the finding the text draws from the figure.
   - Invoke subagent figure_driller (flash) with its parameters.
   - Immediately run:
     python "{output_dir}\\log_spawn.py" "{output_dir}" "figure_driller" "<conversationId>" "<figure_id>"
   - Wait for figure_driller, and insert its evidence block into the fragment.
   - Format figure block so it nests under a bullet matching regex `* **Hình N.**` or `* **Bảng N.**` immediately preceding the image asset.
3. Write fragment to output_file.
4. Verification: Invoke subagent fragment_verifier (flash) to audit the fragment against section_text_file, writing report to {output_dir}\\fragments\\{cid}_verification_1.json.
Immediately run:
python "{output_dir}\\log_spawn.py" "{output_dir}" "fragment_verifier" "<conversationId>" "{cid}"
5. Send completion message to parent."""

    subagents.append({
        "Model": "flash",
        "Prompt": prompt,
        "Role": f"Driller {cid} {title[:25]}",
        "TypeName": "branch_driller",
        "Workspace": "inherit"
    })

with open(os.path.join(output_dir, "drillers_payload.json"), "w", encoding="utf-8") as f:
    json.dump(subagents, f, indent=2, ensure_ascii=False)
print(f"Generated {len(subagents)} driller specs.")
