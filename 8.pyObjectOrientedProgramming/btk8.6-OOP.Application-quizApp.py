class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def check_answer(self, answer):
        return self.answer == answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_index = 0

    def get_question(self):
        return self.questions[self.question_index]

    def display_question(self):                                 # Define question_number and total_questions here                                   
        question_number = self.question_index + 1
        total_questions = len(self.questions)
        print(f" Question {question_number} of {total_questions} ".center(59, "*"))
        question = self.get_question()
        print(f"Question {self.question_index + 1}: {question.text}")

        for i, choice in enumerate(question.choices):
            print(f"{i + 1}. {choice}")                         # Seçenekleri numaralandırarak gösterme

        answer = input("** Answer (enter the number of your choice): ")
        try:
            answer_index = int(answer) - 1                      # Kullanıcıdan gelen cevabı sayıya çevirme
            if 0 <= answer_index < len(question.choices):
                user_answer = question.choices[answer_index]    # Seçenek listesinden cevabı alma
                if question.check_answer(user_answer):
                    self.score += 1
            else:
                print("Invalid choice. Please enter a number between 1 and", len(question.choices))
        except ValueError:
            print("Invalid input. Please enter a number.")

        self.load_next_question()

    def load_next_question(self):
        if self.question_index + 1 < len(self.questions):
            self.display_progress()
            self.question_index += 1
            self.display_question()
        else:
            self.show_score()

    def display_progress(self):                                 # question_number and total_questions are now defined in display_question
                
        print("-" * 30 + "\n")

    def show_score(self):
        total_questions = len(self.questions)
        print(f"Score: {self.score} / {total_questions} ")


# Sorular
questions = [
    Question("What is the best programming language?", ["c++", "python", "javascript", "html"], "javascript"),
    Question("What is the most popular programming language?", ["c++", "python", "javascript", "html"], "python"),
    Question("What is the most money-making programming language?", ["c++", "python", "javascript", "html"], "c++"),
]

# Quiz başlatma
quiz = Quiz(questions)
quiz.display_question()                                         # İlk soruyu göstermek için display_question() çağırılıyor