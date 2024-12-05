# question 

class Question():
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer


# QUIZ

q1 = Question(f'What is the best programming language?'                 , ['c++', 'python', 'javascript', 'html'], 'javascript')
q2 = Question(f'What is the most popular programming language?'         , ['c++', 'python', 'javascript', 'html'], 'python')
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
        question = self.getQuestion()                                   # Renamed 'questions' to 'question' for clarity
        print(f'Question {self.questionIndex + 1}: {question.text}')    # Access the text attribute directly, not as a method call


        for q in question.choices:
            print(' ' + q)

        answer = input('** Answer: ')
        self.guess(answer)                                              # Call self.guess() now that it's an instance method
        self.loadQuestion()                                             # Call self.loadQuestion() now that it's an instance method

        if question.checkAnswer(answer):                                # Call checkAnswer on the Question object (question)
            self.score += 1 

        print('- ' * 30 + '\n')

    
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex + 1:               # Changed to +1 to avoid index error
            self.showScore()                                            # Corrected to call showScore instead of self.score()
        else:
            self.displayProgress()
            self.questionIndex += 1 

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber= self.questionIndex + 1

        if questionNumber > totalQuestion:
            print('Quiz is over.')
        else:
            print(f' Question {questionNumber} of {totalQuestion} '.center(59,'*'))
                                                                        # Define guess() and loadQuestion() as instance methods
    def guess(self,answer):
        question = self.getQuestion()

    def showScore(self):
        print(f'Score: ',self.score)


quiz = Quiz(questions)
quiz.loadQuestion()