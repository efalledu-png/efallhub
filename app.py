import streamlit as st
import json
from google import genai

# Page config
st.set_page_config(page_title="IB PYP Central Portal", layout="wide")

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
        min-height: 300px;
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
    st.title("🌟 IB PYP Central Educational Portal")
    st.write("Please select your portal to begin:")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        st.markdown("### 🍎 Parent / Teacher Portal")
        st.write("Access automated bilingual lesson plans, STEAM challenges, teaching aids, and worksheets.")
        if st.button("Enter Parent / Teacher Portal", use_container_width=True):
            st.session_state['main_portal'] = 'ParentTeacher'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
            
    with col2:
        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        st.markdown("### 🎒 Student Portal")
        st.write("Explore interactive learning stations, student inquiries, and visual cards.")
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

    st.title(f"📌 {portal_title}")

    # LEVEL 1: 4-QUADRANT AGE SELECTION (3-4, 5-6, 7-8, 9-10)
    if st.session_state['selected_age'] is None:
        st.subheader("Select Age Group (4 Quadrants)")
        st.write("Choose the target age group for your learning environment:")
        
        row1_c1, row1_c2 = st.columns(2)
        row2_c1, row2_c2 = st.columns(2)
        
        ages = [
            ("Ages 3-4 (Early Years / Pre-K)", row1_c1),
            ("Ages 5-6 (Senior Kindergarten)", row1_c2),
            ("Ages 7-8 (Early Primary)", row2_c1),
            ("Ages 9-10 (Upper Primary)", row2_c2)
        ]
        
        for age_label, col in ages:
            with col:
                st.markdown(f'<div class="age-card">', unsafe_allow_html=True)
                st.markdown(f"### 👶 {age_label}")
                if st.button(f"Select {age_label.split()[0]} {age_label.split()[1]}", key=f"age_btn_{age_label}"):
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

    # LEVEL 4: 4-QUADRANT UNIT WORKSPACE WITH AUTO-GENERATED LESSON
    else:
        unit = st.session_state['selected_unit']
        age_group = st.session_state['selected_age']
        
        if st.button("⬅️ Back to Units"):
            st.session_state['selected_unit'] = None
            st.rerun()
            
        st.header(f"📚 {unit} | Target: {age_group}")
        st.divider()

        # Automatically generate lesson plan in the background session if not already generated
        if f'auto_lesson_{unit}' not in st.session_state and st.session_state['main_portal'] == 'ParentTeacher':
            with st.spinner("Automatically generating age-appropriate bilingual lesson plan with Gemini..."):
                try:
                    client = genai.Client()
                    system_instruction = f"""
                    You are an expert IB PYP bilingual curriculum designer and early years educator specializing in English and Urdu instruction. 
                    - Target Age Group: {age_group}
                    - Parameters Required: Full integration of English, Urdu, phonics, reading, writing, math (including age-appropriate addition and subtraction), STEAM design thinking, and inquiry routines.
                    - Classroom Constraints: Very small physical space with limited furniture. All STEAM maker challenges must use minimal, compact materials that fit on student desks or small floor mats.
                    - Output format: STRICTLY valid JSON only, matching the exact schema containing bilingual academics and multi-phase teacher scripts using Harvard Project Zero routines. No markdown outside JSON.
                    """
                    user_prompt = f"Generate an automated comprehensive transdisciplinary lesson plan for unit '{unit}' for age group {age_group}."

                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=user_prompt,
                        config={
                            'system_instruction': system_instruction,
                            'response_mime_type': 'application/json',
                        }
                    )
                    st.session_state[f'auto_lesson_{unit}'] = json.loads(response.text)
                except Exception as e:
                    st.error(f"Error generating automated plan: {e}")

        row1_col1, row1_col2 = st.columns(2)
        row2_col1, row2_col2 = st.columns(2)

        # --- QUADRANT 1: LESSON PLAN (Auto-Generated & Multilingual) ---
        with row1_col1:
            st.markdown('<div class="quadrant-box">', unsafe_allow_html=True)
            st.markdown("### 📋 1. Lesson Plan (Auto-Generated)")
            
            if st.session_state['main_portal'] == 'ParentTeacher':
                if f'auto_lesson_{unit}' in st.session_state:
                    data = st.session_state[f'auto_lesson_{unit}']
                    lang = st.radio("Language / زبان", ["English", "Urdu (اردو)"], horizontal=True, key=f"lang_{unit}")
                    is_urdu = (lang == "Urdu (اردو)")

                    acad = data.get("bilingual_academics", {})
                    if is_urdu:
                        st.info(f"🔤 **Phonics & Reading:** {acad.get('urdu', {}).get('phonics_focus')}\n\n📖 **Writing & Literacy:** {acad.get('urdu', {}).get('literacy_task')}\n\n🔢 **Math (+/-):** {acad.get('urdu', {}).get('math_focus')}")
                    else:
                        st.info(f"🔤 **Phonics & Reading:** {acad.get('english', {}).get('phonics_focus')}\n\n📖 **Writing & Literacy:** {acad.get('english', {}).get('literacy_task')}\n\n🔢 **Math (+/-):** {acad.get('english', {}).get('math_focus')}")

                    for key, phase in data.get("phases", {}).items():
                        with st.expander(f"📌 {phase.get('title', 'Phase')}"):
                            st.write(f"**Inquiry Routine:** {phase.get('project_zero_routine', 'N/A')}")
                            if "driving_challenge" in phase:
                                st.write(f"**STEAM Challenge:** {phase.get('driving_challenge')}")
                            if "materials" in phase:
                                st.write(f"**Compact Materials:** {', '.join(phase.get('materials', []))}")
                            
                            script_data = phase.get('bilingual_teacher_script', {})
                            if is_urdu:
                                st.markdown(f"**معلم کی ہدایت:**\n{script_data.get('urdu_translation', '')}")
                            else:
                                st.markdown(f"**Teacher Script:**\n{script_data.get('english', '')}")
                else:
                    st.write("Loading automated lesson plan...")
            else:
                st.write("Student view: Interactive station prompts active.")
            st.markdown('</div>', unsafe_allow_html=True)

        # --- QUADRANT 2: TEACHING AIDS & ACTIVITIES ---
        with row1_col2:
            st.markdown('<div class="quadrant-box">', unsafe_allow_html=True)
            st.markdown("### 🧩 2. Teaching Aids & Activities")
            st.write("Small-space optimized manipulatives and design thinking tools:")
            st.markdown("""
            * **Desk-Top Sorting Trays:** Compact loose-parts bins for math counting (+/-).
            * **Floor Mat Inquiry Cards:** Visual prompts for tight classroom spaces.
            * **Bilingual Word Wall:** English/Urdu vocabulary cards for reading and writing.
            """)
            st.markdown('</div>', unsafe_allow_html=True)

        # --- QUADRANT 3: VIDEOS ---
        with row2_col1:
            st.markdown('<div class="quadrant-box">', unsafe_allow_html=True)
            st.markdown("### 🎬 3. Videos")
            st.write("Curated media hooks and interactive read-alouds:")
            st.markdown("""
            * 🎥 **Provocation Hook:** Core concept introduction clip.
            * 🎥 **STEAM Maker Tutorial:** Desk-friendly construction guide.
            * 🎥 **Bilingual Story Session:** English and Urdu read-aloud.
            """)
            st.markdown('</div>', unsafe_allow_html=True)

        # --- QUADRANT 4: WORKSHEETS ---
        with row2_col2:
            st.markdown('<div class="quadrant-box">', unsafe_allow_html=True)
            st.markdown("### 📝 4. Worksheets")
            st.write("Printable early years learning sheets:")
            st.markdown("""
            * 📄 **Reading & Phonics Sheet:** Letter-tracing and sound matching.
            * 📄 **Math Activity:** Simple addition and subtraction visual worksheets.
            * 📄 **Reflection Sheet:** 'I Notice, I Wonder' drawing prompt.
            """)
            st.markdown('</div>', unsafe_allow_html=True)
