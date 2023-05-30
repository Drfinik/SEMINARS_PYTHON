path = ('Phonebook.txt')
def team_selection():
    while True:
        print("Выберете команду:")
        user_selection = input("1 - Открыть файл\n2 - Найти контакт\n3 - Добавить контакт\n\
4 - Изменить контакт\n5 - Удалить контакт\n6 - Просмотреть все контакты\n7 - Выйти из приложения\n")
        print(user_selection)

        if user_selection == "1":
            open_file()       
        elif user_selection == '2':  
            pass
        elif user_selection == '3':  
            pass
        elif user_selection == '4':  
            pass
        elif user_selection == '5':  
            pass
        elif user_selection == '6':  
            pass
        elif user_selection == '7':
            print('До свидания!')
            break
        else:
            print('Неправильно выбрана команда!')            
            continue

def open_file():# ОТКРЫТИЕ ФАЙЛА 
    with open(path, 'r', encoding='UTF-8'):
        print("Добро пожаловать!")

if __name__ == '__main__':
    team_selection()


