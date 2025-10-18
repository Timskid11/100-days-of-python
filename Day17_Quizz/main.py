from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for eachquestion in question_data:
    text = eachquestion["text"]
    answer= eachquestion["answer"]
    new_question = Question(text,answer)
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)
while quiz.still_questions_or_not():
    
    quiz.next_question()


