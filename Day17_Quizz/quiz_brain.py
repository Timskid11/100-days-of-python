class QuizBrain:
    def __init__(self,question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
    def next_question(self):
        num_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {num_question.text} : (True/False)").lower()
        self.check_answer(num_question.answer,user_answer)
    def check_answer(self,num_question,user_answer):
        if user_answer.lower() == num_question.lower():
            print("You are right")
            self.score += 1
            print(f"Your present score is: {self.score}/{self.question_number}")
        else:
            print("Oh..You are wrong")
            print(f"The correct word: {num_question}")
            print(f"Your score is: {self.score}/{self.question_number}")
            
            
            
    def still_questions_or_not(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
        
        