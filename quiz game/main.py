from data import question_data as q_d
from question_model import Question as q
from quiz_brain import Quizbrain as q_b

question_bank=[]
for question in q_d:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question= q(question_text,question_answer)
    question_bank.append(new_question) 
quiz=q_b(question_bank)
while quiz.still_has_questions():   
    quiz.next_question() 

print("You have completed the quiz")
print(f"The Final score = {quiz.score}/{len(question_bank)}")