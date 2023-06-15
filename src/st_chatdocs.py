import chatdocs
import re
import rich
from datetime import datetime
from pathlib import Path
from sh import rm, chatdocs


def remove_ansi_escape(text_str):
    # See: https://stackoverflow.com/questions/14693701/how-can-i-remove-the-ansi-escape-sequences-from-a-string-in-python
    ansi_escape = re.compile(r"(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]")
    return ansi_escape.sub("", text_str)


def clear_local_chatdocs_db():
    if Path("./db").exists():
        rm("-rf", "./db")
        print(f"Deleted local chatdocs database: {Path('./db').resolve()}")
    else:
        print(f"Skipped: Local chatdocs database not found: {Path('./db').resolve()}")
    return None


DOCUMENT_DIR = Path.cwd() / "data" / "text" / "NIV"


def initialise_chatdocs():
    try:
        output_init = chatdocs("download")
        print("OK: chatdocs components downloaded")
        return output_init
    except Exception as e:
        print("ERROR: Unable to download chatdocs components")
        return None


def add_documents_to_chatdocs(document_dir=DOCUMENT_DIR):
    if not document_dir.exists():
        return None
    try:
        output_add = chatdocs("add", document_dir)
        print(f"OK: Added documents from {document_dir.resolve()}")
        return output_add
    except Exception as e:
        print(f"ERROR: Unable to add documents from {document_dir.resolve()}")
        return None


def query_chatdocs(query_text, add_documents=True, document_dir=DOCUMENT_DIR):
    start_time = datetime.now()
    if add_documents:
        clear_local_chatdocs_db()
        output_add = chatdocs("add", document_dir)
    output_chat = chatdocs("chat", query_text)
    output_chat = remove_ansi_escape(output_chat)
    for line in output_chat.split("A:"):
        rich.print(line.splitlines())
    return (datetime.now() - start_time).seconds
