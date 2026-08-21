import streamlit as st
import base64
from datetime import date

# Page Configuration
st.set_page_config(
    page_title="EFALL Master Hub | آسان تعلیمی پورٹل",
    page_icon="🌟",
    layout="wide"
)

# Initialize Session State
if "lang" not in st.session_state:
    st.session_state.lang = "English"
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"
if "reflection_logs" not in st.session_state:
    st.session_state.reflection_logs = []

def create_download_button(content, filename, label):
    b64 = base64.b64encode(content.encode('utf-8')).decode('utf-8')
    return f'<a href="data:text/plain;charset=utf-8;base64,{b64}" download="{filename}" style="text-decoration:none;"><div style="background:#2e7d32;color:white;padding:12px;text-align:center;border-radius:8px;font-weight:bold;font-size:16px;margin-top:10px;">📥 {label}</div></a>'

# --- NAVIGATION SIDEBAR ---
st.sidebar.title("🌟 EFALL آسان ہب")
st.sidebar.caption("Educated Mother Education Nation")

if st.sidebar.button("🏠 Home / مین صفحہ", use_container_width=True):
    st.session_state.current_page = "Home"
    st.rerun()
if st.sidebar.button("🛠️ Force & Engineering Lesson / فورس کا سبق", use_container_width=True):
    st.session_state.current_page = "Force Lesson"
    st.rerun()
if st.sidebar.button("📝 My Diary / میری ڈائری", use_container_width=True):
    st.session_state.current_page = "Reflection Log"
    st.rerun()

# --- HOME PAGE ---
if st.session_state.current_page == "Home":
    st.title("🌟 Welcome to EFALL Simple Teaching Hub")
    st.markdown("### 🎯 Tap below to open your step-by-step teaching module:")
    
    if st.button("🚪 Unit: Force, Friction & Sound (فورس اور آواز کا سبق)", use_container_width=True):
        st.session_state.current_page = "Force Lesson"
        st.rerun()
        
    st.markdown("---")
    if st.button("📝 Open My Teaching Diary (میری ڈائری)", use_container_width=True):
        st.session_state.current_page = "Reflection Log"
        st.rerun()

