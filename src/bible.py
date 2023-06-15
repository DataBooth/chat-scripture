from functools import cache

from meaningless import WebExtractor as biblegateway

# list of all the books in the Bible
# https://www.kaggle.com/oswinrh/bible

BIBLE_OT_BOOKS = [
    "Genesis",
    "Exodus",
    "Leviticus",
    "Numbers",
    "Deuteronomy",
    "Joshua",
    "Judges",
    "Ruth",
    "1 Samuel",
    "2 Samuel",
    "1 Kings",
    "2 Kings",
    "1 Chronicles",
    "2 Chronicles",
    "Ezra",
    "Nehemiah",
    "Esther",
    "Job",
    "Psalms",
    "Proverbs",
    "Ecclesiastes",
    "Song of Solomon",
    "Isaiah",
    "Jeremiah",
    "Lamentations",
    "Ezekiel",
    "Daniel",
    "Hosea",
    "Joel",
    "Amos",
    "Obadiah",
    "Jonah",
    "Micah",
    "Nahum",
    "Habakkuk",
    "Zephaniah",
    "Haggai",
    "Zechariah",
    "Malachi",
]

BIBLE_NT_BOOKS = [
    "Matthew",
    "Mark",
    "Luke",
    "John",
    "Acts",
    "Romans",
    "1 Corinthians",
    "2 Corinthians",
    "Galatians",
    "Ephesians",
    "Philippians",
    "Colossians",
    "1 Thessalonians",
    "2 Thessalonians",
    "1 Timothy",
    "2 Timothy",
    "Titus",
    "Philemon",
    "Hebrews",
    "James",
    "1 Peter",
    "2 Peter",
    "1 John",
    "2 John",
    "3 John",
    "Jude",
    "Revelation",
]


@cache
def get_text_for_book(book_name=None, bible_version=None):
    if bible_version is None:
        bible_version = "ESV"
    if book_name not in BIBLE_OT_BOOKS + BIBLE_NT_BOOKS:
        raise ValueError(f"book_name must be one of {BIBLE_OT_BOOKS + BIBLE_NT_BOOKS}")
    bible = biblegateway(translation=bible_version)
    return bible.get_book(book_name) if book_name is not None else None


@cache
def lookup_bible_passage(
    book,
    chapter1,
    verse1,
    chapter2,
    verse2,
    BIBLE_VERSION,
):
    bible = biblegateway(translation=BIBLE_VERSION)
    return bible.get_passage_range(book, chapter1, verse1, chapter2, verse2)
