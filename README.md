CLAT CHATBOT:- A smart chatbot for CLAT aspirants using rule-based logic + GPT-3.5 fallback.

Objective:- To provide personalized guidance, study plans, and  improving their preparation efficiency and confidence

Tools:
	-	Python language is used to build app
	-	Streamlit is used for creating the user interface
	-	OpenAI API is used for smart answers
 
 Features :-
- Answers CLAT-related questions using a small knowledge base
- Falls back to GPT-3.5 when answer isn't found
- Uses spaCy for keyword extraction

Sample Question you can ask :-
  - What is CLAT exam pattern?
  - Who can apply for CLAT?
  - How should i prepere for legal reasoning?
  - What is difference between CLAT UG and CLAT PG? 
  
Setup Instructions:-

 1. Open the repository
 2. Replace my openAI key
 3. Run the Chatbot

 ## Scalling Plan from chatbot to tuned GPT model

  1. Data Collection

Gather high-quality, structured CLAT and law exam-related content, ideally from NLTI or similar:

Sources:
	-	NLTI notes, lectures, PDFs, and blog content.
	-	Previous year question papers and answer keys.
	-	FAQs, model answers, and study guides.
	-	Legal principles, case summaries, and mock test answers.

 2. Data Cleaning & Preprocessing
	-	Convert text/PDFs into structured Q&A pairs.

 3. Hosting & Scaling

Once fine-tuned:
	-	Replace the fallback model in your current chatbot with your fine-tuned GPT model.
	-	Streamlit Cloud


 
