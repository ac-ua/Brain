# Personal Drive map

Aurélien's personal Google Drive (`a.caye@hotmail.com`, My Drive). Personal files live here; Notion holds the context
and the links. Layout applied on 2026-10-29. Folder ids never change when a folder is renamed or moved, so tools,
links and the finance app keep working. The work Drive has its own map: `docs/drive-map.md`.

## Tree
```
My Drive
├── 00_Inbox            drop zone: anything not yet filed. Emptied at session close
├── 10_Admin            ID · Visas · Health & Insurance · Housing · Permits & Licences · Education (Baraja backups)
│                       · Jucy Stuff (private, never opened)
├── 20_Finance          read by the finance app (ac-ua/finance) by folder id
│   ├── Banks           one sub-folder per bank (Chase, N26, Revolut, Emirates NBD, Boursorama, La Banque Postale, Amex)
│   ├── Income          payslips per employer + Payslip - Finance.xlsx
│   ├── Taxes           FR <year> · US <year> = income of that year (declared the next spring) · Dons & Misc · amende
│   ├── Investments     PEA · PEE · Assurance Vie · SCPI · 401k - UnifyApps · Shareworks · Projets
│   ├── Real Estate     Marseille - 313 rue Saint Pierre · Avignon - 10 Lanterne · Expert Comptable · Groupe Victor
│   │                   · Projects (Invisty, Escale royale, simulations) · Canceled
│   ├── Advisers        Magdae · Old compta
│   └── Retirement · Receipts
├── 30_Expeditions      planning and ideas only; a finished expedition moves to One Life
│   ├── _Common         gear sheets, Gear invoices, Inspi (films, other expeditions' decks)
│   ├── Planet Heritage Project   the association (statuts, PV, déclarations)
│   ├── South Pole 2027 · Greenland Kite 2027
│   └── Ideas           North West Passage · Morocco - Mhamid · Vatnajökull · Rhône kayak · Plan Laponie
├── 40_Projects         Harbat (run club, SHARED with the club) · Harbat - private (not shared) · Sport data (raw
│                       exports for the sport pipeline) · Places (Mapstr → Google Maps) · Travel (trip planning)
│                       · Famileo US · Old Projects
├── 50_Content          Speeches · Koh Lanta (castings)
├── 60_Library          media, not sorted: Movies · Games · Books · Software · Musique · Musiques pour videos
│                       · Expedition mp3 · Audio to sort
├── 70_Work & Career    CV & Job Search · one folder per employer (UnifyApps, Sprinklr): contracts, career admin and
│                       copies of pro deliverables brought back from the work Mac (pro → perso is allowed). Payslips
│                       stay in 20_Finance/Income
├── 80_Backups          Phone Backup · Claude Backup (claude-home, voice-clone, Notion exports) · Apps: one folder per
│                       personal app (Camp de Base, Sport, Finance), weekly database exports `<app>-YYYY-MM-DD.sql.gz`
│                       from Cloudflare (Aurélien's call, 2026-10-30). Element Logbook (club app, Supabase) keeps its own
├── 99_Archive          dead material and emptied folders. Deleting is Aurélien's call
├── One Life            the photo archive, one folder per trip `YYYY.MM.DD Country - Place`. Leave as is
├── Saved from Chrome   created by Chrome. Leave as is
```

## Rules
- **Where a new file goes:** by domain, as above; unsure → `00_Inbox`. Never at the root.
- **Expeditions:** a planned expedition gets `30_Expeditions/<Name> <year>`, named like its Notion page; its link goes
  at the top of that page. When it is done, its folder moves into its One Life trip folder and the Notion page and
  the 🧭 Expeditions card (« Files: past expeditions ») point there.
- **Finance:** one folder per bank, per year (taxes), per flat; new years and banks get a new sub-folder with the same
  naming (`FR 2026`, `US 2026`). Account numbers and identifiers never go in Notion or this repo.
- **Harbat** is shared with the club: anything moved into it is visible to the club. Guest lists and drafts go to
  `Harbat - private (not shared)`.
- **One Life:** only expedition folders are linked from Notion; photos are never sorted by an agent. Two folders exist
  twice (`2019.08.16 France - Alpes - Alpine Crossing`, `2020.01.06 Norvège - Finnmark - Les enragés`): merging is
  Aurélien's call.
- Moving and renaming are free; deleting (even to the trash) needs Aurélien.

