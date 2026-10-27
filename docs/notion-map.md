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
| 🖼️ Artifacts index | page | System | `40619ca7989381508cc1d9d9e314e71f` | every claude.ai artifact by domain |
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
| 🧳 Brain — Migration inbox (under System) | page | `40619ca7989381cf9cb4dda8206db206` | 44 old memories: migrated to 🧠 Memories; kept as the archive of the work details |
| 📦 Brain — Handoff (2026-10-27) (under System) | page | `40619ca7989381659f0bc60d4591471c` | handoff bundle + full transcript (pro data: stays in Notion) |
| Expeditions | page | `83e58afbe55443f1b234ef36a63a3c1f` | |
| Sponso | database | `collection://2ae19ca7-9893-80d6-b263-000b7171b431` | never move without a validated plan |
| Camp de Base — Roadmap & changelog | database | `collection://6aec51dc-a4b4-4f69-be60-341dea003e59` | merges into Build Roadmap at the Expeditions migration |

## Domain pages
Each domain page is a top-level page that starts with its context card (from the Domain template, < 60 lines) and has
linked views of its Projects and open Tasks; the domain's existing pages sit under it.

| Domain | Page | ID |
|---|---|---|
| Work | 💼 Work | `40619ca798938177a168dccd513c8e4b` |
| Expeditions | 🧭 Expeditions (card at the top of the existing page) | `83e58afbe55443f1b234ef36a63a3c1f` |
| Sport | 🏃 Sport | `40619ca7989381abb531ce6f783a94ec` |
| Content | 🎬 Content | `40619ca798938123b03de86d3c1a9f8e` |
| Admin & Finance | 🗂️ Admin & Finance | `40619ca7989381c38215c78e47b4d0c3` |
| Career | 🎯 Career | `40619ca79893810ba6e9f983c1ffdaf6` |
| Learning | 🗣️ Learning | `40619ca79893816baeb2c5b6b4b22dac` |
| Life | 🌍 Life | `40619ca798938104ba6ae13e84101780` |
| — | 🗄️ Archive | `40619ca7989381ea9df7fac97adfd542` |

## Pages and databases the skills depend on
| What | ID | Used by |
|---|---|---|
| Sponso (inline in 💰 Sponsoring, under South Pole) | db `2ae19ca7989380408259e428ed7ec36a` · `collection://2ae19ca7-9893-80d6-b263-000b7171b431` | the 3 outreach skills — never move |
| Idee sponsors · Idee recherche | `37319ca79893804fbd90c46c840c92f4` · `3a419ca7989380c58078d01c44481dcd` | sponsor / research outreach |
| 🇪🇸 Español hub | `3dc19ca7989381c78132e747f403f832` (Producción, Recomendaciones, Catálogo, Diario: ids in the skill) | spanish-teacher |
| 🏋️ Element Logbook project page | `3ec19ca7989381e79a04f8cb11087cb1` | builder (Element) |
| Old roadmaps (copied into Build Roadmap, to archive) | Camp de Base `709d23a467e44037918e3a3da9f99d68` · Element `094a1fd8f76148938cdd569a19fc3f82` · Spanish `3d919ca798938023ac9ff5f3298a5c29` | none after the merge |

## Reorganisation of 2026-10-27 (after Aurélien's native export)
Nothing was deleted; page ids are unchanged, so old links still work.

| Page | Was under | Now under |
|---|---|---|
| Unify Apps (CRM, Demo Nuggets, Trainings, Context For Claude…) | workspace root | 💼 Work |
| ↳ QBR 23/10/2025 | the 401k call toggle | Unify Apps › Work notes (ex "Brain Drop") |
| Context For Claude | Unify Apps | 🎯 Career |
| Tik Tok, Speeches, Communication (ex "Com") | 🧭 Expeditions | 🎬 Content |
| Camera | Perso | 🎬 Content |
| Training log 2021 (ex "Prep"), Marathon plan, 🏋️ Element Logbook | Expeditions / Perso | 🏃 Sport |
| Healthcare, Taxes, US Visas, Investments | Perso › Admin | 🗂️ Admin & Finance |
| Job Hunt 2025, Job Hunt 2026, Entrepreneurship | Perso, Perso › Admin | 🎯 Career |
| Español | Perso | 🗣️ Learning |
| Voyage, Yearly review, List, Bucket Lists, NYCs, Hunting licence | Perso, root, Perso › Admin | 🌍 Life |
| Sprinklr, 2024 database, Vatnajokull, Kungerlusen, Descente du Rhone, Admin › Archive checklists, Perso (now empty) | various | 🗄️ Archive |
| Expeditions — context card | 🧭 Expeditions | 🗄️ Archive (its content now heads 🧭 Expeditions) |
| 🧳 Migration inbox, 📦 Handoff | workspace root | ⚙️ System |

Left in place on purpose: Sponso and its siblings (outreach skills), the 401k/healthcare call (a toggle block inside
Work notes, not a movable page), the UnifyApps inline Projects database (work data).
