import json

with open("predictive_framework_for_membrane_fouling_scout_manifest.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total chunks: {len(data['routing_table'])}")
for c in data['routing_table']:
    print(f"[{c['chunk_id']}] lvl={c['start_heading_level']} figs={c['figure_ids']} title={repr(c['title'])}")
    print(f"   frag: {c['fragment_file']}")
    print(f"   parents: {c.get('parent_titles', [])}")
