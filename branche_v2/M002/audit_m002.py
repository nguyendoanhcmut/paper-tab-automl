import sys
import json
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

manifest_path = r'C:\Users\Admin\.gemini\antigravity\scratch\mbr_opcond_survey\branches_v2\M002\M002_scout_manifest.json'
with open(manifest_path, 'r', encoding='utf-8') as f:
    manifest = json.load(f)

print('Doc Slug:', manifest.get('doc_slug'))
print('Doc Title:', manifest.get('doc_title'))
print('Doc Type:', manifest.get('doc_type'))
print('Max Heading Level:', manifest.get('max_heading_level'))
print('Global Lexicon:', json.dumps(manifest.get('global_lexicon'), ensure_ascii=False, indent=2))
print('\nMaster Skeleton Items:', len(manifest.get('master_skeleton', [])))
for i, item in enumerate(manifest.get('master_skeleton', [])):
    print(f"{i+1}. [{item.get('id')}] (lvl {item.get('level')}) {item.get('heading')} - words: {item.get('estimated_words')} - exercises: {item.get('has_exercises')}")

print('\nRouting Table items:', len(manifest.get('routing_table', [])))
for r in manifest.get('routing_table', []):
    print(f"Batch {r.get('batch_id')}: {r.get('assigned_sections')} -> {r.get('target_branch_file')}")
