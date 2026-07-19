# 🔄 Instrucciones de Migración: Agy-Skills → Multi-Agent Universal

This file outlines the migration instructions used to convert Antigravity-specific skills to universal formats.

## 🎯 Objetivo

Transformar todos los skills del repositorio actual (diseñados para Antigravity) en skills universales que funcionen en cualquier agente AI moderno (Hermes, Cline, Roo Code, GitHub Copilot, Cursor, etc.).

## 📋 Estructura Universal Requerida para Cada Skill

Todo skill actualizado DEBE tener esta estructura exacta:

```markdown
---
name: <nombre-kebab-case>
description: <Una línea clara>
version: 1.0.0
tags: [universal, <tag1>, <tag2>]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: <YYYY-MM-DD>
author: <tu-nombre>
---
# Skill: <Nombre Legible>
## 🎯 Objetivo
[Descripción agnóstica de lo que hace]
## 🕒 Cuándo usar
- Uso 1
- Uso 2
- Uso 3
## 🛡️ Principios Universales
1. **Regla 1**: Explicación (siempre aplica)
2. **Regla 2**: Explicación (siempre aplica)
...
---
## 🤖 Ejecución Multi-Agente
### ▶️ Si estás en [Agente A]:
...
```