## Notion links
| Notion | Drive |
|---|---|
| Projects row `Drive folder`: Run club (Harbat NY), Sport data pipeline, Finance, Camp de Base | their folders |
| 🧭 Expeditions card, « Where things live » | 30_Expeditions and the One Life folders of past expeditions |
| South Pole, Greenland Kite, NWP, Nansen Greenland Crossing, Great Slave Lake pages | link on the first line |
| 🗂️ Admin & Finance card; Taxes, Investments, 🏠 Real Estate, Healthcare, US Visas pages | link on the first line |

## Folder ids
| Folder | Id |
|---|---|
| 00_Inbox | `1n5R4GTtQ7Zm_2ghuo71XLiCsltxpm4P5` |
| 10_Admin | `1LXxduXucEzNjkAnbPtIdHvpLVZwiMRia` |
| 10_Admin/ID | `1Lah2_TSTZ-rAc9KMNKBw9kC-zWbNzYxX` |
| 10_Admin/Visas | `1zujBt4nHT_WvSnT4zXVJdfcLVpmFL5qn` |
| 10_Admin/Health & Insurance | `1LYgkp6CiESZ4FbCD1f5FyRZOlDfWJKCl` |
| 10_Admin/Housing | `1_owRrv1DnfXmTaL0oH1Jn0kQQKhLRSPq` |
| 20_Finance | `1L_q5BYjEYx-lVZoTMP76hup1cN2aS4Rd` |
| 20_Finance/Banks | `1zGWC7OOeAPL8vtLSnSiEHnng6dVsLexh` |
| 20_Finance/Income | `1w04bK0C-fzIhwF1JdEjv0Tpx1jiqqKAn` |
| 20_Finance/Taxes | `1LY8JQKnPiB_0D9PMDY26Cf0tFfnMA2xi` |
| 20_Finance/Investments | `1eLuOVSHYLHu3nE9N2bfevDROYQU_TLJH` |
| 20_Finance/Real Estate | `1HDPqh2pfpoDRF8TU5RlEf-pgYlOdxxk7` |
| 20_Finance/Real Estate/Marseille | `1AhV9rb_afXdSu8k_ZtjorpaJTqXcmuLk` |
| 20_Finance/Real Estate/Avignon | `1YAeahefKsVk8KUrjJZgD79RN5gVIaZ00` |
| 20_Finance/Advisers | `1uFY-LK0ov6E_8LJd4g89VGNCeRwLRa1J` |
| 20_Finance/Receipts | `1nFsJl53k1rAWUEUigpetJNFNreV85WdB` |
| 30_Expeditions | `1OXiI7lxtI1B2U0RwwTBrIOaCACo8C25L` |
| 30_Expeditions/South Pole 2027 | `1oNkHP0AGpEKFioEgAes7n2pNCg8ufL3t` |
| 30_Expeditions/Greenland Kite 2027 | `14YKU8-OWxD9Z3F_fV2dNkbdWk4geS0N2` |
| 30_Expeditions/Planet Heritage Project | `1O1vBlHY4JiVE7eGnPvciSAozjs9XhyqP` |
| 30_Expeditions/Ideas | `1W90VsdicEoaUh-YgCGawMVMl6zTQ7PMD` |
| 30_Expeditions/_Common | `1yZexPdUpETlu6RRS-6XG_1oKG6L82Xmc` |
| 40_Projects | `15_BPbVpOxCPodFzXZa9rVLC7Yi14j5Tj` |
| 40_Projects/Harbat (shared) | `1xbDH3ShB8u9LyNkZKBXjjVSBloYMVLg1` |
| 40_Projects/Sport data | `1de-_Zel-62hwwtTP67uSUy3mTnvmtSSS` |
| 40_Projects/Travel | `1o6qMKMa-1DLUDAocHCiOfce-rH91yGhC` |
| 50_Content | `1KVXirMj8N8YrVt_7CtFOQekkIi1XW4EI` |
| 60_Library | `12w5Pdwz_H0-R13nilvr15SgbbsfxzZEt` |
| 70_Work & Career | `1u8bcrJh2u9nKSJwxfCy-UpT_KN1oCAnU` |
| 70_Work & Career/UnifyApps | `1IvkKPIcO8xSpNmGA7_2J4OcGZqSiFhTg` |
| 80_Backups | `1HyC16jJ2lfM7wXWhjIWx5y4hESVTaH31` |
| 99_Archive | `1o6mVvFjtSAo3oeo4YSE6P0KaWsR54smB` |
| One Life | `1KQ2yTx-lMEvlulatcmVtSAIcR900kQdY` |
