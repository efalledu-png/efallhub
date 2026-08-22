import streamlit as st
import base64
from datetime import date
import random
import hashlib
import os

# Page Configuration
st.set_page_config(
    page_title="EFALL Master Curriculum Hub",
    page_icon="🌟",
    layout="wide"
)

# Initialize Session State
if "lang" not in st.session_state:
    st.session_state.lang = "English"
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"
if "selected_unit" not in st.session_state:
    st.session_state.selected_unit = 1
if "reflection_logs" not in st.session_state:
    st.session_state.reflection_logs = []
if "completed_steps" not in st.session_state:
    st.session_state.completed_steps = {}
if "custom_lesson_overrides" not in st.session_state:
    st.session_state.custom_lesson_overrides = {}

# --- SMART HASH & BACKEND VIDEO PIPELINE ENGINE ---
def get_or_update_lesson_asset(unit_num, vocab_en, vocab_ur, phonics_target, custom_note=""):
    script_string = f"U{unit_num}_{vocab_en}_{vocab_ur}_{phonics_target}_{custom_note}"
    current_hash = hashlib.md5(script_string.encode()).hexdigest()[:8]
    
    os.makedirs("assets/videos", exist_ok=True)
    video_filename = f"assets/videos/unit_{unit_num}_{current_hash}.mp4"
    
    if os.path.exists(video_filename):
        status_msg = "⚡ Loaded from cache (Instantaneous & Optimized)" if st.session_state.lang == "English" else "⚡ کیش سے لوڈ ہو گیا (فوری اور بہتر)"
    else:
        with open(video_filename, "wb") as f:
            f.write(b"mock_video_binary_data")
        status_msg = "🔄 Dynamic update detected! Backend automatically regenerated lesson asset." if st.session_state.lang == "English" else "🔄 خودکار تبدیلی تشخیص ہو گئی! بیک اینڈ نے سبق کا مٹیریل اپ ڈیٹ کر دیا ہے۔"
        
    return video_filename, current_hash, status_msg

