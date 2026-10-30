#!/usr/bin/env python3
"""Print every tracked playbook in the repo, NUL-separated.

A file counts as a playbook when its top level is a list of plays
(mappings with `hosts`, `import_playbook` or `ansible.builtin.import_playbook`).
Inventories, vars files and vaults are skipped.
"""
import subprocess
import sys

import yaml

PLAY_KEYS = {"hosts", "import_playbook", "ansible.builtin.import_playbook"}

files = subprocess.run(
    ["git", "ls-files", "-z", "*.yml", "*.yaml"],
    check=True,
    capture_output=True,
    text=True,
).stdout.split("\0")

for path in filter(None, files):
    try:
        with open(path, encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
    except yaml.YAMLError:
        # Not YAML at all (e.g. an INI inventory named .yml); yamllint reports it
        continue
    if isinstance(data, list) and any(isinstance(p, dict) and PLAY_KEYS & p.keys() for p in data):
        sys.stdout.write(path + "\0")
