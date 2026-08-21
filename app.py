import streamlit as st
import base64

# Page Configuration
st.set_page_config(
    page_title="EFALL Portal | Teacher & Parent Training Hub (Ages 3-4)",
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
st.sidebar.info("🎯 **Target:** Ages 3-4 | **Styles:** Visual 👁️ | Aural 👂 | Kinesthetic ✋")

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
if st.sidebar.button("📚 50-Unit Master Library (6 Themes)" if lang_choice == "English" else "📚 تمام 50 یونٹس کی ماسٹر لائبریری", use_container_width=True):
    st.session_state.current_page = "Unit Library"
if st.sidebar.button("👧👦 Synchronized Student View" if lang_choice == "English" else "👧👦 طلباء کا صفحہ", use_container_width=True):
    st.session_state.current_page = "Student View"

# --- DYNAMIC CURRICULUM MAPPING ---
def get_unit_curriculum(unit_num):
    if unit_num <= 8:
        theme_name = "Identity, Emotions, & Self-Discovery (Units 1-8)"
        theme_desc = "Exploring body parts, basic emotions, and personal traits"
    elif unit_num <= 16:
        theme_name = "Local Environment & Surroundings (Units 9-16)"
        theme_desc = "Exploring home spaces, favorite room objects, and local surroundings"
    elif unit_num <= 25:
        theme_name = "Expression, Art, & Storytelling (Units 17-25)"
        theme_desc = "Sensory sounds, facial expressions, and simple creative storytelling"
    elif unit_num <= 33:
        theme_name = "Nature, Science, & Elements (Units 26-33)"
        theme_desc = "Water play, light/shadows, and natural outdoor elements"
    elif unit_num <= 41:
        theme_name = "Home Organization & Community Helpers (Units 34-41)"
        theme_desc = "Daily toy cleanup routines and helpful family roles"
    else:
        theme_name = "Plants, Animals, & Sustainability (Units 42-50)"
        theme_desc = "Caring for plants, gentle pet care, and natural appreciation"

    letters_en = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    letters_ur = ["الف", "ب", "پ", "ت", "ٹ", "ث", "ج", "چ", "ح", "خ", "د", "ڈ", "ذ", "ر", "ڑ", "ز", "ژ", "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف"]
    pre_writing_strokes = [
        "Standing vertical lines (Salt tray index finger pull down ⬇️)",
        "Sleeping horizontal lines (Salt tray left-to-right slide ➡)",
        "Slanting diagonal lines (Salt tray tilt-trace ↗️)",
        "Circular and curve motions (Salt tray loops 🔄)",
        "Zig-zag tactile patterns (Salt tray zig-zag peaks ⚡)"
    ]
    
    idx = (unit_num - 1) % len(letters_en)
    en_focus = letters_en[idx]
    ur_focus = letters_ur[idx]
    math_focus = (unit_num % 20) + 1  
    stroke_focus = pre_writing_strokes[(unit_num - 1) % len(pre_writing_strokes)]

    return theme_name, theme_desc, en_focus, ur_focus, math_focus, stroke_focus

def create_download_link(content, filename, label):
    b64 = base64.b64encode(content.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="{filename}" style="text-decoration:none;"><div style="background:#ff4b4b;color:white;padding:10px;text-align:center;border-radius:5px;font-weight:bold;margin-top:10px;">📥 {label}</div></a>'

# --- MAIN VIEWS ---
if st.session_state.current_page == "Teacher/Parent Dashboard":
    if st.session_state.lang == "English":
        st.title("👩‍🏫 EFALL Teacher & Parent Multi-Sensory Hub")
        st.write("Welcome! This portal trains adults to deliver lessons using **Visual 👁️, Aural 👂, and Kinesthetic ✋** multi-sensory techniques designed for small spaces with minimal furniture.")
        
        st.info("💡 **Interactive Guide:** Select any of the 6 Theme Boxes below to access 50 progressive units packed with AI-generated pedagogical videos, dynamic visual salt-tray generators, printable worksheets, and teaching aids.")
        
        st.markdown("---")
        st.subheader("📦 Explore Curriculum by 6 Framed Theme Boxes")
        
        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.markdown("### 🧩 Box 1: Identity & Self-Discovery")
                st.caption("Units 1 to 8 | 👁️ Face Mirrors | 👂 Emotion Songs | ✋ Body Tracing")
                if st.button("Open Box 1 (Units 1-8)", key="box1"):
                    st.session_state.selected_unit = 1
                    st.session_state.current_page = "Unit Library"
                    st.rerun()

            with st.container(border=True):
                st.markdown("### 🏡 Box 2: Local Environment")
                st.caption("Units 9 to 16 | 👁️ Room Flashcards | 👂 Sound Walks | ✋ Object Sorting")
                if st.button("Open Box 2 (Units 9-16)", key="box2"):
                    st.session_state.selected_unit = 9
                    st.session_state.current_page = "Unit Library"
                    st.rerun()

            with st.container(border=True):
                st.markdown("### 🎨 Box 3: Expression & Storytelling")
                st.caption("Units 17 to 25 | 👁️ Picture Cards | 👂 Phonics Chants | ✋ Playdough Sculpting")
                if st.button("Open Box 3 (Units 17-25)", key="box3"):
                    st.session_state.selected_unit = 17
                    st.session_state.current_page = "Unit Library"
                    st.rerun()

        with col2:
            with st.container(border=True):
                st.markdown("### 💧 Box 4: Nature & Elements")
                st.caption("Units 26 to 33 | 👁️ Shadow Tracing | 👂 Water Sounds | ✋ Sponge Squeezing")
                if st.button("Open Box 4 (Units 26-33)", key="box4"):
                    st.session_state.selected_unit = 26
                    st.session_state.current_page = "Unit Library"
                    st.rerun()

            with st.container(border=True):
                st.markdown("### 🧹 Box 5: Home Helpers & Cleanup")
                st.caption("Units 34 to 41 | 👁️ Visual Charts | 👂 Cleanup Rhymes | ✋ Toy Sorting")
                if st.button("Open Box 5 (Units 34-41)", key="box5"):
                    st.session_state.selected_unit = 34
                    st.session_state.current_page = "Unit Library"
                    st.rerun()

            with st.container(border=True):
                st.markdown("### 🌿 Box 6: Plants & Sustainability")
                st.caption("Units 42 to 50 | 👁️ Seed Pictures | 👂 Nature Chants | ✋ Soil Planting")
                if st.button("Open Box 6 (Units 42-50)", key="box6"):
                    st.session_state.selected_unit = 42
                    st.session_state.current_page = "Unit Library"
                    st.rerun()

    else:
        st.title("👩‍🏫 ملٹی سنصری استاد اور والدین کا پورٹل")
        st.write("خوش آمدید! نیچے 6 فریم بکسز میں تمام 50 یونٹس بصری، سمعی اور حرکی طریقوں کے ساتھ موجود ہیں۔")
        if st.button("تمام یونٹس کی لائبریری کھولیں", use_container_width=True):
            st.session_state.current_page = "Unit Library"
            st.rerun()

elif st.session_state.current_page == "Unit Library":
    if st.session_state.lang == "English":
        st.subheader("📚 Ages 3-4: Multi-Sensory Master Library & Generator")
        st.write("Select a unit below. Every selection instantly generates linked AI video training, dynamic salt-tray visuals, lesson plans, and print-ready worksheets.")
        
        if st.button("⬅️ Back to Theme Boxes Dashboard"):
            st.session_state.current_page = "Teacher/Parent Dashboard"
            st.rerun()

        unit_number = st.selectbox("Select Unit Number (1 to 50):", list(range(1, 51)), index=st.session_state.selected_unit - 1, format_func=lambda x: f"Unit {x}: {get_unit_curriculum(x)[0]}")
        
        theme_name, theme_desc, en_focus, ur_focus, math_focus, stroke_focus = get_unit_curriculum(unit_number)

        st.markdown(f"---")
        st.markdown(f"## 🌟 Unit {unit_number} Synchronized Generator Hub")
        st.success(f"**Core Theme:** {theme_name} ({theme_desc})")
        st.info(f"🔤 **Phonics:** English **'{en_focus}'** | Urdu **'{ur_focus}'** &nbsp;&nbsp;|&nbsp;&nbsp; 🔢 **Math:** **{math_focus}** &nbsp;&nbsp;|&nbsp;&nbsp; ✍️ **Pre-Writing:** {stroke_focus}")

        # Sub-Unit Selector (A, B, C, D, E)
        sub_unit = st.radio(
            "Select Sub-Unit Phase (Fully Linked Generator):",
            [
                "Sub-Unit A: 👁️ Visual Provocation & Picture Hook", 
                "Sub-Unit B: ✋ Kinesthetic Pre-Writing & Fine Motor", 
                "Sub-Unit C: 👂 Aural Phonics & Letter Sounds", 
                "Sub-Unit D: 🔢 Pictorial Numeracy & Counting Action", 
                "Sub-Unit E: 🎨 Creative Art & Sensory Reflection"
            ],
            horizontal=False
        )

        # Downloadable Content Packets
        worksheet_text = f"""
================================================================================
EFALL PORTAL - UNIT {unit_number} ({sub_unit}) PRINT-READY WORKSHEET
Theme: {theme_name}
Target Phonics: English '{en_focus}' | Urdu '{ur_focus}'
Target Numeral: {math_focus} | Stroke: {stroke_focus}
================================================================================

[WORKSHEET A: PRE-WRITING STROKE PRACTICE]
Instructions: Place finger or thick crayon on the starting dot and trace across.
  ● -----------------------------------------------------> (Trace: {stroke_focus})

[WORKSHEET B: PHONICS TRACING & SOUND BOX]
Instructions: Say the sound '{en_focus}' and '{ur_focus}' aloud. Trace inside the bubble.
  [ English: {en_focus} ]       [ Urdu: {ur_focus} ]

[WORKSHEET C: NUMERAL COUNTING & FORMATION]
Instructions: Count {math_focus} items and trace numeral {math_focus}.
  Items: (⭐) * {math_focus}
  Numeral Box: [ {math_focus} ]
--------------------------------------------------------------------------------
        """

        teaching_aids_text = f"""
================================================================================
EFALL PORTAL - UNIT {unit_number} PRINTABLE TEACHING AIDS & FLASHCARDS
================================================================================

1. FLASHCARD: ENGLISH & URDU SOUNDS ({en_focus} / {ur_focus})
+-------------------+     +-------------------+
|                   |     |                   |
|        {en_focus}         |     |        {ur_focus}         |
|   (Object Visual) |     |   (Object Visual) |
+-------------------+     +-------------------+

2. DYNAMIC SALT TRAY GUIDE FOR UNIT {unit_number}
- Focus Stroke: {stroke_focus}
- Container: Shallow tray with salt/flour. Trace pattern with index finger.

3. COUNTING CARDS FOR NUMBER {math_focus}
- Display: {math_focus} visual dots for toddler touch-counting.
--------------------------------------------------------------------------------
        """

        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "🎬 1. AI Videos & Audio Hub", 
            "📝 2. Lesson Plan", 
            "📄 3. Printable Worksheets", 
            "🎨 4. Visual Salt Tray & Aids", 
            "🎮 5. Assessment", 
            "💬 6. Teacher Feedback"
        ])

        with tab1:
            st.markdown(f"### 🎬 EFALL AI Video Generator — Unit {unit_number} ({sub_unit})")
            st.write(f"Generated specifically for teaching English **'{en_focus}'**, Urdu **'{ur_focus}'**, and **{math_focus}** using lip close-ups and tactile hand guidance.")
            
            col_vid1, col_vid2 = st.columns(2)
            with col_vid1:
                st.markdown("#### 🎥 1. Student Phonics & Sound Animation")
                st.info(f"**Generated Focus:** Animated character pronouncing **'{en_focus}'** and **'{ur_focus}'** with mouth shape guides.")
                st.video("https://www.youtube.com/watch?v=4thRB7x-YtY")
                st.caption(f"✨ *Active Unit Video:* Phonics & sound integration for Unit {unit_number}.")

            with col_vid2:
                st.markdown("#### 🎥 2. Adult Facilitator Masterclass Video")
                st.info(f"**Generated Focus:** Adult step-by-step guidance for **{stroke_focus}** in compact spaces.")
                st.video("https://www.youtube.com/watch?v=hq3yfQnllfQ")
                st.caption(f"✨ *Active Unit Video:* Tactile facilitation guide for Unit {unit_number}.")

        with tab2:
            st.markdown(f"### 📝 Detailed 75-Minute Lesson Plan ({sub_unit})")
            st.markdown(f"- **Active Theme:** {theme_name}")
            st.markdown(f"- **Core Integration:** English **{en_focus}**, Urdu **{ur_focus}**, Math **{math_focus}**")
            st.markdown(f"- **Kinesthetic Link:** {stroke_focus}")
            st.markdown("---")
            st.write("Step-by-step guidance optimized for small home environments:")
            st.markdown("⏱️ **[00:00 - 00:15] 👁️ Visual Provocation:** Displaying flashcards for letters **{en_focus}** & **{ur_focus}**.")
            st.markdown(f"⏱️ **[00:15 - 00:45] ✋ Kinesthetic & Aural Action:** Practicing **{stroke_focus}** and counting **{math_focus}** objects.")
            st.markdown("⏱️ **[00:45 - 01:15] 🎨 Creative Wrap-Up:** Playdough shaping and calming circle.")

        with tab3:
            st.markdown("### 📄 Print-Ready Worksheets & Teaching Aids")
            st.write(f"Instant downloads dynamically generated for **Unit {unit_number}**:")
            
            col_dl1, col_dl2 = st.columns(2)
            with col_dl1:
                st.markdown("#### 📄 Student Worksheet Packet")
                st.markdown(create_download_link(worksheet_text, f"Unit_{unit_number}_Worksheet.txt", "Download Worksheet (TXT/PDF)"), unsafe_allow_html=True)
            with col_dl2:
                st.markdown("#### ✂️ Printable Teaching Aids & Flashcards")
                st.markdown(create_download_link(teaching_aids_text, f"Unit_{unit_number}_TeachingAids.txt", "Download Teaching Aids (TXT/PDF)"), unsafe_allow_html=True)

            st.markdown("---")
            with st.container(border=True):
                st.markdown(f"**Live Worksheet Preview:**")
                st.markdown(f"- ✍️ Stroke: {stroke_focus}")
                st.markdown(f"- 🔤 Phonics: English **{en_focus}** | Urdu **{ur_focus}**")
                st.markdown(f"- 🔢 Numeral: **{math_focus}**")

        with tab4:
            st.markdown(f"### 🎨 Dynamic Visual Salt Tray Generator — Unit {unit_number}")
            st.write("This visual simulator updates automatically for every unit to show adults exactly how to set up tactile pre-writing practice:")
            
            with st.container(border=True):
                st.markdown(f"#### 🖐️ Active Salt Tray Visual Generator (Stroke: {stroke_focus})")
                st.code(f"""
      +-------------------------------------------------------+
      |  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  |
      |  ~ ~ [ TACTILE FOCUS: {stroke_focus.upper()} ] ~ ~  |
      |  ~ ~ ~ ~ ~ ( INDEX FINGER TRACING: ➔ {en_focus} / {ur_focus} ) ~ ~ ~  |
      |  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  |
      +-------------------------------------------------------+
                """, language="text")
                st.caption(f"💡 *Generated Facilitator Note:* Fill a shallow tray with salt/flour. Guide the child's index finger to practice **{stroke_focus}** while saying sound **{en_focus}** / **{ur_focus}**.")

            st.markdown(f"- **Teaching Aids:** Flashcards for **{en_focus}** and **{ur_focus}** linked above.")
            st.markdown(f"- **Art Activity:** Rolling playdough snakes to form letter **{en_focus}** and number **{math_focus}**.")

        with tab5:
            st.markdown("### 🎮 Multi-Sensory Observation Checklist")
            st.markdown(f"1. **👁️ Visual:** Did the child recognize flashcard **{en_focus}** / **{ur_focus}**?")
            st.markdown(f"2. **👂 Aural:** Did they repeat sound **{en_focus}** aloud?")
            st.markdown(f"3. **✋ Kinesthetic:** Did they trace **{stroke_focus}** in the salt tray successfully?")
            st.radio("Observation Result:", ["Fully Engaged (All 3 Senses)", "Needed Gentle Guidance", "Needs More Playful Repetition"], key=f"assess_{unit_number}")

        with tab6:
            st.markdown("### 💬 Adult Reflection & Feedback")
            st.text_area("Notes:", key=f"fb_{unit_number}")

    else:
        # Urdu Interface Version
        st.subheader("📚 تمام 50 یونٹس اور ملٹی سنصری ذیلی یونٹس")
        st.write("یونٹ کا انتخاب کریں اور بصری، سمعی اور حرکی مواد حاصل کریں۔")
        if st.button("⬅️ ڈیش بورڈ پر واپس جائیں"):
            st.session_state.current_page = "Teacher/Parent Dashboard"
            st.rerun()

elif st.session_state.current_page == "Student View":
    if st.session_state.lang == "English":
        st.subheader("👧👦 Synchronized Student Portal (Ages 3-4)")
        st.write("Child-friendly interactive games, audio stories, and visual prompts synced directly with the active Unit generator.")
    else:
        st.subheader("👧👦 طلباء کا صفحہ (عمر 3-4 سال)")
        st.write("بچوں کے لیے تفریحی کہانیاں اور سرگرمیاں۔")
