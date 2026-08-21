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
        st.write("Welcome! This portal trains adults to deliver bilingual, inquiry-based lessons using **Visual 👁️, Aural 👂, and Kinesthetic ✋** multi-sensory techniques.")
        
        st.info("💡 **Bilingual 50-Unit Curriculum:** Select any Theme Box below. All units include dual English and Urdu alphabet integration across 5 gamified visual worksheets.")
        
        st.markdown("---")
        st.subheader("📦 Explore Curriculum by 6 Progressive Theme Boxes")
        
        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.markdown("### 🧩 Box 1: Identity & Sound Intro (Units 1-8)")
                st.caption("Focus: Dual Phonics & Numerals 1-3 | انگلش اور اردو آوازیں")
                if st.button("Open Box 1 (Units 1-8)", key="box1"):
                    st.session_state.selected_unit = 1
                    st.session_state.current_page = "Unit Library"
                    st.rerun()

            with st.container(border=True):
                st.markdown("### 🏡 Box 2: Local Environment (Units 9-16)")
                st.caption("Focus: Pre-Writing Stems & Tactile Tracing | لکیریں اور حرکی مشق")
                if st.button("Open Box 2 (Units 9-16)", key="box2"):
                    st.session_state.selected_unit = 9
                    st.session_state.current_page = "Unit Library"
                    st.rerun()

            with st.container(border=True):
                st.markdown("### 🎨 Box 3: Expression & Art (Units 17-25)")
                st.caption("Focus: Early Letter Formation | حروف کی تشکیل")
                if st.button("Open Box 3 (Units 17-25)", key="box3"):
                    st.session_state.selected_unit = 17
                    st.session_state.current_page = "Unit Library"
                    st.rerun()

        with col2:
            with st.container(border=True):
                st.markdown("### 💧 Box 4: Nature & Science (Units 26-33)")
                st.caption("Focus: Slanting & Curves | ترچھی اور گول لکیریں")
                if st.button("Open Box 4 (Units 26-33)", key="box4"):
                    st.session_state.selected_unit = 26
                    st.session_state.current_page = "Unit Library"
                    st.rerun()

            with st.container(border=True):
                st.markdown("### 🧹 Box 5: Home Organization (Units 34-41)")
                st.caption("Focus: Independent Writing | آزادانہ لکھائی")
                if st.button("Open Box 5 (Units 34-41)", key="box5"):
                    st.session_state.selected_unit = 34
                    st.session_state.current_page = "Unit Library"
                    st.rerun()

            with st.container(border=True):
                st.markdown("### 🌿 Box 6: Plants & Sustainability (Units 42-50)")
                st.caption("Focus: Full Bilingual Mastery | مکمل دو لسانی مہارت")
                if st.button("Open Box 6 (Units 42-50)", key="box6"):
                    st.session_state.selected_unit = 42
                    st.session_state.current_page = "Unit Library"
                    st.rerun()

    else:
        st.title("👩‍🏫 ملٹی سنصری استاد اور والدین کا پورٹل")
        st.write("خوش آمدید! تمام 50 یونٹس میں انگریزی اور اردو حروف کی بیک وقت تربیت شامل ہے۔")
        if st.button("تمام یونٹس کی لائبریری کھولیں", use_container_width=True):
            st.session_state.current_page = "Unit Library"
            st.rerun()

