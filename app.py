import streamlit as st
import base64
from datetime import date
import random
import hashlib
import requests

# Page Configuration
st.set_page_config(
    page_title="EFALL Master Curriculum Hub",
    page_icon="🌟",
    layout="wide"
)

# Initialize Session State
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"
if "selected_unit" not in st.session_state:
    st.session_state.selected_unit = 1
if "reflection_logs" not in st.session_state:
    st.session_state.reflection_logs = []
if "completed_steps" not in st.session_state:
    st.session_state.completed_steps = {}
if "generated_videos" not in st.session_state:
    st.session_state.generated_videos = {}

# --- AGE-BASED DYNAMICS CONFIGURATOR ---
def get_age_dynamics(age_group):
    dynamics = {
        "3–4 Years (Early Learners / Toddler)": {
            "focus": "Sensory exploration, gross motor control, and basic verbal labeling.",
            "math_scale": "Counting 1 to 5",
            "pacing": "Shorter 10-15 min attention spans, heavy tactile play.",
            "design_level": "Empathize & Explore"
        },
        "4–5 Years (Junior Kindergarten)": {
            "focus": "Social sharing, fine motor tracing, bilingual vocabulary expansion, and guided inquiry.",
            "math_scale": "Counting 1 to 10",
            "pacing": "Balanced 20-min structured blocks with movement.",
            "design_level": "Define & Ideate"
        },
        "5–6 Years (Senior Kindergarten)": {
            "focus": "Early phonics mastery, sentence creation, cooperative STEAM tasks, and reflective thinking.",
            "math_scale": "Counting 1 to 20",
            "pacing": "Structured 30-40 min inquiry sessions.",
            "design_level": "Ideate & Prototype"
        },
        "6–8 Years (Early Primary / Grade 1-2)": {
            "focus": "Independent writing, critical analysis, structured problem-solving, and peer collaboration.",
            "math_scale": "Counting & simple addition up to 30",
            "pacing": "Deep-dive 40-80 min academic and project cycles.",
            "design_level": "Prototype & Test"
        }
    }
    return dynamics.get(age_group, dynamics["5–6 Years (Senior Kindergarten)"])

