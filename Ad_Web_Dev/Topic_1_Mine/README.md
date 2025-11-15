# Topic_1_Mine — Workspace Summary

This repository contains several small Django projects, example data, and a PostgreSQL data directory snapshot used for learning and development exercises.

Overview
- **`peer_graded_assign_wk2/`**: Week 2 peer-graded assignment materials. Contains `requirements.txt` and a Django project in `practice/` (includes `manage.py`, `db.sqlite3`, the `page` app, and project settings in `practice/settings.py`).
- **`tmp_db/`**: A full PostgreSQL data directory (cluster files under `base/`, `global/`, `pg_wal/`, etc.). This is a binary Postgres data store snapshot — do not edit or attempting to run it directly without restoring or proper Postgres tools. It is large and intended for offline/local database experiments only.
- **`topic1/`**: Multiple lightweight Django examples:
  - `lightweightsite/singleFileDjangoApp.py`: single-file Django example for quick demos.
  - `simplesite/`: a small Django app structure (models, views, admin, tests).
  - `simplesite_mine/`: another example with `manage.py` and `db.sqlite3`.
- **`topic2/`** and **`topic3/`**: Bio-related example projects (`bioweb/`) with `manage.py`, supporting package folders, scripts, and an `example_data_to_load.csv` file in each topic.
- **`topic4/`..`topic10/`**: Mostly README placeholders and learning artifacts.
- **`.gitignore`**: Standard ignore rules for the workspace.

Databases
- Several folders contain SQLite DB files (e.g. `db.sqlite3` in some project folders) for quick local testing.
- `tmp_db/` contains a PostgreSQL cluster snapshot. Treat it as large binary data — do not commit changes back to git if it was re-generated locally.

How to run the Django examples (typical)
1. Create and activate a virtual environment:

```bash
cd path/to/<project_folder>
python3 -m venv .venv
source .venv/bin/activate
pip install -r ../peer_graded_assign_wk2/requirements.txt  # if present
```

2. Run the development server from the Django project directory with `manage.py`:

```bash
python manage.py migrate
python manage.py runserver
```

Notes & recommendations
- If you need to conserve disk space or prepare a clean repo for sharing, consider removing or archiving `tmp_db/` outside the repository; it contains raw Postgres files and is typically too large for source control.
- Many example projects include `db.sqlite3` for convenience; delete or reset those if you want a clean state before running migrations.
- Inspect `singleFileDjangoApp.py` for a minimal, self-contained Django demo if you want a quick local test without full project setup.

If you want, I can:
- run a quick smoke test for one of the Django projects,
- remove/ignore `tmp_db/` to reduce repo size, or
- generate per-project READMEs with run/setup instructions.

File summary (top-level)
- `peer_graded_assign_wk2/` - Django assignment materials and practice project
- `tmp_db/` - PostgreSQL data directory snapshot (large)
- `topic1/` - assorted Django examples and a single-file app
- `topic2/`, `topic3/` - bioweb example projects and example CSV data
- `topic4/`..`topic10/` - README files / placeholders

-- End of summary
