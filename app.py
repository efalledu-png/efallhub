def create_complete_unit_lesson_pdf(filename, unit_num, eng_vocab, urdu_vocab, age_group, slot_duration, custom_prompt=""):
    dynamics = get_age_dynamics(age_group)
    theme_name, _, _, _, _, steam_sensory, maker_challenge, space_mgmt, domain_name, sentence_focus, design_phase, _, unit_story = get_unit_curriculum(unit_num)
    
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36
    )
    story = []
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontSize=16,
        leading=20,
        textColor=colors.HexColor("#1A5276"),
        alignment=1
    )
    section_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontSize=13,
        leading=16,
        textColor=colors.HexColor("#1A5276"),
        spaceBefore=10,
        spaceAfter=6
    )

    # --- TITLE & METADATA ---
    story.append(Paragraph(f"<b>MASTER LESSON & WORKSHEET PACKAGE: UNIT {unit_num}</b>", title_style))
    story.append(Paragraph(f"<font size=10 color='#555555'>Theme: {theme_name} ({domain_name}) | Age Tier: {age_group} | Duration: {slot_duration}</font>", ParagraphStyle('Sub', alignment=1)))
    story.append(Spacer(1, 10))
    
    overview_data = [
        [Paragraph(f"<b>Vocab:</b> {eng_vocab} ({urdu_vocab})", styles['Normal']), 
         Paragraph(f"<b>Design Phase:</b> {design_phase}", styles['Normal'])],
        [Paragraph(f"<b>Classroom Space:</b> {space_mgmt}", styles['Normal']), 
         Paragraph(f"<b>Sentence Goal:</b> {sentence_focus}", styles['Normal'])]
    ]
    overview_table = Table(overview_data, colWidths=[270, 270])
    overview_table.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#1A5276")),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F2F4F4")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(overview_table)
    story.append(Spacer(1, 12))

    # --- PHASE 1 ---
    story.append(Paragraph("<b>Phase 1: Bilingual Literacy, Phonics & Story Circle</b>", section_style))
    story.append(Paragraph(f"• <b>Phonics Target:</b> {dynamics['phonics_target']}<br/>• <b>Pre-Writing Skill:</b> {dynamics['pre_writing']}<br/>• <b>Story Prompt:</b> <i>\"{unit_story}\"</i>", styles['Normal']))
    story.append(Spacer(1, 10))

    # --- PHASE 2 ---
    story.append(Paragraph("<b>Phase 2: STEAM & Maker Challenges</b>", section_style))
    story.append(Paragraph(f"• <b>Sensory Phenomenon:</b> {steam_sensory}<br/>• <b>Maker Challenge:</b> {maker_challenge}", styles['Normal']))
    story.append(Spacer(1, 10))

    # --- PHASE 3 ---
    story.append(Paragraph("<b>Phase 3: Detailed Math & Tally Instruction</b>", section_style))
    story.append(Paragraph(f"• <b>Math Scale & Milestone:</b> {dynamics['math_scale']}", styles['Normal']))
    
    # --- PAGE BREAK FOR WORKSHEETS ---
    story.append(PageBreak())
    
    # --- STUDENT WORKSHEET 1: LITERACY ---
    story.append(Paragraph(f"<b>Student Worksheet 1: Bilingual Literacy — Unit {unit_num}</b>", title_style))
    story.append(Spacer(1, 8))
    
    meta_table = Table([[Paragraph("<b>Name:</b> ____________________", styles['Normal']), Paragraph("<b>Date:</b> ______________", styles['Normal'])]], colWidths=[300, 240])
    meta_table.setStyle(TableStyle([('LINEBELOW', (0,0), (-1,-1), 1, colors.lightgrey), ('BOTTOMPADDING', (0,0), (-1,-1), 6)]))
    story.append(meta_table)
    story.append(Spacer(1, 10))
    
    story.append(Paragraph(f"<b>Vocabulary Tracing:</b>", styles['Heading3']))
    vocab_box_data = [
        [Paragraph(f"<b>English:</b> {eng_vocab} <br/><font color='grey'>Trace: __{eng_vocab}__</font>", styles['Normal']),
         Paragraph(f"<b>Urdu:</b> {urdu_vocab} <br/><font color='grey'>Trace: __{urdu_vocab}__</font>", styles['Normal'])]
    ]
    vocab_table = Table(vocab_box_data, colWidths=[270, 270], rowHeights=[50])
    vocab_table.setStyle(TableStyle([('BOX', (0,0), (-1,-1), 1, colors.HexColor("#1A5276")), ('VALIGN', (0,0), (-1,-1), 'MIDDLE')]))
    story.append(vocab_table)
    story.append(Spacer(1, 10))
    
    story.append(Paragraph(f"<b>Drawing Box & Sentence Completion:</b>", styles['Heading3']))
    drawing_box = Table([[Paragraph("<font color='#888888' align='center'><br/>[ Draw Your Response Here ]<br/><br/></font>", styles['Normal'])]], colWidths=[540], rowHeights=[100])
    drawing_box.setStyle(TableStyle([('BOX', (0,0), (-1,-1), 1, colors.HexColor("#1A5276")), ('VALIGN', (0,0), (-1,-1), 'MIDDLE')]))
    story.append(drawing_box)

    # --- PAGE BREAK FOR MATH WORKSHEET ---
    story.append(PageBreak())
    
    # --- STUDENT WORKSHEET 2: MATH ---
    story.append(Paragraph(f"<b>Student Worksheet 2: Math & Tally Practice — Unit {unit_num}</b>", title_style))
    story.append(Spacer(1, 8))
    story.append(meta_table)
    story.append(Spacer(1, 10))
    
    if "3–4" in age_group:
        raw_questions = ["1) Count: 🍎🍎🍎 = ___", "2) Count: 🎈🎈 = ___", "3) Count: ⭐⭐⭐⭐ = ___", "4) Count: 🐱🐱🐱 = ___", "5) Trace: 1, 2, 3", "6) Trace: 4, 5, 6"]
        grid_row_heights = [50, 50, 50]
    elif "4–5" in age_group:
        raw_questions = ["1) 3 + 1 = ____", "2) 2 + 2 = ____", "3) 4 + 1 = ____", "4) 5 + 2 = ____", "5) Count tally: |||| = ___", "6) Count tally: ||| = ___"]
        grid_row_heights = [50, 50, 50]
    else:
        raw_questions = ["1) 5 + 3 = ____", "2) 7 + 2 = ____", "3) 9 + 4 = ____", "4) 6 + 6 = ____", "5) 8 + 1 = ____", "6) 3 + 9 = ____"]
        grid_row_heights = [50, 50, 50]
    
    grid_data = []
    for i in range(0, len(raw_questions), 3):
        grid_data.append([Paragraph(f"<font size=11>{q}</font>", styles['Normal']) for q in raw_questions[i:i+3]])
        
    question_table = Table(grid_data, colWidths=[180, 180, 180], rowHeights=grid_row_heights)
    question_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#1A5276")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
    ]))
    story.append(question_table)
    
    doc.build(story)
