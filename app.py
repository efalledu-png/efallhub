import streamlit as st

# Page config
st.set_page_config(
    page_title="EFALL (Education For All) | IB PYP Portal", 
    layout="wide",
    page_icon="📚"
)

st.markdown("""
    <style>
    .card-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        margin-bottom: 15px;
        text-align: center;
    }
    .quadrant-box {
        padding: 15px;
        border-radius: 8px;
        background-color: #ffffff;
        border: 1px solid #ced4da;
        min-height: 280px;
        margin-bottom: 15px;
    }
    .age-card {
        padding: 25px;
        border-radius: 12px;
        background-color: #e8f4f8;
        border: 2px solid #0077b6;
        text-align: center;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

PYP_THEMES = [
    "1. Who we are",
    "2. Where we are in place and time",
    "3. How we express ourselves",
    "4. How the world works",
    "5. How we organize ourselves",
    "6. Sharing the planet"
]

def get_units_for_theme(theme_name):
    return [f"{theme_name} - Unit {i}" for i in range(1, 9)]

# Initialize session state for navigation
if 'main_portal' not in st.session_state:
    st.session_state['main_portal'] = 'Home'
if 'selected_age' not in st.session_state:
    st.session_state['selected_age'] = None
if 'selected_theme' not in st.session_state:
    st.session_state['selected_theme'] = None
if 'selected_unit' not in st.session_state:
    st.session_state['selected_unit'] = None

# --- MAIN LANDING (2 Main Portals) ---
if st.session_state['main_portal'] == 'Home':
    st.title("🌟 EFALL — Education For All | IB PYP Portal")
    st.write("An open-source digital learning platform providing quality educational experiences for educators, parents, and students.")
    st.write("Please select your portal to begin:")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        st.markdown("### 🍎 Parent / Teacher Portal")
        st.write("Instant bilingual lesson plans (English/Urdu), small-space STEAM challenges, teaching aids, and worksheets.")
        if st.button("Enter Parent / Teacher Portal", use_container_width=True):
            st.session_state['main_portal'] = 'ParentTeacher'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
            
    with col2:
        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        st.markdown("### 🎒 Student Portal")
        st.write("Interactive learning stations, student inquiries, and visual curriculum cards.")
        if st.button("Enter Student Portal", use_container_width=True):
            st.session_state['main_portal'] = 'Student'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- PORTAL WORKFLOW ---
elif st.session_state['main_portal'] in ['ParentTeacher', 'Student']:
    portal_title = "Parent & Teacher Workspace" if st.session_state['main_portal'] == 'ParentTeacher' else "Student Learning Hub"
    
    if st.button("⬅️ Back to Main Portals"):
        st.session_state['main_portal'] = 'Home'
        st.session_state['selected_age'] = None
        st.session_state['selected_theme'] = None
        st.session_state['selected_unit'] = None
        st.rerun()

    st.title(f"📌 {portal_title} — EFALL")

    # LEVEL 1: 4-QUADRANT AGE SELECTION (3-4, 5-6, 7-8, 9-10)
    if st.session_state['selected_age'] is None:
        st.subheader("Select Age Group (4 Quadrants)")
        st.write("Choose the target age group for your classroom environment:")
        
        row1_c1, row1_c2 = st.columns(2)
        row2_c1, row2_c2 = st.columns(2)
        
        ages = [
            ("Ages 3-4", row1_c1),
            ("Ages 5-6", row1_c2),
            ("Ages 7-8", row2_c1),
            ("Ages 9-10", row2_c2)
        ]
        
        for age_label, col in ages:
            with col:
                st.markdown(f'<div class="age-card">', unsafe_allow_html=True)
                st.markdown(f"### 👶 {age_label}")
                if st.button(f"Select {age_label}", key=f"age_btn_{age_label}"):
                    st.session_state['selected_age'] = age_label
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)

    # LEVEL 2: SELECT FROM 6 THEMES
    elif st.session_state['selected_theme'] is None:
        if st.button("⬅️ Back to Age Selection"):
            st.session_state['selected_age'] = None
            st.rerun()
            
        st.subheader(f"Selected Age Group: {st.session_state['selected_age']}")
        st.write("Select a Transdisciplinary Theme (6 Themes):")
        
        cols = st.columns(2)
        for idx, theme in enumerate(PYP_THEMES):
            col = cols[idx % 2]
            with col:
                st.markdown(f'<div class="card-box">', unsafe_allow_html=True)
                st.markdown(f"#### {theme}")
                if st.button(f"Explore Theme", key=f"theme_{idx}"):
                    st.session_state['selected_theme'] = theme
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)

    # LEVEL 3: SELECT FROM 8 UNITS
    elif st.session_state['selected_unit'] is None:
        theme = st.session_state['selected_theme']
        if st.button("⬅️ Back to Themes"):
            st.session_state['selected_theme'] = None
            st.rerun()
            
        st.subheader(f"Theme: {theme}")
        units = get_units_for_theme(theme)
        
        cols = st.columns(2)
        for idx, unit in enumerate(units):
            col = cols[idx % 2]
            with col:
                st.markdown(f'<div class="card-box">', unsafe_allow_html=True)
                st.markdown(f"**{unit}**")
                if st.button(f"Open Unit", key=f"unit_{idx}"):
                    st.session_state['selected_unit'] = unit
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)

    # LEVEL 4: 4-QUADRANT UNIT WORKSPACE
    else:
        unit = st.session_state['selected_unit']
        age_group = st.session_state['selected_age']
        
        if st.button("⬅️ Back to Units"):
            st.session_state['selected_unit'] = None
            st.rerun()
            
        st.header(f"📚 {unit} | Target: {age_group}")
        st.divider()

        row1_col1, row1_col2 = st.columns(2)
        row2_col1, row2_col2 = st.columns(2)

        # --- QUADRANT 1: LESSON PLAN & BILINGUAL ACADEMICS ---
        with row1_col1:
            st.markdown('<div class="quadrant-box">', unsafe_allow_html=True)
            st.markdown("### 📋 1. Lesson Plan & Academics")
            
            lang = st.radio("Language / زبان", ["English", "Urdu (اردو)"], horizontal=True, key=f"lang_{unit}")
            is_urdu = (lang == "Urdu (اردو)")

            if is_urdu:
                st.info("🔤 **حروف اور آوازیں (Phonics):** آوازوں کی شناخت اور الفاظ سازی\n\n📖 ** لکھائی (Literacy):** روزمرہ کے موضوع پر جملہ سازی\n\n🔢 **ریاضی (Math +/-):** اشیاء کی گنتی اور جمع تفریق")
                st.markdown("**تدریسی مرحلہ (Project Zero Routine):**\n* **تجسس (I Notice, I Wonder):** طلباء تصویر دیکھ کر سوالات پوچھتے ہیں۔")
            else:
                st.info("🔤 **Phonics & Reading:** Letter sounds and blending practice.\n\n📖 **Writing & Literacy:** Contextual sentence creation task.\n\n🔢 **Math (+/-):** Small-group sorting and simple addition/subtraction.")
                st.markdown("**Inquiry Routine (Harvard Project Zero):**\n* **See, Think, Wonder:** Guided student provocation prompt.")
            
            st.markdown('</div>', unsafe_allow_html=True)

        # --- QUADRANT 2: TEACHING AIDS & ACTIVITIES ---
        with row1_col2:
            st.markdown('<div class="quadrant-box">', unsafe_allow_html=True)
            st.markdown("### 🧩 2. Teaching Aids & Activities")
            st.write("Optimized for compact local classrooms:")
            st.markdown("""
            * **Desk-Top Sorting Trays:** Bins for tactile math counting (+/-).
            * **Floor Mat Inquiry Cards:** Visual prompt cards for tight spaces.
            * **Bilingual Word Wall:** Dual-script English and Urdu vocabulary cards.
            """)
            st.markdown('</div>', unsafe_allow_html=True)

        # --- QUADRANT 3: VIDEOS ---
        with row2_col1:
            st.markdown('<div class="quadrant-box">', unsafe_allow_html=True)
            st.markdown("### 🎬 3. Videos")
            st.write("Curated media hooks & read-alouds:")
            st.markdown("""
            * 🎥 **Provocation Hook:** Core concept introduction clip.
            * 🎥 **STEAM Maker Tutorial:** Desk-friendly construction guide.
            * 🎥 **Bilingual Story Session:** English and Urdu storytelling link.
            """)
            st.markdown('</div>', unsafe_allow_html=True)

        # --- QUADRANT 4: WORKSHEETS ---
        with row2_col2:
            st.markdown('<div class="quadrant-box">', unsafe_allow_html=True)
            st.markdown("### 📝 4. Worksheets")
            st.write("Printable early years learning sheets:")
            st.markdown("""
            * 📄 **Reading & Phonics Sheet:** Letter-tracing and sound matching.
            * 📄 **Math Activity:** Visual addition and subtraction sheets.
            * 📄 **Reflection Sheet:** 'I Notice, I Wonder' drawing template.
            """)
            st.markdown('</div>', unsafe_allow_html=True)
