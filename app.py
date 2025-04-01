from flask import Flask, render_template, request, redirect, url_for, session
import os
import json
import random

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Load questions from JSON file
def load_questions():
    try:
        with open('questions.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"questions": []}

# Get question by ID
def get_question(question_id):
    questions = load_questions()
    for question in questions["questions"]:
        if question["id"] == question_id:
            return question
    return None

# Calculate result based on answers
def calculate_result(answers):
    positive_answers = sum(1 for answer in answers.values() if answer == "positive")
    total_questions = len(answers)
    
    if total_questions == 0:
        return "neutral"
    
    score_percentage = (positive_answers / total_questions) * 100
    
    if score_percentage >= 70:
        return "happy"
    elif score_percentage >= 40:
        return "neutral"
    else:
        return "angry"

@app.route('/')
def index():
    # Reset game session
    session.clear()
    return render_template('index.html')

@app.route('/game')
def game():
    # Initialize or get current question from session
    if 'current_question' not in session:
        session['current_question'] = "start"
        session['answers'] = {}
        session['questions_asked'] = 0
    
    # Check if we've reached the maximum number of questions
    if session.get('questions_asked', 0) >= 10:
        return redirect(url_for('result'))
    
    # Get the current question
    question = get_question(session['current_question'])
    
    # If no question found (shouldn't happen normally), redirect to result
    if not question:
        return redirect(url_for('result'))
    
    return render_template('game.html', question=question)

@app.route('/answer', methods=['POST'])
def answer():
    if 'current_question' not in session:
        return redirect(url_for('game'))
        
    choice = request.form.get('choice')
    current_question = session['current_question']
    next_question = None
    
    # Record the answer
    if choice:
        current_question_obj = get_question(current_question)
        if current_question_obj:
            for option in current_question_obj["options"]:
                if option["text"] == choice:
                    session['answers'][current_question] = option["effect"]
                    next_question = option["next_question"]
                    break
    
    # Increment questions asked counter
    session['questions_asked'] = session.get('questions_asked', 0) + 1
    
    # Set next question
    if next_question:
        session['current_question'] = next_question
    else:
        # If no next question specified, end the game
        return redirect(url_for('result'))
    
    session.modified = True
    return redirect(url_for('game'))

@app.route('/result')
def result():
    # Calculate the result based on answers
    answers = session.get('answers', {})
    result = calculate_result(answers)
    
    return render_template('result.html', result=result, answers=answers)

if __name__ == '__main__':
    app.run(debug=True)
