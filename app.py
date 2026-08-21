import streamlit as st
import base64

# Page Configuration
st.set_page_config(
    page_title="EFALL Portal | Unified Dynamic Experience (Ages 3-4)",
    page_icon="🌟",
    layout="wide"
)

# Initialize Session State
if "lang" not in st.session_state:
    st.session_state.lang = "English"
if "current_page" not in st.session_state:
    st.session_state.current_page = "Teacher/Parent Dashboard"
if "selected_unit" not in st.session_state:
    st.session_state.selected_unit = 1

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🌟 EFALL Portal")
st.sidebar.caption("Educated Mother Education Nation")
st.sidebar.info("🎯 **Framework:** IB PYP, Inquiry & Design Thinking | **Ages:** 3-4 | **Experience:** 1 Unified Dynamic Engine")

# Language Switcher
lang_choice = st.sidebar.radio(
    "Language / زبان", 
    ["English", "اردو"], 
    index=0 if st.session_state.lang == "English" else 1
)
st.session_state.lang = lang_choice

st.sidebar.markdown("---")
st.sidebar.subheader("Navigation")

if st.sidebar.button("👩‍🏫 Teacher & Parent Training Hub" if lang_choice == "English" else "👩‍🏫 استاد اور والدین کا پورٹل", use_container_width=True):
    st.session_state.current_page = "Teacher/Parent Dashboard"
if st.sidebar.button("📚 50-Unit Progressive Master Library" if lang_choice == "English" else "📚 تمام 50 یونٹس کی ماسٹر لائبریری", use_container_width=True):
    st.session_state.current_page = "Unit Library"
if st.sidebar.button("👧👦 Synchronized Student View" if lang_choice == "English" else "👧👦 طلباء کا صفحہ", use_container_width=True):
    st.session_state.current_page = "Student View"

