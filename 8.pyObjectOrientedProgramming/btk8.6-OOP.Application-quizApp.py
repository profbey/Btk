# question 

class Question():
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer


# QUIZ

q1 = Question(f'What is the best programming language?', ['c++', 'python', 'javascript', 'html'], 'javascript')
q2 = Question(f'What is the most popular programming language?', ['c++', 'python', 'javascript', 'html'], 'python')
q3 = Question(f'What is the the most money-making programming language?', ['c++', 'python', 'javascript', 'html'], 'c++')

questions = [q1,q2,q3]

class Quiz():
    def __init__(self, questions):
        self.questions     = questions
        self.score         = 0 
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()                                  # Renamed 'questions' to 'question' for clarity
        print(f'Question {self.questionIndex + 1}: {question.text}')   # Access the text attribute directly, not as a method call


        for q in question.choices:
            print(' ' + q)

        answer = input('** Answer: ')

        if question.checkAnswer(answer):                              # Call checkAnswer on the Question object (question)
            print('Congrat!')
        else: 
            print(f'False Bro, the true answer is {question.answer}') # Corrected to question.answer
        print('--- ' * 15 + '\n')

quiz = Quiz(questions)
quiz.displayQuestion()



'''
questions = quiz.questions[quiz.questionIndex]
print(questions.text)
'''




'''print(q1.checkAnswer('javascript'))
print(q2.checkAnswer('python'))
print(q3.checkAnswer('python'))'''





