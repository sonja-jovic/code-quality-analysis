**SUMMARY**
This project is a simple API that analyzes the quality of a Python code snippet.
You have the option between using the PyTorch-trained and TensorFlow-trained ML model.

**RUN LOCALLY**
Run the following instructions to run this project locally:
1. Navigate to the project folder on PowerShell or a VSCode terminal.
2. This project requires Python 3.11; run python --version to verify.
3. python -m venv venv
4. Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
5. venv\Scripts\activate
6. pip install -r requirements.txt
7. python -m uvicorn api.main:app --reload
8. The API will be available at: http://127.0.0.1:8000/docs
9. Use the POST /analyse request to submit your Python code snippet (see example) and get LLM-generated feedback.

**EXAMPLES**

```json
{
  "code": "def add(a,b): return a+b"
}
```