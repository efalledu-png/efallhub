import streamlit as st
import base64
from datetime import date

# Page Configuration
st.set_page_config(
    page_title="EFALL Simple Hub | آسان تعلیمی پورٹل",
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
if "age_tier" not in st.session_state:
    st.session_state.age_tier = "Ages 3–5 (Early Years)"
if "reflection_logs" not in st.session_state:
    st.session_state.reflection_logs = []

# --- LARGE VISUAL SIDEBAR ---
st.sidebar.title("🌟 EFALL آسان ہب")
st.sidebar.caption("Educated Mother Education Nation")

# Language Switcher
lang_choice = st.sidebar.radio(
    "Select Language / زبان منتخب کریں", 
    ["English", "اردو"], 
    index=0 if st.session_state.lang == "English" else 1
)
st.session_state.lang = lang_choice

st.sidebar.markdown("---")
st.sidebar.subheader("👶 عمر کا انتخاب / Age Group")
age_tier = st.sidebar.radio(
    "Select Age:",
    [
        "Ages 3–5 (Early Years)", 
        "Ages 6–8 (Lower Primary)", 
        "Ages 9–10 (Upper Primary)"
    ],
    index=["Ages 3–5 (Early Years)", "Ages 6–8 (Lower Primary)", "Ages 9–10 (Upper Primary)"].index(st.session_state.age_tier)
)
st.session_state.age_tier = age_tier

st.sidebar.markdown("---")
st.sidebar.subheader("📍 Menu / مینو")

if st.sidebar.button("🏠 Home / مین صفحہ", use_container_width=True):
    st.session_state.current_page = "Home"
    st.rerun()
if st.sidebar.button("📚 50 Units / اسسباق کی کتاب", use_container_width=True):
    st.session_state.current_page = "Unit Library"
    st.rerun()
if st.sidebar.button("📝 My Diary / میری ڈائری", use_container_width=True):
    st.session_state.current_page = "Reflection Log"
    st.rerun()

# --- BACKEND MASTER CURRICULUM ENGINE (IB PYP Themes) ---
def get_unit_curriculum(unit_num):
    curriculum_database = [
        # Who We Are (Units 1-8)
        ("Who We Are", "My Feelings and Me", "Face / چہرہ", "A, B", "الف، ب", "0, 1", "Circular & Curve Loops", "Inquiring into emotional awareness and personal identity", "Empathize"),
        ("Who We Are", "Emotions & Smiles", "Smile / مسکان", "C, D", "پ، ت", "2, 3", "Sleeping horizontal lines", "Investigating personal expressions and reactions", "Empathize"),
        ("Who We Are", "Eyes & Vision", "Eyes / آنکھیں", "E, F", "ٹ، ث", "4, 5", "Slanting diagonal lines", "Exploring sensory perception and vision", "Define"),
        ("Who We Are", "Heart & Feelings", "Heart / دل", "G, H", "ج، چ", "6, 7", "Circular and curve loops", "Connecting heartbeats, feelings, and empathy", "Define"),
        ("Who We Are", "Family Bonds", "Family / خاندان", "I, J", "ح، خ", "8, 9", "Zig-zag tactile patterns", "Recognizing family roles and cooperative relationships", "Ideate"),
        ("Who We Are", "Hands & Touch", "Hands / ہاتھ", "K, L", "د، ڈ", "10, 11", "Standing vertical lines", "Fine motor coordination and tactile feedback", "Ideate"),
        ("Who We Are", "Voice & Sound", "Voice / آواز", "M, N", "ذ، ر", "12, 13", "Sleeping horizontal lines", "Auditory discovery and vocal expression", "Prototype"),
        ("Who We Are", "My Body", "Me / میں", "O, P", "ڑ، ز", "14, 15", "Slanting diagonal lines", "Body awareness and self-identity mapping", "Test"),
        
        # Where We Are in Place and Time (Units 9-16)
        ("Where We Are in Place and Time", "Doorways & Entry", "Door / دروازہ", "Q, R", "ژ، س", "16, 17", "Circular loops", "Navigating physical spaces and boundary lines", "Empathize"),
        ("Where We Are in Place and Time", "Windows & Light", "Window / کھڑکی", "S, T", "ش، ص", "18, 19", "Zig-zag patterns", "Exploring natural light and indoor viewpoints", "Empathize"),
        ("Where We Are in Place and Time", "Tables & Classroom", "Table / میز", "U, V", "ض، ط", "1, 2", "Standing lines", "Arranging classroom furniture and cooperative layout", "Define"),
        ("Where We Are in Place and Time", "Chairs & Seating", "Chair / کرسی", "W, X", "ظ، ع", "3, 4", "Sleeping lines", "Understanding seating order and body posture", "Define"),
        ("Where We Are in Place and Time", "Floors & Walking", "Floor / فرش", "Y, Z", "غ، ف", "5, 6", "Slanting lines", "Exploring textures underfoot and surface gradients", "Ideate"),
        ("Where We Are in Place and Time", "Walls & Structure", "Wall / دیوار", "A, B", "ق، ک", "7, 8", "Curve loops", "Building structural boundaries and spatial barriers", "Ideate"),
        ("Where We Are in Place and Time", "Mats & Seating", "Mat / چٹائی", "C, D", "گ، ل", "9, 10", "Tactile zig-zag", "Personal space organization on floor mats", "Prototype"),
        ("Where We Are in Place and Time", "Beds & Rest", "Bed / بستر", "E, F", "م، ن", "11, 12", "Vertical lines", "Routine management and restorative resting cycles", "Test"),
        
        # How We Express Ourselves (Units 17-25)
        ("How We Express Ourselves", "Colors & Paint", "Paint / رنگ", "G, H", "و، ہ", "13, 14", "Horizontal lines", "Color mixing and emotional representation through hues", "Empathize"),
        ("How We Express Ourselves", "Brushes & Strokes", "Brush / برش", "I, J", "ھ، ء", "15, 16", "Slanting lines", "Brush stroke control and pre-writing linear mastery", "Empathize"),
        ("How We Express Ourselves", "Clay & Molding", "Clay / مٹی", "K, L", "ی، ے", "17, 18", "Curve loops", "Tactile 3D molding and geometric shape creation", "Define"),
        ("How We Express Ourselves", "Songs & Rhymes", "Song / گیت", "M, N", "ب، پ", "19, 20", "Zig-zag patterns", "Aural pattern recognition and rhythmic expression", "Define"),
        ("How We Express Ourselves", "Stories & Tales", "Story / کہانی", "O, P", "ت، ٹ", "1, 2", "Vertical lines", "Narrative creation and logical sequence understanding", "Ideate"),
        ("How We Express Ourselves", "Smiles & Joy", "Smile / مسکرانا", "Q, R", "ث، ج", "3, 4", "Horizontal lines", "Expressing joy through collaborative art and movement", "Ideate"),
        ("How We Express Ourselves", "Laughter & Fun", "Laugh / ہنسنا", "S, T", "چ، ح", "5, 6", "Slanting lines", "Social bonding through shared cooperative team building", "Prototype"),
        ("How We Express Ourselves", "Dance & Movement", "Dance / ناچ", "U, V", "خ، د", "7, 8", "Curve loops", "Gross motor coordination and expressive physical motion", "Prototype"),
        ("How We Express Ourselves", "Art & Hues", "Color / رنگ", "W, X", "ڈ، ذ", "9, 10", "Tactile zig-zag", "Aesthetic appreciation of color gradients and contrast", "Test"),
        
        # How the World Works (Units 26-33)
        ("How the World Works", "Water & Rivers", "Water / پانی", "Y, Z", "ر، ڑ", "11, 12", "Vertical lines", "Properties of liquids and observation of flow dynamics", "Empathize"),
        ("How the World Works", "Leaves & Foliage", "Leaf / پتا", "A, B", "ز، ژ", "13, 14", "Horizontal lines", "Botanical shapes, symmetry, and vein pattern inquiry", "Empathize"),
        ("How the World Works", "Sunlight & Warmth", "Sun / سورج", "C, D", "س، ش", "15, 16", "Slanting lines", "Observing solar warmth, shadows, and light sources", "Define"),
        ("How the World Works", "Clouds & Sky", "Cloud / بادل", "E, F", "ص، ض", "17, 18", "Curve loops", "Weather observation and atmospheric shifts", "Define"),
        ("How the World Works", "Rain & Showers", "Rain / بارش", "G, H", "ط، ظ", "19, 20", "Vertical lines", "Precipitation tracking and droplet motion testing", "Ideate"),
        ("How the World Works", "Stones & Earth", "Stone / پتھر", "I, J", "ع، غ", "1, 2", "Horizontal lines", "Investigating weight, texture, and density of natural objects", "Ideate"),
        ("How the World Works", "Wind & Breeze", "Wind / ہوا", "K, L", "ف، ق", "3, 4", "Slanting lines", "Air movement, resistance, and kinetic inquiry", "Prototype"),
        ("How the World Works", "Trees & Timber", "Tree / درخت", "M, N", "ک، گ", "5, 6", "Curve loops", "Plant anatomy and structural strength analysis", "Test"),
        
        # How We Organize Ourselves (Units 34-41)
        ("How We Organize Ourselves", "Baskets & Storage", "Basket / ٹوکری", "O, P", "ل، م", "7, 8", "Zig-zag patterns", "Sorting, classifying, and container management systems", "Empathize"),
        ("How We Organize Ourselves", "Toys & Play", "Toy / کھلونا", "Q, R", "ن، و", "9, 10", "Vertical lines", "Inventory management and cooperative sharing protocols", "Empathize"),
        ("How We Organize Ourselves", "Shelves & Books", "Shelf / الماری", "S, T", "ہ، ی", "11, 12", "Horizontal lines", "Library organization and categorization systems", "Define"),
        ("How We Organize Ourselves", "Boxes & Packing", "Box / ڈبہ", "U, V", "ء، ے", "13, 14", "Slanting lines", "Volume analysis, spatial packing, and geometry", "Define"),
        ("How We Organize Ourselves", "Cleaning & Tidying", "Clean / صاف", "W, X", "الف، ب", "15, 16", "Curve loops", "Responsibility routines and environmental care habits", "Ideate"),
        ("How We Organize Ourselves", "Order & Arrangement", "Tidy / درست", "Y, Z", "پ، ت", "17, 18", "Zig-zag patterns", "Pattern sequencing and symmetrical arrangement design", "Ideate"),
        ("How We Organize Ourselves", "Helping Hands", "Help / مدد", "A, B", "ٹ، ث", "19, 20", "Vertical lines", "Community collaboration and shared task execution", "Prototype"),
        ("How We Organize Ourselves", "Sorting Objects", "Sort / ترتیب", "C, D", "ج، چ", "1, 2", "Horizontal lines", "Logical categorization based on physical attributes", "Test"),
        
        # Sharing the Planet (Units 42-50)
        ("Sharing the Planet", "Seeds & Planting", "Seed / بیج", "E, F", "ح، خ", "3, 4", "Slanting lines", "Life cycles and seed germination inquiry", "Empathize"),
        ("Sharing the Planet", "Soil & Ground", "Soil / مٹی", "G, H", "د، ڈ", "5, 6", "Curve loops", "Earth layers and plant growth foundations", "Empathize"),
        ("Sharing the Planet", "Growing Plants", "Plant / پودا", "I, J", "ذ، ر", "7, 8", "Vertical lines", "Water, nutrient, and sunlight requirements for growth", "Define"),
        ("Sharing the Planet", "Flowers & Blossoms", "Flower / پھول", "K, L", "ڑ، ز", "9, 10", "Horizontal lines", "Aesthetic plant parts and basic pollination inquiry", "Define"),
        ("Sharing the Planet", "Birds & Feathers", "Bird / پرندہ", "M, N", "ژ، س", "11, 12", "Slanting lines", "Animal habitats and avian environmental adaptation", "Ideate"),
        ("Sharing the Planet", "Cats & Paws", "Cat / بلی", "O, P", "ش، ص", "13, 14", "Curve loops", "Mammal characteristics, needs, and careful interaction", "Ideate"),
        ("Sharing the Planet", "Dogs & Canines", "Dog / کتا", "Q, R", "ض، ط", "15, 16", "Zig-zag patterns", "Animal behavior, communication, and loyalty concepts", "Prototype"),
        ("Sharing the Planet", "Plant Growth", "Growth / بڑھوتری", "S, T", "ظ، ع", "17, 18", "Vertical lines", "Long-term tracking and measurement of living organisms", "Prototype"),
        ("Sharing the Planet", "Nature Care", "Care / دیکھ بھال", "U, V", "غ، ف", "19, 20", "Horizontal lines", "Environmental stewardship and ecological responsibility", "Test")
    ]
    
    domain, category, vocab, en, ur, math, stroke, inquiry_focus, design_phase = curriculum_database[unit_num - 1]
    theme_name = f"Unit {unit_num}: {category}"
    return theme_name, vocab, en, ur, str(math), stroke, domain, inquiry_focus, design_phase

def create_download_button(content, filename, label):
    b64 = base64.b64encode(content.encode('utf-8')).decode('utf-8')
    return f'<a href="data:text/plain;charset=utf-8;base64,{b64}" download="{filename}" style="text-decoration:none;"><div style="background:#2e7d32;color:white;padding:12px;text-align:center;border-radius:8px;font-weight:bold;font-size:16px;margin-top:10px;">📥 {label}</div></a>'


# --- HOME PAGE (Visual Big-Button Dashboard) ---
if st.session_state.current_page == "Home":
    st.title("🌟 EFALL آسان اسباق اور سکھانے کا طریقہ")
    st.markdown("### 🎯 Tap any box below to start teaching through inquiry and play!")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🧩 Box 1: Who We Are\n(ہم کون ہیں)", use_container_width=True, key="h1"):
            st.session_state.selected_unit = 1
            st.session_state.current_page = "Unit Library"
            st.rerun()
        if st.button("🎨 Box 3: How We Express\n(ہم کیسے اظہار کرتے ہیں)", use_container_width=True, key="h3"):
            st.session_state.selected_unit = 17
            st.session_state.current_page = "Unit Library"
            st.rerun()
        if st.button("🧹 Box 5: How We Organize\n(ہم خود کو کیسے منظم کرتے ہیں)", use_container_width=True, key="h5"):
            st.session_state.selected_unit = 34
            st.session_state.current_page = "Unit Library"
            st.rerun()
    with col2:
        if st.button("🏡 Box 2: Where We Are\n(ہم کہاں ہیں وقت اور جگہ میں)", use_container_width=True, key="h2"):
            st.session_state.selected_unit = 9
            st.session_state.current_page = "Unit Library"
            st.rerun()
        if st.button("💧 Box 4: How World Works\n(دنیا کیسے کام کرتی ہے)", use_container_width=True, key="h4"):
            st.session_state.selected_unit = 26
            st.session_state.current_page = "Unit Library"
            st.rerun()
        if st.button("🌿 Box 6: Sharing Planet\n(سیارے کی مشترکہ دیکھ بھال)", use_container_width=True, key="h6"):
            st.session_state.selected_unit = 42
            st.session_state.current_page = "Unit Library"
            st.rerun()

    st.markdown("---")
    if st.button("📝 Click here to open My Diary (میری ڈائری)", use_container_width=True):
        st.session_state.current_page = "Reflection Log"
        st.rerun()

# --- UNIT LIBRARY & SIMPLE 3-STEP GUIDE ---
elif st.session_state.current_page == "Unit Library":
    if st.button("⬅️ Back / واپس جائیں"):
        st.session_state.current_page = "Home"
        st.rerun()

    st.title("📚 اسباق کی لائبریری / Unit Library")
    
    unit_number = st.selectbox("Select Unit Number (1 to 50) / یونٹ نمبر منتخب کریں:", list(range(1, 51)), index=st.session_state.selected_unit - 1, format_func=lambda x: f"Unit {x}: {get_unit_curriculum(x)[0]}")
    
    theme_name, vocab_theme, en_focus, ur_focus, math_focus, stroke_focus, domain_name, inquiry_focus, design_phase = get_unit_curriculum(unit_number)

    st.markdown("---")
    st.markdown(f"## 📋 {theme_name}")
    st.info(f"🌐 **Theme:** {domain_name} &nbsp;|&nbsp; 💡 **Action Phase:** {design_phase}")

    # SIMPLIFIED 3-STEP PICTURE CARDS FOR TEACHING
    st.markdown("### 👩‍🏫 سکھانے کا آسان طریقہ / 3-Step Teaching Guide")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div style="background: #e8f8f5; border: 2px solid #1abc9c; padding: 15px; border-radius: 10px; text-align: center;">
            <h3 style="color: #16a085; margin:0;">1️⃣ Show / دکھائیں</h3>
            <p style="font-size: 14px; margin-top: 10px;">Bring a real object or picture of <b>'{}'</b>. Let children touch and look at it.</p>
        </div>
        """.format(vocab_theme), unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div style="background: #fdf2e9; border: 2px solid #f39c12; padding: 15px; border-radius: 10px; text-align: center;">
            <h3 style="color: #d35400; margin:0;">2️⃣ Ask / پوچھیں</h3>
            <p style="font-size: 14px; margin-top: 10px;"><b>🔊 سنیے / Listen & Ask:</b><br>"What do you see? آپ کو کیا دکھتا ہے؟"</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div style="background: #ebf5fb; border: 2px solid #3498db; padding: 15px; border-radius: 10px; text-align: center;">
            <h3 style="color: #2980b9; margin:0;">3️⃣ Do / کریں</h3>
            <p style="font-size: 14px; margin-top: 10px;">Practice letters <b>'{0}' / '{1}'</b> and count up to <b>{2}</b> together!</p>
        </div>
        """.format(en_focus, ur_focus, math_focus), unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🖨️ Download Teaching Pack / ڈاؤن لوڈ کریں")
    download_text = f"""EFALL SIMPLE TEACHING GUIDE - {theme_name}
- Vocabulary: {vocab_theme}
- English/Urdu Phonics: {en_focus} / {ur_focus}
- Math Count: {math_focus}
- 3 Steps: 1. Show object. 2. Ask what they notice. 3. Build & trace.
"""
    st.markdown(create_download_button(download_text, f"Unit_{unit_number}_Guide.txt", "Download Unit Guide"), unsafe_allow_html=True)

# --- REFLECTION LOG (One-Tap Emoji Diary) ---
elif st.session_state.current_page == "Reflection Log":
    if st.button("⬅️ Back / واپس جائیں"):
        st.session_state.current_page = "Home"
        st.rerun()

    st.title("📝 میری ڈائری / My Teaching Diary")
    st.markdown("Tap your feelings or progress today! / آج آپ کا دن کیسا رہا؟")
    
    with st.form("simple_diary"):
        user_name = st.text_input("Your Name / آپ کا نام:")
        
        st.markdown("### Select how today went / آج کا تاثر منتخب کریں:")
        emoji_choice = st.radio("Choose One:", [
            "🌟 Very Good / بہت اچھا دن رہا", 
            "💡 Learned Something New / کچھ نیا سیکھا", 
            "🌱 Need More Practice / مزید مشق کی ضرورت ہے"
        ])
        
        note_text = st.text_area("Write or speak a short note / کوئی خاص بات لکھیں:")
        
        save_btn = st.form_submit_button("💾 Save / محفوظ کریں")
        if save_btn:
            if user_name.strip() == "":
                st.warning("Please enter your name. / براہ کرم نام درج کریں۔")
            else:
                st.session_state.reflection_logs.append({
                    "name": user_name,
                    "date": str(date.today()),
                    "mood": emoji_choice,
                    "note": note_text
                })
                st.success("Saved successfully! / کامیابی سے محفوظ ہو گیا!")

    st.markdown("---")
    st.subheader("📖 Saved Diary Entries / محفوظ شدہ ڈائری")
    if len(st.session_state.reflection_logs) == 0:
        st.info("No entries yet. / ابھی تک کوئی ڈائری درج نہیں ہوئی۔")
    else:
        for idx, entry in enumerate(st.session_state.reflection_logs):
            with st.container(border=True):
                st.write(f"**#{idx+1} | {entry['date']} | {entry['name']}**")
                st.write(f"Status: {entry['mood']}")
                if entry['note']:
                    st.write(f"Note: {entry['note']}")
        
        diary_download = "EFALL TEACHER DIARY LOGS\n====================\n\n"
        for idx, entry in enumerate(st.session_state.reflection_logs):
            diary_download += f"Entry #{idx+1} ({entry['date']}) - {entry['name']}\nMood: {entry['mood']}\nNote: {entry['note']}\n--------------------\n"
        st.markdown(create_download_button(diary_download, "My_Teaching_Diary.txt", "Download Diary Logs"), unsafe_allow_html=True)