# --- 1. MASTER CURRICULUM GENERATOR (50 Units Grounded in IB PYP Themes) ---
def get_unit_curriculum(unit_num):
    pyp_themes = [
        ("Who We Are", "Identity & Self", "Face / چہرہ", "A", "الف", "1", "Standing vertical lines"),
        ("Who We Are", "Emotions & Smiles", "Smile / مسکان", "B", "ب", "2", "Sleeping horizontal lines"),
        ("Who We Are", "Eyes & Vision", "Eyes / آنکھیں", "C", "پ", "3", "Slanting diagonal lines"),
        ("Who We Are", "Heart & Feelings", "Heart / دل", "D", "ت", "4", "Circular and curve loops"),
        ("Who We Are", "Family Bonds", "Family / خاندان", "E", "ٹ", "5", "Zig-zag tactile patterns"),
        ("Who We Are", "Hands & Touch", "Hands / ہاتھ", "F", "ث", "6", "Standing vertical lines"),
        ("Who We Are", "Voice & Sound", "Voice / آواز", "G", "ج", "7", "Sleeping horizontal lines"),
        ("Who We Are", "My Body", "Me / میں", "H", "چ", "8", "Slanting diagonal lines"),
        
        ("Where We Are in Place and Time", "Doorways & Entry", "Door / دروازہ", "I", "ح", "9", "Circular and curve loops"),
        ("Where We Are in Place and Time", "Windows & Light", "Window / کھڑکی", "J", "خ", "10", "Zig-zag tactile patterns"),
        ("Where We Are in Place and Time", "Tables & Classroom", "Table / میز", "K", "د", "11", "Standing vertical lines"),
        ("Where We Are in Place and Time", "Chairs & Seating", "Chair / کرسی", "L", "ڈ", "12", "Sleeping horizontal lines"),
        ("Where We Are in Place and Time", "Floors & Walking", "Floor / فرش", "M", "ذ", "13", "Slanting diagonal lines"),
        ("Where We Are in Place and Time", "Walls & Structure", "Wall / دیوار", "N", "ر", "14", "Circular and curve loops"),
        ("Where We Are in Place and Time", "Mats & Seating", "Mat / چٹائی", "O", "ڑ", "15", "Zig-zag tactile patterns"),
        ("Where We Are in Place and Time", "Beds & Rest", "Bed / بستر", "P", "ز", "16", "Standing vertical lines"),
        
        ("How We Express Ourselves", "Colors & Paint", "Paint / رنگ", "Q", "ژ", "17", "Sleeping horizontal lines"),
        ("How We Express Ourselves", "Brushes & Strokes", "Brush / برش", "R", "س", "18", "Slanting diagonal lines"),
        ("How We Express Ourselves", "Clay & Molding", "Clay / مٹی", "S", "ش", "19", "Circular and curve loops"),
        ("How We Express Ourselves", "Songs & Rhymes", "Song / گیت", "T", "ص", "20", "Zig-zag tactile patterns"),
        ("How We Express Ourselves", "Stories & Tales", "Story / کہانی", "U", "ض", "1", "Standing vertical lines"),
        ("How We Express Ourselves", "Smiles & Joy", "Smile / مسکرانا", "V", "ط", "2", "Sleeping horizontal lines"),
        ("How We Express Ourselves", "Laughter & Fun", "Laugh / ہنسنا", "W", "ظ", "3", "Slanting diagonal lines"),
        ("How We Express Ourselves", "Dance & Movement", "Dance / ناچ", "X", "ع", "4", "Circular and curve loops"),
        ("How We Express Ourselves", "Art & Hues", "Color / رنگ", "Y", "غ", "5", "Zig-zag tactile patterns"),
        
        ("How the World Works", "Water & Rivers", "Water / پانی", "Z", "ف", "6", "Standing vertical lines"),
        ("How the World Works", "Leaves & Foliage", "Leaf / پتا", "A", "ق", "7", "Sleeping horizontal lines"),
        ("How the World Works", "Sunlight & Warmth", "Sun / سورج", "B", "ک", "8", "Slanting diagonal lines"),
        ("How the World Works", "Clouds & Sky", "Cloud / بادل", "C", "گ", "9", "Circular and curve loops"),
        ("How the World Works", "Rain & Showers", "Rain / بارش", "D", "ل", "10", "Zig-zag tactile patterns"),
        ("How the World Works", "Stones & Earth", "Stone / پتھر", "E", "م", "11", "Standing vertical lines"),
        ("How the World Works", "Wind & Breeze", "Wind / ہوا", "F", "ن", "12", "Sleeping horizontal lines"),
        ("How the World Works", "Trees & Timber", "Tree / درخت", "G", "و", "13", "Slanting diagonal lines"),
        
        ("How We Organize Ourselves", "Baskets & Storage", "Basket / ٹوکری", "H", "ہ", "14", "Circular and curve loops"),
        ("How We Organize Ourselves", "Toys & Play", "Toy / کھلونا", "I", "ھ", "15", "Zig-zag tactile patterns"),
        ("How We Organize Ourselves", "Shelves & Books", "Shelf / الماری", "J", "ء", "16", "Standing vertical lines"),
        ("How We Organize Ourselves", "Boxes & Packing", "Box / ڈبہ", "K", "ی", "17", "Sleeping horizontal lines"),
        ("How We Organize Ourselves", "Cleaning & Tidying", "Clean / صاف", "L", "ے", "18", "Slanting diagonal lines"),
        ("How We Organize Ourselves", "Order & Arrangement", "Tidy / درست", "M", "الف", "19", "Circular and curve loops"),
        ("How We Organize Ourselves", "Helping Hands", "Help / مدد", "N", "ب", "20", "Zig-zag tactile patterns"),
        ("How We Organize Ourselves", "Sorting Objects", "Sort / ترتیب", "O", "پ", "1", "Standing vertical lines"),
        
        ("Sharing the Planet", "Seeds & Planting", "Seed / بیج", "P", "ت", "2", "Sleeping horizontal lines"),
        ("Sharing the Planet", "Soil & Ground", "Soil / مٹی", "Q", "ٹ", "3", "Slanting diagonal lines"),
        ("Sharing the Planet", "Growing Plants", "Plant / پودا", "R", "ث", "4", "Circular and curve loops"),
        ("Sharing the Planet", "Flowers & Blossoms", "Flower / پھول", "S", "ج", "5", "Zig-zag tactile patterns"),
        ("Sharing the Planet", "Birds & Feathers", "Bird / پرندہ", "T", "چ", "6", "Standing vertical lines"),
        ("Sharing the Planet", "Cats & Paws", "Cat / بلی", "U", "ح", "7", "Sleeping horizontal lines"),
        ("Sharing the Planet", "Dogs & Canines", "Dog / کتا", "V", "خ", "8", "Slanting diagonal lines"),
        ("Sharing the Planet", "Plant Growth", "Growth / بڑھوتری", "W", "د", "9", "Circular and curve loops"),
        ("Sharing the Planet", "Nature Care", "Care / دیکھ بھال", "X", "ڈ", "10", "Zig-zag tactile patterns")
    ]
    
    pyp_theme, theme_category, vocab, en, ur, math, stroke = pyp_themes[unit_num - 1]
    theme_name = f"Unit {unit_num} [{pyp_theme}]: {theme_category}"
    skill_stage = f"Inquiry & Design Thinking for {vocab}"
    return theme_name, skill_stage, en, ur, int(math), stroke, vocab, pyp_theme