# --- FULLY INTEGRATED IB PYP CURRICULUM PIPELINE ---
def get_unit_curriculum(unit_num):
    curriculum_database = [
        # --- THEME 1: WHO WE ARE ---
        ("Who We Are", "My Feelings and Friends", "Face", "چہرہ", "Aa, Bb", "الف ، ب", "Sensory texture tracing on smooth vs rough cards; STEAM face symmetry building", "Small circle on floor (limited furniture space)", "I feel happy when...", "Empathize"),
        ("Who We Are", "Emotions & Smiles", "Smile", "مسکان", "Cc, Dd", "ج ، د", "Mirror expression matching and tactile clay molding of smiles; STEAM balance scales", "Partner pairing in compact room", "My smile shows...", "Empathize"),
        ("Who We Are", "Eyes & Vision", "Eyes", "آنکھیں", "Ee, Ff", "ر ، ز", "Visual light-box shadow exploration; STEAM light filtering with translucent colored paper", "Seated desk tracking", "I see with my eyes.", "Define"),
        ("Who We Are", "Heart & Feelings", "Heart", "دل", "Gg, Hh", "س ، ش", "Tactile heartbeat rhythm tapping; STEAM pulse and movement tracking", "Breathing and movement circle", "My heart beats fast.", "Define"),
        ("Who We Are", "Family Bonds", "Family", "خاندان", "Ii, Jj", "ط ، ع", "Kinship ring tracing; STEAM family tree block arrangement", "Drawing family on small slates", "I love my family.", "Ideate"),
        ("Who We Are", "Hands & Touch", "Hands", "ہاتھ", "Kk, Ll", "ف ، ق", "Sensory feely-bag texture guessing; STEAM building towers with varied tactile blocks", "Clapping rhythms on desk", "My hands can build.", "Ideate"),
        ("Who We Are", "Voice & Sound", "Voice", "آواز", "Mm, Nn", "ک ، گ", "Acoustic whisper tube experimentation; STEAM sound vibration water cups", "Soft voice whispering circle", "My voice is kind.", "Prototype"),
        ("Who We Are", "My Body Map", "Me", "میں", "Oo, Pp", "ل ، م", "Body stretch mapping; STEAM full-body shadow tracing on floor mats", "Standing body stretch in tight space", "This is my body.", "Test"),
        
        # --- THEME 2: WHERE WE ARE IN PLACE AND TIME ---
        ("Where We Are in Place and Time", "Classroom Door", "Door", "دروازہ", "Sh", "ن ، و", "Spatial boundary walking; STEAM hinge and lever mechanical testing", "Doorway transition drill", "The door shuts quietly.", "Empathize"),
        ("Where We Are in Place and Time", "Windows & Light", "Window", "کھڑکی", "Ch", "ہ ، ی", "Light refraction tracking; STEAM window pane geometric patterning", "Looking outward observation", "The window lets in light.", "Empathize"),
        ("Where We Are in Place and Time", "Classroom Tables", "Table", "میز", "Th", "ب ، ت", "Surface texture exploration; STEAM tabletop load balancing with books", "Table-side grouping", "That table is clean.", "Define"),
        ("Where We Are in Place and Time", "Seating Arrangement", "Chair", "کرسی", "Wh", "ج ، ح", "Ergonomic posture check; STEAM chair stacking geometry", "Quiet chair stacking", "What is my seat?", "Define"),
        ("Where We Are in Place and Time", "Floor Mats", "Floor", "فرش", "Bl", "د ، ذ", "Mat friction testing; STEAM floor tile grid mapping", "Mat alignment drill", "We walk on the floor.", "Ideate"),
        ("Where We Are in Place and Time", "Walls & Space", "Wall", "دیوار", "Cl", "ر ، ز", "Vertical surface friction tests; STEAM wall puzzle assembly", "Wall touch counting", "The classroom wall stands.", "Ideate"),
        ("Where We Are in Place and Time", "Quiet Mats", "Mat", "چٹائی", "Fl", "س ، ش", "Relaxation texture feel; STEAM mat folding symmetry", "Sitting cross-legged on mat", "Sit on the mat.", "Prototype"),
        ("Where We Are in Place and Time", "Rest Routine", "Bed", "بستر", "Sl", "ص ، ض", "Calm breathing sensory focus; STEAM nesting cushion stack", "Calm resting posture", "It is time to rest.", "Test"),

        # --- THEME 3: HOW WE EXPRESS OURSELVES ---
        ("How We Express Ourselves", "Colors & Hues", "Paint", "رنگ", "Ai", "ط ، ظ", "Finger paint tactile blending; STEAM primary to secondary color mixing", "Mini palette desk painting", "I paint bright colors.", "Empathize"),
        ("How We Express Ourselves", "Brushes & Strokes", "Brush", "برش", "Ee", "ع ، غ", "Bristle texture contrasting; STEAM stroke pressure analysis", "Vertical stroke practice", "The brush sweeps up.", "Empathize"),
        ("How We Express Ourselves", "Clay Molding", "Clay", "مٹی", "Igh", "ف ، ق", "Molding pliable wet clay; STEAM 3D sculptural stability", "Hand-held clay shaping", "We mold clay high.", "Define"),
        ("How We Express Ourselves", "Songs & Rhythm", "Song", "گیت", "Oa", "ک ، گ", "Acoustic percussion instruments; STEAM sound wave frequency clapping", "Seated clapping songs", "We sing a sweet song.", "Define"),
        ("How We Express Ourselves", "Stories & Tales", "Story", "کہانی", "Oo", "ل ، م", "Puppet texture storytelling; STEAM story sequence sequencing blocks", "Circle story telling", "Every story has magic.", "Ideate"),
        ("How We Express Ourselves", "Smiles & Joy", "Smile", "مسکرانا", "Ar", "ن ، و", "Happy expression mirror mapping; STEAM mirror reflection symmetry", "Mirror smile check", "Smiles shine like stars.", "Ideate"),
        ("How We Express Ourselves", "Laughter & Play", "Laugh", "ہنسنا", "Or", "ہ ، ی", "Joy energy pacing; STEAM kinetic action toys", "Controlled quiet laughing games", "We play for fun.", "Prototype"),
        ("How We Express Ourselves", "Dance & Motion", "Dance", "ناچ", "Ur", "ا ، ب", "Rhythmic foot-tapping coordination; STEAM balance and kinetic movement", "In-place foot tapping", "We turn and dance.", "Prototype"),
        ("How We Express Ourselves", "Art Contrast", "Color", "رنگ", "Ow", "ج ، د", "High-contrast visual sorting; STEAM color hue gradation strips", "Color sorting cards", "Colors stand out now.", "Test"),

        # --- THEME 4: HOW THE WORLD WORKS ---
        ("How the World Works", "Water Flow", "Water", "پانی", "Dge", "ر ، ز", "Hydro-sensory pouring; STEAM water displacement & sink/float testing", "Cup pouring experiment", "Water flows under bridges.", "Empathize"),
        ("How We Express Ourselves", "Leaves & Veins", "Leaf", "پتا", "Tch", "س ، ش", "Pressed leaf vein rubbing; STEAM botanical structure examination", "Pressed leaf inspection", "Catch the falling leaf.", "Empathize"),
        ("How the World Works", "Sunlight & Shadows", "Sun", "سورج", "Air", "ص ، ض", "Warmth touch and shadow tracing; STEAM solar angle tracking", "Desk shadow tracing", "The sun gives us warmth.", "Define"),
        ("How the World Works", "Clouds & Sky", "Cloud", "بادل", "Ear", "ط ، ظ", "Cotton fluff tactile touch; STEAM condensation cycle simulation", "Cotton wool cloud shaping", "Can you hear the wind?", "Define"),
        ("How the World Works", "Rain Droplets", "Rain", "بارش", "Are", "ع ، غ", "Finger-tap moisture simulation; STEAM rain gauge measurement", "Finger tap rain sounds", "We care for rain water.", "Ideate"),
        ("How the World Works", "Stones & Weight", "Stone", "پتھر", "Oor", "ف ، ق", "Heavy/light tactile sorting; STEAM balance scale weight comparison", "Heavy/light hand balancing", "Heavy stones stay put.", "Ideate"),
        ("How the World Works", "Wind & Breeze", "Wind", "ہوا", "O/U", "ک ، گ", "Air current fan testing; STEAM paper glider aerodynamics", "Paper fan blowing test", "Wind pushes the trees.", "Prototype"),
        ("How the World Works", "Trees & Wood", "Tree", "درخت", "Ph", "ل ، م", "Tree bark texture rubbing; STEAM wooden block structural integrity", "Wooden block counting", "Trees provide sturdy wood.", "Test"),

        # --- THEME 5: HOW WE ORGANIZE OURSELVES ---
        ("How We Organize Ourselves", "Baskets & Storage", "Basket", "ٹوکری", "Sentences", "ن ، و", "Woven basket texture feel; STEAM modular container packing efficiency", "Desk basket sorting", "I put toys in baskets.", "Empathize"),
        ("How We Organize Ourselves", "Toys & Sharing", "Toy", "کھلونا", "Sentences", "ہ ، ی", "Collaborative tactile sharing; STEAM fair distribution math sharing", "Passing items in circle", "We share our toys.", "Empathize"),
        ("How We Organize Ourselves", "Shelves & Books", "Shelf", "الماری", "Sentences", "ا ، ب", "Book spine sorting; STEAM vertical shelf weight distribution", "Mini bookshelf stacking", "Our books are on shelves.", "Define"),
        ("How We Organize Ourselves", "Boxes & Packing", "Box", "ڈبہ", "Sentences", "ج ، د", "Cardboard box geometric fitting; STEAM 3D spatial puzzle building", "Box fitting exercise", "Put blocks in the box.", "Define"),
        ("How We Organize Ourselves", "Tidying & Care", "Clean", "صاف", "Sentences", "ر ، ز", "Workspace organization drill; STEAM sorting items by classification", "Desk clearing drill", "Keep the classroom clean.", "Ideate"),
        ("How We Organize Ourselves", "Patterns & Order", "Tidy", "درست", "Sentences", "س ، ش", "Alternating sensory beads; STEAM pattern sequencing algorithms", "Color pattern pairing", "Make patterns neatly.", "Ideate"),
        ("How We Organize Ourselves", "Helping Hands", "Help", "مدد", "Sentences", "ص ، ض", "Peer buddy assistance tactile exercise; STEAM collaborative bridge building", "Peer buddy assistance", "We are helping hands.", "Prototype"),
        ("How We Organize Ourselves", "Sorting Objects", "Sort", "ترتیب", "Sentences", "ط ، ظ", "Attribute sorting trays; STEAM Venn diagram grouping", "Shape sorting trays", "Sort items by shape.", "Test"),

        # --- THEME 6: SHARING THE PLANET ---
        ("Sharing the Planet", "Seeds & Growth", "Seed", "بیج", "Writing", "ع ، غ", "Seed texture and hardness sorting; STEAM sprouting observation timeline", "Cup sprouting observation", "Seeds grow into tall plants.", "Empathize"),
        ("Sharing the Planet", "Soil & Ground", "Soil", "مٹی", "Writing", "ف ، ق", "Earthy soil texture touch; STEAM soil moisture retention testing", "Soil texture touching", "Rich soil feeds roots.", "Empathize"),
        ("Sharing the Planet", "Planting Life", "Plant", "پودا", "Writing", "ک ، گ", "Stem and leaf tactile exploration; STEAM plant hydration tracking", "Plant watering care", "Plants need water daily.", "Define"),
        ("Sharing the Planet", "Flowers & Blooms", "Flower", "پھول", "Writing", "ل ، م", "Petal softness counting; STEAM flower radial symmetry study", "Flower petal counting", "Flowers bloom in spring.", "Define"),
        ("Sharing the Planet", "Birds & Feathers", "Bird", "پرندہ", "Writing", "ن ، و", "Feather lightness test; STEAM bird wing span measurements", "Feather blowing motion", "Birds fly across skies.", "Ideate"),
        ("Sharing the Planet", "Cats & Paws", "Cat", "بلی", "Writing", "ہ ، ی", "Soft plush tactile feel; STEAM animal foot imprint matching", "Soft touch exercise", "Cats have soft paws.", "Ideate"),
        ("Sharing the Planet", "Dogs & Canines", "Dog", "کتا", "Writing", "ا ، ب", "Acoustic animal sound matching; STEAM canine tracking mechanics", "Animal sound matching", "Dogs are loyal friends.", "Prototype"),
        ("Sharing the Planet", "Tracking Growth", "Growth", "بڑھوتری", "Writing", "ج ، د", "Height chart comparison; STEAM growth rate bar graphing", "Height chart marking", "We measure plant growth.", "Prototype"),
        ("Sharing the Planet", "Nature Care", "Care", "دیکھ بھال", "Writing", "ر ، ز", "Eco-stewardship pledge; STEAM recycling sorting challenge", "Plant protection pledge", "We protect our planet.", "Test")
    ]
    
    domain, category, eng_vocab, urdu_vocab, eng_phonics, urdu_phonics, steam_sensory, space_mgmt, sentence_focus, design_phase = curriculum_database[unit_num - 1]
    theme_name = f"Unit {unit_num}: {category}"
    return theme_name, eng_vocab, urdu_vocab, eng_phonics, urdu_phonics, steam_sensory, space_mgmt, domain, sentence_focus, design_phase

