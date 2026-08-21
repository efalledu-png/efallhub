import streamlit as st

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
st.sidebar.caption("Educated Mother Education Nation (Pakistan)")
st.sidebar.info("🎯 **Active Target Group:** Ages 3-4 | **Learning Styles:** Visual 👁️ | Aural 👂 | Kinesthetic ✋")

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

# --- CURRICULUM MAPPING (LEGAL COMPLIANCE + MULTI-SENSORY MAPPING) ---
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
        "Standing lines (Vertical strokes in salt/flour tray 🖐️)",
        "Sleeping lines (Horizontal motions 🛋️)",
        "Slanting lines (Diagonal arm-swings & finger traces ↗️)",
        "Circular and curve motions (Loops in air and playdough ⭕)",
        "Zig-zag tactile touch-and-trace patterns ⚡"
    ]
    
    idx = (unit_num - 1) % len(letters_en)
    en_focus = letters_en[idx]
    ur_focus = letters_ur[idx]
    math_focus = (unit_num % 20) + 1  
    stroke_focus = pre_writing_strokes[(unit_num - 1) % len(pre_writing_strokes)]

    return theme_name, theme_desc, en_focus, ur_focus, math_focus, stroke_focus

# --- MAIN VIEWS ---
if st.session_state.current_page == "Teacher/Parent Dashboard":
    if st.session_state.lang == "English":
        st.title("👩‍🏫 Teacher & Parent Multi-Sensory Training Hub")
        st.write("Welcome! This portal trains adults to deliver lessons using **Visual 👁️, Aural 👂, and Kinesthetic ✋** multi-sensory techniques designed for small spaces with minimal furniture.")
        
        st.info("💡 **Interactive Guide:** Select any of the 6 Theme Boxes below to access 50 progressive units packed with pictorial guides, video links, and tactile activities.")
        
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
        st.write("خوش آمدید! نیچے 6 فریم بکسز میں تمام 50 یونٹس بصری (Visual)، سمعی (Aural) اور حرکی (Kinesthetic) طریقوں کے ساتھ موجود ہیں۔")
        if st.button("تمام یونٹس کی لائبریری کھولیں", use_container_width=True):
            st.session_state.current_page = "Unit Library"
            st.rerun()

