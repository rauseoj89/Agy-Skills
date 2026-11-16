#!/usr/bin/env python3
"""Universal Skills Validator for Agy-Skills."""
from __future__ import annotations

import datetime
import os
import re
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None

if sys.platform.startswith("win"):
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

KEBAB_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

SECRET_ASSIGN_RE = re.compile(
    r"""(?i)\b(password|secret|token|api_key)\b\s*[:=]\s*(['"])(?!\$\{)([^'"]{4,})\2"""
)
PRIVATE_IP_RE = re.compile(
    r"\b(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[0-1])\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3})\b"
)
MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

REQUIRED_SECTIONS = [
    "Objective",
    "When to Use",
    "Universal Principles",
    "Multi-Agent Execution",
    "Fallbacks",
    "Verification",
]


def _parse_frontmatter_fallback(fm_text: str) -> dict:
    """Strict stdlib YAML subset parser for skill frontmatter."""
    data: dict = {}
    for line in fm_text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"Invalid YAML line: {line}")
        key, raw_val = line.split(":", 1)
        key = key.strip()
        val = raw_val.strip()
        if val.startswith('"') and val.endswith('"') and len(val) >= 2:
            data[key] = val[1:-1].replace('\\"', '"')
        elif val.startswith("'") and val.endswith("'") and len(val) >= 2:
            data[key] = val[1:-1]
        elif val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            data[key] = [item.strip().strip("'\"") for item in inner.split(",") if item.strip()]
        else:
            if ":" in val:
                raise ValueError(f"Unquoted colon in YAML value for '{key}'")
            data[key] = val
    return data


def parse_frontmatter(content: str) -> tuple[dict | None, list[str]]:
    issues: list[str] = []
    if not content.startswith("---\n"):
        return None, ["Missing YAML frontmatter opening '---'"]
    end_idx = content.find("\n---\n", 4)
    if end_idx == -1:
        end_idx = content.find("\n---", 4)
        if end_idx == -1:
            return None, ["Missing YAML frontmatter closing '---'"]
    fm_text = content[4:end_idx]

    # Explicit unquoted-colon check on description
    for line in fm_text.splitlines():
        if line.startswith("description:"):
            raw_desc = line[len("description:"):].strip()
            if not (raw_desc.startswith('"') or raw_desc.startswith("'")) and ":" in raw_desc:
                issues.append("Unquoted 'description' contains ':' (wrap in double quotes)")

    if yaml is not None:
        try:
            data = yaml.safe_load(fm_text)
            if not isinstance(data, dict):
                issues.append("Frontmatter must be a YAML mapping")
                return None, issues
        except Exception as exc:
            issues.append(f"Invalid YAML frontmatter: {exc}")
            return None, issues
    else:
        try:
            data = _parse_frontmatter_fallback(fm_text)
        except ValueError as exc:
            issues.append(f"Invalid YAML frontmatter: {exc}")
            return None, issues

    return data, issues