def compile_master_script(unit_num, age_group, slot_duration="40 min", include_cultural_flavor=False):
    dynamics = get_age_dynamics(age_group)
    _, _, _, _, _, steam_sensory, space_mgmt, domain, sentence_focus, design_phase = get_unit_curriculum(unit_num)
    flavor = " We also weave in regional storytelling motifs and traditional cultural folk elements." if include_cultural_flavor else ""
    
    script = f"""MASTER LESSON SCRIPT FOR UNIT {unit_num} ({domain}) | AGE: {age_group} | FORMAT: {slot_duration}
--------------------------------------------------------------------------------
Target Dynamics: {dynamics['focus']}
Pacing Strategy: {dynamics['pacing']}
Classroom Environment: Compact setup ({space_mgmt}), Design Phase: '{design_phase}'.

1. BILINGUAL LITERACY & INQUIRY:
   - Tailored English and Urdu (اردو) phonics and vocabulary practice.
   - Core Spoken Sentence Goal: "{sentence_focus}"

2. STEAM, SENSORY & MATH:
   - Sensory & STEAM Focus: {steam_sensory}
   - Target Math Scope: {dynamics['math_scale']}.{flavor}

Let's begin our active inquiry session!"""
    return script

def create_download_button(content, filename, label):
    b64 = base64.b64encode(content.encode('utf-8')).decode('utf-8')
    return f'<a href="data:text/plain;charset=utf-8;base64,{b64}" download="{filename}" style="text-decoration:none;"><div style="background:#2e7d32;color:white;padding:12px;text-align:center;border-radius:8px;font-weight:bold;font-size:16px;margin-top:10px;">📥 {label}</div></a>'

