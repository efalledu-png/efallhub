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

# --- UNIQUE 50-UNIT CURRICULUM GENERATOR ---
def get_unit_curriculum(unit_num):
    themes = [
        ("Identity & Self", "Face / چہرہ", "A", "الف", "1", "Standing vertical lines"),
        ("Emotions & Smiles", "Smile / مسکان", "B", "ب", "2", "Sleeping horizontal lines"),
        ("Eyes & Vision", "Eyes / آنکھیں", "C", "پ", "3", "Slanting diagonal lines"),
        ("Heart & Feelings", "Heart / دل", "D", "ت", "4", "Circular and curve loops"),
        ("Family Bonds", "Family / خاندان", "E", "ٹ", "5", "Zig-zag tactile patterns"),
        ("Hands & Touch", "Hands / ہاتھ", "F", "ث", "6", "Standing vertical lines"),
        ("Voice & Sound", "Voice / آواز", "G", "ج", "7", "Sleeping horizontal lines"),
        ("My Body", "Me / میں", "H", "چ", "8", "Slanting diagonal lines"),
        
        ("Doorways & Entry", "Door / دروازہ", "I", "ح", "9", "Circular and curve loops"),
        ("Windows & Light", "Window / کھڑکی", "J", "خ", "10", "Zig-zag tactile patterns"),
        ("Tables & Classroom", "Table / میز", "K", "د", "11", "Standing vertical lines"),
        ("Chairs & Seating", "Chair / کرسی", "L", "ڈ", "12", "Sleeping horizontal lines"),
        ("Floors & Walking", "Floor / فرش", "M", "ذ", "13", "Slanting diagonal lines"),
        ("Walls & Structure", "Wall / دیوار", "N", "ر", "14", "Circular and curve loops"),
        ("Mats & Seating", "Mat / چٹائی", "O", "ڑ", "15", "Zig-zag tactile patterns"),
        ("Beds & Rest", "Bed / بستر", "P", "ز", "16", "Standing vertical lines"),
        
        ("Colors & Paint", "Paint / رنگ", "Q", "ژ", "17", "Sleeping horizontal lines"),
        ("Brushes & Strokes", "Brush / برش", "R", "س", "18", "Slanting diagonal lines"),
        ("Clay & Molding", "Clay / مٹی", "S", "ش", "19", "Circular and curve loops"),
        ("Songs & Rhymes", "Song / گیت", "T", "ص", "20", "Zig-zag tactile patterns"),
        ("Stories & Tales", "Story / کہانی", "U", "ض", "1", "Standing vertical lines"),
        ("Smiles & Joy", "Smile / مسکرانا", "V", "ط", "2", "Sleeping horizontal lines"),
        ("Laughter & Fun", "Laugh / ہنسنا", "W", "ظ", "3", "Slanting diagonal lines"),
        ("Dance & Movement", "Dance / ناچ", "X", "ع", "4", "Circular and curve loops"),
        ("Art & Hues", "Color / رنگ", "Y", "غ", "5", "Zig-zag tactile patterns"),
        
        ("Water & Rivers", "Water / پانی", "Z", "ف", "6", "Standing vertical lines"),
        ("Leaves & Foliage", "Leaf / پتا", "A", "ق", "7", "Sleeping horizontal lines"),
        ("Sunlight & Warmth", "Sun / سورج", "B", "ک", "8", "Slanting diagonal lines"),
        ("Clouds & Sky", "Cloud / بادل", "C", "گ", "9", "Circular and curve loops"),
        ("Rain & Showers", "Rain / بارش", "D", "ل", "10", "Zig-zag tactile patterns"),
        ("Stones & Earth", "Stone / پتھر", "E", "م", "11", "Standing vertical lines"),
        ("Wind & Breeze", "Wind / ہوا", "F", "ن", "12", "Sleeping horizontal lines"),
        ("Trees & Timber", "Tree / درخت", "G", "و", "13", "Slanting diagonal lines"),
        
        ("Baskets & Storage", "Basket / ٹوکری", "H", "ہ", "14", "Circular and curve loops"),
        ("Toys & Play", "Toy / کھلونا", "I", "ھ", "15", "Zig-zag tactile patterns"),
        ("Shelves & Books", "Shelf / الماری", "J", "ء", "16", "Standing vertical lines"),
        ("Boxes & Packing", "Box / ڈبہ", "K", "ی", "17", "Sleeping horizontal lines"),
        ("Cleaning & Tidying", "Clean / صاف", "L", "ے", "18", "Slanting diagonal lines"),
        ("Order & Arrangement", "Tidy / درست", "M", "الف", "19", "Circular and curve loops"),
        ("Helping Hands", "Help / مدد", "N", "ب", "20", "Zig-zag tactile patterns"),
        ("Sorting Objects", "Sort / ترتیب", "O", "پ", "1", "Standing vertical lines"),
        
        ("Seeds & Planting", "Seed / بیج", "P", "ت", "2", "Sleeping horizontal lines"),
        ("Soil & Ground", "Soil / مٹی", "Q", "ٹ", "3", "Slanting diagonal lines"),
        ("Growing Plants", "Plant / پودا", "R", "ث", "4", "Circular and curve loops"),
        ("Flowers & Blossoms", "Flower / پھول", "S", "ج", "5", "Zig-zag tactile patterns"),
        ("Birds & Feathers", "Bird / پرندہ", "T", "چ", "6", "Standing vertical lines"),
        ("Cats & Paws", "Cat / بلی", "U", "ح", "7", "Sleeping horizontal lines"),
        ("Dogs & Canines", "Dog / کتا", "V", "خ", "8", "Slanting diagonal lines"),
        ("Plant Growth", "Growth / بڑھوتری", "W", "د", "9", "Circular and curve loops"),
        ("Nature Care", "Care / دیکھ بھال", "X", "ڈ", "10", "Zig-zag tactile patterns")
    ]
    
    theme_category, vocab, en, ur, math, stroke = themes[unit_num - 1]
    theme_name = f"Unit {unit_num}: {theme_category}"
    skill_stage = f"Inquiry & Multi-Sensory Exploration for {vocab}"
    return theme_name, skill_stage, en, ur, int(math), stroke, vocab