def validate_skill(file_path: Path, seen_names: dict[str, Path] | None = None) -> bool:
    raw_content = file_path.read_text(encoding="utf-8")
    content = raw_content.replace("\r\n", "\n")
    issues: list[str] = []

    fm, fm_issues = parse_frontmatter(content)
    issues.extend(fm_issues)

    if fm is not None:
        for req in ("name", "description", "version", "last_updated"):
            if req not in fm or not str(fm[req]).strip():
                issues.append(f"Missing required frontmatter field '{req}'")

        name = str(fm.get("name", "")).strip()
        if name:
            if not KEBAB_RE.match(name):
                issues.append(f"Frontmatter 'name' must be kebab-case: '{name}'")
            if seen_names is not None:
                if name in seen_names:
                    issues.append(f"Duplicate skill name '{name}' (already in {seen_names[name]})")
                else:
                    seen_names[name] = file_path

        version = str(fm.get("version", "")).strip()
        if version and not SEMVER_RE.match(version):
            issues.append(f"Frontmatter 'version' must be semver (X.Y.Z): '{version}'")

        last_updated_raw = fm.get("last_updated", "")
        if isinstance(last_updated_raw, datetime.date):
            last_updated = last_updated_raw.isoformat()
        else:
            last_updated = str(last_updated_raw).strip()
        if last_updated and not ISO_DATE_RE.match(last_updated):
            issues.append(f"Frontmatter 'last_updated' must be ISO date (YYYY-MM-DD): '{last_updated}'")

        # Footer match check
        footer_ver = re.search(r"(?m)^Version:\s*(.+?)\s*$", content)
        footer_upd = re.search(r"(?m)^Last Updated:\s*(.+?)\s*$", content)
        if footer_ver and version and footer_ver.group(1).strip() != version:
            issues.append(
                f"Footer Version '{footer_ver.group(1).strip()}' does not match frontmatter '{version}'"
            )
        if footer_upd and last_updated and footer_upd.group(1).strip() != last_updated:
            issues.append(
                f"Footer Last Updated '{footer_upd.group(1).strip()}' does not match frontmatter '{last_updated}'"
            )

    # Required sections for Antigravity-compatible universal skills
    if "Antigravity" in content:
        for sec in REQUIRED_SECTIONS:
            if sec not in content:
                issues.append(f"Missing required section: '{sec}'")
    else:
        if "Multi-Agent Execution" not in content:
            issues.append("Missing 'Multi-Agent Execution' section")
        if "If you do NOT have tools" not in content and "Fallback" not in content:
            issues.append("Missing fallbacks for tool-less environments")

    # Specific agent hardcoded path check
    for pattern in (r"~/\.hermes/", r"~/\.antigravity/", r"~/\.cline/"):
        if re.search(pattern, content):
            issues.append(f"Specific agent path found: {pattern}")

    # Literal secrets and private IP checks (strip fenced code blocks? No, check whole file except documented regex/pattern examples)
    for idx, line in enumerate(content.splitlines(), 1):
        if SECRET_ASSIGN_RE.search(line):
            issues.append(f"Line {idx}: Possible hardcoded secret literal")
        if PRIVATE_IP_RE.search(line):
            issues.append(f"Line {idx}: Private IP literal found")

    # Relative markdown link check (skip links inside fenced code blocks)
    in_fence = False
    for idx, line in enumerate(content.splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in MD_LINK_RE.finditer(line):
            target = match.group(1).strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target_path = target.split("#", 1)[0]
            if not target_path:
                continue
            if "*" in target_path:
                parent = (file_path.parent / target_path).parent
                if not parent.exists():
                    issues.append(f"Line {idx}: Broken relative link directory '{target}'")
            else:
                resolved = (file_path.parent / target_path).resolve()
                if not resolved.exists():
                    issues.append(f"Line {idx}: Broken relative link '{target}'")

    if issues:
        print(f"\n[FAIL] {file_path}:")
        for issue in issues:
            print(f"   - {issue}")
        return False

    print(f"[OK] {file_path}: Valid")
    return True


def should_skip(file_path: Path) -> bool:
    name_lower = file_path.name.lower()
    if any(k in name_lower for k in ("template", "readme", "migration", "instruction", "website_post", "sync")):
        return True
    if name_lower.endswith(".bak"):
        return True
    parts_lower = [p.lower() for p in file_path.parts]
    if any(d in parts_lower for d in ("chg-review", "resources", ".github", "scripts", "tests", "fixtures")):
        return True
    return False


def collect_skills(target: Path) -> list[Path]:
    if target.is_file():
        return [target]
    files: list[Path] = []
    for ext in ("md", "md.universal"):
        for skill_file in sorted(target.rglob(f"*.{ext}")):
            if not should_skip(skill_file):
                files.append(skill_file)
    return files


def main() -> int:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    if not target.exists():
        print(f"Target path not found: {target}", file=sys.stderr)
        return 1

    skills = collect_skills(target)
    if not skills:
        print(f"No skill files found under: {target}", file=sys.stderr)
        return 1

    seen_names: dict[str, Path] | None = {} if target.is_dir() else None
    valid_count = 0
    for skill_file in skills:
        if validate_skill(skill_file, seen_names):
            valid_count += 1

    print(f"\nSummary: {valid_count}/{len(skills)} valid skills")
    return 0 if valid_count == len(skills) else 1


if __name__ == "__main__":
    sys.exit(main())
