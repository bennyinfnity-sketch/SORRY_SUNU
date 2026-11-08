import streamlit as st
import base64
import os

# 1. Page Settings
st.set_page_config(
    page_title="Forgive Me, Sunu! 🪔❤️", 
    page_icon="🥺", 
    layout="centered"
)

# Helper function to load local assets safely as background / hidden streams
def get_base64_of_local_file(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

# Convert your image file into a working background string layer
local_image_name = "DIWALI.JPG.jpg"
img_base64 = get_base64_of_local_file(local_image_name)

# Initialize a custom session state to check if she lit the diyas
if 'diyas_lit' not in st.session_state:
    st.session_state.diyas_lit = False

# 2. HTML/CSS Injections for Your Local Image Background
if img_base64:
    st.markdown(
        f"""
        <style>
        /* Forces your local image to stretch flawlessly across the entire website viewport canvas */
        .stApp {{
            background-image: linear-gradient(rgba(15, 12, 38, 0.45), rgba(15, 12, 38, 0.6)), url("data:image/jpg;base64,{img_base64}");
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: #ffffff;
        }}
        
        h1 {{
            color: #ffcc00 !important;
            text-align: center;
            text-shadow: 0px 0px 20px #ff5e00, 0px 0px 5px #ffffff;
            font-family: 'Georgia', serif;
            font-size: 42px !important;
        }}
        .diwali-subtitle {{
            text-align: center;
            font-size: 21px;
            color: #ffa500;
            text-shadow: 0px 0px 10px #000000;
            margin-bottom: 25px;
            font-weight: bold;
        }}
        .sorry-card {{
            background-color: rgba(15, 12, 38, 0.88); /* Protective shield box so message reads cleanly on top of the image */
            padding: 30px;
            border-radius: 20px;
            border: 2px solid #ffcc00;
            box-shadow: 0px 0px 25px rgba(255, 204, 0, 0.4);
            text-align: center;
            font-size: 19px;
            margin-top: 20px;
            line-height: 1.6;
        }}
        
        /* Custom button styling */
        .stButton>button {{
            background-color: #ff9933 !important;
            color: white !important;
            border-radius: 10px;
            border: none;
            font-weight: bold;
            font-size: 16px;
            padding: 10px 20px;
            box-shadow: 0px 0px 10px #ff9933;
            width: 100%;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    # Safe backup theme styling in case the filename doesn't match up instantly
    st.markdown("<style>.stApp {background-color: #0b091a; color: white;}</style>", unsafe_allow_html=True)

# 3. Web Layout Elements
st.markdown("<h1>Forgive Your Boy, Sunu? 🥺❤️</h1>", unsafe_allow_html=True)
st.markdown("<p class='diwali-subtitle'>✨ Lighting up this night with a million apologies just for you ✨</p>", unsafe_allow_html=True)

# 4. Center Main Character Card
col_left, col_mid, col_right = st.columns(3)
with col_mid:
    st.image("Sorry.jpg", use_container_width=True)

# 5. Heartfelt Personalized Card
st.markdown(
    """
    <div class='sorry-card'>
        "Oye Bangaram..., I am so incredibly sorry for ruining our mood. 
        Look outside—the entire night sky is shimmering with beautiful lights, 
        but none of them shine as bright as your smile. 
        I don't want a single cloud between us on this festive night. 
        Please forgive your boy, wipe away the fight, and let's celebrate Diwali together? ❤️"
    </div>
    """, 
    unsafe_allow_html=True
)

# 6. Interactive Festive States
st.markdown("<br>", unsafe_allow_html=True)

# Feature A: Lighting virtual candles/diyas for her
if not st.session_state.diyas_lit:
    if st.button("✨Idhi okasari click cheyyii ala chusi velipokuu..✨"):
        st.session_state.diyas_lit = True
        st.rerun()
else:
    st.markdown("<h3 style='text-align: center; color: #ffcc00;'>❤️ 🤌ILA NAVUTHU UNDAVEYY.. CHUSTHU BATHAKESTHAA.. PLCHH EYYY🤌 🥺</h3>", unsafe_allow_html=True)

# Feature B: HIDDEN & LOOPING Embedded Romantic BGM Track 🎵🔄
audio_base64 = get_base64_of_local_file("bgm.mp3.mp3")
if audio_base64:
    st.markdown(
        f"""
        <div style="display:none;">
            <audio autoplay loop>
                <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
            </audio>
        </div>
        """,
        unsafe_allow_html=True
    )

# 7. Main Interactive Forgiveness Action
c1, c2, c3 = st.columns(3)
with c2:
    if st.button("✨ Click to Forgive & Light Up the Sky ✨"):
        st.balloons()  
        st.snow()      
        st.success("🎉 THANKS FOR ACCEPTING MY SORRY, Sunu !Te quiero mucho 🫶🏻 😘💖")
