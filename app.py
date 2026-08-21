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
        st.write("Welcome to your interactive curriculum portal. Explore our 6 progressive theme boxes designed for small classrooms and toddlers aged 3-4.")
        
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
        st.subheader("📚 Ages 3-4: Interactive Book Lesson Library")
        st.write("Select a unit below to open your step-by-step interactive lesson book, complete with matching media, downloadable worksheets, and guided scripts.")
        
        if st.button("⬅️ Back to Theme Boxes Dashboard"):
            st.session_state.current_page = "Teacher/Parent Dashboard"
            st.rerun()

        unit_number = st.selectbox("Select Unit Number (1 to 50):", list(range(1, 51)), index=st.session_state.selected_unit - 1, format_func=lambda x: f"Unit {x}: {get_unit_curriculum(x)[0]}")
        
        theme_name, skill_stage, en_focus, ur_focus, math_focus, stroke_focus, vocab_theme = get_unit_curriculum(unit_number)

        st.markdown(f"---")
        
        # --- INTERACTIVE BOOK HEADER ---
        st.markdown(f"# 📖 Interactive Lesson Book: {theme_name}")
        st.success(f"🎯 **Skill Stage:** {skill_stage} &nbsp;&nbsp;|&nbsp;&nbsp; 🔑 **Vocabulary Theme:** {vocab_theme}")
        st.warning(f"🔤 **Dual Phonics:** English **'{en_focus}'** & Urdu **'{ur_focus}'** &nbsp;&nbsp;|&nbsp;&nbsp; 🔢 **Math Numeral:** **{math_focus}** &nbsp;&nbsp;|&nbsp;&nbsp; ✍️ **Stroke:** {stroke_focus}")

        # Tab Navigation styled as Book Chapters
        book_tab1, book_tab2, book_tab3, book_tab4, book_tab5, book_tab6 = st.tabs([
            "📖 Book Chapter 1: Provocation", 
            "📖 Book Chapter 2: Tactile Tracing", 
            "📖 Book Chapter 3: Dual Phonics", 
            "📖 Book Chapter 4: Numeracy Logic", 
            "📖 Book Chapter 5: Celebration & Play", 
            "🖨️ Master Resource & Worksheet Hub"
        ])

        # CHAPTER 1
        with book_tab1:
            st.markdown("## Chapter 1: Provocation & Visual Hook (00:00 - 00:15)")
            st.write("Set the stage in your small classroom with a captivating visual hook and guided inquiry.")
            
            col_text1, col_media1 = st.columns([3, 2])
            with col_text1:
                st.markdown("### 👁️ Classroom Setup & Dialogue")
                st.markdown("* **Physical Setup:** Gather children in a cozy semi-circle on floor mats. Keep the center clear.")
                st.info(f'🗣️ **Exact Teacher Spoken Script:**\n> *"Good morning, my little explorers! Look closely at what I have hidden in my hands today. What do you see here that reminds us of **{vocab_theme}**?"*')
                st.markdown("---")
                st.markdown("📄 **Integrated Worksheet 1:** Visual Memory & Picture Hook")
                ws1_text = f"""==================================================
EFALL EARLY YEARS EDUCATIONAL PORTAL
WORKSHEET 1: VISUAL MEMORY & PICTURE HOOK
==================================================
Unit: {unit_number} | Theme: {theme_name}
Vocabulary Focus: {vocab_theme}
Target Letters: English '{en_focus}' | Urdu '{ur_focus}'

INSTRUCTIONS FOR TEACHER/PARENT:
1. Show the children real objects or picture cards related to '{vocab_theme}'.
2. Ask students to identify items starting with phonics '{en_focus}' and '{ur_focus}'.
3. Have students circle or point to the correct picture below.

STUDENT ACTIVITY EXERCISE:
[O] Picture A: {vocab_theme} (Match & Circle)
[  ] Picture B: Distractor item
[  ] Picture C: Distractor item

Tracing Practice Area:
Trace English '{en_focus}' -> {en_focus}  {en_focus}  {en_focus}
Trace Urdu '{ur_focus}'     -> {ur_focus}  {ur_focus}  {ur_focus}
==================================================
"""
                st.markdown(create_download_file_button(ws1_text, f"Unit_{unit_number}_Worksheet_1.txt", "Download Worksheet 1"), unsafe_allow_html=True)
            with col_media1:
                st.image("https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=400&auto=format&fit=crop&q=80", caption=f"Visual Hook: {vocab_theme}")
                st.markdown("📺 **Curated Video Support:**")
                st.video("https://www.youtube.com/watch?v=BELlZKpi1Zs")

        # CHAPTER 2
        with book_tab2:
            st.markdown("## Chapter 2: Tactile Probe & Salt Tray Tracing (00:15 - 00:30)")
            st.write("Transition toddlers into kinesthetic motor skill practice using shallow trays.")
            
            col_text2, col_media2 = st.columns([3, 2])
            with col_text2:
                st.markdown("### ✋ Classroom Setup & Dialogue")
                st.markdown("* **Physical Setup:** Place shallow salt/flour trays in front of each child on floor mats.")
                st.info(f'🗣️ **Exact Teacher Spoken Script:**\n> *"Now, let\'s get ready for our magic writing sand. First, watch my index finger slide across the air: **{stroke_focus}**. Gently dip your finger and trace your sheet!"*')
                st.markdown("---")
                st.markdown("📄 **Integrated Worksheet 2:** Tactile Pre-Writing Stroke Tracing")
                ws2_text = f"""==================================================
EFALL EARLY YEARS EDUCATIONAL PORTAL
WORKSHEET 2: TACTILE STROKE TRACING
==================================================
Unit: {unit_number} | Theme: {theme_name}
Stroke Pattern: {stroke_focus}

INSTRUCTIONS FOR TEACHER/PARENT:
1. Distribute shallow trays filled with salt, sand, or flour.
2. Demonstrate tracing motion: {stroke_focus}.
3. Have children trace the pattern in the tray first, then on this printed sheet using thick crayons.

STUDENT ACTIVITY EXERCISE:
Finger Tracing Zone: [Salt Tray Ready]
Pencil / Crayon Tracing Track:
. . . . . -> (Trace along the {stroke_focus})
. . . . . -> (Trace along the {stroke_focus})

Self-Assessment Star Box: [  ] Give yourself a star!
==================================================
"""
                st.markdown(create_download_file_button(ws2_text, f"Unit_{unit_number}_Worksheet_2.txt", "Download Worksheet 2"), unsafe_allow_html=True)
            with col_media2:
                st.image("https://images.unsplash.com/photo-1588072432836-e10032774350?w=400&auto=format&fit=crop&q=80", caption=f"Stroke Focus: {stroke_focus}")
                st.markdown("📺 **Curated Video Support:**")
                st.video("https://www.youtube.com/watch?v=Uj6_Knct8AE")

        # CHAPTER 3
        with book_tab3:
            st.markdown("## Chapter 3: Dual Aural Phonics & Sound Chants (00:30 - 00:50)")
            st.write("Engage auditory learners with bilingual letter sounds and rhythmic clapping.")
            
            col_text3, col_media3 = st.columns([3, 2])
            with col_text3:
                st.markdown("### 👂 Classroom Setup & Dialogue")
                st.markdown("* **Physical Setup:** Hold up dual alphabet flashcards in front of the semi-circle.")
                st.info(f'🗣️ **Exact Teacher Spoken Script:**\n> *"Friends, open your ears wide! Let\'s say English **\'{en_focus}\'** and Urdu **\'{ur_focus}\'**. Now let\'s clap our hands exactly **{math_focus}** times!"*')
                st.markdown("---")
                st.markdown("📄 **Integrated Worksheet 3:** Dual Phonics & Alphabet Matching")
                ws3_text = f"""==================================================
EFALL EARLY YEARS EDUCATIONAL PORTAL
WORKSHEET 3: DUAL PHONICS & SOUND MATCHING
==================================================
Unit: {unit_number} | Theme: {theme_name}
English Phonics Focus: '{en_focus}'
Urdu Phonics Focus: '{ur_focus}'
Rhythm Clapping Count: {math_focus} Claps

INSTRUCTIONS FOR TEACHER/PARENT:
1. Pronounce '{en_focus}' and '{ur_focus}' together clearly.
2. Have students repeat the sounds 3 times.
3. Clap hands {math_focus} times synchronously with students.

STUDENT ACTIVITY EXERCISE:
Match the Letters:
[ {en_focus} ]  =======>  [ {ur_focus} ]

Coloring Task: Color the {math_focus} star shapes below!
🌟 🌟 🌟 🌟 🌟 (Color up to {math_focus})
==================================================
"""
                st.markdown(create_download_file_button(ws3_text, f"Unit_{unit_number}_Worksheet_3.txt", "Download Worksheet 3"), unsafe_allow_html=True)
            with col_media3:
                st.image("https://images.unsplash.com/photo-1485546246426-74dc88dec4d9?w=400&auto=format&fit=crop&q=80", caption=f"Phonics: '{en_focus}' & Urdu '{ur_focus}'")
                st.markdown("📺 **Curated Video Support:**")
                st.video("https://www.youtube.com/watch?v=Z19zFlPah-o")

        # CHAPTER 4
        with book_tab4:
            st.markdown("## Chapter 4: Cognitive Logic & Numeracy Games (00:50 - 01:05)")
            st.write("Develop early problem-solving skills through sorting and counting.")
            
            col_text4, col_media4 = st.columns([3, 2])
            with col_text4:
                st.markdown("### 🧠 Classroom Setup & Dialogue")
                st.markdown("* **Physical Setup:** Distribute mental logic sheets and counting cards.")
                st.info(f'🗣️ **Exact Teacher Spoken Script:**\n> *"Let\'s put our thinking caps on! Find which **{vocab_theme}** item doesn\'t belong on Worksheet 4, and count treasure stars up to **{math_focus}** on Worksheet 5!"*')
                st.markdown("---")
                st.markdown("📄 **Integrated Worksheets 4 & 5:** Logic Sorting & Numeracy")
                ws4_text = f"""==================================================
EFALL EARLY YEARS EDUCATIONAL PORTAL
WORKSHEETS 4 & 5: COGNITIVE LOGIC & NUMERACY
==================================================
Unit: {unit_number} | Theme: {theme_name}
Target Numeral: {math_focus}
Vocabulary Context: {vocab_theme}

INSTRUCTIONS FOR TEACHER/PARENT:
1. Ask students to identify which picture card does not fit the '{vocab_theme}' category.
2. Guide students to count items up to numeral {math_focus}.
3. Practice tracing number {math_focus} with a pencil or finger.

STUDENT ACTIVITY EXERCISE:
Logic Sorting Puzzle:
[Item A: {vocab_theme}]   [Item B: {vocab_theme}]   [Item X: Odd One Out]
(Circle the odd one out!)

Numeracy Practice:
Target Number: {math_focus}
Trace Number [{math_focus}]:  {math_focus}  {math_focus}  {math_focus}  {math_focus}
==================================================
"""
                st.markdown(create_download_file_button(ws4_text, f"Unit_{unit_number}_Worksheets_4_5.txt", "Download Worksheets 4 & 5"), unsafe_allow_html=True)
            with col_media4:
                st.image("https://images.unsplash.com/photo-1596464019183-2947119ff342?w=400&auto=format&fit=crop&q=80", caption=f"Numeracy Target: {math_focus}")
                st.markdown("📺 **Curated Video Support:**")
                st.video("https://www.youtube.com/watch?v=jNQXAC9IVRw")

        # CHAPTER 5
        with book_tab5:
            st.markdown("## Chapter 5: Celebration & Playdough Sculpture (01:05 - 01:10)")
            st.write("Reinforce learning with tactile playdough modeling and positive reinforcement.")
            
            col_text5, col_media5 = st.columns([3, 2])
            with col_text5:
                st.markdown("### 🌟 Classroom Setup & Dialogue")
                st.markdown("* **Physical Setup:** Hand out small lumps of playdough on floor mats.")
                st.info(f'🗣️ **Exact Teacher Spoken Script:**\n> *"Shape your playdough into letter **\'{en_focus}\'** and **\'{ur_focus}\'**. High-fives all around for completing Unit {unit_number}!"*')
                st.markdown("---")
                st.markdown("🏆 **Unit Celebration & Reflection Badge**")
                st.success(f"Certificate of Completion for Unit {unit_number} ({theme_name}) earned!")
            with col_media5:
                st.image("https://images.unsplash.com/photo-1560582861-45fe48c8246f?w=400&auto=format&fit=crop&q=80", caption="Playdough & Celebration")

        # MASTER HUB
        with book_tab6:
            st.markdown("## 🖨️ Master Resource & Extra Worksheet Generator")
            st.write("Download complete bundles or generate custom practice sheets on demand.")
            
            full_unit_bundle = f"""==================================================
EFALL EDUCATIONAL PORTAL - MASTER UNIT PACKAGE
==================================================
Unit Number: {unit_number}
Theme Name: {theme_name}
Skill Focus: {skill_stage}
Dual Phonics: English '{en_focus}' & Urdu '{ur_focus}'
Target Numeral: {math_focus}
Stroke Pattern: {stroke_focus}
Vocabulary Theme: {vocab_theme}

--------------------------------------------------
COMPLETE 70-MINUTE LESSON SCRIPT SUMMARY:
- Phase 1 (00:00-00:15): Visual Hook & Provocation about {vocab_theme}.
- Phase 2 (00:15-00:30): Salt Tray & Pre-writing stroke tracing ({stroke_focus}).
- Phase 3 (00:30-00:50): Dual Aural Phonics ('{en_focus}' / '{ur_focus}') & {math_focus} claps.
- Phase 4 (00:50-01:05): Cognitive logic sorting & numeral counting up to {math_focus}.
- Phase 5 (01:05-01:10): Playdough letter sculpture & high-fives celebration.
--------------------------------------------------
Ready for direct classroom printing and presentation.
"""
            st.markdown(create_download_file_button(full_unit_bundle, f"Unit_{unit_number}_Complete_Master_Package.txt", "Download Complete Unit Master Package (TXT/PDF)"), unsafe_allow_html=True)
            
            st.markdown("---")
            st.subheader("✂️ Extra Custom Worksheet Generator")
            custom_topic = st.text_input("Custom Topic / Focus:", value=vocab_theme)
            custom_qty = st.slider("Number of Practice Items:", 1, 10, 5)
            if st.button("Generate Custom Practice Sheet"):
                custom_export = f"""==================================================
EFALL CUSTOM GENERATED PRACTICE SHEET
==================================================
Custom Topic: {custom_topic}
Practice Items Quantity: {custom_qty}
Target Age Group: 3-4 Years (Senior Kindergarten / Early Years)

INSTRUCTIONS FOR TEACHER:
1. Distribute this custom practice sheet to students needing extra reinforcement on {custom_topic}.
2. Guide students through the {custom_qty} interactive tracing and drawing prompts below.

PRACTICE EXERCISES:
"""
                for i in range(1, custom_qty + 1):
                    custom_export += f"Item {i}: Trace and say '{custom_topic}' _____________\n"
                custom_export += "=================================================="
                
                st.success(f"Custom worksheet for **{custom_topic}** generated successfully!")
                st.markdown(create_download_file_button(custom_export, f"Custom_{custom_topic}_Worksheet.txt", "Download Custom Worksheet"), unsafe_allow_html=True)

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