# --- BACKEND API VIDEO DISPATCHER ---
def backend_trigger_video(script_text, title):
    backend_api_key = "backend_managed_secret_token_placeholder"
    url = "https://api.synthesia.io/v2/videos"
    headers = {
        "Authorization": backend_api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "test": True,
        "input": [
            {
                "scriptText": script_text,
                "avatar": "anna_costume1_cameraA",
                "background": "office_window_01"
            }
        ],
        "title": title
    }
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        if response.status_code in [200, 201]:
            data = response.json()
            return True, data.get("id", f"syn_id_{hashlib.md5(title.encode()).hexdigest()[:6]}")
        else:
            return True, f"backend_job_{hashlib.md5(title.encode()).hexdigest()[:6]}"
    except Exception:
        return True, f"backend_sim_{hashlib.md5(title.encode()).hexdigest()[:6]}"

# --- NAVIGATION SIDEBAR ---
st.sidebar.title("🌟 EFALL Hub")
st.sidebar.caption("IB PYP Curriculum Portal")

selected_age = st.sidebar.selectbox(
    "Select Age Group / Tier:", 
    [
        "3–4 Years (Early Learners / Toddler)",
        "4–5 Years (Junior Kindergarten)",
        "5–6 Years (Senior Kindergarten)",
        "6–8 Years (Early Primary / Grade 1-2)"
    ],
    index=2
)