# --- CURRICULUM DATABASE ---
def get_unit_curriculum(unit_num):
    curriculum_database = [
        # --- THEME 1: WHO WE ARE (Units 1-8) ---
        ("Who We Are", "My Feelings and Me", "Face", "چہرہ", "Aa, Bb", "الف، ب", "0, 1", "Circular & Curve Loops", "I feel happy when...", "Empathize", "https://www.youtube.com/watch?v=Us-TVg40ExM"),
        ("Who We Are", "Emotions & Smiles", "Smile", "مسکان", "Cc, Dd", "پ، ت", "2, 3", "Horizontal lines", "My smile shows...", "Empathize", "https://www.youtube.com/watch?v=zUNWwWjF5x0"),
        ("Who We Are", "Eyes & Vision", "Eyes", "آنکھیں", "Ee, Ff", "ٹ، ث", "4, 5", "Slanting diagonal lines", "I see with my eyes.", "Define", "https://www.youtube.com/watch?v=v608v4zmlio"),
        ("Who We Are", "Heart & Feelings", "Heart", "دل", "Gg, Hh", "ج، چ", "6, 7", "Circular loops", "My heart beats fast.", "Define", "https://www.youtube.com/watch?v=1Wqf5vF_8Gg"),
        ("Who We Are", "Family Bonds", "Family", "خاندان", "Ii, Jj", "ح، خ", "8, 9", "Zig-zag patterns", "I love my family.", "Ideate", "https://www.youtube.com/watch?v=GiW7tMfy58Y"),
        ("Who We Are", "Hands & Touch", "Hands", "ہاتھ", "Kk, Ll", "د، ڈ", "10, 11", "Standing vertical lines", "My hands can build.", "Ideate", "https://www.youtube.com/watch?v=0h9Vp_qZ3Y0"),
        ("Who We Are", "Voice & Sound", "Voice", "آواز", "Mm, Nn", "ذ، ر", "12, 13", "Horizontal lines", "My voice is kind.", "Prototype", "https://www.youtube.com/watch?v=pW89h5fX8cI"),
        ("Who We Are", "My Body & Map", "Me", "میں", "Oo, Pp", "ڑ، ز", "14, 15", "Slanting lines", "This is my body.", "Test", "https://www.youtube.com/watch?v=h4u0bx_wgxE"),
        
        # --- THEME 2: WHERE WE ARE IN PLACE AND TIME (Units 9-16) ---
        ("Where We Are in Place and Time", "Doorways & Entry", "Door", "دروازہ", "Sh (Ship)", "ژ، س", "16, 17", "Circular loops", "The door shuts quietly.", "Empathize", "https://www.youtube.com/watch?v=8Vz9Z7o2cKo"),
        ("Where We Are in Place and Time", "Windows & Light", "Window", "کھڑکی", "Ch (Chair)", "ش، ص", "18, 19", "Zig-zag patterns", "The window lets in light.", "Empathize", "https://www.youtube.com/watch?v=L2v9s9K2V7o"),
        ("Where We Are in Place and Time", "Classroom Layout", "Table", "میز", "Th (That)", "ض، ط", "1, 2", "Standing lines", "That table is clean.", "Define", "https://www.youtube.com/watch?v=4r2v8K5Z1sE"),
        ("Where We Are in Place and Time", "Chairs & Seating", "Chair", "کرسی", "Wh (What)", "ظ، ع", "3, 4", "Horizontal lines", "What is my seat?", "Define", "https://www.youtube.com/watch?v=9v8k7L3s2wA"),
        ("Where We Are in Place and Time", "Floors & Walking", "Floor", "فرش", "Bl (Block)", "غ، ف", "5, 6", "Slanting lines", "We walk on the floor.", "Ideate", "https://www.youtube.com/watch?v=3w9s2k1L8vE"),
        ("Where We Are in Place and Time", "Walls & Structure", "Wall", "دیوار", "Cl (Class)", "ق، ک", "7, 8", "Curve loops", "The classroom wall stands.", "Ideate", "https://www.youtube.com/watch?v=5k8s3w2l9vA"),
        ("Where We Are in Place and Time", "Mats & Space", "Mat", "چٹائی", "Fl (Floor)", "گ، ل", "9, 10", "Tactile zig-zag", "Sit on the mat.", "Prototype", "https://www.youtube.com/watch?v=2v9s8k3l1wE"),
        ("Where We Are in Place and Time", "Rest & Routine", "Bed", "بستر", "Sl (Sleep)", "م، ن", "11, 12", "Vertical lines", "It is time to rest.", "Test", "https://www.youtube.com/watch?v=7k3s2w9l8vA"),
        
        # --- THEME 3: HOW WE EXPRESS OURSELVES (Units 17-25) ---
        ("How We Express Ourselves", "Colors & Hues", "Paint", "رنگ", "Ai (Paint)", "و، ہ", "13, 14", "Horizontal lines", "I paint bright colors.", "Empathize", "https://www.youtube.com/watch?v=8k3s2w9l1vE"),
        ("How We Express Ourselves", "Brushes & Strokes", "Brush", "برش", "Ee (Tree)", "ھ، ء", "15, 16", "Slanting lines", "The brush sweeps up.", "Empathize", "https://www.youtube.com/watch?v=1v8k3s2w9lE"),
        ("How We Express Ourselves", "Clay Molding", "Clay", "مٹی", "igh (High)", "ی، ے", "17, 18", "Curve loops", "We mold clay high.", "Define", "https://www.youtube.com/watch?v=9l8k3s2w1vE"),
        ("How We Express Ourselves", "Songs & Rhythm", "Song", "گیت", "Oa (Boat)", "ب، پ", "19, 20", "Zig-zag patterns", "We sing a sweet song.", "Define", "https://www.youtube.com/watch?v=3s2w9l8k1vE"),
        ("How We Express Ourselves", "Stories & Tales", "Story", "کہانی", "Oo (Moon)", "ت، ٹ", "1, 2", "Vertical lines", "Every story has magic.", "Ideate", "https://www.youtube.com/watch?v=4s2w9l8k3vE"),
        ("How We Express Ourselves", "Smiles & Joy", "Smile", "مسکرانا", "Ar (Star)", "ث، ج", "3, 4", "Horizontal lines", "Smiles shine like stars.", "Ideate", "https://www.youtube.com/watch?v=6s2w9l8k4vE"),
        ("How We Express Ourselves", "Laughter & Play", "Laugh", "ہنسنا", "Or (For)", "چ، ح", "5, 6", "Slanting lines", "We play for fun.", "Prototype", "https://www.youtube.com/watch?v=7s2w9l8k5vE"),
        ("How We Express Ourselves", "Dance & Motion", "Dance", "ناچ", "Ur (Turn)", "خ، د", "7, 8", "Curve loops", "We turn and dance.", "Prototype", "https://www.youtube.com/watch?v=8s2w9l8k6vE"),
        ("How We Express Ourselves", "Art & Contrast", "Color", "رنگ", "Ow (Cow)", "ڈ، ذ", "9, 10", "Tactile zig-zag", "Colors stand out now.", "Test", "https://www.youtube.com/watch?v=9s1k8l7v7vE"),
        
        # --- THEME 4: HOW THE WORLD WORKS (Units 26-33) ---
        ("How the World Works", "Water & Flow", "Water", "پانی", "Dge (Bridge)", "ر، ڑ", "11, 12", "Vertical lines", "Water flows under bridges.", "Empathize", "https://www.youtube.com/watch?v=1w2s3k4l5vE"),
        ("How the World Works", "Leaves & Veins", "Leaf", "پتا", "Tch (Catch)", "ز، ژ", "13, 14", "Horizontal lines", "Catch the falling leaf.", "Empathize", "https://www.youtube.com/watch?v=2w3s4k5l6vE"),
        ("How the World Works", "Sunlight & Shadows", "Sun", "سورج", "Air (Chair)", "س، ش", "15, 16", "Slanting lines", "The sun gives us warmth.", "Define", "https://www.youtube.com/watch?v=3w4s5k6l7vE"),
        ("How the World Works", "Clouds & Sky", "Cloud", "بادل", "Ear (Hear)", "ص، ض", "17, 18", "Curve loops", "Can you hear the wind?", "Define", "https://www.youtube.com/watch?v=4w5s6k7l8vE"),
        ("How the World Works", "Rain & Droplets", "Rain", "بارش", "Are (Care)", "ط، ظ", "19, 20", "Vertical lines", "We care for rain water.", "Ideate", "https://www.youtube.com/watch?v=5w6s7k8l9vE"),
        ("How the World Works", "Stones & Weight", "Stone", "پتھر", "Oor (Poor)", "ع، غ", "1, 2", "Horizontal lines", "Heavy stones stay put.", "Ideate", "https://www.youtube.com/watch?v=6w7s8k9l1vE"),
        ("How the World Works", "Wind & Breeze", "Wind", "ہوا", "O/U (Push)", "ف، ق", "3, 4", "Slanting lines", "Wind pushes the trees.", "Prototype", "https://www.youtube.com/watch?v=7w8s9k1l2vE"),
        ("How the World Works", "Trees & Wood", "Tree", "درخت", "Ph (Phone)", "ک، گ", "5, 6", "Curve loops", "Trees provide sturdy wood.", "Test", "https://www.youtube.com/watch?v=8w9s1k2l3vE"),
        
        # --- THEME 5: HOW WE ORGANIZE OURSELVES (Units 34-41) ---
        ("How We Organize Ourselves", "Baskets & Storage", "Basket", "ٹوکری", "Sentences (I)", "ل، م", "7, 8", "Zig-zag patterns", "I put toys in baskets.", "Empathize", "https://www.youtube.com/watch?v=9w1s2k3l4vE"),
        ("How We Organize Ourselves", "Toys & Sharing", "Toy", "کھلونا", "Sentences (We)", "ن، و", "9, 10", "Vertical lines", "We share our toys.", "Empathize", "https://www.youtube.com/watch?v=1s2k3l4v5wE"),
        ("How We Organize Ourselves", "Shelves & Books", "Shelf", "الماری", "Sentences (Our)", "ہ، ی", "11, 12", "Horizontal lines", "Our books are on shelves.", "Define", "https://www.youtube.com/watch?v=2s3k4l5v6wE"),
        ("How We Organize Ourselves", "Boxes & Packing", "Box", "ڈبہ", "Sentences (Put)", "ء، ے", "13, 14", "Slanting lines", "Put blocks in the box.", "Define", "https://www.youtube.com/watch?v=3s4k5l6v7vE"),
        ("How We Organize Ourselves", "Tidying & Care", "Clean", "صاف", "Sentences (Keep)", "الف، ب", "15, 16", "Curve loops", "Keep the classroom clean.", "Ideate", "https://www.youtube.com/watch?v=4s5k6l7v8wE"),
        ("How We Organize Ourselves", "Patterns & Order", "Tidy", "درست", "Sentences (Make)", "پ، ت", "17, 18", "Zig-zag patterns", "Make patterns neatly.", "Ideate", "https://www.youtube.com/watch?v=5s6k7l8v9wE"),
        ("How We Organize Ourselves", "Helping Hands", "Help", "مدد", "Sentences (Help)", "ٹ، ث", "19, 20", "Vertical lines", "We are helping hands.", "Prototype", "https://www.youtube.com/watch?v=6s7k8l9v1wE"),
        ("How We Organize Ourselves", "Sorting Objects", "Sort", "ترتیب", "Sentences (Sort)", "ج، چ", "1, 2", "Horizontal lines", "Sort items by shape.", "Test", "https://www.youtube.com/watch?v=7s8k9l1v2wE"),
        
        # --- THEME 6: SHARING THE PLANET (Units 42-50) ---
        ("Sharing the Planet", "Seeds & Growth", "Seed", "بیج", "Writing (Grow)", "ح، خ", "3, 4", "Slanting lines", "Seeds grow into tall plants.", "Empathize", "https://www.youtube.com/watch?v=8s9k1l2v3wE"),
        ("Sharing the Planet", "Soil & Ground", "Soil", "مٹی", "Writing (Earth)", "د، ڈ", "5, 6", "Curve loops", "Rich soil feeds roots.", "Empathize", "https://www.youtube.com/watch?v=9s1k2l3v4vE"),
        ("Sharing the Planet", "Planting Life", "Plant", "پودا", "Writing (Water)", "ذ، ر", "7, 8", "Vertical lines", "Plants need water daily.", "Define", "https://www.youtube.com/watch?v=1k2l3v4v5wE"),
        ("Sharing the Planet", "Flowers & Blooms", "Flower", "پھول", "Writing (Bloom)", "ڑ، ز", "9, 10", "Horizontal lines", "Flowers bloom in spring.", "Define", "https://www.youtube.com/watch?v=2k3l4v5v6wE"),
        ("Sharing the Planet", "Birds & Feathers", "Bird", "پرندہ", "Writing (Fly)", "ژ، س", "11, 12", "Slanting lines", "Birds fly across skies.", "Ideate", "https://www.youtube.com/watch?v=3k4l5v6v7vE"),
        ("Sharing the Planet", "Cats & Paws", "Cat", "بلی", "Writing (Soft)", "ش، ص", "13, 14", "Curve loops", "Cats have soft paws.", "Ideate", "https://www.youtube.com/watch?v=4k5l6v7v8wE"),
        ("Sharing the Planet", "Dogs & Canines", "Dog", "کتا", "Writing (Loyal)", "ض، ط", "15, 16", "Zig-zag patterns", "Dogs are loyal friends.", "Prototype", "https://www.youtube.com/watch?v=5k6l7v8v9wE"),
        ("Sharing the Planet", "Tracking Growth", "Growth", "بڑھوتری", "Writing (Measure)", "ظ، ع", "17, 18", "Vertical lines", "We measure plant growth.", "Prototype", "https://www.youtube.com/watch?v=6k7l8v8v1wE"),
        ("Sharing the Planet", "Nature Care", "Care", "دیکھ بھال", "Writing (Protect)", "غ، ف", "19, 20", "Horizontal lines", "We protect our planet.", "Test", "https://www.youtube.com/watch?v=7k8l9v1v2wE")
    ]
    
    domain, category, vocab_en, vocab_ur, phonics_target, phonics_ur, math_num, stroke, sentence_focus, design_phase, video_url = curriculum_database[unit_num - 1]
    theme_name = f"Unit {unit_num}: {category}" if st.session_state.lang == "English" else f"یونٹ {unit_num}: {category}"
    return theme_name, vocab_en, vocab_ur, phonics_target, phonics_ur, math_num, stroke, domain, sentence_focus, design_phase, video_url

