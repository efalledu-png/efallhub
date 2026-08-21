import streamlit as st
import base64

# Page Configuration
st.set_page_config(
    page_title="EFALL Portal | IB PYP & Multi-Sensory Hub (Ages 3-4)",
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
st.sidebar.info("🎯 **Framework:** IB PYP & Inquiry | **Ages:** 3-4 | **Styles:** Visual 👁️ | Aural 👂 | Kinesthetic ✋")

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
        central_idea = "Who We Are: Our bodies, feelings, and personal identities help us connect with others."
    elif unit_num <= 16:
        theme_name = "Local Environment & Surroundings (Units 9-16)"
        central_idea = "Where We Are in Place and Time: Exploring our immediate home spaces and local surroundings."
    elif unit_num <= 25:
        theme_name = "Expression, Art, & Storytelling (Units 17-25)"
        central_idea = "How We Express Ourselves: Using sounds, art, facial expressions, and stories to communicate."
    elif unit_num <= 33:
        theme_name = "Nature, Science, & Elements (Units 26-33)"
        central_idea = "How the World Works: Water play, shadows, and natural outdoor elements around us."
    elif unit_num <= 41:
        theme_name = "Home Organization & Community Helpers (Units 34-41)"
        central_idea = "Sharing the Planet & Communities: Daily routines, toy organization, and family roles."
    else:
        theme_name = "Plants, Animals, & Sustainability (Units 42-50)"
        central_idea = "Sharing the Planet: Caring for growing plants, gentle pet care, and natural appreciation."

    letters_en = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    letters_ur = ["الف", "ب", "پ", "ت", "ٹ", "ث", "ج", "چ", "ح", "خ", "د", "ڈ", "ذ", "ر", "ڑ", "ز", "ژ", "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف"]
    pre_writing_strokes = [
        "Standing vertical lines (Pulling down from top to bottom ⬇️)",
        "Sleeping horizontal lines (Sliding smoothly from left to right ➡)",
        "Slanting diagonal lines (Tilting across from corner to corner ↗️)",
        "Circular and curve loops (Drawing smooth round shapes 🔄)",
        "Zig-zag tactile patterns (Sharply alternating peaks and valleys ⚡)"
    ]
    
    idx = (unit_num - 1) % len(letters_en)
    en_focus = letters_en[idx]
    ur_focus = letters_ur[idx]
    math_focus = (unit_num % 20) + 1  
    stroke_focus = pre_writing_strokes[(unit_num - 1) % len(pre_writing_strokes)]

    return theme_name, central_idea, en_focus, ur_focus, math_focus, stroke_focus

def create_download_link(content, filename, label):
    b64 = base64.b64encode(content.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="{filename}" style="text-decoration:none;"><div style="background:#ff4b4b;color:white;padding:10px;text-align:center;border-radius:5px;font-weight:bold;margin-top:10px;">📥 {label}</div></a>'

# --- MAIN VIEWS ---
if st.session_state.current_page == "Teacher/Parent Dashboard":
    if st.session_state.lang == "English":
        st.title("👩‍🏫 EFALL Teacher & Parent IB PYP Hub")
        st.write("Welcome! This portal trains adults to deliver inquiry-based lessons using **Visual 👁️, Aural 👂, and Kinesthetic ✋** multi-sensory techniques designed for small spaces with minimal furniture.")
        
        st.info("💡 **Interactive Guide:** Select any of the 6 Theme Boxes below to access 50 progressive units packed with EFALL training videos, detailed IB lesson plans, worksheets, and teaching aids.")
        
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
        st.subheader("📚 Ages 3-4: IB PYP Master Library & Generator")
        st.write("Select a unit below. Every unit generates linked AI training videos, inquiry-based lesson plans with sequential steps, rich worksheets, teaching aids, and salt tray guides.")
        
        if st.button("⬅️ Back to Theme Boxes Dashboard"):
            st.session_state.current_page = "Teacher/Parent Dashboard"
            st.rerun()

        unit_number = st.selectbox("Select Unit Number (1 to 50):", list(range(1, 51)), index=st.session_state.selected_unit - 1, format_func=lambda x: f"Unit {x}: {get_unit_curriculum(x)[0]}")
        
        theme_name, central_idea, en_focus, ur_focus, math_focus, stroke_focus = get_unit_curriculum(unit_number)

        st.markdown(f"---")
        st.markdown(f"## 🌟 Unit {unit_number} Synchronized Generator Hub")
        st.success(f"**Core Theme:** {theme_name}")
        st.info(f"💡 **IB Central Idea:** {central_idea}")
        st.warning(f"🔤 **Phonics Focus:** English **'{en_focus}'** | Urdu **'{ur_focus}'** &nbsp;&nbsp;|&nbsp;&nbsp; 🔢 **Math:** **{math_focus}** &nbsp;&nbsp;|&nbsp;&nbsp; ✍️ **Pre-Writing Stroke:** {stroke_focus}")

        # Sub-Unit Selector (A, B, C, D, E)
        sub_unit = st.radio(
            "Select Sub-Unit Inquiry Phase:",
            [
                "Sub-Unit A: 👁️ Tune In (Visual Provocation & Hook)", 
                "Sub-Unit B: ✋ Find Out (Tactile & Pre-Writing Investigation)", 
                "Sub-Unit C: 👂 Sorting Out (Aural Phonics & Sound Chants)", 
                "Sub-Unit D: 🔢 Going Further (Numeracy & Counting Action)", 
                "Sub-Unit E: 🎨 Reflect & Act (Creative Art & Sharing)"
            ],
            horizontal=False
        )

        # Detailed Downloadable Worksheet Text Payload
        worksheet_text = f"""
================================================================================
EFALL PORTAL - UNIT {unit_number} ({sub_unit}) PRINT-READY WORKSHEET
Theme: {theme_name}
Central Idea: {central_idea}
Target Phonics: English '{en_focus}' | Urdu '{ur_focus}'
Target Numeral: {math_focus} | Pre-Writing Stroke: {stroke_focus}
================================================================================

[ACTIVITY 1: PRE-WRITING STROKE TRACING]
Instructions for Adult/Teacher:
1. Place child's finger on the starting dot (●).
2. Guide them to trace the stroke smoothly: {stroke_focus}.
3. Ask child to say the sound while tracing.

Trace Area:
  ● -----------------------------------------------------> [ Finish ]
  ● -----------------------------------------------------> [ Finish ]


[ACTIVITY 2: PHONICS LETTER & SOUND RECOGNITION]
Instructions: Point to the English and Urdu letters. Sound them out together.
  English Focus: [ {en_focus} ]           Urdu Focus: [ {ur_focus} ]
  
  [ ] Color the circle if you can find an object starting with '{en_focus}' in your room.
  [ ] Trace inside the letter bubble with a thick colored crayon.


[ACTIVITY 3: NUMERACY & COUNTING PRACTICE]
Instructions: Count the items aloud together. Trace numeral {math_focus}.
  Target Number: {math_focus}
  Visual Items: (⭐) (⭐) (⭐) ... (Total: {math_focus})
  
  Trace Numeral Box: [ {math_focus} ]
================================================================================
        """

        # Detailed Downloadable Teaching Aids Text Payload
        teaching_aids_text = f"""
================================================================================
EFALL PORTAL - UNIT {unit_number} PRINTABLE TEACHING AIDS & FLASHCARDS
================================================================================

1. FLASHCARDS: ENGLISH '{en_focus}' & URDU '{ur_focus}'
+-----------------------------------+     +-----------------------------------+
|                                   |     |                                   |
|               {en_focus}                  |     |               {ur_focus}                  |
|    (Object: Everyday Local Item)  |     |    (Object: Everyday Local Item)  |
+-----------------------------------+     +-----------------------------------+

2. COUNTING CARDS FOR NUMBER {math_focus}
- Display Grid: {math_focus} dot counters for toddler finger-touch counting.
- Prompt: "Let's touch and count {math_focus} fingers together!"

3. TACTILE VOCABULARY WORD STRIP
- Keyword 1: {en_focus} sound object card
- Keyword 2: {ur_focus} sound object card
--------------------------------------------------------------------------------
        """

        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "🎬 1. AI Videos & Training Hub", 
            "📝 2. IB Inquiry Lesson Plan", 
            "📄 3. Printable Worksheets", 
            "✂️ 4. Teaching Aids & Flashcards", 
            "🖐️ 5. Visual Salt Tray Guide",
            "💬 6. Assessment & Feedback"
        ])

        with tab1:
            st.markdown(f"### 🎬 EFALL Video Generator — Unit {unit_number} ({sub_unit})")
            st.info("📌 *Note on Videos:* EFALL exclusive animated training videos are currently provisioned using compatible high-quality educational references while native exclusive asset rendering builds out.")
            
            col_vid1, col_vid2 = st.columns(2)
            with col_vid1:
                st.markdown("#### 🎥 1. EFALL Exclusive Student Phonics & Lip Movement Video")
                st.write(f"Simulates animated character mouth/lip shaping for English **'{en_focus}'** and Urdu **'{ur_focus}'**.")
                st.video("https://www.youtube.com/watch?v=4thRB7x-YtY")
                st.caption(f"✨ *Active Module:* Phonics pronunciation close-up for Unit {unit_number}.")

            with col_vid2:
                st.markdown("#### 🎥 2. Adult Facilitator Masterclass Video")
                st.write(f"Demonstrates how adults should guide tiny hands through **{stroke_focus}** in small spaces.")
                st.video("https://www.youtube.com/watch?v=hq3yfQnllfQ")
                st.caption(f"✨ *Active Module:* Tactile guidance & room setup for Unit {unit_number}.")

        with tab2:
            st.markdown(f"### 📝 Detailed 75-Minute IB PYP Inquiry Lesson Plan ({sub_unit})")
            st.markdown(f"- **Central Idea:** {central_idea}")
            st.markdown(f"- **Design Thinking & Inquiry Focus:** {sub_unit}")
            st.markdown("---")
            
            st.markdown("#### ⏱️ Step-by-Step Sequence & Flow:")
            st.markdown("1. **First (00:00 - 00:15):** 👁️ **Worksheet Activity (Tune In):** Introduce the unit theme using the printable worksheet picture hook. Do not write yet; just talk about what is seen.")
            st.markdown(f"2. **Second (00:15 - 00:45):** ✋ **Kinesthetic Practice (Find Out & Sorting Out):** Transition to the tactile salt tray to practice **{stroke_focus}** and review phonics letters **{en_focus}** / **{ur_focus}**.")
            st.markdown(f"3. **Third (00:45 - 01:15):** 🔢 **Application & Reflection (Going Further):** Count **{math_focus}** objects using teaching aids and complete the playdough shaping.")

            st.markdown("---")
            st.markdown("#### 🗣️ Essential Socratic Questions to Ask Students:")
            st.markdown(f"- *\"What do you notice about the letter shape **{en_focus}**?\"*")
            st.markdown(f"- *\"Can you find anything around our small room that sounds like **{ur_focus}**?\"*")
            st.markdown(f"- *\"How does your finger feel when tracing in the salt tray?\"*")

            st.markdown("---")
            st.markdown("#### ✅ Formative Learning Check (How to Check Progress):")
            st.markdown("- Observe if the child tracks the stroke from top-to-bottom or left-to-right independently.")
            st.markdown("- Listen to whether the child attempts to produce the phonetic sound when shown the flashcard.")

        with tab3:
            st.markdown("### 📄 Print-Ready Worksheets")
            st.write(f"Download your complete, structured student worksheet for **Unit {unit_number}** below:")
            st.markdown(create_download_link(worksheet_text, f"Unit_{unit_number}_Student_Worksheet.txt", "Download Student Worksheet (PDF/TXT)"), unsafe_allow_html=True)

            st.markdown("---")
            with st.container(border=True):
                st.markdown("#### 🔍 Live Worksheet Content Preview:")
                st.markdown(f"- **Pre-Writing Stroke:** {stroke_focus}")
                st.markdown(f"- **Phonics Focus:** English **{en_focus}** | Urdu **{ur_focus}**")
                st.markdown(f"- **Numeracy Count:** {math_focus} items")

        with tab4:
            st.markdown("### ✂️ Printable Teaching Aids & Flashcards")
            st.write(f"Download printable flashcards and counting aids specifically matched to **Unit {unit_number}**:")
            st.markdown(create_download_link(teaching_aids_text, f"Unit_{unit_number}_Teaching_Aids.txt", "Download Teaching Aids & Flashcards (PDF/TXT)"), unsafe_allow_html=True)

            st.markdown("---")
            with st.container(border=True):
                st.markdown("#### 📌 Teaching Aid Preview:")
                st.markdown(f"- **Flashcard Set:** English **{en_focus}** & Urdu **{ur_focus}** letter cards.")
                st.markdown(f"- **Counting Aid:** Number **{math_focus}** dot grid card.")

        with tab5:
            st.markdown(f"### 🖐️ Visual Salt Tray Demonstration Guide (Unit {unit_number})")
            st.write("The salt tray is a tactile pre-writing reference tool. Use this visual guide to set up a small tray in your limited classroom/home space:")
            
            with st.container(border=True):
                st.markdown(f"#### Tactile Setup for: {stroke_focus}")
                st.code(f"""
      +-------------------------------------------------------+
      |  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  |
      |  ~ ~ [ TACTILE TRAY: {stroke_focus.upper()} ] ~ ~  |
      |  ~ ~ ~ ~ ~ ( INDEX FINGER TRACE: ➔ {en_focus} / {ur_focus} ) ~ ~ ~  |
      |  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  |
      +-------------------------------------------------------+
                """, language="text")
                st.caption(f"💡 *Adult Facilitation Tip:* Fill a shallow container with 1/2 inch of table salt or flour. Guide the child's index finger to practice **{stroke_focus}** while producing the sound **{en_focus}** / **{ur_focus}**.")

        with tab6:
            st.markdown("### 💬 Assessment & Teacher Feedback")
            st.markdown(f"1. **👁️ Visual Inquiry:** Did the child engage with the picture hook?")
            st.markdown(f"2. **👂 Aural Phonics:** Did they repeat sound **{en_focus}** / **{ur_focus}**?")
            st.markdown(f"3. **✋ Kinesthetic Motor:** Did they trace **{stroke_focus}** smoothly?")
            st.radio("Observation Result:", ["Fully Engaged (All 3 Senses)", "Needed Gentle Guidance", "Needs More Playful Repetition"], key=f"assess_{unit_number}")
            st.text_area("Adult Reflection Notes:", key=f"fb_{unit_number}")

    else:
        # Urdu Interface Version
        st.subheader("📚 تمام 50 یونٹس اور آئی بی پی وائی پی نصاب")
        st.write("یونٹ کا انتخاب کریں اور تفصیلی اسباق حاصل کریں۔")
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
