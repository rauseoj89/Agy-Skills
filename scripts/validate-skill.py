#!/usr/bin/env python3
"""Universal Skills Validator for Agy-Skills"""
import re
import sys
from pathlib import Path

# Force UTF-8 stdout to avoid Windows console encoding errors
if sys.platform.startswith('win'):
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def validate_skill(file_path: Path) -> bool:
    raw_content = file_path.read_text(encoding="utf-8")
    # Normalize CRLF to LF for consistent validation across operating systems
    content = raw_content.replace("\r\n", "\n")
    issues = []
    
    # 1. Verify frontmatter
    if not content.startswith('---\nname:'):
        issues.append("❌ Missing YAML frontmatter or name")
        
    # 2. Verify "Multi-Agent Execution" section
    if "Multi-Agent Execution" not in content:
        issues.append("❌ Missing multi-agent execution section")
        
    # 3. Verify fallback sections
    if "If you do NOT have tools" not in content and "Fallback" not in content:
        issues.append("❌ Missing fallbacks for tool-less environments")
        
    # 4. Verify no agent-specific hardcoded paths
    specific_patterns = [
        r'~\/\.hermes/', r'~\/\.antigravity/', r'~\/\.cline/'
    ]
    for pattern in specific_patterns:
        if re.search(pattern, content):
            issues.append(f"⚠️  Specific agent path found: {pattern}")
            
    # 5. Verify universal principles
    if "Universal Principles" not in content:
        issues.append("⚠️  Recommended to add universal principles section")
        
    if issues:
        print(f"\n📄 {file_path}:")
        for issue in issues:
            print(f"   {issue}")
        return False
    else:
        print(f"✅ {file_path}: Valid")
        return True

def should_skip(file_path: Path) -> bool:
    name_lower = file_path.name.lower()
    path_lower = str(file_path).lower()
    
    # Skip documentation, instructions, reviews, and templates by explicit filenames or directory components
    if any(k in name_lower for k in ["template", "readme", "migration", "instruction", "website_post"]):
        return True
    if name_lower.endswith(".bak"):
        return True
    # Skip dedicated review / resource directories
    parts_lower = [p.lower() for p in file_path.parts]
    if "chg-review" in parts_lower or "resources" in parts_lower:
        return True
    return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        skill_file = Path(sys.argv[1])
        if validate_skill(skill_file):
            sys.exit(0)
        else:
            sys.exit(1)
            
    valid_count = 0
    total_count = 0
    
    for ext in ["md", "md.universal"]:
        for skill_file in sorted(Path(".").rglob(f"*.{ext}")):
            if should_skip(skill_file):
                continue
            total_count += 1
            if validate_skill(skill_file):
                valid_count += 1
                
    print(f"\n📊 Summary: {valid_count}/{total_count} valid skills")
    if valid_count < total_count:
        sys.exit(1)