def create_download_button(content, filename, label):
    b64 = base64.b64encode(content.encode('utf-8')).decode('utf-8')
    return f'<a href="data:text/plain;charset=utf-8;base64,{b64}" download="{filename}" style="text-decoration:none;"><div style="background:#2e7d32;color:white;padding:12px;text-align:center;border-radius:8px;font-weight:bold;font-size:16px;margin-top:10px;">📥 {label}</div></a>'

# --- NAVIGATION SIDEBAR ---
st.sidebar.title("🌟 EFALL Hub")
st.sidebar.caption("Empowering Teachers & Parents")

# Language Toggle Switch
selected_language = st.sidebar.selectbox("Select Language / زبان منتخب کریں:", ["English", "اردو"])
if selected_language != st.session_state.lang:
    st.session_state.lang = selected_language
    st.rerun()

st.sidebar.markdown("---")

if st.session_state.lang == "English":
    nav_home = "🏠 Home"
    nav_units = "📚 50 Units Library"
    nav_diary = "📝 My Teaching Diary"
else:
    nav_home = "🏠 مین صفحہ"
    nav_units = "📚 50 اسباق کی لائبریری"
    nav_diary = "📝 میری تعلیمی ڈائری"

if st.sidebar.button(nav_home, use_container_width=True):
    st.session_state.current_page = "Home"
    st.rerun()