def create_download_file_button(content, filename, label):
    b64 = base64.b64encode(content.encode('utf-8')).decode('utf-8')
    return f'<a href="data:text/plain;charset=utf-8;base64,{b64}" download="{filename}" style="text-decoration:none;"><div style="background:#2e7d32;color:white;padding:10px;text-align:center;border-radius:6px;font-weight:bold;margin-top:5px;">📥 {label}</div></a>'

# --- MAIN VIEWS ---
if st.session_state.current_page == "Teacher/Parent Dashboard":
    if st.session_state.lang == "English":
        st.title("👩‍🏫 EFALL Teacher & Parent Training Hub")
        st.write("Welcome to your professional curriculum portal. Explore our 6 progressive theme boxes designed for small classrooms and toddlers aged 3-4.")
        
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
        st.subheader("📚 Ages 3-4: Master Unit Library & Lesson Plan Hub")
        st.write("Select any unit below to access your professional, structured lesson plan format featuring detailed teacher spoken scripts, action steps, custom demonstration guides, and printable worksheets.")
        
        if st.button("⬅️ Back to Theme Boxes Dashboard"):
            st.session_state.current_page = "Teacher/Parent Dashboard"
            st.rerun()

        unit_number = st.selectbox("Select Unit Number (1 to 50):", list(range(1, 51)), index=st.session_state.selected_unit - 1, format_func=lambda x: f"Unit {x}: {get_unit_curriculum(x)[0]}")
        
        theme_name, skill_stage, en_focus, ur_focus, math_focus, stroke_focus, vocab_theme = get_unit_curriculum(unit_number)

        st.markdown(f"---")
        
        # --- PROFESSIONAL LESSON PLAN HEADER BLOCK ---
        st.markdown(f"# 📋 Professional Lesson Plan: {theme_name}")
        st.success(f"🎯 **Skill Stage:** {skill_stage} &nbsp;&nbsp;|&nbsp;&nbsp; 🔑 **Vocabulary Theme:** {vocab_theme}")
        st.warning(f"🔤 **Dual Phonics:** English **'{en_focus}'** & Urdu **'{ur_focus}'** &nbsp;&nbsp;|&nbsp;&nbsp; 🔢 **Math Numeral:** **{math_focus}** &nbsp;&nbsp;|&nbsp;&nbsp; ✍️ **Stroke:** {stroke_focus}")

        # Standard Tabbed Structure
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "📝 Detailed 70-Min Lesson Plan", 
            "🎬 Custom Demonstration Guides", 
            "📄 Printable Worksheets Hub", 
            "✂️ Extra Worksheet Generator",
            "💬 Assessment & Feedback"
        ])

        # TAB 1: DETAILED LESSON PLAN
        with tab1:
            st.markdown("### 🕒 70-Minute Step-by-Step Lesson Plan")
            st.write("Structured format featuring precise teacher scripts, action movements, and rich embedded preview text.")
            
            # Phase 1
            with st.container(border=True):
                st.markdown("#### Phase 1: Provocation & Visual Hook (00:00 - 00:15)")
                col_p1_text, col_p1_media = st.columns([3, 2])
                with col_p1_text:
                    st.markdown("👁️ **Classroom Action:** Gather children in a cozy semi-circle on floor mats. Keep physical space clear.")
                    st.info(f'🗣️ **Teacher Spoken Script:**\n> *"Good morning, my little explorers! Look closely at what I have hidden in my hands today. What do you see here that reminds us of **{vocab_theme}**?"*')
                    ws1_content = f"""┌─────────────────────────────────────────────────────────────┐
│                 EFALL LEARNING ACTIVITY SHEET               │
├─────────────────────────────────────────────────────────────┤
│ UNIT {unit_number}: {theme_name.upper()}                                      │
│ TOPIC: {vocab_theme:<36}│
│ NAME: _______________________________ DATE: ________________│
├─────────────────────────────────────────────────────────────┤
│ INSTRUCTIONS:                                               │
│ 1. Point to the main vocabulary picture for '{vocab_theme}'.        │
│ 2. Trace the matching English letter '{en_focus}' and Urdu letter '{ur_focus}'.  │
│                                                             │
│    [   {vocab_theme}   ]               [   {en_focus} / {ur_focus}   ]            │
│  (Target Vocabulary Item)         (Bilingual Phonics Box)   │
│                                                             │
│ TRACING TRACK:                                              │
│ {en_focus} . . . . {en_focus} . . . . {en_focus}                                            │
│ {ur_focus} . . . . {ur_focus} . . . . {ur_focus}                                            │
│                                                             │
│ ⭐ Teacher Stamp Box: [      ]                              │
└─────────────────────────────────────────────────────────────┘"""
                    st.markdown(create_download_file_button(ws1_content, f"Unit_{unit_number}_Worksheet_1_VisualHook.txt", "Download Worksheet 1"), unsafe_allow_html=True)
                with col_p1_media:
                    st.markdown(f"**Visual Preview Box:**\n- Theme: {vocab_theme}\n- Focus: Interactive Object Exploration\n- Setup: Small Group Floor Mats")
                    st.image("https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=400&auto=format&fit=crop&q=80", caption=f"Visual Aid: {vocab_theme}")

            # Phase 2
            with st.container(border=True):
                st.markdown("#### Phase 2: Tactile Probe & Salt Tray Tracing (00:15 - 00:30)")
                col_p2_text, col_p2_media = st.columns([3, 2])
                with col_p2_text:
                    st.markdown("✋ **Classroom Action:** Place shallow salt/flour trays in front of each child on floor mats.")
                    st.info(f'🗣️ **Teacher Spoken Script:**\n> *"Now, let\'s get ready for our magic writing sand. First, watch my index finger slide across the air: **{stroke_focus}**. Gently dip your finger and trace your sheet!"*')
                    ws2_content = f"""┌─────────────────────────────────────────────────────────────┐
│                 EFALL LEARNING ACTIVITY SHEET               │
├─────────────────────────────────────────────────────────────┤
│ UNIT {unit_number}: TACTILE MOTOR & STROKE PRACTICE         │
│ STROKE PATTERN: {stroke_focus:<27}│
│ NAME: _______________________________ DATE: ________________│
├─────────────────────────────────────────────────────────────┤
│ INSTRUCTIONS:                                               │
│ 1. Practice pattern in salt tray.                           │
│ 2. Use crayon to trace dotted lines below.                  │
│                                                             │
│ LINE PRACTICE:                                              │
│ Start ──> . . . . . . . . . . . . . . . . . ➔ ({stroke_focus})  │
│ Start ──> _________________________________                 │
│                                                             │
│ ⭐ Teacher Stamp Box: [      ]                              │
└─────────────────────────────────────────────────────────────┘"""
                    st.markdown(create_download_file_button(ws2_content, f"Unit_{unit_number}_Worksheet_2_TactileTracing.txt", "Download Worksheet 2"), unsafe_allow_html=True)
                with col_p2_media:
                    st.markdown(f"**Kinesthetic Preview Box:**\n- Motion: {stroke_focus}\n- Medium: Salt / Flour Tray\n- Posture: Seated on Floor")
                    st.image("https://images.unsplash.com/photo-1588072432836-e10032774350?w=400&auto=format&fit=crop&q=80", caption=f"Stroke Focus: {stroke_focus}")

            # Phase 3
            with st.container(border=True):
                st.markdown("#### Phase 3: Dual Aural Phonics & Sound Chants (00:30 - 00:50)")
                col_p3_text, col_p3_media = st.columns([3, 2])
                with col_p3_text:
                    st.markdown("👂 **Classroom Action:** Hold up dual alphabet flashcards in front of the semi-circle.")
                    st.info(f'🗣️ **Teacher Spoken Script:**\n> *"Friends, open your ears wide! Let\'s say English **\'{en_focus}\'** and Urdu **\'{ur_focus}\'**. Now let\'s clap our hands exactly **{math_focus}** times!"*')
                    ws3_content = f"""┌─────────────────────────────────────────────────────────────┐
│                 EFALL LEARNING ACTIVITY SHEET               │
├─────────────────────────────────────────────────────────────┤
│ UNIT {unit_number}: DUAL PHONICS & RHYTHM COUNT             │
│ PHONICS TARGET: English '{en_focus}' & Urdu '{ur_focus}'                  │
│ NAME: _______________________________ DATE: ________________│
├─────────────────────────────────────────────────────────────┤
│ INSTRUCTIONS:                                               │
│ 1. Say sounds aloud. Match English to Urdu.                 │
│ 2. Color exactly {math_focus} star items below.                     │
│                                                             │
│ [ {en_focus} ]  =========>  [ {ur_focus} ]                              │
│                                                             │
│ Star Count ({math_focus} target):                             │
│ 🌟 🌟 🌟 🌟 🌟 🌟 🌟 🌟 🌟 🌟                              │
│                                                             │
│ ⭐ Teacher Stamp Box: [      ]                              │
└─────────────────────────────────────────────────────────────┘"""
                    st.markdown(create_download_file_button(ws3_content, f"Unit_{unit_number}_Worksheet_3_Phonics.txt", "Download Worksheet 3"), unsafe_allow_html=True)
                with col_p3_media:
                    st.markdown(f"**Aural Preview Box:**\n- English Sound: '{en_focus}'\n- Urdu Sound: '{ur_focus}'\n- Rhythm Claps: {math_focus}")
                    st.image("https://images.unsplash.com/photo-1485546246426-74dc88dec4d9?w=400&auto=format&fit=crop&q=80", caption=f"Phonics: '{en_focus}' & '{ur_focus}'")

            # Phase 4
            with st.container(border=True):
                st.markdown("#### Phase 4: Cognitive Logic & Numeracy Games (00:50 - 01:05)")
                col_p4_text, col_p4_media = st.columns([3, 2])
                with col_p4_text:
                    st.markdown("🧠 **Classroom Action:** Distribute mental logic sheets and counting cards.")
                    st.info(f'🗣️ **Teacher Spoken Script:**\n> *"Let\'s put our thinking caps on! Find which **{vocab_theme}** item doesn\'t belong on Worksheet 4, and count treasure stars up to **{math_focus}** on Worksheet 5!"*')
                    ws4_content = f"""┌─────────────────────────────────────────────────────────────┐
│                 EFALL LEARNING ACTIVITY SHEET               │
├─────────────────────────────────────────────────────────────┤
│ UNIT {unit_number}: LOGIC SORTING & NUMERACY TARGET         │
│ NUMERAL FOCUS: {math_focus} | TOPIC: {vocab_theme:<23}│
│ NAME: _______________________________ DATE: ________________│
├─────────────────────────────────────────────────────────────┤
│ INSTRUCTIONS:                                               │
│ 1. Cross out (X) the item that does not belong.             │
│ 2. Trace numeral {math_focus} across the dotted boxes.          │
│                                                             │
│ [ {vocab_theme} ]   [ {vocab_theme} ]   [ ❌ Odd One Out ]          │
│                                                             │
│ Numeral Trace: {math_focus}  {math_focus}  {math_focus}  {math_focus}  {math_focus}                             │
│                                                             │
│ ⭐ Teacher Stamp Box: [      ]                              │
└─────────────────────────────────────────────────────────────┘"""
                    st.markdown(create_download_file_button(ws4_content, f"Unit_{unit_number}_Worksheets_4_5_Logic.txt", "Download Worksheets 4 & 5"), unsafe_allow_html=True)
                with col_p4_media:
                    st.markdown(f"**Logic Preview Box:**\n- Category: {vocab_theme}\n- Numeral Target: {math_focus}\n- Skill: Odd-One-Out Sorting")
                    st.image("https://images.unsplash.com/photo-1596464019183-2947119ff342?w=400&auto=format&fit=crop&q=80", caption=f"Numeracy Target: {math_focus}")

            # Phase 5
            with st.container(border=True):
                st.markdown("#### Phase 5: Reflection & Celebration (01:05 - 01:10)")
                st.markdown("🌟 **Classroom Action:** Hand out small lumps of playdough on floor mats.")
                st.info(f'🗣️ **Teacher Spoken Script:**\n> *"Shape your playdough into letter **\'{en_focus}\'** and **\'{ur_focus}\'**. High-fives all around for completing Unit {unit_number}!"*')
                st.success("🏆 Certificate of Unit Completion earned!")

        # TAB 2: CUSTOM DEMONSTRATION GUIDES (Replaces random YouTube videos)
        with tab2:
            st.markdown("### 🎬 Custom Teacher Demonstration Guides")
            st.write("Instead of random videos, follow these custom built-in classroom demonstration walkthroughs designed specifically for your small classroom setup:")
            
            col_d1, col_d2 = st.columns(2)
            with col_d1:
                with st.container(border=True):
                    st.markdown(f"#### ✍️ Salt Tray Tracing Guide: '{stroke_focus}'")
                    st.markdown("1. **Setup:** Place a shallow tray with 2mm of fine salt or flour on floor mats.")
                    st.markdown(f"2. **Teacher Action:** Model the motion slowly in front of children: *{stroke_focus}*.")
                    st.markdown("3. **Child Practice:** Children dip their index finger and duplicate the movement.")
                    st.info("💡 **Small Space Tip:** Keep trays stable on floor mats to prevent spills.")
            with col_d2:
                with st.container(border=True):
                    st.markdown(f"#### 🗣️ Phonics Articulation Guide: '{en_focus}' & '{ur_focus}'")
                    st.markdown(f"1. **English Sound ('{en_focus}'):** Keep mouth relaxed, say sound clearly with breath.")
                    st.markdown(f"2. **Urdu Sound ('{ur_focus}'):** Round lips softly, project sound forward.")
                    st.markdown(f"3. **Rhythm:** Clap hands together exactly **{math_focus}** times.")
                    st.info("💡 **Engagement Tip:** Use hand puppets to model sounds for toddlers.")

        # TAB 3: PRINTABLE WORKSHEETS HUB
        with tab3:
            st.markdown("### 📄 Complete Formatted Printable Workbook")
            st.write("Download all exercises for this unit packed into a fully formatted structured workbook document:")
            full_packet = f"""======================================================================
                  EFALL EDUCATIONAL PORTAL WORKBOOK                   
======================================================================
Unit Number: {unit_number} | Theme Name: {theme_name}
Vocabulary Focus: {vocab_theme}
Dual Phonics: English '{en_focus}' & Urdu '{ur_focus}'
Target Numeral: {math_focus} | Stroke Pattern: {stroke_focus}
----------------------------------------------------------------------

[EXERCISE 1: VISUAL HOOK & RECOGNITION]
Instructions: Identify pictures matching {vocab_theme}.
Tracing Area: {en_focus} . . . . . . . . . .   |   {ur_focus} . . . . . . . . . .

[EXERCISE 2: TACTILE STROKE PRACTICE]
Instructions: Salt tray finger trace followed by pencil line control.
Pattern Trace: {stroke_focus} ➔ ➔ ➔ ➔ ➔

[EXERCISE 3: DUAL PHONICS & AURAL MATCHING]
Instructions: Connect English '{en_focus}' to Urdu '{ur_focus}'.
Star Coloring: Color up to {math_focus} target stars.

[EXERCISE 4 & 5: LOGIC & NUMERACY]
Instructions: Cross out odd-one-out; trace numeral {math_focus}.
Numeral Practice: {math_focus}   {math_focus}   {math_focus}   {math_focus}   {math_focus}

======================================================================
Designed for Ages 3-4 | Inquiry-Based Multi-Sensory Curriculum
======================================================================
"""
            st.markdown(create_download_file_button(full_packet, f"Unit_{unit_number}_Complete_Workbook.txt", "Download Complete Workbook Packet"), unsafe_allow_html=True)
            with st.container(border=True):
                st.markdown(full_packet)

        # TAB 4: EXTRA WORKSHEET GENERATOR
        with tab4:
            st.markdown("### ✂️ Custom Worksheet Generator")
            st.write("Need extra practice sheets for specific topics? Generate custom printable exercises on demand:")
            custom_topic = st.text_input("Custom Topic / Focus:", value=vocab_theme)
            custom_qty = st.slider("Number of Practice Items:", 1, 10, 5)
            if st.button("Generate Custom Practice Sheet"):
                custom_export = f"""┌─────────────────────────────────────────────────────────────┐
│                 EFALL CUSTOM PRACTICE SHEET                 │
├─────────────────────────────────────────────────────────────┤
│ CUSTOM TOPIC: {custom_topic:<33}│
│ ITEMS QUANTITY: {custom_qty:<31}│
│ NAME: _______________________________ DATE: ________________│
├─────────────────────────────────────────────────────────────┤
│ INSTRUCTIONS FOR TEACHER:                                   │
│ Distribute this sheet to students needing reinforcement on  │
│ {custom_topic}. Guide children through tracing below.       │
│                                                             │
"""
                for i in range(1, custom_qty + 1):
                    custom_export += f"│ ({i}) Trace [{custom_topic}]: _______________________ [⭐] │\n"
                custom_export += f"""│                                                             │
│ ⭐ Teacher Stamp Box: [      ]                              │
└─────────────────────────────────────────────────────────────┘"""
                st.success(f"Custom worksheet for **{custom_topic}** generated successfully!")
                st.markdown(create_download_file_button(custom_export, f"Custom_{custom_topic}_Worksheet.txt", "Download Custom Worksheet"), unsafe_allow_html=True)

        # TAB 5: ASSESSMENT
        with tab5:
            st.markdown("### 💬 Assessment & Teacher Reflection")
            st.markdown(f"1. **Engagement:** Did children connect with the **{vocab_theme}** provocation?")
            st.markdown(f"2. **Bilingual Articulation:** Did they articulate English **'{en_focus}'** and Urdu **'{ur_focus}'**?")
            st.markdown(f"3. **Motor Skills:** Did they successfully trace **{stroke_focus}**?")
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