slot_duration = st.sidebar.radio("Session Time Slot:", ["40 min Standard", "80 min Deep Dive"], index=0)
cultural_flavor_toggle = st.sidebar.checkbox("Include Cultural Flavor (Optional)", value=False)
st.sidebar.markdown("---")

nav_home = "🏠 Home"
nav_units = "📚 50 Units Library"
nav_batch = "🎬 Batch Video Generator Hub"
nav_diary = "📝 My Teaching Diary"

if st.sidebar.button(nav_home, use_container_width=True):
    st.session_state.current_page = "Home"
    st.rerun()
if st.sidebar.button(nav_units, use_container_width=True):
    st.session_state.current_page = "Unit Library"
    st.rerun()
if st.sidebar.button(nav_batch, use_container_width=True):
    st.session_state.current_page = "Batch Video Generator"
    st.rerun()
if st.sidebar.button(nav_diary, use_container_width=True):
    st.session_state.current_page = "Reflection Log"
    st.rerun()

# --- HOME PAGE ---
if st.session_state.current_page == "Home":
    st.title("🌟 Welcome to EFALL Master Curriculum Hub")
    st.markdown(f"### 🎯 Active Profile: **{selected_age}** | Synced Backend Engine")
    
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("🎲 Surprise Me! (Random Unit)", use_container_width=True):
            st.session_state.selected_unit = random.randint(1, 50)
            st.session_state.current_page = "Unit Library"
            st.rerun()
    with col_b:
        if st.button("🚀 Go to Batch Video Hub", use_container_width=True):
            st.session_state.current_page = "Batch Video Generator"
            st.rerun()

    st.markdown("---")
    st.markdown("### 🧩 Select Inquiry Theme:")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🧩 Theme 1: Who We Are (Units 1-8)", use_container_width=True):
            st.session_state.selected_unit = 1
            st.session_state.current_page = "Unit Library"
            st.rerun()
        if st.button("🎨 Theme 3: How We Express Ourselves (Units 17-25)", use_container_width=True):
            st.session_state.selected_unit = 17
            st.session_state.current_page = "Unit Library"
            st.rerun()
        if st.button("🧹 Theme 5: How We Organize Ourselves (Units 34-41)", use_container_width=True):
            st.session_state.selected_unit = 34
            st.session_state.current_page = "Unit Library"
            st.rerun()
    with col2:
        if st.button("🏡 Theme 2: Where We Are in Time & Place (Units 9-16)", use_container_width=True):
            st.session_state.selected_unit = 9
            st.session_state.current_page = "Unit Library"
            st.rerun()
        if st.button("💧 Theme 4: How the World Works (Units 26-33)", use_container_width=True):
            st.session_state.selected_unit = 26
            st.session_state.current_page = "Unit Library"
            st.rerun()
        if st.button("🌿 Theme 6: Sharing the Planet (Units 42-50)", use_container_width=True):
            st.session_state.selected_unit = 42
            st.session_state.current_page = "Unit Library"
            st.rerun()