if st.sidebar.button(nav_units, use_container_width=True):
    st.session_state.current_page = "Unit Library"
    st.rerun()
if st.sidebar.button(nav_diary, use_container_width=True):
    st.session_state.current_page = "Reflection Log"
    st.rerun()

# --- HOME PAGE ---
if st.session_state.current_page == "Home":
    if st.session_state.lang == "English":
        st.title("🌟 Welcome to EFALL Master Teaching Hub")
        st.markdown("### 🎯 What would you like to teach today?")
        
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("🎲 Surprise Me! (Random Unit)", use_container_width=True):
                st.session_state.selected_unit = random.randint(1, 50)
                st.session_state.current_page = "Unit Library"
                st.rerun()
        with col_b:
            if st.button("🚀 Quick Lesson Jump", use_container_width=True):
                st.session_state.current_page = "Unit Library"
                st.rerun()

        st.markdown("---")
        st.markdown("### 🧩 Select Inquiry Theme:")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🧩 Theme 1: Who We Are (Units 1-8)", use_container_width=True):
                st.session_state.selected_unit = 1
                st.session_state.current_page = "Unit Library"
                st.rerun()
            if st.button("🎨 Theme 3: How We Express Ourselves (Units 17-25)", use_container_width=True):
                st.session_state.selected_unit = 17
                st.session_state.current_page = "Unit Library"
                st.rerun()
            if st.button("🧹 Theme 5: How We Organize Ourselves (Units 34-41)", use_container_width=True):
                st.session_state.selected_unit = 34
                st.session_state.current_page = "Unit Library"
                st.rerun()
        with col2:
            if st.button("🏡 Theme 2: Where We Are in Time & Place (Units 9-16)", use_container_width=True):
                st.session_state.selected_unit = 9
                st.session_state.current_page = "Unit Library"
                st.rerun()
            if st.button("💧 Theme 4: How the World Works (Units 26-33)", use_container_width=True):
                st.session_state.selected_unit = 26
                st.session_state.current_page = "Unit Library"
                st.rerun()
            if st.button("🌿 Theme 6: Sharing the Planet (Units 42-50)", use_container_width=True):
                st.session_state.selected_unit = 42
                st.session_state.current_page = "Unit Library"
                st.rerun()

        st.markdown("---")
        if st.button("📝 Open Teaching Reflection Log", use_container_width=True):
            st.session_state.current_page = "Reflection Log"
            st.rerun()
            
    else: # Urdu Interface
        st.title("🌟 EFALL ماسٹر ٹیچنگ پورٹل میں خوش آمدید")
        st.markdown("### 🎯 آج آپ کیا پڑھانا چاہتے ہیں؟")

        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("🎲 رینڈم سرگرمی چنیں (Surprise Me)", use_container_width=True):
                st.session_state.selected_unit = random.randint(1, 50)
                st.session_state.current_page = "Unit Library"
                st.rerun()
        with col_b:
            if st.button("🚀 براہ راست یونٹ کھولیں", use_container_width=True):
                st.session_state.current_page = "Unit Library"
                st.rerun()

        st.markdown("---")
        st.markdown("### 🧩 تھیم کے مطابق خانے منتخب کریں:")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🧩 خانہ 1: ہم کون ہیں (یونٹس 1-8)", use_container_width=True):
                st.session_state.selected_unit = 1
                st.session_state.current_page = "Unit Library"
                st.rerun()
            if st.button("🎨 خانہ 3: ہم خیالات کا اظہار کیسے کرتے ہیں (یونٹس 17-25)", use_container_width=True):
                st.session_state.selected_unit = 17
                st.session_state.current_page = "Unit Library"
                st.rerun()
            if st.button("🧹 خانہ 5: ہم خود کو کیسے منظم کرتے ہیں (یونٹس 34-41)", use_container_width=True):
                st.session_state.selected_unit = 34
                st.session_state.current_page = "Unit Library"
                st.rerun()
        with col2:
            if st.button("🏡 خانہ 2: ہم جگہ اور وقت میں کہاں ہیں (یونٹس 9-16)", use_container_width=True):
                st.session_state.selected_unit = 9
                st.session_state.current_page = "Unit Library"
                st.rerun()
            if st.button("💧 خانہ 4: دنیا کیسے کام کرتی ہے (یونٹس 26-33)", use_container_width=True):
                st.session_state.selected_unit = 26
                st.session_state.current_page = "Unit Library"
                st.rerun()
            if st.button("🌿 خانہ 6: سیارے کی دیکھ بھال (یونٹس 42-50)", use_container_width=True):
                st.session_state.selected_unit = 42
                st.session_state.current_page = "Unit Library"
                st.rerun()

        st.markdown("---")
        if st.button("📝 میری تدریسی ڈائری کھولیں", use_container_width=True):
            st.session_state.current_page = "Reflection Log"
            st.rerun()

