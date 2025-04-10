import openai
import streamlit as st

openai.api_key = "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"

# Rule-based layer
def rule_based_response(user_input):
    user_input = user_input.lower()
    if "exam pattern" in user_input:
        return "CLAT has 5 sections: English, GK, Legal Reasoning, Logical Reasoning, and Quantitative Techniques."
    elif "eligibility" in user_input:
        return "For CLAT UG, you need 45% in 12th standard (40% for SC/ST)."
    elif "negative marking" in user_input:
        return "Yes, there's a negative marking of 0.25 per wrong answer."
    elif "legal reasoning tips" in user_input:
        return "Focus on case-based comprehension, legal principles, and daily practice of reasoning."
    elif "date" in user_input or "exam date" in user_input:
        return "CLAT 2025 is expected in December 2024. Check official site for updates."
    else:
        return None

# LLM fallback
def llm_fallback(user_input):
    print("using LLM fallback")
    prompt = f"You are a helpful mentor for CLAT aspirants. Answer this question:\n\n{user_input}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error fetching response: {str(e)}"

# Streamlit app
def main():
    st.title("CLAT Chatbot - LexMentor AI")

    user_input = st.text_input("Ask your CLAT-related question:")

    if user_input:
        response = rule_based_response(user_input)
        if not response:
            response = llm_fallback(user_input)
        st.write("*Answer:*", response)

if __name__ == "__main__":
    main()