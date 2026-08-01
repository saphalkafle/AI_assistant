from flask import Flask,render_template,request,jsonify
from ai_assistant import PersonalAssistant
import groq_client

app= Flask(__name__)

assistant = PersonalAssistant()

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/ask",methods=["POST"])
def ask():
    question = request.form.get("question")

    if not question:
        return jsonify({"error": "Question is required"}),400

    answer = assistant.ans_query(question)
    return jsonify ({"answer": answer}) , 200

@app.route("/summarize",methods=["POST"])
def summarize():
    email_text = request.form.get("email")

    if not email_text:
        return jsonify ({"error": "Email text is required"}),400

    summary = assistant.summarize_email(email_text)
    return jsonify({"summary":summary}) , 200

    
if __name__ == "__main__":
    app.run(debug=True)