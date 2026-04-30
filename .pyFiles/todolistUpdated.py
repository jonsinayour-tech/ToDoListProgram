class ToDo:
    def __init__(self):
        self.lines = []
        self.load()
    

    def add_task(self):
        print("====== Додати задачу ======")
        self.lines.append("\n" + input("Введіть задачу: "))
        self.save()
        print("===========================")

    def show_tasks(self):
        print("====== Список задач =======")
        for x in self.lines:
            print(x)
        print("===========================")

    def delete_task(self):
        print("==== Видалити елемент =====")
        self.show_tasks()

        self.lines.pop(int(input("Виберіть задачу яку хочете видалити "))-1)
        self.save()
        print("===========================")
    
    def close_program(self):
        print("Adios amigo")
        exit()

    def save(self):
        with open("./txtFiles/todolist.txt", "w") as f:
            f.writelines(self.lines)

    def load(self):
        with open("./txtFiles/todolist.txt", "r") as f:
            self.lines = f.readlines()
        
todo = ToDo()
while True:
    print("====== TODOLIST ======")
    print("1. Додати задачу")
    print("2. Показати всі задачі")
    print("3. Видалити задачу")
    print("4. Вийти")
    print("======================")
    user_choise = int(input("Виберіть пункт(1-4) "))
    
    match user_choise:
        case 1:
            todo.add_task()
        case 2:
            todo.show_tasks()
        case 3:
            todo.delete_task()
        case 4:
            todo.close_program()