const express = require('express');
const { GoogleGenAI } = require('@google/genai');

const app = express();
app.use(express.json());

// This serves your HTML frontend file from the 'public' folder
app.use(express.static('public'));

// Initialize the Google Gen AI SDK
const ai = new GoogleGenAI();

app.post('/api/generate-lesson', async (req, res) => {
  try {
    const { ageGroup, centralIdea, unitTitle } = req.body;

    const systemInstruction = `
You are an expert International Baccalaureate Primary Years Programme (IB PYP) bilingual curriculum designer and early years educator specializing in English and Urdu instruction. 

CRITICAL PARAMETERS TO INCORPORATE:
- Target Languages: Provide all key vocabulary, phonics targets, and teacher presentation scripts in BOTH English and Urdu.
- Target Age Group: ${ageGroup} (Adapt complexity accordingly).
- Classroom Constraints: The physical classroom is very small with limited furniture. All STEAM maker challenges must use minimal, compact materials that fit on student desks or small floor mats.
- Output format: STRICTLY valid JSON only, matching the exact requested schema. No markdown formatting outside the JSON block.
`;

    const userPrompt = `Generate a transdisciplinary lesson plan for the unit titled "${unitTitle}" with the Central Idea: "${centralIdea}".`;

    const response = await ai.models.generateContent({
      model: 'gemini-2.5-flash',
      contents: userPrompt,
      config: {
        systemInstruction: systemInstruction,
        responseMimeType: 'application/json',
      }
    });

    const lessonData = JSON.parse(response.text);
    res.status(200).json({ success: true, data: lessonData });

  } catch (error) {
    console.error('Error generating lesson plan:', error);
    res.status(500).json({ success: false, error: error.message });
  }
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
