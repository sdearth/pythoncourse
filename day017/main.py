from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []

for q in question_data:
    question_bank.append(Question(q["text"], q["answer"]))

brain = QuizBrain(question_bank)

while brain.still_has_questions():
    brain.next_question()

brain.print_results()