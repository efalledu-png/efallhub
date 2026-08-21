import streamlit as st
import base64
from datetime import date

# Page Configuration
st.set_page_config(
    page_title="EFALL Master Curriculum Hub | آسان تعلیمی پورٹل",
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

# --- CURRICULUM ENGINE WITH EMBEDDED IB ATTRIBUTES & LANGUAGE SEPARATION ---
def get_unit_curriculum(unit_num):
    curriculum_database = [
        # --- THEME 1: WHO WE ARE (Units 1-8: Single Letters & Basic Words) ---
        ("Who We Are", "My Feelings and Me", "Face", "چہرہ", "Aa, Bb", "الف، ب", "0, 1", "Circular & Curve Loops", "I feel happy when...", "Empathize", "https://www.youtube.com/watch?v=Us-TVg40ExM"),
        ("Who We Are", "Emotions & Smiles", "Smile", "مسکان", "Cc, Dd", "پ، ت", "2, 3", "Horizontal lines", "My smile shows...", "Empathize", "https://www.youtube.com/watch?v=zUNWwWjF5x0"),
        ("Who We Are", "Eyes & Vision", "Eyes", "آنکھیں", "Ee, Ff", "ٹ، ث", "4, 5", "Slanting diagonal lines", "I see with my eyes.", "Define", "https://www.youtube.com/watch?v=v608v4zmlio"),
        ("Who We Are", "Heart & Feelings", "Heart", "دل", "Gg, Hh", "ج، چ", "6, 7", "Circular loops", "My heart beats fast.", "Define", "https://www.youtube.com/watch?v=1Wqf5vF_8Gg"),
        ("Who We Are", "Family Bonds", "Family", "خاندان", "Ii, Jj", "ح، خ", "8, 9", "Zig-zag patterns", "I love my family.", "Ideate", "https://www.youtube.com/watch?v=GiW7tMfy58Y"),
        ("Who We Are", "Hands & Touch", "Hands", "ہاتھ", "Kk, Ll", "د، ڈ", "10, 11", "Standing vertical lines", "My hands can build.", "Ideate", "https://www.youtube.com/watch?v=0h9Vp_qZ3Y0"),
        ("Who We Are", "Voice & Sound", "Voice", "آواز", "Mm, Nn", "ذ، ر", "12, 13", "Horizontal lines", "My voice is kind.", "Prototype", "https://www.youtube.com/watch?v=pW89h5fX8cI"),
        ("Who We Are", "My Body & Map", "Me", "میں", "Oo, Pp", "ڑ، ز", "14, 15", "Slanting lines", "This is my body.", "Test", "https://www.youtube.com/watch?v=h4u0bx_wgxE"),
        
        # --- THEME 2: WHERE WE ARE IN PLACE AND TIME (Units 9-16: Consonant Digraphs) ---
        ("Where We Are in Place and Time", "Doorways & Entry", "Door", "دروازہ", "Sh (Ship)", "ژ، س", "16, 17", "Circular loops", "The door shuts quietly.", "Empathize", "https://www.youtube.com/watch?v=8Vz9Z7o2cKo"),
        ("Where We Are in Place and Time", "Windows & Light", "Window", "کھڑکی", "Ch (Chair)", "ش، ص", "18, 19", "Zig-zag patterns", "The window lets in light.", "Empathize", "https://www.youtube.com/watch?v=L2v9s9K2V7o"),
        ("Where We Are in Place and Time", "Classroom Layout", "Table", "میز", "Th (That)", "ض، ط", "1, 2", "Standing lines", "That table is clean.", "Define", "https://www.youtube.com/watch?v=4r2v8K5Z1sE"),
        ("Where We Are in Place and Time", "Chairs & Seating", "Chair", "کرسی", "Wh (What)", "ظ، ع", "3, 4", "Horizontal lines", "What is my seat?", "Define", "https://www.youtube.com/watch?v=9v8k7L3s2wA"),
        ("Where We Are in Place and Time", "Floors & Walking", "Floor", "فرش", "Bl (Block)", "غ، ف", "5, 6", "Slanting lines", "We walk on the floor.", "Ideate", "https://www.youtube.com/watch?v=3w9s2k1L8vE"),
        ("Where We Are in Place and Time", "Walls & Structure", "Wall", "دیوار", "Cl (Class)", "ق، ک", "7, 8", "Curve loops", "The classroom wall stands.", "Ideate", "https://www.youtube.com/watch?v=5k8s3w2l9vA"),
        ("Where We Are in Place and Time", "Mats & Space", "Mat", "چٹائی", "Fl (Floor)", "گ، ل", "9, 10", "Tactile zig-zag", "Sit on the mat.", "Prototype", "https://www.youtube.com/watch?v=2v9s8k3l1wE"),
        ("Where We Are in Place and Time", "Rest & Routine", "Bed", "بستر", "Sl (Sleep)", "م، ن", "11, 12", "Vertical lines", "It is time to rest.", "Test", "https://www.youtube.com/watch?v=7k3s2w9l8vA"),
        
        # --- THEME 3: HOW WE EXPRESS OURSELVES (Units 17-25: Vowel Teams & Blends) ---
        ("How We Express Ourselves", "Colors & Hues", "Paint", "رنگ", "Ai (Paint)", "و، ہ", "13, 14", "Horizontal lines", "I paint bright colors.", "Empathize", "https://www.youtube.com/watch?v=8k3s2w9l1vE"),
        ("How We Express Ourselves", "Brushes & Strokes", "Brush", "برش", "Ee (Tree)", "ھ، ء", "15, 16", "Slanting lines", "The brush sweeps up.", "Empathize", "https://www.youtube.com/watch?v=1v8k3s2w9lE"),
        ("How We Express Ourselves", "Clay Molding", "Clay", "مٹی", "igh (High)", "ی، ے", "17, 18", "Curve loops", "We mold clay high.", "Define", "https://www.youtube.com/watch?v=9l8k3s2w1vE"),
        ("How We Express Ourselves", "Songs & Rhythm", "Song", "گیت", "Oa (Boat)", "ب، پ", "19, 20", "Zig-zag patterns", "We sing a sweet song.", "Define", "https://www.youtube.com/watch?v=3s2w9l8k1vE"),
        ("How We Express Ourselves", "Stories & Tales", "Story", "کہانی", "Oo (Moon)", "ت، ٹ", "1, 2", "Vertical lines", "Every story has magic.", "Ideate", "https://www.youtube.com/watch?v=4s2w9l8k3vE"),
        ("How We Express Ourselves", "Smiles & Joy", "Smile", "مسکرانا", "Ar (Star)", "ث، ج", "3, 4", "Horizontal lines", "Smiles shine like stars.", "Ideate", "https://www.youtube.com/watch?v=6s2w9l8k4vE"),
        ("How We Express Ourselves", "Laughter & Play", "Laugh", "ہنسنا", "Or (For)", "چ، ح", "5, 6", "Slanting lines", "We play for fun.", "Prototype", "https://www.youtube.com/watch?v=7s2w9l8k5vE"),
        ("How We Express Ourselves", "Dance & Motion", "Dance", "ناچ", "Ur (Turn)", "خ، د", "7, 8", "Curve loops", "We turn and dance.", "Prototype", "https://www.youtube.com/watch?v=8s2w9l8k6vE"),
        ("How We Express Ourselves", "Art & Contrast", "Color", "رنگ", "Ow (Cow)", "ڈ، ذ", "9, 10", "Tactile zig-zag", "Colors stand out now.", "Test", "https://www.youtube.com/watch?v=9s1k8l7v7vE"),
        
        # --- THEME 4: HOW THE WORLD WORKS (Units 26-33: Trigraphs & Complex Phonics) ---
        ("How the World Works", "Water & Flow", "Water", "پانی", "Dge (Bridge)", "ر، ڑ", "11, 12", "Vertical lines", "Water flows under bridges.", "Empathize", "https://www.youtube.com/watch?v=1w2s3k4l5vE"),
        ("How the World Works", "Leaves & Veins", "Leaf", "پتا", "Tch (Catch)", "ز، ژ", "13, 14", "Horizontal lines", "Catch the falling leaf.", "Empathize", "https://www.youtube.com/watch?v=2w3s4k5l6vE"),
        ("How the World Works", "Sunlight & Shadows", "Sun", "سورج", "Air (Chair)", "س، ش", "15, 16", "Slanting lines", "The sun gives us warmth.", "Define", "https://www.youtube.com/watch?v=3w4s5k6l7vE"),
        ("How the World Works", "Clouds & Sky", "Cloud", "بادل", "Ear (Hear)", "ص، ض", "17, 18", "Curve loops", "Can you hear the wind?", "Define", "https://www.youtube.com/watch?v=4w5s6k7l8vE"),
        ("How the World Works", "Rain & Droplets", "Rain", "بارش", "Are (Care)", "ط، ظ", "19, 20", "Vertical lines", "We care for rain water.", "Ideate", "https://www.youtube.com/watch?v=5w6s7k8l9vE"),
        ("How the World Works", "Stones & Weight", "Stone", "پتھر", "Oor (Poor)", "ع، غ", "1, 2", "Horizontal lines", "Heavy stones stay put.", "Ideate", "https://www.youtube.com/watch?v=6w7s8k9l1vE"),
        ("How the World Works", "Wind & Breeze", "Wind", "ہوا", "O/U (Push)", "ف، ق", "3, 4", "Slanting lines", "Wind pushes the trees.", "Prototype", "https://www.youtube.com/watch?v=7w8s9k1l2vE"),
        ("How the World Works", "Trees & Wood", "Tree", "درخت", "Ph (Phone)", "ک، گ", "5, 6", "Curve loops", "Trees provide sturdy wood.", "Test", "https://www.youtube.com/watch?v=8w9s1k2l3vE"),
        
        # --- THEME 5: HOW WE ORGANIZE OURSELVES (Units 34-41: Sentences & Descriptive Writing) ---
        ("How We Organize Ourselves", "Baskets & Storage", "Basket", "ٹوکری", "Sentences (I)", "ل، م", "7, 8", "Zig-zag patterns", "I put toys in baskets.", "Empathize", "https://www.youtube.com/watch?v=9w1s2k3l4vE"),
        ("How We Organize Ourselves", "Toys & Sharing", "Toy", "کھلونا", "Sentences (We)", "ن، و", "9, 10", "Vertical lines", "We share our toys.", "Empathize", "https://www.youtube.com/watch?v=1s2k3l4v5wE"),
        ("How We Organize Ourselves", "Shelves & Books", "Shelf", "الماری", "Sentences (Our)", "ہ، ی", "11, 12", "Horizontal lines", "Our books are on shelves.", "Define", "https://www.youtube.com/watch?v=2s3k4l5v6wE"),
        ("How We Organize Ourselves", "Boxes & Packing", "Box", "ڈبہ", "Sentences (Put)", "ء، ے", "13, 14", "Slanting lines", "Put blocks in the box.", "Define", "https://www.youtube.com/watch?v=3s4k5l6v7wE"),
        ("How We Organize Ourselves", "Tidying & Care", "Clean", "صاف", "Sentences (Keep)", "الف، ب", "15, 16", "Curve loops", "Keep the classroom clean.", "Ideate", "https://www.youtube.com/watch?v=4s5k6l7v8wE"),
        ("How We Organize Ourselves", "Patterns & Order", "Tidy", "درست", "Sentences (Make)", "پ، ت", "17, 18", "Zig-zag patterns", "Make patterns neatly.", "Ideate", "https://www.youtube.com/watch?v=5s6k7l8v9wE"),
        ("How We Organize Ourselves", "Helping Hands", "Help", "مدد", "Sentences (Help)", "ٹ، ث", "19, 20", "Vertical lines", "We are helping hands.", "Prototype", "https://www.youtube.com/watch?v=6s7k8l9v1wE"),
        ("How We Organize Ourselves", "Sorting Objects", "Sort", "ترتیب", "Sentences (Sort)", "ج، چ", "1, 2", "Horizontal lines", "Sort items by shape.", "Test", "https://www.youtube.com/watch?v=7s8k9l1v2wE"),
        
        # --- THEME 6: SHARING THE PLANET (Units 42-50: Independent Writing & Paragraphs) ---
        ("Sharing the Planet", "Seeds & Growth", "Seed", "بیج", "Writing (Grow)", "ح، خ", "3, 4", "Slanting lines", "Seeds grow into tall plants.", "Empathize", "https://www.youtube.com/watch?v=8s9k1l2v3wE"),
        ("Sharing the Planet", "Soil & Ground", "Soil", "مٹی", "Writing (Earth)", "د، ڈ", "5, 6", "Curve loops", "Rich soil feeds roots.", "Empathize", "https://www.youtube.com/watch?v=9s1k2l3v4wE"),
        ("Sharing the Planet", "Planting Life", "Plant", "پودا", "Writing (Water)", "ذ، ر", "7, 8", "Vertical lines", "Plants need water daily.", "Define", "https://www.youtube.com/watch?v=1k2l3v4v5wE"),
        ("Sharing the Planet", "Flowers & Blooms", "Flower", "پھول", "Writing (Bloom)", "ڑ، ز", "9, 10", "Horizontal lines", "Flowers bloom in spring.", "Define", "https://www.youtube.com/watch?v=2k3l4v5v6wE"),
        ("Sharing the Planet", "Birds & Feathers", "Bird", "پرندہ", "Writing (Fly)", "ژ، س", "11, 12", "Slanting lines", "Birds fly across skies.", "Ideate", "https://www.youtube.com/watch?v=3k4l5v6v7wE"),
        ("Sharing the Planet", "Cats & Paws", "Cat", "بلی", "Writing (Soft)", "ش، ص", "13, 14", "Curve loops", "Cats have soft paws.", "Ideate", "https://www.youtube.com/watch?v=4k5l6v7v8wE"),
        ("Sharing the Planet", "Dogs & Canines", "Dog", "کتا", "Writing (Loyal)", "ض، ط", "15, 16", "Zig-zag patterns", "Dogs are loyal friends.", "Prototype", "https://www.youtube.com/watch?v=5k6l7v8v9wE"),
        ("Sharing the Planet", "Tracking Growth", "Growth", "بڑھوتری", "Writing (Measure)", "ظ، ع", "17, 18", "Vertical lines", "We measure plant growth.", "Prototype", "https://www.youtube.com/watch?v=6k7l8v8v1wE"),
        ("Sharing the Planet", "Nature Care", "Care", "دیکھ بھال", "Writing (Protect)", "غ، ف", "19, 20", "Horizontal lines", "We protect our planet.", "Test", "https://www.youtube.com/watch?v=7k8l9v1v2wE")
    ]
    
    domain, category, vocab_en, vocab_ur, phonics_target, phonics_ur, math_num, stroke, sentence_focus, design_phase, video_url = curriculum_database[unit_num - 1]
    theme_name = f"Unit {unit_num}: {category}"
    return theme_name, vocab_en, vocab_ur, phonics_target, phonics_ur, math_num, stroke, domain, sentence_focus, design_phase, video_url

def create_download_button(content, filename, label):
    b64 = base64.b64encode(content.encode('utf-8')).decode('utf-8')
    return f'<a href="data:text/plain;charset=utf-8;base64,{b64}" download="{filename}" style="text-decoration:none;"><div style="background:#2e7d32;color:white;padding:12px;text-align:center;border-radius:8px;font-weight:bold;font-size:16px;margin-top:10px;">📥 {label}</div></a>'

# --- NAVIGATION SIDEBAR ---
st.sidebar.title("🌟 EFALL Hub")
st.sidebar.caption("Educated Mother Education Nation")

if st.sidebar.button("🏠 Home", use_container_width=True):
    st.session_state.current_page = "Home"
    st.rerun()
if st.sidebar.button("📚 50 Units Library", use_container_width=True):
    st.session_state.current_page = "Unit Library"
    st.rerun()
if st.sidebar.button("📝 My Diary", use_container_width=True):
    st.session_state.current_page = "Reflection Log"
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.title("🌟 آسان تعلیمی ہب")
st.sidebar.caption("تعلیم یافتہ ماں، روشن مستقبل")

if st.sidebar.button("🏠 مین صفحہ", use_container_width=True):
    st.session_state.current_page = "Home"
    st.rerun()
if st.sidebar.button("📚 اسباق کی لائبریری", use_container_width=True):
    st.session_state.current_page = "Unit Library"
    st.rerun()
if st.sidebar.button("📝 میری ڈائری", use_container_width=True):
    st.session_state.current_page = "Reflection Log"
    st.rerun()

# --- HOME PAGE ---
if st.session_state.current_page == "Home":
    st.title("🌟 Welcome to EFALL Master Teaching Hub")
    st.markdown("### 🎯 Select an IB PYP Theme Box below to open units:")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🧩 Box 1: Who We Are\n(Letters & Basics - Units 1-8)", use_container_width=True):
            st.session_state.selected_unit = 1
            st.session_state.current_page = "Unit Library"
            st.rerun()
        if st.button("🎨 Box 3: How We Express\n(Vowels & Blends - Units 17-25)", use_container_width=True):
            st.session_state.selected_unit = 17
            st.session_state.current_page = "Unit Library"
            st.rerun()
        if st.button("🧹 Box 5: How We Organize\n(Sentences - Units 34-41)", use_container_width=True):
            st.session_state.selected_unit = 34
            st.session_state.current_page = "Unit Library"
            st.rerun()
    with col2:
        if st.button("🏡 Box 2: Where We Are\n(Digraphs - Units 9-16)", use_container_width=True):
            st.session_state.selected_unit = 9
            st.session_state.current_page = "Unit Library"
            st.rerun()
        if st.button("💧 Box 4: How World Works\n(Trigraphs - Units 26-33)", use_container_width=True):
            st.session_state.selected_unit = 26
            st.session_state.current_page = "Unit Library"
            st.rerun()
        if st.button("🌿 Box 6: Sharing Planet\n(Independent Writing - Units 42-50)", use_container_width=True):
            st.session_state.selected_unit = 42
            st.session_state.current_page = "Unit Library"
            st.rerun()

    st.markdown("---")
    st.title("🌟 خوش آمدید: آسان تدریسی پورٹل")
    st.markdown("### 🎯 کسی بھی یونٹ کو کھولنے کے لیے ذیل میں سے سیکشن منتخب کریں:")
    
    if st.button("📝 میری تدریسی ڈائری کھولیں", use_container_width=True):
        st.session_state.current_page = "Reflection Log"
        st.rerun()

# --- UNIT LIBRARY & CHRONOLOGICAL LESSON COACH ---
elif st.session_state.current_page == "Unit Library":
    if st.button("⬅️ Back / واپس جائیں"):
        st.session_state.current_page = "Home"
        st.rerun()

    st.title("📚 50-Unit Curriculum Hub & اسباق کی تفصیلی لائبریری")
    
    unit_number = st.selectbox(
        "Select Unit Number (1 to 50) / یونٹ نمبر منتخب کریں:", 
        list(range(1, 51)), 
        index=st.session_state.selected_unit - 1, 
        format_func=lambda x: f"Unit {x}: {get_unit_curriculum(x)[0]}"
    )
    st.session_state.selected_unit = unit_number
    
    theme_name, vocab_en, vocab_ur, phonics_target, phonics_ur, math_num, stroke_focus, domain_name, sentence_focus, design_phase, video_url = get_unit_curriculum(unit_number)

    st.markdown("---")
    st.markdown(f"## 📋 {theme_name}")
    st.info(f"🌐 **IB Theme:** {domain_name} &nbsp;|&nbsp; 🔤 **Literacy Target:** {phonics_target} &nbsp;|&nbsp; ✍️ **Sentence Goal:** {sentence_focus}")
    st.info(f"🌐 **آئی بی تھیم:** {domain_name} &nbsp;|&nbsp; 🔤 **اردو الفاظ اور صوتی ہدف:** {vocab_ur} ({phonics_ur})")

    # --- TOP 3-STEP QUICK FACILITATION CARD ---
    st.markdown("### 👩‍🏫 Quick Facilitation Guide & آسان تدریسی طریقہ")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""
        <div style="background: #e8f8f5; border: 2px solid #1abc9c; padding: 10px; border-radius: 8px; text-align: center;">
            <h4 style="color: #16a085; margin:0;">1️⃣ Show</h4>
            <p style="font-size: 12px; margin-top: 5px;">Show flashcard for <b>{vocab_en}</b> & sound <b>{phonics_target}</b>.</p>
            <hr style="margin:5px 0;">
            <h4 style="color: #16a085; margin:0;">دکھائیں۔</h4>
            <p style="font-size: 12px; margin-top: 5px;"><b>{vocab_ur}</b> اور آواز <b>{phonics_ur}</b> کا فلیش کارڈ دکھائیں۔</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div style="background: #fdf2e9; border: 2px solid #f39c12; padding: 10px; border-radius: 8px; text-align: center;">
            <h4 style="color: #d35400; margin:0;">2️⃣ Ask</h4>
            <p style="font-size: 12px; margin-top: 5px;"><b>Listen:</b> "What do you notice? How do others see this?"</p>
            <hr style="margin:5px 0;">
            <h4 style="color: #d35400; margin:0;">پوچھیں۔</h4>
            <p style="font-size: 12px; margin-top: 5px;"><b>سنیے:</b> "دوسرے اس کو کیسے دیکھتے ہیں؟ آپ کو کیا محسوس ہوتا ہے؟"</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div style="background: #ebf5fb; border: 2px solid #3498db; padding: 10px; border-radius: 8px; text-align: center;">
            <h4 style="color: #2980b9; margin:0;">3️⃣ Do</h4>
            <p style="font-size: 12px; margin-top: 5px;">Trace <b>{stroke_focus}</b> & write: <b>{sentence_focus}</b> thoughtfully.</p>
            <hr style="margin:5px 0;">
            <h4 style="color: #2980b9; margin:0;">کریں۔</h4>
            <p style="font-size: 12px; margin-top: 5px;">لاب اسٹروک <b>{stroke_focus}</b> بنائیں اور ذمہ داری سے مشق کریں۔</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    # --- DETAILED CHRONOLOGICAL LESSON TABS ---
    t1, t2, t3, t4, t5 = st.tabs([
        "🕒 Phase 1: Setup & Opening", 
        "🕒 Phase 2: Phonics & Writing", 
        "🕒 Phase 3: Challenge & Worksheet", 
        "🕒 Phase 4: Reflection & Boards",
        "🎥 Aligned Video & Resources"
    ])

    with t1:
        st.markdown(f"### Phase 1: Opening & Provocation (0-10 mins) — {vocab_en}")
        st.markdown("""
        * **Small Space Setup:** Clear classroom furniture to maximize floor space, welcoming diverse perspectives as children sit together on the circle carpet.
        * **Gathering Students:** Bring children into small collaborative circles to encourage open communication and mutual respect.
        * **Teacher Script & Inquiry Routine:** Use open-ended inquiry prompts (*"Imagine if everyone around the world shared this feeling..."*) to cultivate global empathy and balanced thinking.
        """)
        st.markdown("---")
        st.markdown(f"### مرحلہ اول: آغاز اور تعارف (0 تا 10 منٹ) — {vocab_ur}")
        st.markdown("""
        * **چھوٹی جگہ کا انتظام:** فرنیچر ہٹا کر بچوں کو گول دائرے میں اس طرح بٹھائیں کہ سب ایک دوسرے کی بات غور سے سن سکیں۔
        * **بچوں کو اکٹھا کرنا:** چھوٹے گروپس میں ایک دوسرے کے خیالات کا احترام کرنے کی عادت ڈالیں۔
        * **تدریسی انداز:** بچوں سے ایسے سوالات پوچھیں جو انہیں دنیا بھر کے ماحول اور دوستوں کے بارے میں سوچنے پر آمادہ کریں۔
        """)

    with t2:
        st.markdown(f"### Phase 2: Phonics, Digraphs & Pre-Writing (10-20 mins)")
        st.markdown(f"""
        * **Literacy Progression:** Practice target sound **{phonics_target}** alongside vocabulary **{vocab_en}**, encouraging risk-taking and articulate expression.
        * **Pre-Writing Stroke Practice:** Trace linear or curved stroke pattern **{stroke_focus}** with reflective care and patience.
        * **Sentence Building:** Guide students to articulate, risk trying new words, and write the sentence goal: *"{sentence_focus}"*.
        """)
        st.markdown("---")
        st.markdown("### مرحلہ دوم: صوتیات اور تحریری مشق (10 تا 20 منٹ)")
        st.markdown(f"""
        * **صوتی ہدف:** اردو الفاظ اور آوازوں <b>{vocab_ur} ({phonics_ur})</b> کی مشق کریں اور بچوں کو نئے الفاظ بولنے کی ترغیب دیں۔
        * **لاب لکھائی:** صبر اور توجہ کے ساتھ لکیروں اور دائروں کی مشق کریں۔
        * **جملہ سازی:** بچوں کو با اعتماد طریقے سے سوچ کر سادہ جملے لکھنے کی رہنمائی کریں۔
        """)

    with t3:
        st.markdown(f"### Phase 3: The Inquiry Challenge & Custom Worksheet (20-40 mins)")
        st.markdown(f"""
        * **Hands-On Activity:** Engage students in collaborative inquiry challenges, promoting principled sharing of materials from the supply basket.
        * **Math Integration:** Measure objects using finger units, reflecting on different ways peers solve problems up to count **{math_num}**.
        * **Custom Worksheet:** Distribute the downloadable activity sheet tailored to this unit's literacy, caring attitudes, and math goals.
        """)
        st.markdown("---")
        st.markdown("### مرحلہ سوم: عملی چیلنج اور ورک شیٹ (20 تا 40 منٹ)")
        st.markdown(f"""
        * **عملی سرگرمی:** بچوں کو ٹوکری میں موجود اشیاء کو آپس میں مل کر بانٹ کر استعمال کرنے کا سکھائیں۔
        * **ریاضی کا امتزاج:** چیزوں کی گنتی کریں، مختلف طریقوں سے سوچیں اور ہندسہ <b>{math_num}</b> تک کے نشانات لگائیں۔
        * **ورک شیٹ:** اس یونٹ کے لیے خاص طور پر تیار کردہ ورک شیٹ تقسیم کریں۔
        """)

    with t4:
        st.markdown(f"### Phase 4: Reflection, Boards & Closing (40-60 mins)")
        st.markdown("""
        * **Lab Board Documentation:** Post Polaroid photos, student blueprints, vocabulary cards, and tally graphs to celebrate diverse ideas and open-minded inquiry.
        * **Responsibility Board:** Mount group pictures with created projects, discussing how caring actions positively impact our local and global community.
        * **Bridge to Next Session:** Conclude with reflective inquiry questions that inspire principled habits.
        """)
        st.markdown("---")
        st.markdown("### مرحلہ چہارم: جائزہ اور اختتام (40 تا 60 منٹ)")
        st.markdown("""
        * **لاگ بورڈ:** بچوں کے بنائے ہوئے کام اور تخلیقی خیالات کو ڈسپلے بورڈ پر سجا کر ایک دوسرے کے کام کی تعریف کریں۔
        * **ذمے داری بورڈ:** بچوں کو یہ سمجھائیں کہ ان کے چھوٹے چھوٹے اچھے کام کس طرح دنیا کو بہتر بناتے ہیں۔
        * **اگلے سبق کا تسلسل:** اگلے دن کے لیے فکری اور دلچسپ سوالات کے ساتھ سیشن ختم کریں۔
        """)

    with t5:
        st.markdown("### Aligned Video & Downloadable Materials")
        st.info(f"💡 **Aligned Video Resource:** Watch this topic-matched video to support your lesson: [Open Video Link]({video_url})")
        
        worksheet_content = f"""EFALL MASTER CURRICULUM WORKBOOK - UNIT {unit_number}
Theme: {theme_name}
Vocabulary Focus: {vocab_en} / {vocab_ur}
Literacy / Phonics / Digraph Target: {phonics_target}
Urdu Phonics & Letters: {phonics_ur}
Sentence Writing Goal: {sentence_focus}
Math Counting Target: {math_num}
Pre-Writing Stroke Pattern: {stroke_focus}

Student Name: _______________________ Date: ____________

1. Phonics & Letter/Digraph Tracing ({phonics_target} | {phonics_ur}):
   Trace and write: ____________________________________

2. Vocabulary & Sentence Construction:
   Draw or paste a picture of {vocab_en} ({vocab_ur}).
   Write the sentence: {sentence_focus}

3. Math & Tally Counting (Target: {math_num}):
   Count and draw tally marks for {math_num} objects.
"""
        st.markdown(create_download_button(worksheet_content, f"Unit_{unit_number}_FineTuned_Worksheet.txt", f"Download Unit {unit_number} Custom Worksheet (.txt)"), unsafe_allow_html=True)

# --- REFLECTION LOG ---
elif st.session_state.current_page == "Reflection Log":
    if st.button("⬅️ Back / واپس جائیں"):
        st.session_state.current_page = "Home"
        st.rerun()

    st.title("📝 My Teaching Diary & میری تعلیمی ڈائری")
    
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
