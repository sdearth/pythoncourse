class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_input, answer):
        if user_input.lower() == answer.lower():
            self.score +=1
            print("You got it right!")
        else:
            print("You got it wrong!")
        print(f"The correct answer was {answer}")
        print(f"Your current score is {self.score}/{self.question_number}")

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}: {question.text}. (True/False)? ")
        self.check_answer(user_input, question.answer)

    def print_results(self):
       print("You've completed the quiz.")
       print(f"Your final score was {self.score}/{len(self.question_list)}")