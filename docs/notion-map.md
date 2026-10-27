# Notion map

Every Notion page and database the brain uses, in Aurélien's personal workspace (free plan).
URLs are `https://app.notion.com/p/<id>`. Data sources (`collection://…`) are what tools write to.

## Created in phase 1 (2026-10-27)
| Name | Kind | Parent | ID | Data source |
|---|---|---|---|---|
| ⚙️ System | page | workspace | `40619ca7989381c7ac74e43b0d146e62` | |
| 📓 Session Log | database | System | `49ffc3ee378147489d1824798ba9c908` | `collection://89c0d830-aec0-4bd7-b16f-f2d939db3d58` |
| 📥 Brain Inbox | database | System | `4f7a52915a724c7da08b3c8d9167c470` | `collection://49575d7c-0da1-43c9-a54d-5a0b3c8effc4` |
| 🧠 Memories | database | System | `2effbd92c2dc4e5ea2b059cd058b7338` | `collection://5b6902fc-e510-4975-b133-06e9273f602e` |
| 🧩 Domain template | page | System | `40619ca7989381a08cd7c93c8f4c011e` | |
| 🏠 Home | page | workspace | `40619ca79893813b8899c27a533cf076` | |
| 📋 Tasks | database | workspace | `9ac22ef9618d4645a0741102863e60fc` | `collection://d2dce682-22a5-4e39-b0d3-75b9399b5c47` |
| 📁 Projects | database | workspace | `abea83098f1f4534a66b6dc1f180e3e0` | `collection://127dc180-4e2f-4650-b120-0b4ff4cc9eab` |
| 🛠️ Build Roadmap | database | workspace | `f2b2d5bb5c2d45358bd0576dfc8af2fc` | `collection://8ce17531-538f-4186-9f58-8a8c17c14a14` |

### Projects rows
| Project | Page ID |
|---|---|
| 🧠 Brain | `40619ca79893817ba7cbc34ca914eed7` |
| 🏔️ Camp de Base | `40619ca7989381f49820cc52a06b094a` |
| 🏋️ Element Logbook | `40619ca7989381a0a5ead7c140decb3e` |
| 🇪🇸 Spanish app | `40619ca79893819e920df62835d6f33f` |
| 🌐 Personal website | `40619ca7989381f5953ddbaf568a16f5` |

### Saved views
| View | On | Shows | View URL |
|---|---|---|---|
| Today | Home | Tasks Next/Doing or due today, not Done; quick filter Context | `view://40619ca7-9893-815c-9e41-000c39625597` |
| Inbox | Home | Tasks with Status = Inbox | `view://40619ca7-9893-8137-aa4f-000c9b5d7c7c` |
| Work | Home | Tasks Context = Work, not Done, by Status | `view://40619ca7-9893-8158-bc85-000cde841a39` |
| Perso | Home | Tasks Context = Perso, not Done, by Status | `view://40619ca7-9893-81e4-ac98-000c3228bf5d` |
| Active projects | Home | Projects Status = Active | `view://40619ca7-9893-8113-861a-000c9699d8c5` |
| Latest Brain Inbox | Home | Brain Inbox New / Accepted | `view://40619ca7-9893-8175-a672-000c70ca9b59` |
| Brain roadmap | Projects → Brain | Build Roadmap, Project = Brain, by Status | `view://40619ca7-9893-81f2-aa9f-000c9911880d` |

## Existing, used by the brain (not created here)
| Name | Kind | ID | Note |
|---|---|---|---|
| About Aurélien | page (Notion Memory) | `40619ca7989381599acfdce904faf34f` | loaded at every session start |
| Memories (Notion Memory) | database | `40619ca7989381f59000cf1f8b6cff47` | Notion Memory's system database: schema locked to the API, not in the sidebar. Left as is; the brain uses 🧠 Memories |
| 🧳 Brain — Migration inbox | page | `40619ca7989381cf9cb4dda8206db206` | 44 old memories, sorted by domain |
| 📦 Brain — Handoff (2026-10-27) | page | `40619ca7989381659f0bc60d4591471c` | handoff bundle + full transcript (pro data: stays in Notion) |
| Expeditions | page | `83e58afbe55443f1b234ef36a63a3c1f` | |
| Sponso | database | `collection://2ae19ca7-9893-80d6-b263-000b7171b431` | never move without a validated plan |
| Camp de Base — Roadmap & changelog | database | `collection://6aec51dc-a4b4-4f69-be60-341dea003e59` | merges into Build Roadmap at the Expeditions migration |

## Domain context cards
Created from the Domain template when a domain is migrated; each has linked views of its Projects and open Tasks.

| Domain | Card | ID | Views |
|---|---|---|---|
| Expeditions | Expeditions — context card (child of 🧭 Expeditions) | `40619ca7989381628da7f60326404e83` | `view://40619ca7-9893-81f9-879e-000c4a6b6dce` projects · `view://40619ca7-9893-810a-83c2-000cae8a99b5` tasks |
| Content | 🎬 Content (workspace top level) | `40619ca798938123b03de86d3c1a9f8e` | `view://40619ca7-9893-81f8-b93b-000cc00eb165` projects · `view://40619ca7-9893-81fd-a19b-000ce2ad4798` tasks |

Other domains: not migrated. Add each new card here and in the routing table of `AGENTS.md`.
