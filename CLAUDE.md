# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A **Quartz v4** static site serving as a D&D campaign wiki for the "Wordle Warriors" campaign. Content lives in `content/` as Obsidian-flavored Markdown. The site deploys to GitHub Pages at `wordlewarriors.github.io/normal-door-opening/` on push to the `v4` branch.

## Commands

```bash
# Local development - build and serve with hot reload
npx quartz build --serve

# Production build (output goes to public/)
npx quartz build

# Type check + Prettier format check
npm run check

# Auto-format all files
npm run format

# Run tests
npm test

# Sync frontmatter tags from inline #hashtags across all content files
python scripts/update_metadata.py
# Or for a specific subdirectory:
python scripts/update_metadata.py content/Sessions
```

Node.js version: 22 (see `.node-version`). Use `npm ci` to install dependencies.

## Architecture

### Quartz Configuration
- **`quartz.config.ts`** - Plugin pipeline (transformers, filters, emitters) and site theme. Key settings: `ObsidianFlavoredMarkdown`, `CrawlLinks` with shortest-path resolution, `RemoveDrafts` filter.
- **`quartz.layout.ts`** - Page layout components (sidebar, graph view, backlinks, TOC, explorer).
- Folders matching `private/`, `templates/`, `.obsidian` are excluded from the build.

### Content Structure (`content/`)
| Folder | Purpose |
|--------|---------|
| `Sessions/` | Session notes, one file per session (YYYY-MM-DD.md) |
| `People/` | NPC and character pages |
| `Places/` | Location pages |
| `Organisations/` | Faction and group pages |
| `Bad Guys/` | Antagonist pages |
| `Monsters/` | Monster entries |
| `Props/` | Physical prop images and notes |
| `OneShots/` | One-shot session notes |
| `templates/` | Obsidian templates (excluded from build) |

### Frontmatter Schema (Sessions)
```yaml
date: 'YYYY-MM-DD'
title: 'YYYY-MM-DD'
draft: false
session: 26          # session number
arc: Plague Investigation
themes:
  - plague
  - soultrial
tags:
  - aust
  - jorund
```

### Tag Management
Inline `#hashtag` references in body text are automatically merged into the frontmatter `tags` list by `scripts/update_metadata.py`. Run this script after editing content files to keep frontmatter in sync. The dashboard (`content/dashboard.md`) uses Dataview queries against frontmatter fields.

### Wikilinks
Content uses Obsidian-style `[[Page Name]]` wikilinks. Quartz resolves these with shortest-path matching (`markdownLinkResolution: "shortest"`).

### Deployment
Push to `v4` branch triggers `.github/workflows/deploy.yml`, which builds with `npx quartz build` and deploys the `public/` directory to GitHub Pages.
