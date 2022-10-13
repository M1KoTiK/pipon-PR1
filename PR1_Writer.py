"""Simple Writer to file
Reads user data through the console, and writes them 
to a file one word, separated by the symbol ";"
"""
import argparse
import pathlib
import subprocess
def check_quit(text:str) ->bool:
    print(text + " y/n")
    str = input()
    if str == 'y':
        return False
    elif str == 'n':
        return True
    else:
        print("Вводить можно только y/n")
        return check_quit(text)
def main():
    # использование библиотеки pathlib для создания стандартного пути к редактируемому файлу
    path_to_file = pathlib.Path(pathlib.Path.cwd(),'test.txt')
    # использование библиотеки agrparse для обработки аргументов начальной настройки программы (задание пути)
    set_up = argparse.ArgumentParser()
    # Аргументы строки (один аргумент, имеюющий стандартное относительное значение пути для редактируемого файла)
    set_up.add_argument('path', type=str, nargs='?', help=' path to file', default = str(path_to_file))
    arguments = set_up.parse_args()
    print("-------------------------------------------------------------------")
    print("Местоположение текстового файла - " + arguments.path)
    print("-------------------------------------------------------------------")
    print("Формат ввода данных: Фамилия Имя Отчество Год_Рождения")
    print("-------------------------------------------------------------------")
    #Код логической части
    count_add :int = 0
    while True:   
        try:            
            if count_add !=0 and check_quit("Хотите продолжить ввод данных?") == True:
                break   
            elif count_add !=0:
                print("Можете вводить данные снова")   
            count_add :int = count_add + 1     
            # total_str - строка в которую мы собираем нашу запись   
            total_str :str = ""     
            str_inp :str = input().split()
            test_year :int = int(str_inp[3])                            
            for i in range(4):
                if i == 0:
                    total_str = str_inp[i]
                else:
                    total_str =  total_str + ";" +  str_inp[i]

            file = open(arguments.path, 'a')
            """
            Если нужно открыть папку в которуюю ведётся 
            запись, то можно использовать следующую команду:
            subprocess.Popen(r'explorer /select,' + arguments.path)
            :3
            """           
            # Тут мы записываем собранную total_str в файл и ставим знак перехода на следующую строку 
            file.write(total_str + "\n")         
            file.close()
            print("-------------------------------------------------------------------")
            print("Записанная строка: " + total_str )
            print("Всего добавлено строк: " + str(count_add)) 
            print("-------------------------------------------------------------------")
        except IndexError:
            print("Введено меньше чем нужно слов. Повторите попытку")
            count_add :int = count_add - 1
            continue
        except ValueError:
            print("Введено неправильное значения для года рождения. Повторите попытку")
            count_add :int = count_add - 1
            continue
        except (ModuleNotFoundError):
            print("Не найдены библиотеки. Повторите попытку")
            count_add :int = count_add - 1
            continue  
        except Exception:
            print("Незарезирвированная ошибка")
            continue
if __name__ == "__main__":
	main()

