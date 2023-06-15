from pathlib import Path

try:
    import tomllib  # works if using Python 3.11+
except ModuleNotFoundError:
    import tomli as tomllib  # else use tomli package (needs pip install tomli)


from streamlit import cache_data, markdown

APP_CONFIG = "./src/app_config.toml"


def read_markdown_file(markdown_file):
    if Path(markdown_file).exists():
        return Path(markdown_file).read_text()
    else:
        raise FileNotFoundError


@cache_data
def read_render_markdown_file(markdown_file):
    try:
        md_text = read_markdown_file(markdown_file)
        markdown(md_text, unsafe_allow_html=True)
    except Exception:
        print(f"Error with markdown file: {markdown_file}")
        return None


@cache_data
def read_app_config(toml_file=APP_CONFIG):
    if Path(toml_file).exists():
        with open(toml_file, "rb") as f:
            return tomllib.load(f)
    else:
        raise FileNotFoundError
