"""Simple Reader to file
Reads data from a file and outputs it to the console
"""
import argparse
from asyncio.windows_events import NULL
import pathlib
import subprocess
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
    #Код логической части
    try:
        print("Фамилия\tИмя\tОтчество\tГод рождения")
        file = open(arguments.path, "r")  
        while True:           
            current_line = file.readline()
            if not current_line:
                print("End Of File")
                break
            inp_str = current_line.split(";")  
            print (inp_str[0], end= "\t")
            print (inp_str[1], end= "\t")
            print (inp_str[2], end= "\t")
            print (inp_str[3], end= "")
        file.close()       
    except IOError:
        print("Файл отсутствует или пустой")
    except IndexError:  
        print("Нету необходимого слова в файле")
    except Exception:
        print("Незарезирвированная ошибка")
        
if __name__ == "__main__":
    	main()
