# Domain: Sport

Training and racing (HYROX, strength, running, then cycling and swimming) and the Element Logbook app.
Notion domain page: **🏃 Sport** (`40619ca7989381abb531ce6f783a94ec`). Athlete facts: 🧠 Memories with Domain = Sport.

## How each capability applies
**builder — Element Logbook.** Repo `ac-ua/c_ET`, cloud environment `app-element`, live at
https://logbook.element-training.com. The repo's `HANDOVER.md` and `docs/MOVE.md` win on conventions (artifact + guide +
in-app changelog + Build Roadmap card on every change).

**chief-of-staff.** Race dates and training blocks in Tasks (Domain = Sport). Runna's calendar is in his personal
Google Calendar.

**builder — Sport data.** Repo `ac-ua/sport` (Projects row « Sport data pipeline »), cloud environment `app-sport`.
One database of every session since 2018 (Garmin, Strava, Hercule, Element Logbook, Strava workout notes), nightly
Worker sync (intervals.icu, Strava, Element) into Cloudflare D1, BI dashboard and app. Registry, setup and release
sheet in the repo (`docs/artifacts.md`, `docs/setup.md`, `docs/RELEASE.md`). Session and note rules exist in Python
and JavaScript; `scripts/check.sh` checks they agree. Garmin watch is the source; home-trainer power once it
arrives, no power meter today.

**Coaching (later).** A `sport-coach` skill reads the database (sessions, load, recovery) and the goals on the Sport
card. Proposals are never stored as facts.

**Facts.** Only store what Aurélien stated or confirmed, with a date; never a plan Claude suggested.

## Open
- Publishable identifiers on the Element Notion page move into the repo docs; the password-like string and the Mindbody
  sandbox credentials there go to the password manager (Aurélien).
