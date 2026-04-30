#Змінні
task_list = []
#Виводжу інтерфейс
def interface():
    while True:
        print("== TODOLIST ==")
        print("1. Додати задачу")
        print("2. Показати всі задачі")
        print("3. Видалити задачу")
        print("4. Вийти")
        user_choise = int(input("Виберіть пункт(1-4) "))
        main(user_choise)    
    
#Створення завдання
def add_task(task_list):
    print("-- Додати задачу --")
    task_list.append(input("Введіть задачу: "))

    print("")
    print("")
    print("-------------------")

    interface()

#Відобразити завдання
def show_tasks(task_list):
    print("-- Список задач --")

    for tasks in task_list:
        print(tasks)
    
    print("")
    print("")
    print("-------------------")
    interface()


#Видалити завдання
def del_task(task_list):
    print("-- Видалити задачу --")

    task_list.pop(int(input("Виберіть задачу яку хочете видалити "))-1)

    print("")
    print("")
    print("-------------------")

    interface()
           
#Завершити роботу програми
def finish_task():
    print("Adios amigo")
    exit()

#Основна гілка
def main(user_choise):
    match user_choise:
        case 1:
            add_task(task_list)
        case 2:
            show_tasks(task_list)
        case 3:
            del_task(task_list)
        case 4:
            finish_task()

#Запуск програми
interface()