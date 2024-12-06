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
            print(f"{i + 1}. {choice}")                         # Secenekleri numaralandirarak gosterme

        answer = input("** Answer (enter the number of your choice): ")
        try:
            answer_index = int(answer) - 1                      # Kullanicidan gelen cevabi sayiya cevirme
            if 0 <= answer_index < len(question.choices):
                user_answer = question.choices[answer_index]    # Secenek listesinden cevabi alma
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
    Question("What is the correct way to print 'Hello, World!'", 
             ["print('Hello, World!')", "echo 'Hello, World!'", 
              "System.out.println('Hello, World!')", 
              "Console.WriteLine('Hello, World!')"], 
             "print('Hello, World!')"),
    Question("Which data type is used to store a sequence of", 
             ["int", "float", "str", "bool"], "str"),
    Question("x = 5\ny = 2\nprint(x // y)\nWhat is the output of the following codei\n", 
             ["2.5", "2", "3", "2.0"], "2"),
    Question("How do you define a function in Pythoni", 
             ["function my_function():", "def my_function():", 
              "my_function():", "func my_function():"], 
             "def my_function():"),
    Question("What is the purpose of the `len()` function", 
             ["To calculate the length of a string", 
              "To find the maximum value in a list", 
              "To sort a list", "To reverse a string"], 
             "To calculate the length of a string"),
]

# Quiz baslatma
quiz = Quiz(questions)
quiz.display_question()                                         # İlk soruyu gostermek icin display_question() cağiriliyor



'''
Algoritma:

    Baslangic:
        Question sinifi, her bir soruyu temsil eder ve sorunun metnini, seceneklerini ve dogru cevabini depolar.
        Quiz sinifi, sorulari yonetir, skoru tutar ve mevcut soru indeksini izler.
        Sorular questions listesinde tanimlanir ve Quiz sinifina iletilir.

    Soru Gosterme:
        display_question() fonksiyonu, mevcut soruyu ekrana yazdirir ve kullanicidan cevap ister.
        Kullanici cevabini girer.

    Cevap Kontrolu:
        Kullanicinin cevabi, check_answer() fonksiyonu ile dogru cevapla karsilastirilir.
        Cevap dogruysa, skor 1 artirilir.

    Sonraki Soru:
        load_next_question() fonksiyonu, bir sonraki soruyu yukler ve goruntuler.
        Eger tum sorular cevaplanmissa, show_score() fonksiyonu cagirilir.

    Skor Gosterme:
        show_score() fonksiyonu, kullanicinin toplam skorunu ekrana yazdirir.

        
Tetikleyiciler:

    Quiz Baslatma:
        quiz = Quiz(questions) satiri, Quiz sinifini baslatir ve quiz oyununu baslatir.
        quiz.display_question() satiri, ilk soruyu gostermek icin display_question() fonksiyonunu tetikler.

    Cevap Verme:
        Kullanici cevabini girdisinde, display_question() fonksiyonu icindeki kod tetiklenir ve cevap kontrol edilir.

    Sonraki Soru:
        load_next_question() fonksiyonu, bir sonraki soruyu yklemek ve goruntulemek icin tetiklenir.
        Bu fonksiyon, display_question() fonksiyonu icindeki cevap kontrolunden sonra veya quiz baslatildiginda cagirilir.

    Quiz Bitisi:
        Tum sorular cevaplandiginda, show_score() fonksiyonu tetiklenir ve kullanicinin skoru gosterilir.'''