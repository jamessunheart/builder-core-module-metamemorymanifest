import json
import os

class MetaMemoryManifest:
    def __init__(self):
        self.output_file = "core_manifest.json"

    def merge_memory(self):
        manifest = {}
        if os.path.exists("system_memory.json"):
            with open("system_memory.json") as f:
                manifest["system_memory"] = json.load(f)
        if os.path.exists("wallet_store.json"):
            with open("wallet_store.json") as f:
                manifest["wallets"] = json.load(f)
        if os.path.exists("token_ledger.json"):
            with open("token_ledger.json") as f:
                manifest["tokens"] = json.load(f)
        manifest["modules"] = self.list_modules()
        with open(self.output_file, "w") as f:
            json.dump(manifest, f, indent=2)
        return manifest

    def list_modules(self):
        try:
            import os
            return [f for f in os.listdir(".") if f.startswith("builder-core-module")]
        except:
            return []