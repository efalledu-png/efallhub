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
    }
    .quadrant-box {
        padding: 15px;
        border-radius: 8px;
        background-color: #ffffff;
        border: 1px solid #ced4da;
        min-height: 300px;
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
if 'selected_theme' not in st.session_state:
    st.session_state['selected_theme'] = None
if 'selected_unit' not in st.session_state:
    st.session_state['selected_unit'] = None

# --- MAIN LANDING (2 Main Portals) ---
if st.session_state['main_portal'] == 'Home':
    st.title("🌟 IB PYP Central Educational Portal")
    st.write("Please select your portal to explore units across the 6 transdisciplinary themes.")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🍎 Parent / Teacher Portal")
        st.write("Access detailed curriculum frameworks, full lesson generators, small-space STEAM maker challenges, and home connections.")
        if st.button("Enter Parent / Teacher Portal", use_container_width=True):
            st.session_state['main_portal'] = 'ParentTeacher'
            st.rerun()
            
    with col2:
        st.markdown("### 🎒 Student Portal")
        st.write("Explore interactive learning stations, student-friendly inquiries, and visual curriculum cards.")
        if st.button("Enter Student Portal", use_container_width=True):
            st.session_state['main_portal'] = 'Student'
            st.rerun()

# --- THEMES & UNITS NAVIGATION ---
elif st.session_state['main_portal'] in ['ParentTeacher', 'Student']:
    portal_title = "Parent & Teacher Workspace" if st.session_state['main_portal'] == 'ParentTeacher' else "Student Learning Hub"
    
    if st.button("⬅️ Back to Main Portals"):
        st.session_state['main_portal'] = 'Home'
        st.session_state['selected_theme'] = None
        st.session_state['selected_unit'] = None
        st.rerun()

    st.title(f"📌 {portal_title}")

    # LEVEL 1: Select from 6 Themes
    if st.session_state['selected_theme'] is None:
        st.subheader("Select a Transdisciplinary Theme (6 Themes)")
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

    # LEVEL 2: Select from 8 Units within the Theme
    elif st.session_state['selected_unit'] is None:
        theme = st.session_state['selected_theme']
        if st.button("⬅️ Back to Themes"):
            st.session_state['selected_theme'] = None
            st.rerun()
            
        st.subheader(f"Units under: {theme}")
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

    # LEVEL 3: Unit Content with 4-Quadrant Detailed Layout
    else:
        unit = st.session_state['selected_unit']
        if st.button("⬅️ Back to Units"):
            st.session_state['selected_unit'] = None
            st.rerun()
            
        st.header(f"📚 {unit}")
        st.write("Detailed 4-Quadrant Operational Workspace:")
        st.divider()

        row1_col1, row1_col2 = st.columns(2)
        row2_col1, row2_col2 = st.columns(2)

        # --- QUADRANT 1: LESSON PLAN (Backend Sync & Detailed Parameters) ---
        with row1_col1:
            st.markdown('<div class="quadrant-box">', unsafe_allow_html=True)
            st.markdown("### 📋 1. Lesson Plan (AI Generator)")
            
            if st.session_state['main_portal'] == 'ParentTeacher':
                age_group = st.selectbox("Target Age Group", ["Toddlers & Pre-K (Ages 3-4)", "Junior Kindergarten (Ages 4-5)", "Senior Kindergarten (Ages 5-6)", "Early Primary (Ages 7-10)"], key=f"age_{unit}")
                central_idea = st.text_input("Central Idea", "Natural forces shape our environment.", key=f"ci_{unit}")
                
                if st.button("Generate Detailed Plan", key=f"gen_{unit}"):
                    with st.spinner("Connecting to Gemini backend..."):
                        try:
                            client = genai.Client()
                            system_instruction = f"""
                            You are an expert IB PYP bilingual curriculum designer and early years educator specializing in English and Urdu instruction. 
                            - Target Age Group: {age_group}
                            - Classroom Constraints: The physical classroom is very small with limited furniture. All STEAM maker challenges must use minimal, compact materials that fit on student desks or small floor mats.
                            - Output format: STRICTLY valid JSON only, matching the exact requested schema containing bilingual academics (phonics, literacy, math) and multi-phase teacher scripts using Harvard Project Zero routines. No markdown outside JSON.
                            """
                            user_prompt = f"Generate a detailed transdisciplinary lesson plan for unit '{unit}' with Central Idea: '{centralIdea}'."

                            response = client.models.generate_content(
                                model='gemini-2.5-flash',
                                contents=user_prompt,
                                config={
                                    'system_instruction': system_instruction,
                                    'response_mime_type': 'application/json',
                                }
                            )
                            st.session_state[f'lesson_{unit}'] = json.loads(response.text)
                            st.success("Lesson Plan Synced!")
                        except Exception as e:
                            st.error(f"Error: {e}")

                if f'lesson_{unit}' in st.session_state:
                    data = st.session_state[f'lesson_{unit}']
                    lang = st.radio("Language / زبان", ["English", "Urdu (اردو)"], horizontal=True, key=f"lang_{unit}")
                    is_urdu = (lang == "Urdu (اردو)")

                    acad = data.get("bilingual_academics", {})
                    if is_urdu:
                        st.info(f"🔤 **Phonics:** {acad.get('urdu', {}).get('phonics_focus')}\n\n📖 **Literacy:** {acad.get('urdu', {}).get('literacy_task')}\n\n🔢 **Math:** {acad.get('urdu', {}).get('math_focus')}")
                    else:
                        st.info(f"🔤 **Phonics:** {acad.get('english', {}).get('phonics_focus')}\n\n📖 **Literacy:** {acad.get('english', {}).get('literacy_task')}\n\n🔢 **Math:** {acad.get('english', {}).get('math_focus')}")

                    for key, phase in data.get("phases", {}).items():
                        with st.expander(f"📌 {phase.get('title', 'Phase')}"):
                            st.write(f"**Project Zero Routine:** {phase.get('project_zero_routine', 'N/A')}")
                            if "driving_challenge" in phase:
                                st.write(f"**Maker Challenge:** {phase.get('driving_challenge')}")
                            if "materials" in phase:
                                st.write(f"**Compact Materials:** {', '.join(phase.get('materials', []))}")
                            
                            script_data = phase.get('bilingual_teacher_script', {})
                            if is_urdu:
                                st.markdown(f"**معلم کی ہدایت (Urdu Script):**\n{script_data.get('urdu_translation', '')}")
                            else:
                                st.markdown(f"**Teacher Script (English):**\n{script_data.get('english', '')}")
            else:
                st.write("Student active view: Access teacher prompts and inquiry steps here.")
            st.markdown('</div>', unsafe_allow_html=True)

        # --- QUADRANT 2: TEACHING AIDS & ACTIVITIES (Small-Space Maker Focus) ---
        with row1_col2:
            st.markdown('<div class="quadrant-box">', unsafe_allow_html=True)
            st.markdown("### 🧩 2. Teaching Aids & Activities")
            st.write("Optimized for small classrooms with limited furniture:")
            st.markdown("""
            * **Desk-Top Sorting Trays:** Compact compartmentalized bins for loose parts inquiry.
            * **Floor Mat Challenge Cards:** Laminated visual prompts designed for tight spaces.
            * **Bilingual Vocabulary Word Wall:** Dual-script English and Urdu cards for early years language acquisition.
            * **Design Thinking Manipulatives:** Hands-on prototyping tools that fit within a single student desk footprint.
            """)
            st.markdown('</div>', unsafe_allow_html=True)

        # --- QUADRANT 3: VIDEOS ---
        with row2_col1:
            st.markdown('<div class="quadrant-box">', unsafe_allow_html=True)
            st.markdown("### 🎬 3. Videos & Provocations")
            st.write("Curated media resources for inquiry launching:")
            st.markdown("""
            * 🎥 **Thematic Provocation Hook:** Short visual clips to spark inquiry and wonder.
            * 🎥 **Desk-Top Maker Tutorial:** Step-by-step visual guides for compact construction challenges.
            * 🎥 **Bilingual Story Read-Alouds:** Engaging digital story sessions supporting English and Urdu comprehension.
            """)
            st.markdown('</div>', unsafe_allow_html=True)

        # --- QUADRANT 4: WORKSHEETS ---
        with row2_col2:
            st.markdown('<div class="quadrant-box">', unsafe_allow_html=True)
            st.markdown("### 📝 4. Worksheets & Reflections")
            st.write("Printable and digital early years templates:")
            st.markdown("""
            * 📄 **'I Notice, I Wonder' Sheet:** Visual reflection template for young learners.
            * 📄 **Math & Patterning Activity:** Small-scale sorting and counting sheets.
            * 📄 **Bilingual Phonics Tracing:** Letter and vocabulary formation worksheets (English & Urdu).
            """)
            st.markdown('</div>', unsafe_allow_html=True)
