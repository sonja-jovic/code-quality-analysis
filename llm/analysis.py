import ollama

# Define a function that sends code to the LLM and receives feedback
def analyze_code_llama(code: str) -> str:

    # Define the model we want to use
    model_name = "tinyllama"

    # Prompt for the LLM
    prompt = f"""
You are a software engineering assistant.

Your job is to review code and give simple improvement suggestions.

Instructions:
- Be concise
- Focus on readability and structure
- Mention if variables, formatting, or logic could be improved
- Do NOT give overly long explanations

Code to analyze:

{code}
"""

    try:
        # Send the prompt to the LLM using Ollama
        response = ollama.chat(
            model=model_name,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert software engineer who reviews code."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        # Extract the model's response text
        analysis = response["message"]["content"]

        return analysis

    except Exception as e:
        # If something goes wrong (model not running, memory issue, etc.)
        return f"LLM analysis failed: {str(e)}"