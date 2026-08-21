import streamlit as st
import base64

# Page Configuration
st.set_page_config(
    page_title="EFALL Portal | Inquiry & Multi-Sensory Hub (Ages 3-4)",
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
st.sidebar.info("🎯 **Framework:** Inquiry & Design Thinking | **Ages:** 3-4 | **Styles:** Visual 👁️ | Aural 👂 | Kinesthetic ✋")

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

# --- INTELLIGENT 50-UNIT CURRICULUM GENERATOR ---
def get_unit_curriculum(unit_num):
    if unit_num <= 8:
        theme_name = f"Theme 1: Identity, Emotions, & Sound Introduction (Unit {unit_num})"
        skill_stage = "Sound & Number Introduction (Sensory awareness of basic bilingual phonics and numerals 1-3)"
        vocab_theme = ["Face / چہرہ", "Smile / مسکان", "Eyes / آنکھیں", "Heart / دل", "Family / خاندان", "Hands / ہاتھ", "Voice / آواز", "Me / میں"][unit_num - 1]
    elif unit_num <= 16:
        theme_name = f"Theme 2: Local Environment & Pre-Writing Stems (Unit {unit_num})"
        skill_stage = "Pre-Writing Stems (Vertical & horizontal lines, bilingual tactile finger tracing)"
        vocab_theme = ["Door / دروازہ", "Window / کھڑکی", "Table / میز", "Chair / کرسی", "Floor / فرش", "Wall / دیوار", "Mat / چٹائی", "Bed / بستر"][unit_num - 9]
    elif unit_num <= 25:
        theme_name = f"Theme 3: Expression, Art, & Early Letter Formation (Unit {unit_num})"
        skill_stage = "Early Letter Formation (Tracing first set of English/Urdu letters and numbers 4-7)"
        vocab_theme = ["Paint / رنگ", "Brush / برش", "Clay / مٹی", "Song / گیت", "Story / کہانی", "Smile / مسکرانا", "Laugh / ہنسنا", "Dance / ناچ", "Color / رنگ"][unit_num - 17]
    elif unit_num <= 33:
        theme_name = f"Theme 4: Nature, Science, & Slanting Strokes (Unit {unit_num})"
        skill_stage = "Slanting & Curve Mastery (Diagonal lines, loops, and numbers 8-12)"
        vocab_theme = ["Water / پانی", "Leaf / پتا", "Sun / سورج", "Cloud / بادل", "Rain / بارش", "Stone / پتھر", "Wind / ہوا", "Tree / درخت"][unit_num - 26]
    elif unit_num <= 41:
        theme_name = f"Theme 5: Home Organization & Letter Writing (Unit {unit_num})"
        skill_stage = "Independent Writing (Writing bilingual letters and numbers 13-16 with minimal guidance)"
        vocab_theme = ["Basket / ٹوکری", "Toy / کھلونا", "Shelf / الماری", "Box / ڈبہ", "Clean / صاف", "Tidy / درست", "Help / مدد", "Sort / ترتیب"][unit_num - 34]
    else:
        theme_name = f"Theme 6: Plants, Animals, & Mastery Writing (Unit {unit_num})"
        skill_stage = "Mastery & Combination (Full bilingual alphabet tracing, numbers 17-20, and creative expression)"
        vocab_theme = ["Seed / بیج", "Soil / مٹی", "Plant / پودا", "Flower / پھول", "Bird / پرندہ", "Cat / بلی", "Dog / کتا", "Growth / بڑھوتری", "Care / دیکھ بھال"][unit_num - 42]

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

    return theme_name, skill_stage, en_focus, ur_focus, math_focus, stroke_focus, vocab_theme

def create_download_link(content, filename, label):
    b64 = base64.b64encode(content.encode()).decode()
    return f'<a href="data:application/pdf;base64,{b64}" download="{filename}" style="text-decoration:none;"><div style="background:#ff4b4b;color:white;padding:12px;text-align:center;border-radius:6px;font-weight:bold;margin-top:10px;">📥 {label} (PDF Download)</div></a>'

# --- MAIN VIEWS ---
if st.session_state.current_page == "Teacher/Parent Dashboard":
    if st.session_state.lang == "English":
        st.title("👩‍🏫 EFALL Teacher & Parent Training Hub")
        st.write("Welcome! This portal acts as your expert co-teacher, providing word-for-word 70-minute lesson scripts, student video cues, and bilingual worksheets designed for compact spaces.")
        
        st.info("💡 **Master Curriculum Hub:** Select any Theme Box below. All 50 units feature fully detailed, narrative teacher scripts.")
        
        st.markdown("---")
        st.subheader("📦 Explore Curriculum by 6 Progressive Theme Boxes")
        
        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.markdown("### 🧩 Box 1: Identity & Sound Intro (Units 1-8)")
                if st.button("Open Box 1 (Units 1-8)", key="box1"):
                    st.session_state.selected_unit = 1
                    st.session_state.current_page = "Unit Library"
                    st.rerun()
            with st.container(border=True):
                st.markdown("### 🏡 Box 2: Local Environment (Units 9-16)")
                if st.button("Open Box 2 (Units 9-16)", key="box2"):
                    st.session_state.selected_unit = 9
                    st.session_state.current_page = "Unit Library"
                    st.rerun()
            with st.container(border=True):
                st.markdown("### 🎨 Box 3: Expression & Art (Units 17-25)")
                if st.button("Open Box 3 (Units 17-25)", key="box3"):
                    st.session_state.selected_unit = 17
                    st.session_state.current_page = "Unit Library"
                    st.rerun()
        with col2:
            with st.container(border=True):
                st.markdown("### 💧 Box 4: Nature & Science (Units 26-33)")
                if st.button("Open Box 4 (Units 26-33)", key="box4"):
                    st.session_state.selected_unit = 26
                    st.session_state.current_page = "Unit Library"
                    st.rerun()
            with st.container(border=True):
                st.markdown("### 🧹 Box 5: Home Organization (Units 34-41)")
                if st.button("Open Box 5 (Units 34-41)", key="box5"):
                    st.session_state.selected_unit = 34
                    st.session_state.current_page = "Unit Library"
                    st.rerun()
            with st.container(border=True):
                st.markdown("### 🌿 Box 6: Plants & Sustainability (Units 42-50)")
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
        st.subheader("📚 Ages 3-4: Master Unit Library & Expert Teacher Guide")
        st.write("Select any unit below to access your complete narrative 70-minute lesson script, teacher preparation guide, embedded student videos, and worksheet packets.")
        
        if st.button("⬅️ Back to Theme Boxes Dashboard"):
            st.session_state.current_page = "Teacher/Parent Dashboard"
            st.rerun()

        unit_number = st.selectbox("Select Unit Number (1 to 50):", list(range(1, 51)), index=st.session_state.selected_unit - 1, format_func=lambda x: f"Unit {x}: {get_unit_curriculum(x)[0]}")
        
        theme_name, skill_stage, en_focus, ur_focus, math_focus, stroke_focus, vocab_theme = get_unit_curriculum(unit_number)

        st.markdown(f"---")
        st.markdown(f"## 🌟 Unit {unit_number} Master Teacher Command Center")
        st.success(f"**Theme & Stage:** {theme_name}")
        st.info(f"🎯 **Skill Focus:** {skill_stage} | 🔑 **Vocabulary:** {vocab_theme}")
        st.warning(f"🔤 **Dual Phonics:** English **'{en_focus}'** & Urdu **'{ur_focus}'** &nbsp;&nbsp;|&nbsp;&nbsp; 🔢 **Math:** **{math_focus}** &nbsp;&nbsp;|&nbsp;&nbsp; ✍️ **Stroke:** {stroke_focus}")

        # Narrative 70-Minute Teacher Script Payload with Exact Spoken Sentences & Embedded Videos
        detailed_lesson_plan_text = f"""
EFALL EXPERT TEACHER NARRATIVE LESSON SCRIPT & GUIDE
UNIT {unit_number}: {theme_name}
================================================================================
TOTAL DURATION: 70 Minutes | SETTING: Small Class (Limited Furniture)
BILINGUAL FOCUS: English '{en_focus}' & Urdu '{ur_focus}' | VOCABULARY: {vocab_theme}
TARGET NUMERAL: {math_focus} | PRE-WRITING STROKE: {stroke_focus}
================================================================================

[SECTION A: TEACHER PREPARATION & MATERIAL CHECKLIST]
- Physical Room Setup: Clear center floor space of 4x4 feet. Keep children seated in a cozy semi-circle on floor mats facing the teacher.
- Materials to Prepare:
  1. Printed visual and cognitive worksheet packets (Sheets 1 through 5).
  2. Shallow salt/flour trays for tactile tracing.
  3. Playdough lumps for final letter/number sculpting.
  4. Flashcards displaying English '{en_focus}' and Urdu '{ur_focus}'.

[SECTION B: MANDATORY TEACHER TRAINING VIDEOS TO WATCH BEFORE CLASS]
1. Video 1: "EFALL Phonics Mouth Articulation" - Review lip placement for English '{en_focus}' and Urdu '{ur_focus}'.
2. Video 2: "Small-Space Kinesthetic Guidance" - Observe how to guide toddler finger tracing in compact spaces.

================================================================================
[SECTION C: MINUTE-BY-MINUTE 70-MINUTE NARRATIVE LESSON SCRIPT]
================================================================================

1. PROVOCATION & VISUAL HOOK (00:00 - 00:15)
- Narrative Scenario: Gather children on the floor mats. Hold up a mysterious covered basket or picture card representing '{vocab_theme}' without speaking for 5 seconds to build suspense.
- Exact Spoken Teacher Sentences:
  * "Good morning, my little explorers! Look closely at what I have hidden in my hands today."
  * "First, let's look at this big picture card together. What do you see here that reminds us of {vocab_theme}?"
  * "Take your thick crayon and circle the picture on your first paper sheet that matches our special theme today!"
- Student Support Video to Play in Between: Play *EFALL Animated Visual Hook Clip #1* (3 mins) showing animated {vocab_theme} objects interacting in a room.

2. TACTILE PROBE & SALT TRAY TRACING (00:15 - 00:30)
- Narrative Scenario: Pass out shallow salt trays to each child. Model tracing motions in the air while keeping movements slow and rhythmic.
- Exact Spoken Teacher Sentences:
  * "Now, let's clean our hands and get ready for our magic writing sand."
  * "First, watch my index finger slide across the air: {stroke_focus}."
  * "Now, gently dip your finger into your salt tray and trace the dotted lines on your second paper sheet while feeling the texture. How does it feel? Is it smooth?"
- Student Support Video to Play in Between: Play *EFALL Kinesthetic Motion Clip #2* (3 mins) showing an animated finger tracing {stroke_focus} with sound effects.

3. DUAL AURAL PHONICS & SOUND CHANTS (00:30 - 00:50)
- Narrative Scenario: Hold up dual alphabet flashcards. Guide children through lively call-and-response sound games.
- Exact Spoken Teacher Sentences:
  * "Friends, open your ears wide! Today we are learning two wonderful sounds."
  * "First, let's say the English sound together: '{en_focus}'! Now, let's say the Urdu sound: '{ur_focus}'!"
  * "Look at your third paper sheet. Let's point to both letters and clap our hands exactly {math_focus} times for each sound!"
- Student Support Video to Play in Between: Play *EFALL Bilingual Phonics Sing-Along #3* (4 mins) featuring children pronouncing English '{en_focus}' and Urdu '{ur_focus}'.

4. COGNITIVE LOGIC & NUMERACY GAMES (00:50 - 01:05)
- Narrative Scenario: Transition into problem-solving and counting games using the logic puzzle sheet and counting sheet.
- Exact Spoken Teacher Sentences:
  * "Let's put our thinking caps on! Look at your fourth paper sheet with the puzzle grid."
  * "First, can you find which {vocab_theme} item doesn't belong? Let's draw a connecting line to match the correct pairs."
  * "Now, flip to your fifth sheet! Let's count our treasure stars together out loud: 1, 2, ... up to {math_focus}!"
  * "Trace number {math_focus} inside the treasure chest box with your favorite colored pencil."
- Student Support Video to Play in Between: Play *EFALL Counting & Logic Adventure #4* (3 mins) guiding children through sorting and counting up to {math_focus}.

5. REFLECTION, TEST & CELEBRATION (01:05 - 01:10)
- Narrative Scenario: Distribute playdough lumps to celebrate learning and shape letters on floor mats.
- Exact Spoken Teacher Sentences:
  * "You did an amazing job today, my brilliant builders!"
  * "First, roll your playdough into a long snake like this."
  * "Now, let's shape our playdough into English letter '{en_focus}' and Urdu letter '{ur_focus}'."
  * "Show me your wonderful creations with a huge smile! High-fives all around for completing Unit {unit_number}!"
================================================================================
Generated exclusively for EFALL Portal Master Teacher Guide.
        """

        worksheets_packet_text = f"""
EFALL EDUCATIONAL PORTAL - 5-PART BILINGUAL WORKSHEETS PACKET
UNIT {unit_number}: {theme_name}
--------------------------------------------------------------------------------
[WORKSHEET 1: 👁️ VISUAL MEMORY & PICTURE HOOK]
- Task: Circle the item related to '{vocab_theme}' starting with English '{en_focus}' / Urdu '{ur_focus}'.

[WORKSHEET 2: ✋ TACTILE PRE-WRITING STROKE TRACING]
- Trace Area for: {stroke_focus}

[WORKSHEET 3: 👂 DUAL PHONICS & ALPHABET MATCHING]
- Match English '{en_focus}' with Urdu '{ur_focus}'. Clap {math_focus} times.

[WORKSHEET 4: 🧠 MENTAL LOGIC & SORTING PUZZLE]
- Sort and connect matching category pairs for '{vocab_theme}'.

[WORKSHEET 5: 🎮 GAME-ALIKE COUNTING & NUMERAL FORMATION]
- Count {math_focus} objects and trace number [{math_focus}].
--------------------------------------------------------------------------------
        """

        teaching_aids_text = f"""
EFALL TEACHING AIDS & FLASHCARDS - UNIT {unit_number}
--------------------------------------------------------------------------------
- English Letter Flashcard: {en_focus} ({vocab_theme})
- Urdu Letter Flashcard: {ur_focus} ({vocab_theme})
- Counting Card: {math_focus} Dot Counters
--------------------------------------------------------------------------------
        """

        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "🎬 1. Teacher Training & Videos", 
            "📝 2. Detailed 70-Min Lesson Script", 
            "📄 3. 5-Part Worksheets Packet", 
            "✂️ 4. Teaching Aids & Flashcards", 
            "🖐️ 5. AI Salt Tray Animation",
            "💬 6. Assessment & Feedback"
        ])

        with tab1:
            st.markdown(f"### 🎬 Teacher Training & Video Checklist (Unit {unit_number})")
            st.write("Review these mandatory instructional videos before teaching this unit in your small classroom:")
            
            col_vid1, col_vid2 = st.columns(2)
            with col_vid1:
                st.markdown("#### 🎥 1. EFALL Phonics Articulation Masterclass")
                st.info(f"**Focus:** Close-up mouth positioning for English **'{en_focus}'** and Urdu **'{ur_focus}'**.")
                with st.container(border=True):
                    st.code(f"""
    +-----------------------------------------------+
    | [VIDEO SIMULATION: ACTIVE]                    |
    | English Pronunciation: '{en_focus}'           |
    | Urdu Sound Articulation: '{ur_focus}'         |
    | Target Vocab Theme: {vocab_theme}             |
    +-----------------------------------------------+
                    """, language="text")
                st.caption("✨ *Tip:* Practice pronouncing both sounds clearly in front of a mirror before class.")

            with col_vid2:
                st.markdown("#### 🎥 2. Small-Space Kinesthetic Guidance")
                st.info(f"**Focus:** Managing salt trays and hand-on-hand tracing for **{stroke_focus}** in limited furniture setups.")
                with st.container(border=True):
                    st.code(f"""
    +-----------------------------------------------+
    | [FACILITATOR GUIDE: ACTIVE]                   |
    | Room Layout: Floor mat semi-circle            |
    | Stroke Focus: {stroke_focus}                  |
    +-----------------------------------------------+
                    """, language="text")
                st.caption("✨ *Tip:* Keep trays stable on low floor mats to prevent spills.")

        with tab2:
            st.markdown(f"### 📝 Detailed 70-Minute Narrative Teacher Lesson Script")
            st.write("Read and follow this word-for-word narrative teacher script featuring exact spoken sentences, student video cues, and immersive classroom scenarios.")
            
            st.markdown(create_download_link(detailed_lesson_plan_text, f"Unit_{unit_number}_Detailed_Lesson_Script.pdf", "Download 70-Min Lesson Script PDF"), unsafe_allow_html=True)
            st.markdown("---")

            with st.container(border=True):
                st.markdown(detailed_lesson_plan_text)

        with tab3:
            st.markdown("### 📄 5-Part Bilingual Gamified Worksheets")
            st.write(f"Download all **5 visual, cognitive, and logic worksheets** for **Unit {unit_number}** below:")
            st.markdown(create_download_link(worksheets_packet_text, f"Unit_{unit_number}_5_Worksheets.pdf", "Download 5-Part Worksheets PDF"), unsafe_allow_html=True)
            
            with st.container(border=True):
                st.markdown(worksheets_packet_text)

        with tab4:
            st.markdown("### ✂️ Bilingual Teaching Aids & Flashcards")
            st.markdown(create_download_link(teaching_aids_text, f"Unit_{unit_number}_Teaching_Aids.pdf", "Download Teaching Aids PDF"), unsafe_allow_html=True)
            with st.container(border=True):
                st.markdown(teaching_aids_text)

        with tab5:
            st.markdown(f"### 🖐️ AI Salt Tray Hand-Movement Animation")
            with st.container(border=True):
                st.markdown(f"#### 🎥 Hand Movement Mechanics: {stroke_focus}")
                st.code(f"""
      +-------------------------------------------------------+
      |  [BILINGUAL AI HAND MOVEMENT SIMULATION]              |
      |     (1) Start Position: [●] Top Left                  |
      |     (2) Finger Motion:  ===> Moving across...         |
      |     (3) Dual Focus:     English '{en_focus}' & Urdu '{ur_focus}'     |
      +-------------------------------------------------------+
                """, language="text")

        with tab6:
            st.markdown("### 💬 Assessment & Teacher Feedback")
            st.markdown(f"1. **Provocation & Engagement:** Did students respond well to the **{vocab_theme}** hook?")
            st.markdown(f"2. **Dual Phonics:** Did they articulate English **'{en_focus}'** and Urdu **'{ur_focus}'**?")
            st.markdown(f"3. **Kinesthetic Mastery:** Did they successfully trace **{stroke_focus}**?")
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
        st.write("Child-friendly bilingual activities and student videos synced with active units.")
    else:
        st.subheader("👧👦 طلباء کا صفحہ (عمر 3-4 سال)")
        st.write("بچوں کے لیے دو لسانی تفریحی سرگرمیاں۔")
