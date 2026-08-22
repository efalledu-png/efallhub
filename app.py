import streamlit as st
import json
from google import genai

# Page config for iPad / browser
st.set_page_config(page_title="IB PYP Bilingual Portal", layout="centered")

st.title("🌱 IB PYP Bilingual Lesson Portal")
st.write("Generate automated, small-space friendly STEAM maker challenges with integrated phonics, literacy, and math in English and Urdu.")

# User inputs
unit_title = st.text_input("Unit Title", "Structures & Habitats")
central_idea = st.text_input("Central Idea", "Natural forces shape our environment.")
age_group = st.selectbox("Age Group", ["Senior Kindergarten (5-6 yrs)", "Grade 1 (6-7 yrs)", "Grade 2 (7-8 yrs)"])

if st.button("Generate Lesson Plan"):
    with st.spinner("Generating bilingual lesson plan with Gemini..."):
        try:
            # Initialize Gemini client (reads from Streamlit secrets or environment variables)
            client = genai.Client()
            
            system_instruction = f"""
            You are an expert IB PYP bilingual curriculum designer specializing in English and Urdu instruction. 
            - Target Age Group: {age_group}
            - Classroom Constraints: Very small physical space with limited furniture. All STEAM maker challenges must use minimal, compact materials that fit on student desks.
            - Output format: STRICTLY valid JSON only, matching the exact requested schema. No markdown outside JSON.
            """

            user_prompt = f"Generate a transdisciplinary lesson plan for the unit '{unitTitle}' with the Central Idea: '{centralIdea}'."

            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=user_prompt,
                config={
                    'system_instruction': system_instruction,
                    'response_mime_type': 'application/json',
                }
            )

            data = json.loads(response.text)
            st.session_state['lesson_data'] = data
            st.success("Lesson generated successfully!")

        except Exception as e:
            st.error(f"Error generating lesson: {e}")

# Display lesson if available in session state
if 'lesson_data' in st.session_state:
    data = st.session_state['lesson_data']
    
    st.divider()
    
    # Language Toggle
    lang = st.radio("Select Language / زبان منتخب کریں", ["English", "Urdu (اردو)"], horizontal=True)
    is_urdu = (lang == "Urdu (اردو)")

    st.subheader(data.get("lesson_title", "Lesson Plan"))
    st.write(f"**Central Idea:** {data.get('central_idea')}")

    # Academics Banner
    st.markdown("### 📚 Academic Targets")
    acad = data.get("bilingual_academics", {})
    if is_urdu:
        st.info(f"🔤 **Phonics:** {acad.get('urdu', {}).get('phonics_focus')}\n\n📖 **Literacy:** {acad.get('urdu', {}).get('literacy_task')}\n\n🔢 **Math:** {acad.get('urdu', {}).get('math_focus')}")
    else:
        st.info(f"🔤 **Phonics:** {acad.get('english', {}).get('phonics_focus')}\n\n📖 **Literacy:** {acad.get('english', {}).get('literacy_task')}\n\n🔢 **Math:** {acad.get('english', {}).get('math_focus')}")

    # Phases Accordion / Expanders
    phases = data.get("phases", {})
    for key, phase in phases.items():
        with st.expander(f"📌 {phase.get('title', 'Phase')}"):
            st.write(f"**Routine:** {phase.get('project_zero_routine', 'N/A')}")
            
            if "driving_challenge" in phase:
                st.write(f"**Challenge:** {phase.get('driving_challenge')}")
            if "materials" in phase:
                st.write(f"**Materials (Small Space):** {', '.join(phase.get('materials', []))}")
            
            script_data = phase.get('bilingual_teacher_script', {})
            if is_urdu:
                st.markdown(f"**معلم کی ہدایت (Urdu):**\n\n{script_data.get('urdu_translation', '')}")
            else:
                st.markdown(f"**Teacher Script (English):**\n\n{script_data.get('english', '')}")
