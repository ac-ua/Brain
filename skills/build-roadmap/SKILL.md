---
name: build-roadmap
description: Keep the shared Notion Build Roadmap current for any personal build — one row per release or workstream, same fields and statuses everywhere. Use when planning a build, starting or finishing a release, logging an idea or suggestion for a project, or when Aurélien asks "where are we on X".
---

# build-roadmap

One database for every build: **🛠️ Build Roadmap**, data source `collection://8ce17531-538f-4186-9f58-8a8c17c14a14`.
Each project page shows a filtered view (Project = that project). Schema: `templates/notion/build-roadmap.md`.

## One row = one release or one workstream
Not one row per commit or per small fix. A row is something Aurélien would name: "Offline mode", "v1.3 — coach
programming", "Migrate to Supabase auth".

## Fields
| Property | Use |
|---|---|
| Name | short, plain |
| Status | `🤖 Claude suggestion` (your proposals) · `Idea` · `To do` · `In progress` · `Done` · `Dropped` |
| Priority | `P0 Now` · `P1 Next` · `P2 Later` · `P3 Someday` |
| Value | `High` · `Medium` · `Low` |
| Effort | `S` (< ½ day) · `M` (1–2 days) · `L` (more) |
| Area | `Harness` · `Notion` · `Routines` · `Infra` · `Domains` · `Skills`; add project-specific areas when needed |
| Detail | what and why, 1–3 sentences; link the PR when shipped |
| Version | release tag when shipped (`v1.3`, `v0.1.0`) |
| Shipped on | date it reached production |
| Project | relation to Projects (required) |

## Rules
- Your own ideas go in as `🤖 Claude suggestion`; only Aurélien promotes them to `Idea` or `To do`.
- Starting work → `In progress`. Shipped → `Done` + `Version` + `Shipped on`. Abandoned → `Dropped` (never delete).
- Fetch the data source before writing; use the project view to read, not SQL queries.
- A project shared outside, or with truly specific fields, gets its own database built from the same schema.
- Existing per-project roadmaps (Camp de Base, Element, Spanish) move here during each domain's migration, not before.
