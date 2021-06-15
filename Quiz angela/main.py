from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
#
# item = 0
# q_test = Question(question_data[item]["text"], question_data[item]["answer"])
# print(q_test.text)
# print(q_test.answer)
# print(len(question_data))
#
# for item in range(len(question_data)):
#     question_bank.append(Question(question_data[item]["text"], question_data[item]["answer"]))
#
# print(question_bank)
# print(question_bank[10].text)
# print(question_bank[0].answer)

# making question_bank object that contains question_data/ It can access to a value by typing  question_bank.text
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank)
print(question_bank[10].text)
print(question_bank[0].answer)

quiz = QuizBrain(question_bank) #parameter q_list -> question_bank
quiz.next_question()