def create_download_button(content, filename, label):
    b64 = base64.b64encode(content.encode('utf-8')).decode('utf-8')
    return f'<a href="data:text/plain;charset=utf-8;base64,{b64}" download="{filename}" style="text-decoration:none;"><div style="background:#2e7d32;color:white;padding:10px;text-align:center;border-radius:6px;font-weight:bold;margin-top:5px;">📥 {label}</div></a>'


# --- MAIN INTERFACE VIEWS ---
if st.session_state.current_page == "Teacher/Parent Dashboard":
    if st.session_state.lang == "English":
        st.title("👩‍🏫 EFALL Teacher & Parent Training Hub")
        st.write("Welcome to your unified dynamic curriculum portal. Select a theme box below to launch the complete multi-engine learning experience.")
        
        st.markdown("---")
        st.subheader("📦 Explore Curriculum by 6 Progressive IB PYP Theme Boxes")
        
        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.markdown("### 🧩 Box 1: Who We Are (Units 1-8)")
                if st.button("Open Box 1 (Units 1-8)", key="box1"):
                    st.session_state.selected_unit = 1
                    st.session_state.current_page = "Unit Library"
                    st.rerun()
            with st.container(border=True):
                st.markdown("### 🏡 Box 2: Where We Are in Place and Time (Units 9-16)")
                if st.button("Open Box 2 (Units 9-16)", key="box2"):
                    st.session_state.selected_unit = 9
                    st.session_state.current_page = "Unit Library"
                    st.rerun()
            with st.container(border=True):
                st.markdown("### 🎨 Box 3: How We Express Ourselves (Units 17-25)")
                if st.button("Open Box 3 (Units 17-25)", key="box3"):
                    st.session_state.selected_unit = 17
                    st.session_state.current_page = "Unit Library"
                    st.rerun()
        with col2:
            with st.container(border=True):
                st.markdown("### 💧 Box 4: How the World Works (Units 26-33)")
                if st.button("Open Box 4 (Units 26-33)", key="box4"):
                    st.session_state.selected_unit = 26
                    st.session_state.current_page = "Unit Library"
                    st.rerun()
            with st.container(border=True):
                st.markdown("### 🧹 Box 5: How We Organize Ourselves (Units 34-41)")
                if st.button("Open Box 5 (Units 34-41)", key="box5"):
                    st.session_state.selected_unit = 34
                    st.session_state.current_page = "Unit Library"
                    st.rerun()
            with st.container(border=True):
                st.markdown("### 🌿 Box 6: Sharing the Planet (Units 42-50)")
                if st.button("Open Box 6 (Units 42-50)", key="box6"):
                    st.session_state.selected_unit = 42
                    st.session_state.current_page = "Unit Library"
                    st.rerun()
    else:
        st.title("👩‍🏫 استاد اور والدین کا پورٹل")
        if st.button("تمام یونٹس کی لائبریری کھولیں", use_container_width=True):
            st.session_state.current_page = "Unit Library"
            st.rerun()