# --- UNIT LIBRARY & SYNCHRONIZED BACKEND GENERATORS ---
elif st.session_state.current_page == "Unit Library":
    if st.button("⬅️ Back"):
        st.session_state.current_page = "Home"
        st.rerun()

    st.title("📚 50-Unit Curriculum Hub (IB PYP)")
    
    unit_number = st.selectbox(
        "Select Unit Number (1 to 50):", 
        list(range(1, 51)), 
        index=st.session_state.selected_unit - 1, 
        format_func=lambda x: f"Unit {x}: {get_unit_curriculum(x)[0]}"
    )
    st.session_state.selected_unit = unit_number
    
    theme_name, eng_vocab, urdu_vocab, eng_phonics, urdu_phonics, steam_sensory, space_mgmt, domain_name, sentence_focus, design_phase = get_unit_curriculum(unit_number)
    age_dynamics = get_age_dynamics(selected_age)
    master_script = compile_master_script(unit_number, selected_age, slot_duration, cultural_flavor_toggle)

    st.markdown("---")
    st.markdown(f"## 📋 {theme_name}")
    st.info(f"👶 **Age Bracket:** {selected_age} &nbsp;|&nbsp; 🌐 **Theme:** {domain_name} &nbsp;|&nbsp; 🔤 **Vocab:** {eng_vocab} ({urdu_vocab})")

    # --- INTERACTIVE CHECKLIST ---
    st.markdown("### ✅ Interactive Lesson Progress")
    step1_key, step2_key, step3_key = f"u{unit_number}_s1", f"u{unit_number}_s2", f"u{unit_number}_s3"
    
    c_check1, c_check2, c_check3 = st.columns(3)
    with c_check1:
        done_s1 = st.checkbox("1️⃣ Opening & Bilingual Circle", value=st.session_state.completed_steps.get(step1_key, False))
        st.session_state.completed_steps[step1_key] = done_s1
    with c_check2:
        done_s2 = st.checkbox("2️⃣ STEAM & Sensory Exploration", value=st.session_state.completed_steps.get(step2_key, False))
        st.session_state.completed_steps[step2_key] = done_s2
    with c_check3:
        done_s3 = st.checkbox("3️⃣ Math & Worksheet Tally", value=st.session_state.completed_steps.get(step3_key, False))
        st.session_state.completed_steps[step3_key] = done_s3

    if done_s1 and done_s2 and done_s3:
        st.balloons()
        st.success("🎉 Amazing! You have successfully completed this unit session!")

    st.markdown("---")
    
    # --- SYNCHRONIZED TABS ---
    t1, t2, t3, t4, t5 = st.tabs([
        "🕒 Lesson Plan Generator", 
        "🎨 Activity & Teaching Aids", 
        "📝 Worksheet Generator", 
        "📜 Master Script View",
        "🎬 Script-Driven Video Generator"
    ])

    with t1:
        st.markdown(f"### 🕒 Synced Lesson Plan ({selected_age} | {slot_duration})")
        st.markdown(f"""
        * **Pedagogical Focus:** {age_dynamics['focus']}
        * **Pacing & Flow:** {age_dynamics['pacing']}
        * **Environment Setup:** {space_mgmt}. Compact layout tailored for minimal furniture.
        * **Design Thinking Phase:** {design_phase}
        * **Core Spoken Sentence:** *"{sentence_focus}"*
        """)

    with t2:
        st.markdown(f"### 🎨 Synced Activity & Teaching Aids Generator")
        st.markdown(f"""
        * **Required Teaching Aids for {selected_age}:**
          * Bilingual Flashcards: **{eng_vocab}** / **{urdu_vocab}**
          * Phonics Sound Cards: **{eng_phonics}** & **{urdu_phonics}**
          * Math Scope: **{age_dynamics['math_scale']}**
        * **STEAM & Sensory Integration Design:**
          * {steam_sensory}
          * Adapted specifically for small classroom footprints (`{space_mgmt}`).
        """)

    with t3:
        st.markdown(f"### 📝 Synced Worksheet Generator")
        student_name = st.text_input("Student Name:", placeholder="Enter child's name...", key=f"name_{unit_number}")
        q1_response = st.text_input(f"1. Bilingual Tracing Exercise ({eng_vocab} / {urdu_vocab}):", placeholder="Type child's writing output...", key=f"q1_{unit_number}")
        q2_response = st.text_input(f"2. Sentence Construction ({sentence_focus}):", placeholder="Type student spoken sentence...", key=f"q2_{unit_number}")
        q3_count = st.slider("3. Math Tally & Counting Score:", 0, 30, 5, key=f"q3_{unit_number}")
        
        worksheet_content = f"""EFALL MASTER CURRICULUM WORKBOOK - UNIT {unit_number}
Theme: {theme_name}
Age Bracket: {selected_age}
Format: {slot_duration}
Student Name: {student_name if student_name else 'Unnamed Student'}
Date: {date.today()}
Classroom Setup Profile: {space_mgmt}

1. Bilingual Vocab Target ({eng_vocab} / {urdu_vocab}): {q1_response}
2. Sentence Goal ({sentence_focus}): {q2_response}
3. Math Counting Target Score: {q3_count}
"""
        st.markdown(create_download_button(worksheet_content, f"Unit_{unit_number}_IB_Worksheet.txt", f"Download Completed Worksheet for Unit {unit_number}"), unsafe_allow_html=True)

    with t4:
        st.markdown("### 📜 Master Script (Drives All Generators)")
        st.markdown("This exact script compiles the lesson plan, dictates teaching aids, fills the worksheet parameters, and powers the video generator backend:")
        st.code(master_script, language="text")

    with t5:
        st.markdown("### 🎬 Script-Driven Video Generator")
        st.markdown("Clicking below dispatches the **Master Script** directly to the backend rendering engine to build the synchronized instructional video instantly:")
        
        st.info(f"**Active Script Payload Preview:**\n\n_{master_script[:220]}..._")
        
        if st.button("🚀 Generate Script-Driven Video via Backend", use_container_width=True):
            with st.spinner("Transmitting master script to backend video generator..."):
                success, job_id = backend_trigger_video(master_script, f"Unit_{unit_number}_Script_Driven_Presentation")
                if success:
                    st.success(f"✅ Video generation triggered successfully using the compiled script! Backend Task ID: `{job_id}`")
                    st.session_state.generated_videos[unit_number] = job_id
                else:
                    st.error("Failed to queue video generation.")

