import json

manifest_path = "C:/antgravity workplace/ML/PAPER TAB AUTOML/llm_fe_papers/llm_fe/llm_fe_scout_manifest.json"
with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

subagents = []
for c in manifest["routing_table"]:
    cid = c["chunk_id"]
    title = c["title"]
    s_lvl = c["start_heading_level"]
    thresh = c.get("drill_threshold_words", 800)
    figs = c.get("figure_ids", [])
    sec_txt = c["section_text_file"].replace("\\", "/")
    frag_file = c["fragment_file"]
    out_file = f"C:/antgravity workplace/ML/PAPER TAB AUTOML/llm_fe_papers/llm_fe/{frag_file}".replace("\\", "/")
    prompt = f"""Read-scope: read only prompt, parameter files, and script outputs.
chunk_id: {cid}, title: "{title}", start_level: {s_lvl}, max_level: 4, threshold: {thresh}
section_text_file: {sec_txt}
output_file: {out_file}
assigned_figures: {figs}
figures_manifest: C:/antgravity workplace/ML/PAPER TAB AUTOML/llm_fe_papers/llm_fe/figures_manifest.json
global_context_pack: C:/antgravity workplace/ML/PAPER TAB AUTOML/llm_fe_papers/llm_fe/global_context_pack.md
output_language: vi. Drill Vietnamese Markdown subtree fragment directly to output_file in UTF-8."""

    subagents.append({
        "Model": "flash",
        "TypeName": "branch_driller",
        "Role": f"Driller {cid}",
        "Prompt": prompt
    })

s = json.dumps(subagents, ensure_ascii=False)
print("Compact total characters:", len(s), "Estimated tokens:", len(s) // 4)
with open("C:/antgravity workplace/ML/PAPER TAB AUTOML/llm_fe_papers/llm_fe/subagents_compact.json", "w", encoding="utf-8") as f:
    json.dump(subagents, f, indent=2, ensure_ascii=False)
