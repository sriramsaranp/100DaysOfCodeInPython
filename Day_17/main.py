from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_bank.append(Question(item['text'], item['answer']))


quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()


print("You have finished the quiz!")
print(f"Your score is {quiz_brain.score}/{len(question_bank)}")