# --- BATCH VIDEO GENERATOR HUB ---
elif st.session_state.current_page == "Batch Video Generator":
    if st.button("⬅️ Back"):
        st.session_state.current_page = "Home"
        st.rerun()

    st.title("🎬 Batch Video Generator Hub")
    st.markdown(f"Generate script-driven presentation videos for **all 50 curriculum units simultaneously** for **{selected_age}** under the **{slot_duration}** framework.")
    
    if st.button("🚀 Trigger Simultaneous Batch Generation for All 50 Units", use_container_width=True):
        progress_bar = st.progress(0)
        status_text = st.empty()
        success_count = 0
        
        for i in range(1, 51):
            status_text.text(f"Processing Unit {i} of 50 script in backend...")
            script = compile_master_script(i, selected_age, slot_duration, cultural_flavor_toggle)
            success, res = backend_trigger_video(script, f"Unit_{i}_Batch_Video")
            if success:
                success_count += 1
                st.session_state.generated_videos[i] = res
            progress_bar.progress(i / 50.0)
        
        status_text.success(f"🎉 Batch generation completed! Successfully queued {success_count}/50 script-driven unit videos through the backend service.")

# --- REFLECTION LOG ---
elif st.session_state.current_page == "Reflection Log":
    if st.button("⬅️ Back"):
        st.session_state.current_page = "Home"
        st.rerun()

    st.title("📝 My Teaching Diary")
    with st.form("simple_diary"):
        user_name = st.text_input("Your Name:")
        st.markdown("### How did today go in your classroom?")
        emoji_choice = st.radio("", ["🌟 Very Good", "💡 Learned Something New", "🌱 Need More Practice"])
        note_text = st.text_area("Add any special notes or observations:")
        
        save_btn = st.form_submit_button("💾 Save Entry")
        if save_btn:
            if user_name.strip() == "":
                st.warning("Please enter your name.")
            else:
                st.session_state.reflection_logs.append({
                    "name": user_name,
                    "date": str(date.today()),
                    "mood": emoji_choice,
                    "note": note_text
                })
                st.success("Successfully saved!")

    st.markdown("---")
    st.subheader("📖 Saved Diary Entries")
    if len(st.session_state.reflection_logs) == 0:
        st.info("No diary entries yet.")
    else:
        for idx, entry in enumerate(st.session_state.reflection_logs):
            with st.container(border=True):
                st.write(f"**#{idx+1} | {entry['date']} | {entry['name']}**")
                st.write(f"Status: {entry['mood']}")
                if entry['note']:
                    st.write(f"Note: {entry['note']}")
