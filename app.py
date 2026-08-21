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
        st.write("Select any unit below to access your professional, structured lesson plan format featuring detailed teacher spoken scripts, action steps, embedded media, and Twinkl-style printable worksheets.")
        
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
            "🎬 Training & Videos", 
            "📄 Twinkl-Style Worksheets", 
            "✂️ Extra Worksheet Generator",
            "💬 Assessment & Feedback"
        ])

        # TAB 1: DETAILED LESSON PLAN
        with tab1:
            st.markdown("### 🕒 70-Minute Step-by-Step Lesson Plan")
            st.write("Structured format featuring precise teacher scripts, action movements, and in-line resources.")
            
            # Phase 1
            with st.container(border=True):
                st.markdown("#### Phase 1: Provocation & Visual Hook (00:00 - 00:15)")
                col_p1_text, col_p1_media = st.columns([3, 2])
                with col_p1_text:
                    st.markdown("👁️ **Classroom Action:** Gather children in a cozy semi-circle on floor mats. Keep physical space clear.")
                    st.info(f'🗣️ **Teacher Spoken Script:**\n> *"Good morning, my little explorers! Look closely at what I have hidden in my hands today. What do you see here that reminds us of **{vocab_theme}**?"*')
                    ws1_content = f"""======================================================================
🌟 EFALL EARLY YEARS LEARNING RESOURCE | TWINKL-STYLE ACTIVITY SHEET 🌟
======================================================================
UNIT {unit_number}: {theme_name.upper()}
TOPIC: {vocab_theme} | FOCUS: English '{en_focus}' & Urdu '{ur_focus}'
NAME: _______________________________   DATE: _________________
----------------------------------------------------------------------
INSTRUCTIONS: Look at the pictures below. Point to each item, say the 
vocabulary word '{vocab_theme}', and circle the correct matching card!

[ 🎨 PICTURE CARD A: {vocab_theme} ]     [ ❌ DISTRACTOR ITEM ]
   (Circle this correct card!)             (Do not circle)

TRACING PRACTICE ZONE:
Trace the starting letters below with your finger or crayon:
English: {en_focus}   {en_focus}   {en_focus}   {en_focus}   {en_focus}
Urdu:    {ur_focus}   {ur_focus}   {ur_focus}   {ur_focus}   {ur_focus}

⭐️⭐️⭐️ Teacher's Star Stamp Box: [       ] ⭐️⭐️⭐️
======================================================================
"""
                    st.markdown(create_download_file_button(ws1_content, f"Unit_{unit_number}_Worksheet_1_VisualHook.txt", "Download Worksheet 1"), unsafe_allow_html=True)
                with col_p1_media:
                    st.image("https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=400&auto=format&fit=crop&q=80", caption=f"Visual Hook: {vocab_theme}")
                    st.video("https://www.youtube.com/watch?v=BELlZKpi1Zs")

            # Phase 2
            with st.container(border=True):
                st.markdown("#### Phase 2: Tactile Probe & Salt Tray Tracing (00:15 - 00:30)")
                col_p2_text, col_p2_media = st.columns([3, 2])
                with col_p2_text:
                    st.markdown("✋ **Classroom Action:** Place shallow salt/flour trays in front of each child on floor mats.")
                    st.info(f'🗣️ **Teacher Spoken Script:**\n> *"Now, let\'s get ready for our magic writing sand. First, watch my index finger slide across the air: **{stroke_focus}**. Gently dip your finger and trace your sheet!"*')
                    ws2_content = f"""======================================================================
🌟 EFALL EARLY YEARS LEARNING RESOURCE | TWINKL-STYLE ACTIVITY SHEET 🌟
======================================================================
UNIT {unit_number}: {theme_name.upper()}
TACTILE STROKE PRACTICE: {stroke_focus}
NAME: _______________________________   DATE: _________________
----------------------------------------------------------------------
INSTRUCTIONS: First, practice tracing the pattern in your salt/flour tray.
Then, use your favorite crayon to trace along the dotted lines below!

SALT TRAY STATUS: [ Ready for Finger Tracing 🖐️ ]

PENCIL CONTROL TRACK:
Line 1: . . . . . . . . . . ➔ ({stroke_focus})
Line 2: . . . . . . . . . . ➔ ({stroke_focus})
Line 3: _________________________________________

⭐️⭐️⭐️ Teacher's Star Stamp Box: [       ] ⭐️⭐️⭐️
======================================================================
"""
                    st.markdown(create_download_file_button(ws2_content, f"Unit_{unit_number}_Worksheet_2_TactileTracing.txt", "Download Worksheet 2"), unsafe_allow_html=True)
                with col_p2_media:
                    st.image("https://images.unsplash.com/photo-1588072432836-e10032774350?w=400&auto=format&fit=crop&q=80", caption=f"Stroke Focus: {stroke_focus}")
                    st.video("https://www.youtube.com/watch?v=Uj6_Knct8AE")

            # Phase 3
            with st.container(border=True):
                st.markdown("#### Phase 3: Dual Aural Phonics & Sound Chants (00:30 - 00:50)")
                col_p3_text, col_p3_media = st.columns([3, 2])
                with col_p3_text:
                    st.markdown("👂 **Classroom Action:** Hold up dual alphabet flashcards in front of the semi-circle.")
                    st.info(f'🗣️ **Teacher Spoken Script:**\n> *"Friends, open your ears wide! Let\'s say English **\'{en_focus}\'** and Urdu **\'{ur_focus}\'**. Now let\'s clap our hands exactly **{math_focus}** times!"*')
                    ws3_content = f"""======================================================================
🌟 EFALL EARLY YEARS LEARNING RESOURCE | TWINKL-STYLE ACTIVITY SHEET 🌟
======================================================================
UNIT {unit_number}: {theme_name.upper()}
DUAL PHONICS & RHYTHM MATCHING
NAME: _______________________________   DATE: _________________
----------------------------------------------------------------------
INSTRUCTIONS: Say the English sound '{en_focus}' and Urdu sound '{ur_focus}' 
out loud with your teacher. Draw a line to connect them!

LETTER MATCHING:
[ English: {en_focus} ]  =========>  [ Urdu: {ur_focus} ]

CLAPPING RHYTHM COUNT: {math_focus} Claps
Color exactly {math_focus} star shapes below:
🌟 🌟 🌟 🌟 🌟 🌟 🌟 🌟 🌟 🌟 (Color up to {math_focus})

⭐️⭐️⭐️ Teacher's Star Stamp Box: [       ] ⭐️⭐️⭐️
======================================================================
"""
                    st.markdown(create_download_file_button(ws3_content, f"Unit_{unit_number}_Worksheet_3_Phonics.txt", "Download Worksheet 3"), unsafe_allow_html=True)
                with col_p3_media:
                    st.image("https://images.unsplash.com/photo-1485546246426-74dc88dec4d9?w=400&auto=format&fit=crop&q=80", caption=f"Phonics: '{en_focus}' & '{ur_focus}'")
                    st.video("https://www.youtube.com/watch?v=Z19zFlPah-o")

            # Phase 4
            with st.container(border=True):
                st.markdown("#### Phase 4: Cognitive Logic & Numeracy Games (00:50 - 01:05)")
                col_p4_text, col_p4_media = st.columns([3, 2])
                with col_p4_text:
                    st.markdown("🧠 **Classroom Action:** Distribute mental logic sheets and counting cards.")
                    st.info(f'🗣️ **Teacher Spoken Script:**\n> *"Let\'s put our thinking caps on! Find which **{vocab_theme}** item doesn\'t belong on Worksheet 4, and count treasure stars up to **{math_focus}** on Worksheet 5!"*')
                    ws4_content = f"""======================================================================
🌟 EFALL EARLY YEARS LEARNING RESOURCE | TWINKL-STYLE ACTIVITY SHEET 🌟
======================================================================
UNIT {unit_number}: {theme_name.upper()}
LOGIC SORTING & NUMERACY TARGET: {math_focus}
NAME: _______________________________   DATE: _________________
----------------------------------------------------------------------
INSTRUCTIONS PART 1 (LOGIC): Look at the three item boxes below. Cross 
out (X) the one that does not belong to the '{vocab_theme}' category!
[ 📦 Item A: {vocab_theme} ]   [ 📦 Item B: {vocab_theme} ]   [ ❌ Odd One Out ]

INSTRUCTIONS PART 2 (NUMERACY): Count the objects and practice writing 
numeral {math_focus} along the dotted tracing track below.
Trace Number [{math_focus}]:  {math_focus}   {math_focus}   {math_focus}   {math_focus}   {math_focus}

⭐️⭐️⭐️ Teacher's Star Stamp Box: [       ] ⭐️⭐️⭐️
======================================================================
"""
                    st.markdown(create_download_file_button(ws4_content, f"Unit_{unit_number}_Worksheets_4_5_Logic.txt", "Download Worksheets 4 & 5"), unsafe_allow_html=True)
                with col_p4_media:
                    st.image("https://images.unsplash.com/photo-1596464019183-2947119ff342?w=400&auto=format&fit=crop&q=80", caption=f"Numeracy Target: {math_focus}")
                    st.video("https://www.youtube.com/watch?v=jNQXAC9IVRw")

            # Phase 5
            with st.container(border=True):
                st.markdown("#### Phase 5: Reflection & Celebration (01:05 - 01:10)")
                st.markdown("🌟 **Classroom Action:** Hand out small lumps of playdough on floor mats.")
                st.info(f'🗣️ **Teacher Spoken Script:**\n> *"Shape your playdough into letter **\'{en_focus}\'** and **\'{ur_focus}\'**. High-fives all around for completing Unit {unit_number}!"*')
                st.success("🏆 Certificate of Unit Completion earned!")

        # TAB 2: TRAINING & VIDEOS
        with tab2:
            st.markdown("### 🎬 Teacher Training & Instructional Videos")
            st.write("Master pronunciation, classroom pacing, and small-space management before teaching:")
            col_t1, col_t2 = st.columns(2)
            with col_t1:
                st.markdown("#### 🎥 Phonics Articulation Masterclass")
                st.info(f"Focus: Mouth positioning for English '{en_focus}' and Urdu '{ur_focus}'.")
                st.video("https://www.youtube.com/watch?v=BELlZKpi1Zs")
            with col_t2:
                st.markdown("#### 🎥 Small-Space Kinesthetic Management")
                st.info(f"Focus: Managing salt trays for '{stroke_focus}' in compact rooms.")
                st.video("https://www.youtube.com/watch?v=Uj6_Knct8AE")

        # TAB 3: DOWNLOADABLE WORKSHEETS
        with tab3:
            st.markdown("### 📄 Complete Twinkl-Style Worksheet Packet")
            st.write("Download all exercises for this unit packed into a beautifully structured printable workbook:")
            full_packet = f"""======================================================================
🌟 EFALL EDUCATIONAL PORTAL - COMPLETE TWINKL-STYLE WORKBOOK 🌟
======================================================================
Unit Number: {unit_number}
Theme Name: {theme_name}
Vocabulary Theme: {vocab_theme}
Dual Phonics Focus: English '{en_focus}' & Urdu '{ur_focus}'
Target Numeral: {math_focus}
Pre-Writing Stroke: {stroke_focus}

----------------------------------------------------------------------
[ACTIVITY 1: VISUAL MEMORY & PICTURE HOOK]
- Objective: Circle pictures matching '{vocab_theme}'.
- Tracing: Practice writing '{en_focus}' and '{ur_focus}'.

[ACTIVITY 2: TACTILE STROKE TRACING]
- Objective: Finger trace salt tray, then complete {stroke_focus} line tracing.

[ACTIVITY 3: DUAL PHONICS & SOUND MATCHING]
- Objective: Match English '{en_focus}' to Urdu '{ur_focus}'. Color {math_focus} stars.

[ACTIVITY 4 & 5: LOGIC SORTING & NUMERACY]
- Objective: Find odd-one-out for {vocab_theme}; trace numeral {math_focus}.
----------------------------------------------------------------------
Designed for Ages 3-4 | Early Years Foundation & IB PYP Framework
======================================================================
"""
            st.markdown(create_download_file_button(full_packet, f"Unit_{unit_number}_Complete_Twinkl_Workbook.txt", "Download Complete Workbook Packet"), unsafe_allow_html=True)
            with st.container(border=True):
                st.markdown(full_packet)

        # TAB 4: EXTRA WORKSHEET GENERATOR
        with tab4:
            st.markdown("### ✂️ Twinkl-Style Custom Worksheet Generator")
            st.write("Need extra practice sheets for specific topics? Generate custom printable exercises on demand:")
            custom_topic = st.text_input("Custom Topic / Focus:", value=vocab_theme)
            custom_qty = st.slider("Number of Practice Items:", 1, 10, 5)
            if st.button("Generate Custom Practice Sheet"):
                custom_export = f"""======================================================================
🌟 EFALL CUSTOM GENERATED TWINKL-STYLE PRACTICE SHEET 🌟
======================================================================
Custom Topic: {custom_topic}
Practice Items Quantity: {custom_qty}
Target Age Group: 3-4 Years (Senior Kindergarten / Early Years)
NAME: _______________________________   DATE: _________________

INSTRUCTIONS FOR TEACHER:
1. Distribute this custom practice sheet to students needing reinforcement on {custom_topic}.
2. Guide students through the {custom_topic} interactive tracing and drawing prompts below.

PRACTICE EXERCISES:
"""
                for i in range(1, custom_qty + 1):
                    custom_export += f"({i}) Draw & Trace [{custom_topic}]:  ___________________________  [⭐️]\n"
                custom_export += f"""
----------------------------------------------------------------------
⭐️⭐️⭐️ Teacher's Star Stamp & Sticker Box: [       ] ⭐️⭐️⭐️
======================================================================
"""
                st.success(f"Custom worksheet for **{custom_topic}** generated successfully!")
                st.markdown(create_download_file_button(custom_export, f"Custom_{custom_topic}_Twinkl_Worksheet.txt", "Download Custom Worksheet"), unsafe_allow_html=True)

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
