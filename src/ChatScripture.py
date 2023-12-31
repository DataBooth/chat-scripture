import streamlit as st

from st_helper import read_app_config, read_render_markdown_file

from chatdocs.chains import get_retrieval_qa


# from st_sidebar import create_sidebar
# from data_source import load_data


APP_TITLE = "Chat Scripture"
SUB_TITLE = "Asking questions of scripture using chatdocs"
APP_ICON = "💿"
APP_LAYOUT = "wide"
APP_SIDEBAR_INITIAL = "expanded"
APP_MENU = {
    "Get Help": "https://www.databooth.com.au/help",
    "Report a bug": "https://www.databooth.com.au/bug",
    "About": "Created with love & care at DataBooth - www.databooth.com.au",
}

# Note this must be the first function call in the Streamlit app code

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout=APP_LAYOUT,
    initial_sidebar_state=APP_SIDEBAR_INITIAL,
    menu_items=APP_MENU,
)


def create_app_header(app_title, subtitle=None):
    st.header(app_title)
    if subtitle is not None:
        st.subheader(subtitle)
    return None


# Read in the app config file if needed
# app_config = read_app_config()

# Get data
# df = load_data()

# Create UI

create_app_header(APP_TITLE, SUB_TITLE)
read_render_markdown_file("docs/app_main.md")

# create_sidebar()

query_text = st.text_input(label="Enter your query here:")


def run_query_chatdocs(query_text, config):
    qa = get_retrieval_qa(config, callback=None)
    res = qa(query_text)
    return res["result"] if config["llm"] != "ctransformers" else None