elif st.session_state.current_page == "Unit Library":
    if st.session_state.lang == "English":
        st.subheader("📚 Ages 3-4: Unified Dynamic Learning Experience")
        st.write("Each unit seamlessly synthesizes your Lesson Plan, Activity Guide, Intelligent GIF, Visual/Video Creators, Worksheet Layout, and PDF Export into one synchronized flow.")
        
        if st.button("⬅️ Back to Theme Boxes Dashboard"):
            st.session_state.current_page = "Teacher/Parent Dashboard"
            st.rerun()

        unit_number = st.selectbox("Select Unit Number (1 to 50):", list(range(1, 51)), index=st.session_state.selected_unit - 1, format_func=lambda x: f"Unit {x}: {get_unit_curriculum(x)[0]}")
        
        theme_name, skill_stage, en_focus, ur_focus, math_focus, stroke_focus, vocab_theme, pyp_theme = get_unit_curriculum(unit_number)

        st.markdown(f"---")
        
        # --- UNIFIED EXPERIENCE HEADER ---
        st.markdown(f"# 📋 Unified Dynamic Curriculum: {theme_name}")
        st.success(f"🌐 **PYP Theme:** {pyp_theme} &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Inquiry Focus:** {vocab_theme}")
        st.warning(f"🔤 **Dual Phonics:** English **'{en_focus}'** & Urdu **'{ur_focus}'** &nbsp;&nbsp;|&nbsp;&nbsp; 🔢 **Math Numeral:** **{math_focus}** &nbsp;&nbsp;|&nbsp;&nbsp; ✍️ **Stroke:** {stroke_focus}")

        # --- SINGLE FLUID EXPERIENCE DISPLAY ---
        st.markdown("---")
        st.markdown("## 🌟 1. Dynamic Lesson Plan & Inquiry Flow")
        lesson_text = f"""[PHASE 1: PROVOCATION & EMPATHY (Harvard Project Zero 'See, Think, Wonder')]
- Gather children on floor mats. Present **{vocab_theme}**.
- Script: "Look closely at **{vocab_theme}**. What do you notice?"

[PHASE 2: DESIGN THINKING IDEATION & TACTILE TRACING]
- Model motion in salt tray: **{stroke_focus}**.
- Script: "Dip your index finger and slide across the sand with me!"

[PHASE 3: DUAL AURAL PHONICS & SOUND CHANTS]
- Recite English **'{en_focus}'** and Urdu **'{ur_focus}'**. Clap **{math_focus}** times.

[PHASE 4: PROTOTYPE & COGNITIVE LOGIC]
- Form letters with playdough and sort items related to **{vocab_theme}**.

[PHASE 5: REFLECTION & CELEBRATION]
- High-fives all around for completing Unit {unit_number}!"""
        
        with st.container(border=True):
            st.markdown(lesson_text)

        st.markdown("---")
        st.markdown("## 🌟 2. Intelligent GIF Animation & Visual Guides")
        col_g1, col_g2 = st.columns(2)
        with col_g1:
            st.markdown(f"""
            <div style="border: 2px dashed #ff9800; padding: 15px; border-radius: 8px; background: #fff8e1; text-align: center;">
                <h4 style="color: #e65100; margin: 0 0 5px 0;">🎬 Dynamic GIF Animation Engine</h4>
                <p style="font-size: 13px; color: #333;">Tracing <b>{vocab_theme}</b> using <em>{stroke_focus}</em></p>
                <div style="font-size: 20px; font-weight: bold; color: #d84315; margin: 10px 0; padding: 8px; background: #fff; border-radius: 6px;">
                    👉 [ ✍️ <b>{en_char := en_focus}</b> & <b>{ur_char := ur_focus}</b> via {stroke_focus} ] 👈
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col_g2:
            st.markdown(f"""
            <div style="border: 2px dashed #2196f3; padding: 15px; border-radius: 8px; background: #e3f2fd; text-align: center;">
                <h4 style="color: #0d47a1; margin: 0 0 5px 0;">🖼️ & 🎬 Visual & Video Engine Prompts</h4>
                <p style="font-size: 13px; color: #333;"><b>Anchor Image:</b> High-contrast vector of {vocab_theme}</p>
                <p style="font-size: 13px; color: #333;"><b>Storyboard Video:</b> 50-sec classroom walkthrough</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("## 🌟 3. Intelligent Worksheet Layout & Live Preview")
        worksheet_html = f"""
        <div style="border: 3px solid #2e7d32; padding: 20px; border-radius: 10px; background-color: #fafafa; font-family: monospace; color: #000;">
            <h3 style="text-align: center; color: #2e7d32; margin-top: 0;">★ EFALL UNIFIED DYNAMIC WORKSHEET ★</h3>
            <hr style="border: 1px dashed #2e7d32;">
            <p><b>UNIT {unit_number} [{pyp_theme}]:</b> {theme_name}</p>
            <p><b>TOPIC:</b> {vocab_theme} &nbsp;&nbsp;|&nbsp;&nbsp; <b>DATE:</b> _______________</p>
            <br>
            <div style="border: 2px dashed #666; padding: 15px; background: #fff; text-align: center; border-radius: 6px;">
                <span style="font-size: 18px; font-weight: bold;">[ TARGET VISUAL: {vocab_theme} ]</span><br><br>
                <span style="font-size: 14px;">Bilingual Phonics: English <b>'{en_focus}'</b> &nbsp;⚡&nbsp; Urdu <b>'{ur_focus}'</b></span>
            </div>
            <br>
            <p><b>TACTILE STROKE PRACTICE ({stroke_focus}):</b></p>
            <div style="background: #eee; padding: 8px; border-radius: 4px; text-align: center; letter-spacing: 3px;">
                Start ➔ . . . . . {stroke_focus} . . . . . ➔ End
            </div>
            <br>
            <p><b>NUMERACY COUNT ({math_focus}):</b> ⭐ (Target: {math_focus})</p>
            <div style="float: right; border: 2px solid #333; padding: 6px 12px; text-align: center; background: #fff;">
                <b>Teacher Stamp</b><br>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]
            </div>
            <div style="clear: both;"></div>
        </div>
        """
        st.markdown(worksheet_html, unsafe_allow_html=True)
        
        raw_ws_text = f"""======================================================================
EFALL UNIFIED WORKSHEET: UNIT {unit_number} [{pyp_theme}]
THEME: {theme_name} | TOPIC: {vocab_theme}
DUAL PHONICS: English '{en_focus}' & Urdu '{ur_focus}' | NUMERAL: {math_focus}
----------------------------------------------------------------------
[VISUAL BLOCK]: {vocab_theme}
[TRACING TRACK]: Start ➔ . . . . {stroke_focus} . . . . ➔ End
[NUMERACY]: Target Count = {math_focus}
Teacher Stamp Box: [      ]                 Score: ________
======================================================================
"""

        st.markdown("---")
        st.markdown("## 🌟 4. PDF Export Engine Package")
        pdf_package = f"""======================================================================
EFALL UNIFIED DYNAMIC CURRICULUM PACKAGE - UNIT {unit_number}
PYP Transdisciplinary Theme: {pyp_theme}
======================================================================

{lesson_text}

----------------------------------------------------------------------
WORKSHEET SPECIFICATION:
----------------------------------------------------------------------
{raw_ws_text}

======================================================================
Certified for IB PYP Early Years Education (Ages 3-4)
======================================================================
"""
        col_dl1, col_dl2 = st.columns(2)
        with col_dl1:
            st.markdown(create_download_button(pdf_package, f"Unit_{unit_number}_Unified_Lesson.txt", "Download Text Format"), unsafe_allow_html=True)
        with col_dl2:
            st.markdown(create_download_button(pdf_package, f"Unit_{unit_number}_Unified_Package.pdf", "Download PDF Package"), unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("## 💬 Assessment & Reflection")
        st.radio("Observation Result:", ["Fully Engaged", "Needed Guidance", "Needs More Practice"], key=f"assess_{unit_number}")
        st.text_area("Teacher Reflection Notes:", key=f"fb_{unit_number}")

    else:
        st.subheader("📚 تمام 50 یونٹس اور اسباق")
        if st.button("⬅️ ڈیش بورڈ پر واپس جائیں"):
            st.session_state.current_page = "Teacher/Parent Dashboard"
            st.rerun()

elif st.session_state.current_page == "Student View":
    if st.session_state.lang == "English":
        st.subheader("👧👦 Synchronized Student Portal (Ages 3-4)")
        st.write("Child-friendly bilingual activities synced with active units.")
    else:
        st.subheader("👧👦 طلباء کا صفحہ (عمر 3-4 سال)")
        st.write("بچوں کے لیے دو لسانی تفریحی سرگرمیاں۔")