elif st.session_state.current_page == "Unit Library":
    if st.session_state.lang == "English":
        st.subheader("📚 Ages 3-4: Bilingual Master Library & Unit Generator")
        st.write("Select any unit below. Every packet includes **5 dual English & Urdu worksheets**, lesson plans, and salt tray guides.")
        
        if st.button("⬅️ Back to Theme Boxes Dashboard"):
            st.session_state.current_page = "Teacher/Parent Dashboard"
            st.rerun()

        unit_number = st.selectbox("Select Unit Number (1 to 50):", list(range(1, 51)), index=st.session_state.selected_unit - 1, format_func=lambda x: f"Unit {x}: {get_unit_curriculum(x)[0]}")
        
        theme_name, skill_stage, en_focus, ur_focus, math_focus, stroke_focus, vocab_theme = get_unit_curriculum(unit_number)

        st.markdown(f"---")
        st.markdown(f"## 🌟 Unit {unit_number} Bilingual Generator Hub")
        st.success(f"**Theme & Stage:** {theme_name}")
        st.info(f"🎯 **Skill Focus:** {skill_stage} | 🔑 **Bilingual Vocabulary:** {vocab_theme}")
        st.warning(f"🔤 **Dual Phonics:** English **'{en_focus}'** & Urdu **'{ur_focus}'** &nbsp;&nbsp;|&nbsp;&nbsp; 🔢 **Math:** **{math_focus}** &nbsp;&nbsp;|&nbsp;&nbsp; ✍️ **Stroke:** {stroke_focus}")

        # Sub-Unit Selector
        sub_unit = st.radio(
            "Select Design Thinking & Inquiry Phase:",
            [
                "Phase 1: 👁️ Empathize & Tune In (Visual Hook)", 
                "Phase 2: ✋ Define & Tactile Probe (Salt Tray & Bilingual Tracing)", 
                "Phase 3: 👂 Ideate & Dual Phonics Chants (English & Urdu)", 
                "Phase 4: 🔢 Prototype & Numeracy (Counting & Worksheets 1-5)", 
                "Phase 5: 🎨 Test & Reflect (Creative Expression & Sharing)"
            ],
            horizontal=False
        )

        # 5 Dual English & Urdu Worksheets Payload
        worksheets_packet_text = f"""
EFALL BILINGUAL EDUCATIONAL PORTAL - 5-PART GAMIFIED WORKSHEET PACKET
UNIT {unit_number}: {theme_name}
--------------------------------------------------------------------------------
BILINGUAL FOCUS: English Letter '{en_focus}' & Urdu Letter '{ur_focus}'
VOCABULARY: {vocab_theme} | NUMERAL: {math_focus} | STROKE: {stroke_focus}
--------------------------------------------------------------------------------

[WORKSHEET 1: 👁️ VISUAL MEMORY & BILINGUAL PICTURE HOOK]
- Objective: Spot and circle the item related to '{vocab_theme}'.
- English Prompt: Find objects starting with '{en_focus}'.
- Urdu Prompt: '{ur_focus}' سے شروع ہونے والی چیز تلاش کریں۔
- Task: Circle the picture card with a thick colored crayon.


[WORKSHEET 2: ✋ TACTILE PRE-WRITING & BILINGUAL FINGER TRACING]
- Objective: Build fine motor control through stroke trace '{stroke_focus}'.
- Trace Area:
  ● ------------------------------------------------------------------------> [FINISH / ختم]
  ● ------------------------------------------------------------------------> [FINISH / ختم]
- Bilingual Note: Trace while saying English '{en_focus}' and Urdu '{ur_focus}' aloud.


[WORKSHEET 3: 👂 AURAL PHONICS & DUAL ALPHABET MATCHING]
- Objective: Connect English sound '{en_focus}' with Urdu sound '{ur_focus}'.
- Visual Boxes: 
  [ English Box: {en_focus} ]  <===>  [ Urdu Box: {ur_focus} ]
- Task: Pronounce both sounds clearly. Clap {math_focus} times for each letter!


[WORKSHEET 4: 🧠 MENTAL LOGIC & BILINGUAL SORTING PUZZLE]
- Objective: Sort items by category matching bilingual vocabulary '{vocab_theme}'.
- Logic Grid: [ English Group ] <---> [ Urdu Group / اردو گروہ ]
- Task: Draw a connecting line between matching pairs.


[WORKSHEET 5: 🎮 GAME-ALIKE COUNTING & NUMERAL FORMATION]
- Objective: Count {math_focus} objects and write numeral {math_focus}.
- Counting Items: (⭐) (⭐) (⭐) ... (Total Target: {math_focus})
- Numeral Box: Trace number [ {math_focus} ] inside the treasure chest box.
--------------------------------------------------------------------------------
Generated exclusively for EFALL Portal. Bilingual Early Learning.
        """

        # Detailed Lesson Plan Payload referencing Worksheet numbers
        lesson_plan_pdf_text = f"""
EFALL BILINGUAL EDUCATIONAL PORTAL - DETAILED DESIGN THINKING LESSON PLAN
UNIT {unit_number}: {theme_name}
--------------------------------------------------------------------------------
BILINGUAL LETTERS: English '{en_focus}' & Urdu '{ur_focus}' | VOCAB: {vocab_theme}
DURATION: 75 Minutes (Optimized for Small Spaces)
--------------------------------------------------------------------------------

[DESIGN THINKING & INQUIRY PHASE BREAKDOWN & WORKSHEET MAPPING]

1. EMPATHIZE & TUNE IN (00:00 - 00:15)
- Action & Worksheet: Deploy **Worksheet 1 (Bilingual Picture Hook)**. Discuss everyday {vocab_theme} items.
- Question: "What do you see that sounds like English '{en_focus}' or Urdu '{ur_focus}'?"

2. DEFINE & TACTILE PROBE (00:15 - 00:30)
- Action & Worksheet: Deploy **Worksheet 2 (Tactile Pre-Writing)** in salt tray. Trace **{stroke_focus}**.
- Question: "How does the salt feel when tracing our bilingual letters?"

3. IDEATE & DUAL PHONICS CHANTS (00:30 - 00:45)
- Action & Worksheet: Deploy **Worksheet 3 (Dual Alphabet Matching)**. Chant English '{en_focus}' and Urdu '{ur_focus}' together.
- Question: "Can you say '{en_focus}' and '{ur_focus}' clearly and clap {math_focus} times?"

4. PROTOTYPE & COGNITIVE LOGIC (00:45 - 01:00)
- Action & Worksheet: Deploy **Worksheet 4 (Logic Puzzle)** and **Worksheet 5 (Counting)**.
- Question: "Let's sort our vocabulary and count {math_focus} items!"

5. TEST & REFLECT (01:00 - 01:15)
- Action: Roll playdough snakes to form both English letter '{en_focus}' and Urdu letter '{ur_focus}'!
--------------------------------------------------------------------------------
        """

        teaching_aids_text = f"""
EFALL BILINGUAL EDUCATIONAL PORTAL - TEACHING AIDS & FLASHCARDS
UNIT {unit_number}: {theme_name}
--------------------------------------------------------------------------------
1. BILINGUAL FLASHCARDS: ENGLISH '{en_focus}' & URDU '{ur_focus}'
+-----------------------------------+     +-----------------------------------+
|                                   |     |                                   |
|       English: {en_focus}                 |     |        Urdu: {ur_focus}           |
|    ({vocab_theme})                |     |     ({vocab_theme})               |
+-----------------------------------+     +-----------------------------------+

2. COUNTING CARDS FOR NUMBER {math_focus}
- Display Grid: {math_focus} dot counters for bilingual touch counting.
--------------------------------------------------------------------------------
        """

        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "🎬 1. AI Training Videos", 
            "📝 2. Design Thinking Lesson Plan", 
            "📄 3. 5-Part Bilingual Worksheets", 
            "✂️ 4. Teaching Aids & Flashcards", 
            "🖐️ 5. AI Salt Tray Animation",
            "💬 6. Assessment & Feedback"
        ])

        with tab1:
            st.markdown(f"### 🎬 EFALL Bilingual AI Training Video — Unit {unit_number}")
            st.write(f"Simulates dual pronunciation guides for English **'{en_focus}'** and Urdu **'{ur_focus}'** (**{vocab_theme}**), alongside tactile hand guidance for **{stroke_focus}**.")
            
            col_vid1, col_vid2 = st.columns(2)
            with col_vid1:
                st.markdown("#### 🎥 1. Bilingual Phonics & Lip Movement Video")
                st.info(f"**Active Frame:** Pronouncing English **'{en_focus}'** and Urdu **'{ur_focus}'** with side-by-side mouth shape guides.")
                with st.container(border=True):
                    st.code(f"""
    +-----------------------------------------------+
    | [BILINGUAL AI VIDEO SYNC - ACTIVE]            |
    | English Phonics: '{en_focus}' | Urdu Sound: '{ur_focus}'|
    | Vocabulary Theme: {vocab_theme}               |
    +-----------------------------------------------+
                    """, language="text")
                st.caption(f"✨ *Unit {unit_number} Bilingual Audio Engine:* Active.")

            with col_vid2:
                st.markdown("#### 🎥 2. Adult Facilitator Masterclass")
                st.info(f"**Active Frame:** Guiding tiny hands through **{stroke_focus}** while teaching both alphabets.")
                with st.container(border=True):
                    st.code(f"""
    +-----------------------------------------------+
    | [FACILITATOR BILINGUAL GUIDE - ACTIVE]        |
    | Compact Space Setup | Dual Alphabet Pacing    |
    +-----------------------------------------------+
                    """, language="text")
                st.caption(f"✨ *Unit {unit_number} Facilitator Guide:* Active.")

        with tab2:
            st.markdown(f"### 📝 Detailed Design Thinking Lesson Plan ({sub_unit})")
            st.write("Download your bilingual lesson plan PDF below, mapped directly to the 5 numbered worksheets.")
            st.markdown(create_download_link(lesson_plan_pdf_text, f"Unit_{unit_number}_Bilingual_Lesson_Plan.pdf", "Download Bilingual Lesson Plan PDF"), unsafe_allow_html=True)
            st.markdown("---")

            col_lp1, col_lp2 = st.columns([2, 1])
            with col_lp1:
                st.markdown("#### ⏱️ 75-Minute Bilingual Sequence & Worksheet Mapping:")
                st.markdown("1. **Empathize & Tune In (00:00 - 00:15):** Deploy **Worksheet 1**. Discuss **{vocab_theme}** in English & Urdu.")
                st.markdown(f"2. **Define & Tactile Probe (00:15 - 00:30):** Deploy **Worksheet 2** in salt tray for **{stroke_focus}**.")
                st.markdown(f"3. **Ideate & Dual Chants (00:30 - 00:45):** Deploy **Worksheet 3**. Chant English **{en_focus}** & Urdu **{ur_focus}**.")
                st.markdown(f"4. **Prototype & Logic (00:45 - 01:00):** Deploy **Worksheets 4 & 5**. Count **{math_focus}** items.")
                st.markdown(f"5. **Test & Reflect (01:00 - 01:15):** Form both letters using playdough.")
            with col_lp2:
                st.markdown("#### 👁️ Side Visual Aids")
                with st.container(border=True):
                    st.markdown(f"**Dual Letters:**")
                    st.code(f" [🔤 {en_focus} & {ur_focus}] ", language="text")
                    st.markdown(f"**Worksheets 1-5:**")
                    st.code(f" [📄 Bilingual Pack] ", language="text")

        with tab3:
            st.markdown("### 📄 5-Part Bilingual Gamified Worksheets")
            st.write(f"Download your complete packet containing all **5 visual, cognitive, and logic worksheets** featuring **both English and Urdu alphabets** for **Unit {unit_number}** below:")
            st.markdown(create_download_link(worksheets_packet_text, f"Unit_{unit_number}_Bilingual_5_Worksheets.pdf", "Download 5-Part Bilingual Worksheets PDF"), unsafe_allow_html=True)

            st.markdown("---")
            with st.container(border=True):
                st.markdown("#### 🔍 Worksheets Overview & Dual Alphabet Sequencing:")
                st.markdown(f"- **Worksheet 1:** 👁️ Visual Memory & Bilingual Picture Hook ({vocab_theme})")
                st.markdown(f"- **Worksheet 2:** ✋ Tactile Pre-Writing Stroke Tracing ({stroke_focus})")
                st.markdown(f"- **Worksheet 3:** 👂 Dual Phonics Matching (English **{en_focus}** & Urdu **{ur_focus}**) ✨")
                st.markdown(f"- **Worksheet 4:** 🧠 Mental Logic & Bilingual Sorting Puzzle")
                st.markdown(f"- **Worksheet 5:** 🎮 Game-Alike Counting & Numeral Formation ({math_focus})")

        with tab4:
            st.markdown("### ✂️ Bilingual Teaching Aids & Flashcards")
            st.write(f"Download printable bilingual flashcards for **Unit {unit_number}**:")
            st.markdown(create_download_link(teaching_aids_text, f"Unit_{unit_number}_Bilingual_Teaching_Aids.pdf", "Download Bilingual Teaching Aids PDF"), unsafe_allow_html=True)

            st.markdown("---")
            with st.container(border=True):
                st.markdown(f"**Bilingual Preview:** English **{en_focus}** and Urdu **{ur_focus}** cards matched with vocabulary **{vocab_theme}**.")

        with tab5:
            st.markdown(f"### 🖐️ AI Salt Tray Hand-Movement Animation (Unit {unit_number})")
            st.write("Simulates finger tracing mechanics for both English and Urdu letter formations:")
            
            with st.container(border=True):
                st.markdown(f"#### 🎥 Bilingual Hand Movement Animation: {stroke_focus}")
                st.code(f"""
      +-------------------------------------------------------+
      |  [BILINGUAL AI HAND MOVEMENT SIMULATION]              |
      |                                                       |
      |     (1) Start Position: [●] Top Left                  |
      |     (2) Finger Motion:  ===> Moving across...         |
      |     (3) Dual Focus:     English '{en_focus}' & Urdu '{ur_focus}'     |
      |                                                       |
      |  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  |
      +-------------------------------------------------------+
                """, language="text")
                st.caption(f"💡 *Facilitator Tip:* Guide the child's index finger through **{stroke_focus}** while pronouncing both **{en_focus}** and **{ur_focus}**.")

        with tab6:
            st.markdown("### 💬 Assessment & Teacher Feedback")
            st.markdown(f"1. **👁️ Visual Engagement:** Did the child engage with Worksheet 1?")
            st.markdown(f"2. **👂 Dual Phonics:** Did they repeat both English **{en_focus}** and Urdu **{ur_focus}** sounds?")
            st.markdown(f"3. **✋ Kinesthetic Motor:** Did they trace **{stroke_focus}** successfully?")
            st.radio("Observation Result:", ["Fully Engaged (Both Languages)", "Needed Gentle Guidance", "Needs More Repetition"], key=f"assess_{unit_number}")
            st.text_area("Adult Reflection Notes:", key=f"fb_{unit_number}")

    else:
        # Urdu Interface Version
        st.subheader("📚 تمام 50 یونٹس اور اردو/انگریزی نصاب")
        st.write("یونٹ کا انتخاب کریں اور دو لسانی اسباق حاصل کریں۔")
        if st.button("⬅️ ڈیش بورڈ پر واپس جائیں"):
            st.session_state.current_page = "Teacher/Parent Dashboard"
            st.rerun()

elif st.session_state.current_page == "Student View":
    if st.session_state.lang == "English":
        st.subheader("👧👦 Synchronized Student Portal (Ages 3-4)")
        st.write("Child-friendly bilingual games and audio prompts synced with active units.")
    else:
        st.subheader("👧👦 طلباء کا صفحہ (عمر 3-4 سال)")
        st.write("بچوں کے لیے دو لسانی تفریحی سرگرمیاں۔")
