class Note:
    def __init__(self):
        # Initialization, if needed 
        pass

    def show_notes(self):
        # Implementation for showing notes
        pass

    def enter_notes(self):
        name       = input("Student Name: ")
        surname    = input("Student surname: ")
        mt1        = input("midterm 1 grade: ")
        mt2        = input("Midterm 2 grade: ")
        finalGrade = input("Final grade: ")

        with open('sinavNotlari.txt', 'a', encoding='utf-8') as file:
            file.write(f'*{name}/{surname}/{mt1}/{mt2}/{finalGrade}\n')

    def save_notes(self):
        # Implementation for saving notes
        pass

    def give_letter_grade(self):
        # Implementation for assigning letter grades
        pass

    def save_and_quit(self):
        # Implementation for saving and exiting
        pass

def main():
    note_instance = Note() 

    while True:
        islem = int(input('1) Showing Notes\n2) Enter Notes\n3) Save Notes\n4) Give Letter Grade and Export\n5) Quit\n'))

        if islem == 1:
            note_instance.show_notes()
        elif islem == 2:
            note_instance.enter_notes()
        elif islem == 3:
            note_instance.save_notes()
        elif islem == 4:
            note_instance.give_letter_grade()
        elif islem == 5:
            note_instance.save_and_quit()
            break  # Exit the loop when the user chooses to quit
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()