# --- STEP-BY-STEP CHRONOLOGICAL LESSON COACH ---
elif st.session_state.current_page == "Force Lesson":
    if st.button("⬅️ Back / واپس جائیں"):
        st.session_state.current_page = "Home"
        st.rerun()

    st.title("🛠️ Step-by-Step Teaching Guide: Force & Silencer Challenge")
    st.info("🌐 **IB Theme:** How the World Works &nbsp;|&nbsp; 👩‍🏫 **Teacher Coaching Mode:** Chronological Flow for Small Classrooms")

    # --- TOP 3-STEP VISUAL SUMMARY ---
    st.markdown("### 📌 Quick Overview Card")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div style="background: #e8f8f5; border: 2px solid #1abc9c; padding: 10px; border-radius: 8px; text-align: center;">
            <h4 style="color: #16a085; margin:0;">1️⃣ Step 1: Open</h4>
            <p style="font-size: 12px; margin-top: 5px;">Move furniture, create sound anomalies, do 'Imagine If' circle talk.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div style="background: #fdf2e9; border: 2px solid #f39c12; padding: 10px; border-radius: 8px; text-align: center;">
            <h4 style="color: #d35400; margin:0;">2️⃣ Step 2: Build</h4>
            <p style="font-size: 12px; margin-top: 5px;">Measure with fingers, tally counts, build door/chair silencers.</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div style="background: #ebf5fb; border: 2px solid #3498db; padding: 10px; border-radius: 8px; text-align: center;">
            <h4 style="color: #2980b9; margin:0;">3️⃣ Step 3: Reflect</h4>
            <p style="font-size: 12px; margin-top: 5px;">Post on boards, take Polaroid pictures, discuss caring classroom.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("⏱️ Chronological Teacher Script & Action Timeline")
    st.write("Follow these exact chronological steps in your classroom from start to finish:")

    # CHRONOLOGICAL TABS
    t1, t2, t3, t4 = st.tabs([
        "🕒 Phase 1: Setup & Start (0-10 mins)", 
        "🕒 Phase 2: The Inquiry Tour (10-20 mins)", 
        "🕒 Phase 3: The Challenge & Worksheet (20-40 mins)", 
        "🕒 Phase 4: Wrap-up & Reflection (40-60 mins)"
    ])

    with t1:
        st.markdown("### Step-by-Step Instructions: Opening & Provocation")
        st.markdown("""
        * **1. Before Students Arrive (Room Setup):** 
          * Push your few pieces of classroom furniture to the sides to maximize center floor space.
          * Deliberately leave the door slightly misaligned so it makes a screeching noise, pull a table out so its legs scrape loudly, and place the supplies bin right in the middle of the circle carpet.
          * Set up toy tracks on your desk with a car and ball.
        * **2. Gathering the Children:** 
          * Bring children to the floor carpet in groups of 5.
        * **3. What to Say Out Loud (Teacher Script):** 
          * *"Hello little engineers! Today we are going to look at how things move and make sounds using Push and Pull."*
        * **4. Introduce the Thinking Routine:** 
          * Ask the class: **'Imagine if'** our classroom door and chairs are always this loud and noisy every time we move. How will that affect our ears and our learning? How will fixing it make us kinder to each other?
        """)

    with t2:
        st.markdown("### Step-by-Step Instructions: Class Tour & Sensory Exploration")
        st.markdown("""
        * **1. What to Do:** 
          * Take your groups on a quick interactive walk around the small classroom. Have them touch the screeching door and slide the chairs.
        * **2. What to Ask (Scaffolding Questions):** 
          * *“Did I just hear a funny noise when pulling that?”*
          * *“Is it hard to push this table? Why do you think it feels rough?”*
        * **3. Action Task:** 
          * Hand out sticky notes. Let students paste sticky notes directly onto the objects that are making noise or are out of order.
        """)

    with t3:
        st.markdown("### Step-by-Step Instructions: The Engineering Challenge & Worksheet")
        st.markdown("""
        * **1. Introduce the Challenge (When to start):** 
          * Tell students: *"Now you are engineers! Let's build a 'silencer' using felt, foam strips, and glue from our material basket."*
        * **2. When to Use the Worksheet & Measurements:** 
          * Have students use **finger units** to measure the space under the doorway and the bottom of the chair legs.
          * Hand out the **Tally Mark Graph Worksheet**. Have children draw tally marks to record their measurements.
        * **3. Building & Testing:** 
          * Students sketch a simple 2D blueprint, stick foam/felt to their object, and test whether pushing or pulling reduces the noise and friction.
        * **4. Peer Sharing ('Teach-Ok' Strategy):** 
          * Pair groups together. Have one student explain to a partner *why* and *how* their material choice reduced the screeching sound.
        """)

    with t4:
        st.markdown("### Step-by-Step Instructions: Reflection, Boards & Closing")
        st.markdown("""
        * **1. Documenting on the Boards:** 
          * Take photos with a Polaroid camera. Help students stick their photos, vocabulary word cards, blueprints, and tally worksheets onto the **Force Lab Board**.
          * Add a collective class tally chart showing before-and-after noise levels.
        * **2. Responsibility Board:** 
          * Have groups pin up pictures of their final prototypes alongside themselves, discussing how reducing noise creates a peaceful, caring classroom environment.
        * **3. Closing Bridge (*Imagine if*):** 
          * End the session by planting a seed for the next lesson: *(i) Imagine if our school had mud floors like villages, how would that change your design? (ii) Imagine if we needed to move something heavier faster instead of quieter, what would we do?*
        """)

    st.markdown("---")
    st.subheader("📥 Download This Step-by-Step Guide")
    lesson_bundle = """EFALL STEP-BY-STEP TEACHING GUIDE - FORCE & FRICTION
======================================================
PHASE 1: SETUP & OPENING (0-10m)
- Clear furniture, set up door/table noise anomalies.
- Gather students in groups of 5 on the carpet.
- Run 'Imagine if' routine regarding classroom noise.

PHASE 2: CLASS TOUR & INQUIRY (10-20m)
- Walk around, touch doors and chairs.
- Ask scaffolding questions about push, pull, and friction.
- Hand out sticky notes for students to mark noisy objects.

PHASE 3: ENGINEERING & WORKSHEET (20-40m)
- Hand out material baskets (foam, felt, glue).
- Use finger units to measure gaps; record data using tally mark worksheets.
- Build prototypes and use 'Teach-Ok' peer sharing.

PHASE 4: REFLECTION & BOARDS (40-60m)
- Post Polaroid pictures, blueprints, and tally charts on the Force Lab Board.
- Mount final prototypes on the Responsibility Board.
- Close with advanced 'Imagine if' prompts for the next session.
"""
    st.markdown(create_download_button(lesson_bundle, "Step_By_Step_Force_Lesson.txt", "Download Master Teacher Script (.txt)"), unsafe_allow_html=True)

# --- REFLECTION LOG ---
elif st.session_state.current_page == "Reflection Log":
    if st.button("⬅️ Back / واپس جائیں"):
        st.session_state.current_page = "Home"
        st.rerun()

    st.title("📝 میری ڈائری / My Teaching Diary")
    st.markdown("Tap your feelings or progress today! / آج آپ کا دن کیسا رہا؟")
    
    with st.form("simple_diary"):
        user_name = st.text_input("Your Name / آپ کا نام:")
        
        st.markdown("### Select how today went / آج کا تاثر منتخب کریں:")
        emoji_choice = st.radio("Choose One:", [
            "🌟 Very Good / بہت اچھا دن رہا", 
            "💡 Learned Something New / کچھ نیا سیکھا", 
            "🌱 Need More Practice / مزید مشق کی ضرورت ہے"
        ])
        
        note_text = st.text_area("Write or speak a short note / کوئی خاص بات لکھیں:")
        
        save_btn = st.form_submit_button("💾 Save / محفوظ کریں")
        if save_btn:
            if user_name.strip() == "":
                st.warning("Please enter your name. / براہ کرم نام درج کریں۔")
            else:
                st.session_state.reflection_logs.append({
                    "name": user_name,
                    "date": str(date.today()),
                    "mood": emoji_choice,
                    "note": note_text
                })
                st.success("Saved successfully! / کامیابی سے محفوظ ہو گیا!")

    st.markdown("---")
    st.subheader("📖 Saved Diary Entries / محفوظ شدہ ڈائری")
    if len(st.session_state.reflection_logs) == 0:
        st.info("No entries yet. / ابھی تک کوئی ڈائری درج نہیں ہوئی۔")
    else:
        for idx, entry in enumerate(st.session_state.reflection_logs):
            with st.container(border=True):
                st.write(f"**#{idx+1} | {entry['date']} | {entry['name']}**")
                st.write(f"Status: {entry['mood']}")
                if entry['note']:
                    st.write(f"Note: {entry['note']}")
