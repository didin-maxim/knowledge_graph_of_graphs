import sqlite3
from pathlib import Path

from lib import ROOT, collect_text, load_definitions, load_import_batches, load_problems, load_relations, load_standard_ideas


def main():
    index_dir = ROOT / "index"
    index_dir.mkdir(exist_ok=True)
    db_path = index_dir / "generated.sqlite"
    if db_path.exists():
        db_path.unlink()

    con = sqlite3.connect(db_path)
    con.execute("create table problems(id text primary key, title text, path text, text text)")
    con.execute("create virtual table problem_fts using fts5(id, title, text)")
    con.execute("create table definitions(id text primary key, title text, text text)")
    con.execute("create virtual table definition_fts using fts5(id, title, text)")
    con.execute("create table standard_ideas(id text primary key, title text, text text)")
    con.execute("create virtual table standard_idea_fts using fts5(id, title, text)")
    con.execute("create table relations(id text primary key, source text, target text, type text, distance int, status text, text text)")
    con.execute("create table import_batches(id text primary key, title text, status text, text text)")

    problems = load_problems()
    for problem in problems.values():
        text = collect_text(problem)
        con.execute("insert into problems values(?, ?, ?, ?)", (problem["id"], problem["title"], problem["_path"], text))
        con.execute("insert into problem_fts values(?, ?, ?)", (problem["id"], problem["title"], text))

    for relation in load_relations():
        text = relation["forward_text"] + "\n" + relation["backward_text"]
        con.execute(
            "insert into relations values(?, ?, ?, ?, ?, ?, ?)",
            (relation["id"], relation["from"], relation["to"], relation["type"], relation["distance"], relation["status"], text),
        )

    for definition in load_definitions().values():
        text = collect_text(definition)
        con.execute("insert into definitions values(?, ?, ?)", (definition["id"], definition["title"], text))
        con.execute("insert into definition_fts values(?, ?, ?)", (definition["id"], definition["title"], text))

    for idea in load_standard_ideas().values():
        text = collect_text(idea)
        con.execute("insert into standard_ideas values(?, ?, ?)", (idea["id"], idea["title"], text))
        con.execute("insert into standard_idea_fts values(?, ?, ?)", (idea["id"], idea["title"], text))

    for batch in load_import_batches():
        text = collect_text(batch)
        con.execute("insert into import_batches values(?, ?, ?, ?)", (batch["id"], batch["title"], batch.get("status", ""), text))

    con.commit()
    con.close()
    print(f"Built {db_path}")


if __name__ == "__main__":
    main()