elif st.session_state.current_page == "Unit Library":
    if st.session_state.lang == "English":
        st.subheader("📚 Ages 3-4: Multi-Sensory Master Library & Sub-Unit Generator")
        st.write("Select a unit below. Each unit contains **5 pictorial sub-units (A, B, C, D, E)** integrated with visual, aural, and kinesthetic learning elements.")
        
        if st.button("⬅️ Back to Theme Boxes Dashboard"):
            st.session_state.current_page = "Teacher/Parent Dashboard"
            st.rerun()

        unit_number = st.selectbox("Select Unit Number (1 to 50):", list(range(1, 51)), index=st.session_state.selected_unit - 1, format_func=lambda x: f"Unit {x}: {get_unit_curriculum(x)[0]}")
        
        theme_name, theme_desc, en_focus, ur_focus, math_focus, stroke_focus = get_unit_curriculum(unit_number)

        st.markdown(f"---")
        st.markdown(f"## 🌟 Unit {unit_number} Multi-Sensory Master Hub")
        st.success(f"**Core Theme:** {theme_name} ({theme_desc})")
        st.info(f"🔤 **Phonics:** English **'{en_focus}'** | Urdu **'{ur_focus}'** &nbsp;&nbsp;|&nbsp;&nbsp; 🔢 **Math:** **{math_focus}** &nbsp;&nbsp;|&nbsp;&nbsp; ✍️ **Pre-Writing:** {stroke_focus}")

        # Sub-Unit Selector (A, B, C, D, E) with Emojis
        sub_unit = st.radio(
            "Select Sub-Unit Phase (Pictorial & Multi-Sensory):",
            [
                "Sub-Unit A: 👁️ Visual Provocation & Picture Hook", 
                "Sub-Unit B: ✋ Kinesthetic Pre-Writing & Fine Motor", 
                "Sub-Unit C: 👂 Aural Phonics & Letter Sounds", 
                "Sub-Unit D: 🔢 Pictorial Numeracy & Counting Action", 
                "Sub-Unit E: 🎨 Creative Art & Sensory Reflection"
            ],
            horizontal=False
        )

        complete_package = f"""
================================================================================
EFALL PORTAL - UNIT {unit_number} ({sub_unit}) MULTI-SENSORY PACKAGE
Theme: {theme_name}
English Phonics: {en_focus} | Urdu Phonics: {ur_focus} | Math Number: {math_focus}
Pre-Writing Stroke: {stroke_focus}
================================================================================

1. MULTI-SENSORY SCRIPT & PAKISTAN-CONTEXT VIDEO SUPPORT
- 👁️ Visual: Showing colorful flashcards for '{en_focus}' and '{ur_focus}'.
- 👂 Aural: Singing local Urdu Alif-Baa phonics rhymes.
- ✋ Kinesthetic: Drawing shapes in salt trays and molding playdough numbers.
- Local Video Resource: Culturally tailored Urdu Alif-Baa phonics and handwriting guide.

2. DETAILED 75-MINUTE TIME-MAPPED LESSON PLAN ({sub_unit})
- Focus: {sub_unit} integrated with {theme_name}.
- Space & Setup: Small floor mat, optimized for small rooms with minimal furniture.

3. PRINT-READY STUDENT WORKSHEETS (VISUAL & TACTILE)
- Worksheet: Targeted practice for {sub_unit} featuring letter '{en_focus}' and number '{math_focus}'.
--------------------------------------------------------------------------------
        """

        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "🎬 1. Script, Videos & Multi-Sensory Cues", 
            "📝 2. Sub-Unit Lesson Plan", 
            "📄 3. Print-Ready Worksheets", 
            "🎨 4. Teaching Aids & Art", 
            "🎮 5. Assessment", 
            "💬 6. Teacher Feedback"
        ])

        with tab1:
            st.markdown(f"### 🎬 Multi-Sensory Script & Learning Support Videos ({sub_unit})")
            
            col_v, col_a, col_k = st.columns(3)
            with col_v:
                st.markdown("#### 👁️ Visual Cue")
                st.write(f"Show picture flashcard of letter **{en_focus}** / **{ur_focus}** and point to **{math_focus}** objects.")
            with col_a:
                st.markdown("#### 👂 Aural Cue")
                st.write(f"Sing aloud: *'Bzz bzz goes the sound, letter **{en_focus}** is all around!'*")
            with col_k:
                st.markdown("#### ✋ Kinesthetic Cue")
                st.write(f"Trace **{stroke_focus}** in the air with big arm motions before touching sand/salt.")

            st.markdown("---")
            st.markdown("#### 📺 Pakistan-Context Educational Support Video")
            st.write("Use this culturally tailored Urdu phonics and handwriting demonstration to support visual and aural learning:")
            st.video("https://www.youtube.com/watch?v=4thRB7x-YtY")
            st.caption("🎥 *Suggested Resource:* Local Urdu Alif-Baa Phonics and Handwriting Practice for Early Learners.")

        with tab2:
            st.markdown(f"### 📝 Detailed 75-Minute Multi-Sensory Lesson Plan for {sub_unit}")
            st.markdown(f"- **Active Phase:** {sub_unit}")
            st.markdown(f"- **Core Integration:** English **{en_focus}**, Urdu **{ur_focus}**, Math **{math_focus}**")
            st.markdown(f"- **Pre-Writing Link:** {stroke_focus}")
            st.markdown("---")
            st.write("Step-by-step guidance designed for small home spaces in Pakistan:")
            st.markdown("⏱️ **[00:00 - 00:15] 👁️ Visual & Sensory Setup:** Displaying pictorial cards and holding household objects.")
            st.markdown(f"⏱️ **[00:15 - 00:45] ✋ Kinesthetic & Aural Action ({sub_unit}):** Finger tracing, chanting letter sounds **{en_focus}** / **{ur_focus}**, and counting **{math_focus}** items.")
            st.markdown("⏱️ **[00:45 - 01:15] 🎨 Creative Wrap-Up:** Playdough molding and calming reflection circle.")

        with tab3:
            st.markdown("### 📄 Print-Ready Visual & Tactile Worksheets")
            st.write("Pictorial worksheets formatted for instant printing or tablet viewing:")
            
            with st.container(border=True):
                st.markdown(f"#### 📄 Worksheet A: ✋ Kinesthetic Stroke Practice")
                st.markdown(f"*Pictorial Instruction: Trace the dotted lines using a thick crayon or finger.*")
                st.info(f"**Stroke Focus:** {stroke_focus} [ 🖍️ ======= (Dotted Practice Lines) ======= ]")

            with st.container(border=True):
                st.markdown(f"#### 📄 Worksheet B: 👁️ & 👂 Phonics Tracing Box")
                st.markdown(f"*Pictorial Instruction: Look at the picture, say the sound, and trace.*")
                st.markdown(f"🔤 English: **{en_focus}** &nbsp;&nbsp;|&nbsp;&nbsp; Urdu: **{ur_focus}** &nbsp;&nbsp; [ 🔤 Tracing Grid ]")

            with st.container(border=True):
                st.markdown(f"#### 📄 Worksheet C: 🔢 Pictorial Math Counting")
                st.markdown(f"*Pictorial Instruction: Count the icons and trace the numeral.*")
                st.markdown(f"🔢 Target Number: **{math_focus}** &nbsp;&nbsp; [ 🔢 Trace: {math_focus} ]")

            st.download_button(
                label=f"📥 Download Complete Multi-Sensory Package ({sub_unit})",
                data=complete_package,
                file_name=f"EFALL_Unit_{unit_number}_SubUnit.txt",
                mime="text/plain",
                use_container_width=True
            )

        with tab4:
            st.markdown("### 🎨 Teaching Aids & Multi-Sensory Art Activity")
            st.markdown(f"- **👁️ Visual & ✋ Kinesthetic Aids:** Shallow salt/flour tray, pictorial flashcards for **{en_focus}** and **{ur_focus}**.")
            st.markdown(f"- **Art Activity:** Rolling playdough snakes to form letter **{en_focus}** and number **{math_focus}**.")

        with tab5:
            st.markdown("### 🎮 Multi-Sensory Observation Checklist")
            st.markdown(f"1. **👁️ Visual:** Did the child recognize the flashcard pictures?")
            st.markdown(f"2. **👂 Aural:** Did they repeat the phonics sound (**{en_focus}** / **{ur_focus}**) aloud?")
            st.markdown(f"3. **✋ Kinesthetic:** Did they actively trace in salt or mold playdough?")
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
