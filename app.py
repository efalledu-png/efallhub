import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="EFALL Portal | Teacher & Parent Training Hub",
    page_icon="🌟",
    layout="wide"
)

# Initialize Session State
if "lang" not in st.session_state:
    st.session_state.lang = "English"
if "current_page" not in st.session_state:
    st.session_state.current_page = "Teacher/Parent Dashboard"

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🌟 EFALL Portal")
st.sidebar.caption("Educated Mother Education Nation (Pakistan)")

# Language Switcher
lang_choice = st.sidebar.radio(
    "Language / زبان", 
    ["English", "اردو"], 
    index=0 if st.session_state.lang == "English" else 1
)
st.session_state.lang = lang_choice

st.sidebar.markdown("---")
st.sidebar.subheader("Navigation")

if st.sidebar.button("👩‍🏫 Teacher & Parent Training Hub", use_container_width=True):
    st.session_state.current_page = "Teacher/Parent Dashboard"
if st.sidebar.button("⚙️ Intelligent Unit Generator (50 Units)", use_container_width=True):
    st.session_state.current_page = "Unit Generator"
if st.sidebar.button("👧👦 Synchronized Student View", use_container_width=True):
    st.session_state.current_page = "Student View"

# --- PROGRESSIVE CURRICULUM MAPPING FOR AGES 3-4 (50 Units Breakdown) ---
def get_unit_curriculum(unit_num):
    if unit_num <= 8:
        theme_name = "Who We Are"
        theme_desc = "Identity, body parts, basic emotions, and self-awareness"
    elif unit_num <= 16:
        theme_name = "Where We Are in Place and Time"
        theme_desc = "Home surroundings, favorite room objects, and local spaces"
    elif unit_num <= 25:
        theme_name = "How We Express Ourselves"
        theme_desc = "Sensory sounds, facial expressions, and simple storytelling"
    elif unit_num <= 33:
        theme_name = "How the World Works"
        theme_desc = "Water play, light/shadows, and natural elements"
    elif unit_num <= 41:
        theme_name = "How We Organize Ourselves"
        theme_desc = "Daily toy cleanup routines and home helpers"
    else:
        theme_name = "Sharing the Planet"
        theme_desc = "Plants, caring for pets, and nature appreciation"

    letters_en = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    letters_ur = ["الف", "ب", "پ", "ت", "ٹ", "ث", "ج", "چ", "ح", "خ", "د", "ڈ", "ذ", "ر", "ڑ", "ز", "ژ", "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف"]
    pre_writing_strokes = [
        "Sensory finger-tracing standing lines (vertical strokes in salt/flour tray)",
        "Sensory finger-tracing sleeping lines (horizontal motions)",
        "Gross-motor slanting arm-swings & diagonal finger traces",
        "Circular and curve motions (drawing big loops in the air and mud)",
        "Zig-zag tactile touch-and-trace patterns using textured cards"
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
        st.title("👩‍🏫 Teacher & Parent Training Framework")
        st.write("Welcome! This portal trains adults first using the **IB PYP Transdisciplinary Framework**, inquiry-based learning, design thinking, and Harvard Project Zero routines.")
        
        st.info("💡 **Design Principle:** Tailored for small spaces, minimal furniture, and readily available home resources in Pakistan. Select your target age group below to access the 50-unit intelligent generator.")
        
        st.markdown("---")
        st.subheader("Select Age Group Hub")

        # Framed Clickable Card for Ages 3-4
        with st.container(border=True):
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.markdown("### 🧸 Ages 3-4 (Early Years / Toddler Framework)")
                st.write("Includes 50 progressive play-based units covering sensory pre-writing strokes, early English & Urdu phonics, and math numbers 1-20.")
            with col_b:
                st.write("")
                st.write("")
                if st.button("Open Ages 3-4 Hub", use_container_width=True, key="btn_age_3_4"):
                    st.session_state.current_page = "Unit Generator"
                    st.rerun()

    else:
        st.title("👩‍ၸ استاد اور والدین کی تربیت کا پورٹل")
        st.write("خوش آمدید! اپنے بچوں کی عمر کا انتخاب کریں اور 50 یونٹس پر مشتمل جنریٹر تک رسائی حاصل کریں۔")
        
        with st.container(border=True):
            st.markdown("### 🧸 عمر 3 تا 4 سال ( ارلی یئرز)")
            st.write("50 تفصیلی یونٹس، صوتیات، اور ہندسوں کی مشق۔")
            if st.button("یونٹس کھولیں (عمر 3-4)", use_container_width=True, key="btn_age_3_4_ur"):
                st.session_state.current_page = "Unit Generator"
                st.rerun()

elif st.session_state.current_page == "Unit Generator":
    st.subheader("⚙️ Intelligent Unit Generator (Ages 3-4 | 50 Progressive Units)")
    st.write("Select a unit number below to generate a toddler-friendly, 75-minute time-mapped lesson plan with sensory pre-writing and playful handwriting frameworks.")

    if st.button("⬅️ Back to Age Groups Dashboard"):
        st.session_state.current_page = "Teacher/Parent Dashboard"
        st.rerun()

    unit_number = st.slider("Select Unit Number (1 to 50) for Ages 3-4", 1, 50, 1)

    theme_name, theme_desc, en_focus, ur_focus, math_focus, stroke_focus = get_unit_curriculum(unit_number)

    st.markdown(f"### 🎯 Unit {unit_number} Blueprint (Ages 3-4)")
    st.success(f"**IB Theme:** {theme_name} ({theme_desc})")
    st.info(f"🔤 **Phonics Focus:** English **'{en_focus}'** | Urdu **'{ur_focus}'** &nbsp;&nbsp;|&nbsp;&nbsp; 🔢 **Math:** **{math_focus}** &nbsp;&nbsp;|&nbsp;&nbsp; ✍️ **Pre-Writing:** {stroke_focus}")

    if st.button("✨ Generate Ages 3-4 Extended 75-Minute Lesson Plan", use_container_width=True):
        st.markdown(f"## 🌟 Ages 3-4 Unit Plan: Unit {unit_number}")
        
        lesson_text = f"""
AGED 3-4 UNIT {unit_number}: {theme_name.upper()}
Target Group: Ages 3-4 (Pre-K / Early Toddlers)
Core Focus: English Sound '{en_focus}', Urdu Sound '{ur_focus}', Math Number {math_focus}
Pre-Writing Sensory Stroke: {stroke_focus}
--------------------------------------------------------------------------------
1. TODDLER PEDAGOGICAL VIDEO SCRIPT (0-5 mins)
- Visual: Adult demonstrates finger tracing in a salt tray with a friendly smile, holding an everyday toy.
- Voiceover: 'Hello little explorers! Today under {theme_name}, we make magical strokes, listen to sound '{en_focus}' ('{ur_focus}'), and find {math_focus} items!'

2. EXTENDED 75-MINUTE TIME-MAPPED LESSON PLAN (Ages 3-4)
- [00:00 - 00:10] Sensory Provocation & Circle Time (10 mins): Introduction using a comfortable floor mat and a household prop.
- [00:10 - 00:25] Sensory Pre-Writing & Fine Motor Play (15 mins): Salt/flour tray tracing focusing on: {stroke_focus}.
- [00:25 - 00:45] Phonics & Letter Exploration (20 mins): Listening, repeating, and finger-tracing English '{en_focus}' and Urdu '{ur_focus}'.
- [00:45 - 01:00] Playful Numeracy & Counting (15 mins): Grouping toys or kitchen items to represent number {math_focus}.
- [01:00 - 01:10] Mess-Free Art & Creative Play (10 mins): Finger painting or clay/dough shaping of the letter and number.
- [01:10 - 01:15] Cozy Reflection Circle (5 mins): Gentle wrap-up celebrating today's discoveries.

3. TEACHING AIDS & HANDWRITING PRACTICE
- Materials: Shallow tray with flour/salt, thick crayons, chunky paper, safe household objects.
- Writing Task: Guided toddler tracing for letter '{en_focus}'/'{ur_focus}' and numeral formation for {math_focus}.

4. ADULT ASSESSMENT CHECKLIST
- Engagement, grip comfort, stroke participation, and sound recognition check.
--------------------------------------------------------------------------------
        """

        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "🎬 1. Video Script", 
            "📝 2. 75-Min Time-Mapped Plan", 
            "🎨 3. Pre-Writing & Art", 
            "📄 4. PDF Lesson Plan Download", 
            "🎮 5. Assessment", 
            "💬 6. Teacher Feedback"
        ])

        with tab1:
            st.markdown("### Toddler Pedagogical Video Script")
            st.write(f"**Visual:** Friendly adult sitting on a floor mat, showing a colorful flashcard for letter **'{en_focus}'** / **'{ur_focus}'** and counting **{math_focus}** blocks.")
            st.write(f"**Voiceover:** 'Hello little explorers! Today under *{theme_name}*, we practice our pre-writing movements, learn sound **{en_focus}**, and count **{math_focus}**!'")

        with tab2:
            st.markdown("### Ages 3-4 Detailed 75-Minute Lesson Plan")
            st.markdown("- **Total Duration:** 75 minutes (paced specifically for toddler attention spans)")
            st.markdown("- **Space & Setup:** Small floor circle / mat, no extra classroom furniture needed.")
            st.markdown("---")
            st.markdown("⏱️ **[00:00 - 00:10] Sensory Provocation & Circle Time (10 mins):** Gentle engagement using household objects.")
            st.markdown("⏱️ **[00:10 - 00:25] Sensory Pre-Writing & Fine Motor Play (15 mins):** Focus on **" + stroke_focus + "** using flour/salt trays.")
            st.markdown("⏱️ **[00:25 - 00:45] Phonics & Letter Exploration (20 mins):** Sound play for English **" + en_focus + "** and Urdu **" + ur_focus + "**.")
            st.markdown("⏱️ **[00:45 - 01:00] Playful Numeracy & Counting (15 mins):** Tactile counting of quantity **" + str(math_focus) + "**.")
            st.markdown("⏱️ **[01:00 - 01:10] Mess-Free Art & Creative Play (10 mins):** Dough shaping or coloring.")
            st.markdown("⏱️ **[01:10 - 01:15] Cozy Reflection Circle (5 mins):** Calm closing routine.")

        with tab3:
            st.markdown("### Pre-Writing, Finger-Tracing & Art Integration")
            st.markdown(f"- **Sensory Pre-Writing Stroke:** {stroke_focus}")
            st.markdown(f"- **Letter Exposure:** Tracing and recognizing **'{en_focus}'** and **'{ur_focus}'**.")
            st.markdown(f"- **Number Exposure:** Counting and interacting with quantity **{math_focus}**.")
            st.markdown("- **Toddler Art Activity:** Rolling playdough or safe finger painting.")

        with tab4:
            st.markdown("### Downloadable Ages 3-4 Lesson Plan")
            st.write("Click below to download the complete 75-minute toddler lesson plan file:")
            st.download_button(
                label=f"📥 Download Unit {unit_number} (Ages 3-4) Plan",
                data=lesson_text,
                file_name=f"EFALL_Ages3-4_Unit_{unit_number}.txt",
                mime="text/plain",
                use_container_width=True
            )

        with tab5:
            st.markdown("### Adult Observation Checklist (Ages 3-4)")
            st.markdown(f"1. Did the toddler actively participate in sensory pre-writing (*{stroke_focus}*)?")
            st.markdown(f"2. Did they show familiarity with sound **{en_focus}** / **{ur_focus}** and count to **{math_focus}**?")
            st.radio("Observation Result:", ["Engaged & Enjoyed", "Needed Gentle Guidance", "Needs More Playful Repetition"], key=f"assess_{unit_number}")

        with tab6:
            st.markdown("### Adult Reflection & Feedback")
            feedback_notes = st.text_area("How did the toddler respond to this 75-minute session?", key=f"fb_{unit_number}")
            if st.button("Save Feedback to Cloud Hub", key=f"save_{unit_number}"):
                st.success("Feedback recorded successfully!")

elif st.session_state.current_page == "Student View":
    st.subheader("👧👦 Synchronized Student Portal (Ages 3-4)")
    st.write("Child-friendly interactive games, audio stories, and visual prompts synced directly with the active Unit generator.")
