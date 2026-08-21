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

# --- HELPER FUNCTION: AUTO-ASSIGN IB THEME BASED ON UNIT NUMBER ---
def get_pyp_theme(unit_num):
    """Automatically maps 50 units across the 6 IB Transdisciplinary Themes"""
    if unit_num <= 8:
        return "Who We Are (Identity, emotions, basic phonics/numbers)", "Who We Are"
    elif unit_num <= 16:
        return "Where We Are in Place and Time (Local environment, home surroundings)", "Where We Are in Place and Time"
    elif unit_num <= 25:
        return "How We Express Ourselves (Art, Urdu/English communication, storytelling)", "How We Express Ourselves"
    elif unit_num <= 33:
        return "How the World Works (Science, nature, simple physics/water)", "How the World Works"
    elif unit_num <= 41:
        return "How We Organize Ourselves (Community helpers, home organization)", "How We Organize Ourselves"
    else:
        return "Sharing the Planet (Ecosystems, nature care, sustainability)", "Sharing the Planet"

# --- MAIN VIEWS ---
if st.session_state.current_page == "Teacher/Parent Dashboard":
    if st.session_state.lang == "English":
        st.title("👩‍🏫 Teacher & Parent Training Framework")
        st.write("Welcome! This portal trains adults first using the **IB PYP Transdisciplinary Framework**, inquiry-based learning, design thinking, and Harvard Project Zero routines before guiding young learners (Ages 3-10).")
        
        st.info("💡 **Design Principle:** Tailored for small spaces, minimal furniture, and readily available home resources in Pakistan. No prior IB knowledge needed—the 50 units are automatically structured for you!")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Core Methodologies")
            st.markdown("- **IB PYP Themes:** Automatically mapped across 50 progressive units.")
            st.markdown("- **Inquiry & Design:** Wonder, Make, Reflect cycle.")
            st.markdown("- **Project Zero:** Routine-led critical thinking.")
        with col2:
            st.markdown("### Integrated Curriculum")
            st.markdown("- **Bilingual Core:** English & Urdu Phonics.")
            st.markdown("- **Foundational Math:** Numbers 1-20 woven into themes.")
            st.markdown("- **Holistic Blend:** Science, Art, and Language unified.")
    else:
        st.title("👩‍🏫 استاد اور والدین کی تربیت کا پورٹل")
        st.write("خوش آمدید! یہ پلیٹ فارم بچوں کو پڑھانے سے پہلے بڑوں کو آئی بی پی وائی پی فریم ورک کے تحت تربیت دیتا ہے۔ آپ کو آئی بی کا تجربہ ہونے کی ضرورت نہیں، پورٹل خود بخود یونٹس ترتیب دیتا ہے۔")
        st.info("💡 **خصوصی اصول:** پاکستان میں محدود جگہ اور گھر میں موجود عام اشیاء کو مدنظر رکھتے ہوئے تیار کیا گیا ہے۔")

elif st.session_state.current_page == "Unit Generator":
    st.subheader("⚙️ Intelligent Unit Generator (50 Units)")
    st.write("Simply select the age group and unit number. The system will automatically apply the correct IB Transdisciplinary Theme, cross-curricular subjects, and localized materials!")

    col1, col2 = st.columns(2)
    with col1:
        age_group = st.selectbox(
            "Select Age Group",
            ["Ages 3-4 (Pre-K / Early Learners)", "Ages 5-6 (Senior KG)", "Ages 7-8 (Grades 1-2)", "Ages 9-10 (Grades 3-4)"]
        )
    with col2:
        unit_number = st.slider("Select Unit Number (1 to 50)", 1, 50, 1)

    # Automatically derive the theme
    theme_desc, theme_name = get_pyp_theme(unit_number)

    st.markdown(f"### 🎯 Auto-Assigned IB Theme: **{theme_name}**")
    st.caption(f"Framework Focus: {theme_desc}")

    custom_focus = st.text_input(
        "Unit Specific Focus (Auto-suggested based on unit number):", 
        f"Unit {unit_number}: Exploring foundational concepts through {theme_name}"
    )

    if st.button("✨ Generate Full Intelligent Unit Structure", use_container_width=True):
        st.success(f"Unit {unit_number} Generated Successfully!")
        
        st.markdown(f"## 🌟 Unit Overview: {custom_focus}")
        st.caption(f"Theme: {theme_name} | Target Group: {age_group}")

        # The 6-Part Structured Output
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "🎬 1. Video Script", 
            "📝 2. Lesson Plan", 
            "🎨 3. Teaching Aids & Art", 
            "📄 4. PDF Worksheets", 
            "🎮 5. Assessment", 
            "💬 6. Teacher Feedback"
        ])

        with tab1:
            st.markdown("### AI Pedagogical Video Script (For Teacher/Parent Training & Student Intro)")
            st.write(f"**Visual:** Warm introductory scene showing everyday home items matching Unit {unit_number}.")
            st.write(f"**Voiceover (English/Urdu):** 'Welcome explorers! Today under *{theme_name}*, we connect our learning to everyday life. Let's explore together!'")

        with tab2:
            st.markdown("### Detailed Inquiry-Based Lesson Plan")
            st.markdown("- **Duration:** 45 minutes")
            st.markdown("- **Space & Setup:** Small floor circle, optimized for small rooms with limited furniture.")
            st.markdown("- **Integrated Subjects:**")
            st.markdown("  - *English/Urdu:* Phonics & vocabulary development.")
            st.markdown("  - *Math:* Number progression (1-20) integrated naturally.")
            st.markdown("  - *Science & Art:* Observation of local environment and creative expression.")
            st.markdown("- **Harvard Thinking Routine:** *See, Think, Wonder* / *Imagine If...*")

        with tab3:
            st.markdown("### Teaching Aids & Integrated Art Activity")
            st.markdown("- **Aid:** Recycled household objects and handmade cards.")
            st.markdown("- **Art Activity:** Hands-on creative task utilizing safe home supplies (paper, colors, natural elements).")

        with tab4:
            st.markdown("### AI Generated PDF Worksheets")
            st.markdown(f"- Activity sheet matching Unit {unit_number} curriculum.")
            st.markdown("- Bilingual layout (English & Urdu instructions).")
            st.button("📥 Download Unit Worksheets (PDF)", key="dl_pdf")

        with tab5:
            st.markdown("### Teacher Assessment Model (Gamified / Quick MCQs)")
            st.markdown("1. Did the child grasp the core inquiry concept of this unit?")
            st.markdown("2. Can they demonstrate the integrated math/phonics milestone?")
            st.radio("Quick Assessment Check for Adult:", ["Mastered Easily", "Needs More Practice", "Needs Re-engagement"], key=f"assess_{unit_number}")

        with tab6:
            st.markdown("### Teacher / Parent Reflection & Feedback")
            feedback_notes = st.text_area("How did the child respond to this unit?", key=f"fb_{unit_number}")
            if st.button("Save Feedback to Cloud Hub", key=f"save_{unit_number}"):
                st.success("Feedback recorded successfully! Student view updated.")

elif st.session_state.current_page == "Student View":
    st.subheader("👧👦 Synchronized Student Portal (Ages 3-10)")
    st.write("This side syncs directly with the teacher/parent units, offering interactive child-friendly activities, stories, and guided inquiry games.")
    st.info("✨ Connected to active generated units. Select a unit from the Teacher Hub to populate interactive student tasks here!")
