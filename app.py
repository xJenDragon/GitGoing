import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="GitGoing Contributors", layout="wide")
st.title("GitGoing Workshop Profiles 🚀")

contributors_folder = Path("contributors")

if not contributors_folder.exists():
    st.warning("No contributors folder found!")
else:
    json_files = list(contributors_folder.glob("*.json"))

    for file in json_files:
        try:
            data = json.load(open(file))

            # Create a box per person
            with st.container():
                st.markdown("---")  # separator line

                cols = st.columns([1, 12])

                # Photo
                if data.get("photo_url"):
                    cols[0].image(data["photo_url"], width=120)
                else:
                    cols[0].empty()

                # Personal info
                info = f"""
                **Name:** {data.get('name', 'Unknown')}  
                **Fun Fact:** {data.get('fun_fact', '')}  
                **Favorite Language:** {data.get('favorite_language', '')}  
                **Hobby:** {data.get('hobby', '')}  
                """
                if data.get("personal_website"):
                    info += f"[Website]({data.get('personal_website')})  \n"
                if data.get("linkedin"):
                    info += f"[LinkedIn]({data.get('linkedin')})"

                cols[1].markdown(info)

        except Exception as e:
            st.error(f"Error reading {file.name}: {e}")
