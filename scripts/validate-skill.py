#!/usr/bin/env python3
"""Validador de Skills Universales para Agy-Skills"""
import re
import sys
from pathlib import Path

# Force UTF-8 stdout to avoid Windows console encoding errors
if sys.platform.startswith('win'):
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def validate_skill(file_path: Path) -> bool:
    content = file_path.read_text(encoding="utf-8")
    issues = []
    
    # 1. Verificar frontmatter
    if not content.startswith('---\nname:'):
        issues.append("❌ Faltando YAML frontmatter o nombre")
        
    # 2. Verificar sección "Ejecución Multi-Agente" o "Multi-Agent Execution"
    if "Ejecución Multi-Agente" not in content and "Multi-Agent Execution" not in content:
        issues.append("❌ Faltando sección de ejecución multi-agente")
        
    # 3. Verificar secciones de fallback
    if "Si NO tienes herramientas" not in content and "Fallback" not in content:
        issues.append("❌ Faltando fallbacks para sin herramientas")
        
    # 4. Verificar que no haya paths específicos de un agente
    patterns_especificos = [
        r'~\/\.hermes/', r'~\/\.antigravity/', r'~\/\.cline/'
    ]
    for pattern in patterns_especificos:
        if re.search(pattern, content):
            issues.append(f"⚠️  Path específico encontrado: {pattern}")
            
    # 5. Verificar principios universales
    if "Principios Universales" not in content and "Universal Principles" not in content:
        issues.append("⚠️  Recomendable agregar sección de principios universales")
        
    if issues:
        print(f"\n📄 {file_path}:")
        for issue in issues:
            print(f"   {issue}")
        return False
    else:
        print(f"✅ {file_path}: Válido")
        return True

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
        for skill_file in Path(".").rglob(f"*.{ext}"):
            # Skip templates, readmes, guides, posts, chg-reviews, and security directives resources
            if any(p in str(skill_file).lower() for p in ["template", "readme", "migration", "instruction", ".bak", "post", "chg-review", "resources\\"]):
                continue
            total_count += 1
            if validate_skill(skill_file):
                valid_count += 1
                
    print(f"\n📊 Resumen: {valid_count}/{total_count} skills válidos")
    if valid_count < total_count:
        sys.exit(1)
