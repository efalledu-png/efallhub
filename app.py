import streamlit as st
import json
from google import genai

# Page config
st.set_page_config(page_title="IB PYP Central Portal", layout="wide")

# Custom styling for clean portal cards and 4-quadrant layout
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
        min-height: 250px;
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
        st.write("Access curriculum frameworks, lesson generators, small-space maker challenges, and home connections.")
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

    # LEVEL 3: Unit Content with 4-Quadrant Column Layout
    else:
        unit = st.session_state['selected_unit']
        if st.button("⬅️ Back to Units"):
            st.session_state['selected_unit'] = None
            st.rerun()
            
        st.header(f"📚 {unit}")
        st.write("Explore the four core components for this unit below:")
        st.divider()

        # 4-QUADRANT LAYOUT (2x2 Column Grid)
        row1_col1, row1_col2 = st.columns(2)
        row2_col1, row2_col2 = st.columns(2)

        # --- QUADRANT 1: LESSON PLAN ---
        with row1_col1:
            st.markdown('<div class="quadrant-box">', unsafe_allow_html=True)
            st.markdown("### 📋 1. Lesson Plan")
            
            if st.session_state['main_portal'] == 'ParentTeacher':
                age_group = st.selectbox("Age Group", ["Toddlers & Pre-K (Ages 3-4)", "Junior Kindergarten (Ages 4-5)", "Senior Kindergarten (Ages 5-6)", "Early Primary (Ages 7-10)"], key=f"age_{unit}")
                central_idea = st.text_input("Central Idea", "Inquiry drives our understanding of the world.", key=f"ci_{unit}")
                
                if st.button("Generate Bilingual Plan", key=f"gen_{unit}"):
                    with st.spinner("Generating via Gemini..."):
                        try:
                            client = genai.Client()
                            system_instruction = f"""
                            You are an expert IB PYP bilingual curriculum designer specializing in English and Urdu instruction. 
                            - Target Age Group: {age_group}
                            - Classroom Constraints: Very small physical space with limited furniture. All STEAM maker challenges must use minimal, compact materials that fit on student desks.
                            - Output format: STRICTLY valid JSON only, matching the exact requested schema. No markdown outside JSON.
                            """
                            user_prompt = f"Generate a transdisciplinary lesson plan for unit '{unit}' with Central Idea: '{centralIdea}'."

                            response = client.models.generate_content(
                                model='gemini-2.5-flash',
                                contents=user_prompt,
                                config={
                                    'system_instruction': system_instruction,
                                    'response_mime_type': 'application/json',
                                }
                            )
                            st.session_state[f'lesson_{unit}'] = json.loads(response.text)
                            st.success("Generated!")
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
                            st.write(f"**Routine:** {phase.get('project_zero_routine', 'N/A')}")
                            if "driving_challenge" in phase:
                                st.write(f"**Challenge:** {phase.get('driving_challenge')}")
                            if "materials" in phase:
                                st.write(f"**Materials (Small Space):** {', '.join(phase.get('materials', []))}")
                            
                            script_data = phase.get('bilingual_teacher_script', {})
                            if is_urdu:
                                st.markdown(f"**معلم کی ہدایت:**\n{script_data.get('urdu_translation', '')}")
                            else:
                                st.markdown(f"**Script:**\n{script_data.get('english', '')}")
            else:
                st.write("Student view: Access active teacher prompts and interactive lesson steps here.")
            st.markdown('</div>', unsafe_allow_html=True)

        # --- QUADRANT 2: TEACHING AIDS & ACTIVITIES ---
        with row1_col2:
            st.markdown('<div class="quadrant-box">', unsafe_allow_html=True)
            st.markdown("### 🧩 2. Teaching Aids & Activities")
            st.write("Compact, small-space friendly maker cards and hands-on manipulatives.")
            st.markdown("""
            * **Card 1:** Desk-friendly loose parts sorting tray.
            * **Card 2:** Small-space floor mat inquiry cards.
            * **Card 3:** Bilingual vocabulary flashcards (English/Urdu).
            """)
            st.markdown('</div>', unsafe_allow_html=True)

        # --- QUADRANT 3: VIDEOS ---
        with row2_col1:
            st.markdown('<div class="quadrant-box">', unsafe_allow_html=True)
            st.markdown("### 🎬 3. Videos")
            st.write("Curated visual provocations and interactive read-aloud prompts.")
            st.markdown("""
            * 🎥 **Provocation Hook:** Introduction to unit core concepts.
            * 🎥 **Maker Tutorial:** Step-by-step desk construction guide.
            * 🎥 **Story Time:** Bilingual thematic read-aloud session.
            """)
            st.markdown('</div>', unsafe_allow_html=True)

        # --- QUADRANT 4: WORKSHEETS ---
        with row2_col2:
            st.markdown('<div class="quadrant-box">', unsafe_allow_html=True)
            st.markdown("### 📝 4. Worksheets")
            st.write("Downloadable student reflection sheets and drawing prompts.")
            st.markdown("""
            * 📄 **Reflection Sheet:** 'I notice, I wonder' drawing template.
            * 📄 **Math Activity:** Counting & sorting challenge sheet.
            * 📄 **Language Task:** Phonics letter-tracing sheet (English & Urdu).
            """)
            st.markdown('</div>', unsafe_allow_html=True)