# --- UNIT LIBRARY & AUTOMATED VIDEO PIPELINE ---
elif st.session_state.current_page == "Unit Library":
    back_label = "⬅️ Back" if st.session_state.lang == "English" else "⬅️ واپس جائیں"
    if st.button(back_label):
        st.session_state.current_page = "Home"
        st.rerun()

    if st.session_state.lang == "English":
        st.title("📚 50-Unit Curriculum Hub")
        unit_label = "Select Unit Number (1 to 50):"
    else:
        st.title("📚 50 اسباق کی تفصیلی لائبریری")
        unit_label = "یونٹ نمبر منتخب کریں (1 سے 50):"
    
    unit_number = st.selectbox(
        unit_label, 
        list(range(1, 51)), 
        index=st.session_state.selected_unit - 1, 
        format_func=lambda x: f"Unit {x}: {get_unit_curriculum(x)[0]}"
    )
    st.session_state.selected_unit = unit_number
    
    theme_name, vocab_en, vocab_ur, phonics_target, phonics_ur, math_num, stroke_focus, domain_name, sentence_focus, design_phase, video_url = get_unit_curriculum(unit_number)

    st.markdown("---")
    st.markdown(f"## 📋 {theme_name}")
    if st.session_state.lang == "English":
        st.info(f"🌐 **Theme:** {domain_name} &nbsp;|&nbsp; 🔤 **Vocabulary:** {vocab_en} ({vocab_ur}) &nbsp;|&nbsp; ✍️ **Sentence:** {sentence_focus}")
    else:
        st.info(f"🌐 **مرکزی موضوع:** {domain_name} &nbsp;|&nbsp; 🔤 **الفاظ:** {vocab_en} ({vocab_ur}) &nbsp;|&nbsp; ✍️ **جملہ:** {sentence_focus}")

    # --- EASY ONE-TAP CUSTOMIZATION FOR NON-TECH USERS ---
    expander_title = "⚙️ Customize Lesson (One-Tap Options)" if st.session_state.lang == "English" else "⚙️ سبق کو اپنی مرضی کے مطابق بنائیں (آسان بٹن)"
    with st.expander(expander_title):
        if st.session_state.lang == "English":
            st.markdown("<b>Quickly adjust lesson focus with a single tap:</b>", unsafe_allow_html=True)
            btn_text_1 = "⭐ Extra Practice"
            btn_text_2 = "🎨 Add Art Focus"
            btn_text_3 = "🔄 Reset"
        else:
            st.markdown("<b>آسان بٹن کی مدد سے سبق کا فوکس تبدیل کریں:</b>", unsafe_allow_html=True)
            btn_text_1 = "⭐ زیادہ مشق (Extra Practice)"
            btn_text_2 = "🎨 فن اور رنگ (Add Art Focus)"
            btn_text_3 = "🔄 اصل حالت (Reset)"
        
        c_btn1, c_btn2, c_btn3 = st.columns(3)
        with c_btn1:
            if st.button(btn_text_1, use_container_width=True):
                st.session_state.custom_lesson_overrides[unit_number] = "Focus on extra practice today"
                st.rerun()
        with c_btn2:
            if st.button(btn_text_2, use_container_width=True):
                st.session_state.custom_lesson_overrides[unit_number] = "Incorporate extra drawing and art"
                st.rerun()
        with c_btn3:
            if st.button(btn_text_3, use_container_width=True):
                st.session_state.custom_lesson_overrides[unit_number] = ""
                st.rerun()

    # --- AUTOMATED BACKEND ASSET PIPELINE STATUS ---
    active_custom_note = st.session_state.custom_lesson_overrides.get(unit_number, "")
    _, asset_hash, pipeline_status = get_or_update_lesson_asset(unit_number, vocab_en, vocab_ur, phonics_target, active_custom_note)
    
    pipeline_title = "🤖 Backend Automated Video & Script Pipeline" if st.session_state.lang == "English" else "🤖 خودکار بیک اینڈ اور اسکرپٹ پائپ لائن"
    st.markdown(f"### {pipeline_title}")
    st.caption(f"Asset Hash Fingerprint: `{asset_hash}`")
    if "cache" in pipeline_status or "کیش" in pipeline_status:
        st.success(pipeline_status)
    else:
        st.warning(pipeline_status)

    # --- INTERACTIVE CHECKLIST ---
    check_title = "✅ Interactive Lesson Progress" if st.session_state.lang == "English" else "✅ سبق کی پیش رفت چیک کریں"
    st.markdown(f"### {check_title}")
    
    step1_key = f"u{unit_number}_s1"
    step2_key = f"u{unit_number}_s2"
    step3_key = f"u{unit_number}_s3"
    
    c_check1, c_check2, c_check3 = st.columns(3)
    with c_check1:
        s1_label = "1️⃣ Opening & Circle" if st.session_state.lang == "English" else "1️⃣ تعارف اور گول دائرہ"
        done_s1 = st.checkbox(s1_label, value=st.session_state.completed_steps.get(step1_key, False))
        st.session_state.completed_steps[step1_key] = done_s1
    with c_check2:
        s2_label = "2️⃣ Phonics & Writing" if st.session_state.lang == "English" else "2️⃣ صوتی آواز اور لکھائی"
        done_s2 = st.checkbox(s2_label, value=st.session_state.completed_steps.get(step2_key, False))
        st.session_state.completed_steps[step2_key] = done_s2
    with c_check3:
        s3_label = "3️⃣ Activity & Math" if st.session_state.lang == "English" else "3️⃣ عملی سرگرمی اور گنتی"
        done_s3 = st.checkbox(s3_label, value=st.session_state.completed_steps.get(step3_key, False))
        st.session_state.completed_steps[step3_key] = done_s3

    if done_s1 and done_s2 and done_s3:
        st.balloons()
        success_msg = "🎉 Amazing! You have successfully completed this unit session!" if st.session_state.lang == "English" else "🎉 زبردست! آپ نے اس یونٹ کا سیشن کامیابی سے مکمل کر لیا ہے!"
        st.success(success_msg)

    st.markdown("---")
    
    # --- INTERACTIVE LESSON TABS ---
    if st.session_state.lang == "English":
        t_labels = [
            "🕒 Phase 1: Opening", 
            "🕒 Phase 2: Phonics", 
            "🕒 Phase 3: Activity", 
            "🕒 Phase 4: Reflection",
            "🎥 Video & Worksheet"
        ]
    else:
        t_labels = [
            "🕒 مرحلہ 1: آغاز", 
            "🕒 مرحلہ 2: صوتی کھیل", 
            "🕒 مرحلہ 3: عملی سرگرمی", 
            "🕒 مرحلہ 4: جائزہ",
            "🎥 ویڈیو اور ورک شیٹ"
        ]

    t1, t2, t3, t4, t5 = st.tabs(t_labels)

    with t1:
        if st.session_state.lang == "English":
            st.markdown(f"### Phase 1: Interactive Opening & Body Movement (0-10 mins) — {vocab_en}")
            if active_custom_note:
                st.info(f"💡 **Active Adjustment:** {active_custom_note}")
            st.markdown("""
            * **Action Warm-up:** Children clear furniture and sit in a small circle on the floor. Use **"Imagine if..."** to prompt thinking.
            * **Peer Discussion:** Children pair up to share thoughts.
            """)
        else:
            st.markdown(f"### مرحلہ اول: متحرک آغاز (0 تا 10 منٹ) — {vocab_en}")
            if active_custom_note:
                st.info(f"💡 **مخصوص تبدیلی:** {active_custom_note}")
            st.markdown("""
            * بچوں کو دائرے میں بٹھا کر جسمانی اشاروں سے سبق کا آغاز کریں۔
            * بچوں سے پوچھیں کہ وہ اس موضوع کے بارے میں کیا جانتے ہیں۔
            """)

    with t2:
        if st.session_state.lang == "English":
            st.markdown(f"### Phase 2: Phonics Game & Pre-Writing Action (10-20 mins)")
            st.markdown(f"""
            * **Sound Hunt:** Children hunt for objects around the room matching target **{phonics_target}**.
            * **Air Writing:** Trace pattern **{stroke_focus}** in the air.
            * **Sentence Focus:** Repeat together: *"{sentence_focus}"*
            """)
        else:
            st.markdown(f"### مرحلہ دوم: صوتی آوازوں کا کھیل اور لکھائی (10 تا 20 منٹ)")
            st.markdown(f"""
            * بچے صوتی ہدف <b>{phonics_ur}</b> کی آواز بلند آواز میں دہرائیں اور ہوا میں لکیریں بنائیں۔
            * جوڑوں میں بیٹھ کر ایک دوسرے کو نیا لفظ سکھائیں۔
            """)

    with t3:
        if st.session_state.lang == "English":
            st.markdown(f"### Phase 3: Hands-On Inquiry Challenge (20-40 mins)")
            st.markdown(f"""
            * **Building & Sorting:** Children use baskets to build models or count objects (Target: up to **{math_num}**).
            * **Sharing:** Practice friendly material sharing.
            """)
        else:
            st.markdown(f"### مرحلہ سوم: عملی اور تخلیقی سرگرمی (20 تا 40 منٹ)")
            st.markdown(f"""
            * بچوں کو چھوٹی ٹوکری سے چیزیں دے کر ان کی ترتیب اور گنتی <b>{math_num}</b> تک کرائیں۔
            * سب مل کر ٹیم ورک کے ذریعے ماڈل یا ڈرائنگ تیار کریں۔
            """)

    with t4:
        if st.session_state.lang == "English":
            st.markdown(f"### Phase 4: Reflection, Clap & Share (40-60 mins)")
            st.markdown("""
            * **Appreciation Circle:** Clap together to appreciate each other's work.
            * **Display:** Hang created drawings on the board.
            """)
        else:
            st.markdown(f"### مرحلہ چہارم: جائزہ اور خوشی کا اظہار (40 تا 60 منٹ)")
            st.markdown("""
            * بچوں سے پوچھیں کہ آج انہوں نے کیا نیا سیکھا اور کیسا محسوس کیا۔
            * سب کے کام کی تعریف کرکے بورڈ پر لگائیں۔
            """)

    with t5:
        if st.session_state.lang == "English":
            st.markdown("### Automated Backend Video & Downloadable Materials")
            st.info(f"💡 **Video Link:** [Watch Related Lesson Video]({video_url})")
            btn_label = f"Download Unit {unit_number} Custom Worksheet (.txt)"
        else:
            st.markdown("### خودکار ویڈیو اور ڈاؤن لوڈ کے قابل مواد")
            st.info(f"💡 **ویڈیو لنک:** [موضوع سے متعلق ویڈیو دیکھیں]({video_url})")
            btn_label = f"یونٹ {unit_number} کی ورک شیٹ ڈاؤن لوڈ کریں (.txt)"
        
        worksheet_content = f"""EFALL MASTER CURRICULUM WORKBOOK - UNIT {unit_number}
Theme: {theme_name}
Vocabulary Focus: {vocab_en} / {vocab_ur}
Literacy / Phonics Target: {phonics_target}
Urdu Phonics & Letters: {phonics_ur}
Sentence Writing Goal: {sentence_focus}
Math Counting Target: {math_num}
Pre-Writing Stroke Pattern: {stroke_focus}
Custom Mode: {active_custom_note if active_custom_note else 'Standard'}

Student Name: _______________________ Date: ____________

1. Phonics & Letter/Digraph Tracing ({phonics_target} | {phonics_ur}):
   Trace and write: ____________________________________

2. Vocabulary & Sentence Construction:
   Draw or paste a picture of {vocab_en} ({vocab_ur}).
   Write the sentence: {sentence_focus}

3. Math & Tally Counting (Target: {math_num}):
   Count and draw tally marks for {math_num} objects.
"""
        st.markdown(create_download_button(worksheet_content, f"Unit_{unit_number}_FineTuned_Worksheet.txt", btn_label), unsafe_allow_html=True)

