class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0 #default value
        self.question_list = q_list #quiz_bank will be received inside self.question_list

    def next_question(self):
        current_question = self.question_list[self.question_number] #assumption is question list is a list form - quiz_bank will be passed
        number = self.question_number + 1
        input(f"Q.{number}: {current_question.text} (True/False): ")

# quiz = QuizBrain()
#
# quiz.next_question(1)
