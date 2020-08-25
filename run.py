import os
from src.file_random_line import FileRandomLine

file_path = os.path.dirname(os.path.realpath(__file__))


def presentation():
    print("Seja bem vindo(a)!")
    print("Referêncie um arquivo que esteja com valores separados por linha.")
    print("Cada linha será lida e um valor será sorteado. ")
    print("*****************************************************************\n")


def open_file():
    file_name = input("Digite o nome do arquivo para ser lido (** Se não for digitado, será lido o 'v.txt'): \n")
    if file_name == None or file_name == "" or file_name == 0:
        file_name = "v.txt"
        
    opened_file = open(file_path + "/" + file_name, 'r')
    return opened_file


def show_draw_result(result):
    print("O valor sorteado foi:")
    print(">>>",result, "<<<")
    

if __name__ == "__main__":
    presentation()
    opened_file = open_file()

    file_sorter = FileRandomLine(opened_file)
    sorted_value = file_sorter.get_file_random_line()

    show_draw_result(sorted_value)
