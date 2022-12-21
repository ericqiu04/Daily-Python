class QuizBrain:

    def __init__(self, questionBank):
        self.question_number= 0;
        self.correct = 0;
        self.total = 0;
        self.question_list = questionBank

    def QuizCheck(self):
        if(self.question_number == len(self.question_list)):
            return False
        else:
            return True

    def AnswerCheck(self, x, question):
       if(question.answer == x):
           self.correct += 1;
           print(f"Correct\nCurrent Score {self.correct} / {self.total} ")
       else:
           print(f"Incorrect\nCorrect Answer {question.answer}\nCurrent Score {self.correct} / {self.total} ")
    def next_question(self):
        cq = self.question_list[self.question_number]
        x = input(f"Q.{self.question_number + 1}: {cq.question} (True/False): ")
        self.total +=1
        self.AnswerCheck(x, cq)

        self.question_number +=1
