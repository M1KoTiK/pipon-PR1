"""Simple Reader to file
Reads data from a file and outputs it to the console
"""
import argparse
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
    """ Если нужно открыть папку в которуюю ведётся 
        запись, то можно использовать следующую команду:
        subprocess.Popen(r'explorer /select,' + arguments.path)
        :3
    """           
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
