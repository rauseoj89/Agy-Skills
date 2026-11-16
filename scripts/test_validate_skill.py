#!/usr/bin/env python3
"""Unit tests for scripts/validate-skill.py covering all 7 failure cases."""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

VALIDATOR = Path(__file__).resolve().parent / "validate-skill.py"

VALID_SKILL = """---
name: sample-skill
description: "A valid sample skill description."
version: 1.0.0
last_updated: 2026-11-16
---

# Skill: Sample

## Objective
Test objective.

## When to Use
- Case 1

## Universal Principles
1. Rule 1

## Multi-Agent Execution
### Antigravity
Run tests.

### If you do NOT have tools:
Manual steps.

## Fallbacks
| A | B | C |
| :--- | :--- | :--- |
| x | y | z |

## Verification
- [ ] Zero secrets

---

Last Updated: 2026-11-16
Version: 1.0.0
"""


def run_validator(target: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), str(target)],
        capture_output=True,
        text=True,
        check=False,
    )


def main() -> int:
    cases = {
        "1_invalid_frontmatter_version": VALID_SKILL.replace("version: 1.0.0", "version: v1"),
        "2_unquoted_colon_description": VALID_SKILL.replace(
            'description: "A valid sample skill description."',
            "description: Sample skill: with unquoted colon",
        ),
        "4_footer_mismatch": VALID_SKILL.replace("Version: 1.0.0", "Version: 9.9.9"),
        "5a_literal_secret": VALID_SKILL + '\npassword = "supersecretvalue123"\n',
        "5b_private_ip": VALID_SKILL + "\nConnect to 192.168.1.50\n",
        "6_broken_relative_link": VALID_SKILL + "\nSee [missing](does_not_exist.md)\n",
        "7_missing_section": VALID_SKILL.replace("## Fallbacks", "## Other"),
    }

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)

        # Valid single file passes
        valid_file = tmp_path / "valid_skill.md"
        valid_file.write_text(VALID_SKILL, encoding="utf-8")
        res = run_validator(valid_file)
        assert res.returncode == 0, f"Expected valid_file to pass, got:\n{res.stdout}\n{res.stderr}"

        # Case 3: directory argument works and detects duplicate names
        dup_dir = tmp_path / "dup_dir"
        dup_dir.mkdir()
        (dup_dir / "a.md").write_text(VALID_SKILL, encoding="utf-8")
        (dup_dir / "b.md").write_text(VALID_SKILL, encoding="utf-8")
        res_dup = run_validator(dup_dir)
        assert res_dup.returncode != 0, "Expected duplicate skill names in directory to fail"

        for case_name, content in cases.items():
            f = tmp_path / f"{case_name}.md"
            f.write_text(content, encoding="utf-8")
            r = run_validator(f)
            assert r.returncode != 0, f"Case {case_name} unexpectedly passed!"
            print(f"[PASS] {case_name} failed as expected")

    print("All validator test fixtures passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
