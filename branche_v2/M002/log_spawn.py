import os
import sys
import json
import time

def log_spawn(output_dir, role, conv_id, scope):
    log_path = os.path.join(output_dir, "spawn_log.json")
    for _ in range(10):
        try:
            data = []
            if os.path.exists(log_path):
                with open(log_path, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                    if content:
                        data = json.loads(content)
            # check if already exists
            exists = False
            for entry in data:
                if entry.get("conversationId") == conv_id:
                    exists = True
                    break
            if not exists:
                data.append({
                    "role": role,
                    "conversationId": conv_id,
                    "scope": scope
                })
                with open(log_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
            break
        except Exception as e:
            time.sleep(0.5)

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python log_spawn.py <output_dir> <role> <conv_id> <scope>")
        sys.exit(1)
    log_spawn(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
