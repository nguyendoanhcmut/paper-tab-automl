import json
import os

manifest_path = r"C:\antgravity workplace\ML\PAPER TAB AUTOML\interpretable_prediction_coagulant_dosage_automl_v2\interpretable_prediction_coagulant_dosage_automl_v2_scout_manifest.json"
txt_path = r"C:\antgravity workplace\ML\PAPER TAB AUTOML\interpretable_prediction_coagulant_dosage_automl_v2\interpretable_prediction_coagulant_dosage_automl_v2.txt"
out_src_dir = r"C:\antgravity workplace\ML\PAPER TAB AUTOML\interpretable_prediction_coagulant_dosage_automl_v2\fragments\src"
os.makedirs(out_src_dir, exist_ok=True)

with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

with open(txt_path, "r", encoding="utf-8") as f:
    full_text = f.read()

routing = manifest["routing_table"]
markers = [(c["chunk_id"], c["start_marker"]) for c in routing]
markers.append(("end", "CRediT authorship contribution"))

indices = []
for cid, m in markers:
    idx = full_text.find(m)
    print(f"{cid}: marker='{m}', pos={idx}")
    indices.append((cid, m, idx))

for i in range(len(routing)):
    cid = routing[i]["chunk_id"]
    start_pos = indices[i][2]
    end_pos = indices[i+1][2]
    if start_pos == -1:
        print(f"ERROR: Start marker not found for {cid}")
        continue
    if end_pos == -1:
        print(f"WARNING: End marker not found for {cid}, slicing to end")
        chunk_text = full_text[start_pos:]
    else:
        chunk_text = full_text[start_pos:end_pos]
    
    out_file = os.path.join(out_src_dir, f"{cid}.txt")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(chunk_text.strip())
    print(f"Wrote {out_file}: {len(chunk_text.split())} words, {len(chunk_text)} chars")
