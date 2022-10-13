"""Simple Writer to file
Reads user data through the console, and writes them 
to a file one word, separated by the symbol ";"
"""
import argparse
import pathlib
def main():
    # использование библиотеки pathlib для создания стандартного пути к редактируемому файлу
    path_to_file = pathlib.Path(pathlib.Path.cwd(),'test.txt')
    # использование библиотеки agrparse для обработки аргументов начальной настройки программы(задание пути)
    set_up = argparse.ArgumentParser()
    # Аргументы строки(один аргумент, имеюющий стандартное относительное значение пути для редактируемого файла)
    set_up.add_argument('path', type=str, nargs='?', help=' path to file', default = str(path_to_file))
    arguments = set_up.parse_args()
    print(arguments.path)
    #Код логической части





if __name__ == "__main__":
	main()

