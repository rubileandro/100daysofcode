from question_model import Question
from data import question_data

question_bank = []
for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)

print(question_bank)