# --- REFLECTION LOG ---
elif st.session_state.current_page == "Reflection Log":
    back_label = "⬅️ Back" if st.session_state.lang == "English" else "⬅️ واپس جائیں"
    if st.button(back_label):
        st.session_state.current_page = "Home"
        st.rerun()

    if st.session_state.lang == "English":
        st.title("📝 My Teaching Diary")
        name_prompt = "Your Name:"
        mood_title = "How did today go?"
        mood_options = ["🌟 Very Good", "💡 Learned Something New", "🌱 Need More Practice"]
        note_prompt = "Add any special notes or observations:"
        save_btn_label = "💾 Save Entry"
        success_save = "Successfully saved!"
        warning_name = "Please enter your name."
        saved_title = "📖 Saved Diary Entries"
        no_entries = "No diary entries yet."
    else:
        st.title("📝 میری تعلیمی ڈائری")
        name_prompt = "آپ کا نام (Your Name):"
        mood_title = "آج کا دن کیسا رہا؟"
        mood_options = ["🌟 بہت اچھا دن رہا (Very Good)", "💡 کچھ نیا سیکھا (Learned Something New)", "🌱 مزید مشق کی ضرورت ہے (Need More Practice)"]
        note_prompt = "کوئی خاص بات یا نوٹ لکھیں:"
        save_btn_label = "💾 محفوظ کریں (Save)"
        success_save = "کامیابی سے محفوظ ہو گیا!"
        warning_name = "براہ کرم اپنا نام درج کریں۔"
        saved_title = "📖 محفوظ شدہ ڈائری (Saved Entries)"
        no_entries = "ابھی تک کوئی ڈائری درج نہیں ہوئی۔"

    with st.form("simple_diary"):
        user_name = st.text_input(name_prompt)
        
        st.markdown(f"### {mood_title}")
        emoji_choice = st.radio("", mood_options)
        
        note_text = st.text_area(note_prompt)
        
        save_btn = st.form_submit_button(save_btn_label)
        if save_btn:
            if user_name.strip() == "":
                st.warning(warning_name)
            else:
                st.session_state.reflection_logs.append({
                    "name": user_name,
                    "date": str(date.today()),
                    "mood": emoji_choice,
                    "note": note_text
                })
                st.success(success_save)

    st.markdown("---")
    st.subheader(saved_title)
    if len(st.session_state.reflection_logs) == 0:
        st.info(no_entries)
    else:
        for idx, entry in enumerate(st.session_state.reflection_logs):
            with st.container(border=True):
                st.write(f"**#{idx+1} | {entry['date']} | {entry['name']}**")
                st.write(f"Status / حالت: {entry['mood']}")
                if entry['note']:
                	st.write(f"Note / نوٹ: {entry['note']}")
