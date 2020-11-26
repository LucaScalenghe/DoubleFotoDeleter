import sys
import os
import shutil
from pathlib import Path

# importtant reference
# https://www.decodingdevops.com/python-os-walk-recursive-examples/#Python_os_walk()_Example3_with_Recursive

# how to intialize a set
# https://stackoverflow.com/questions/31656572/python-error-dict-object-has-no-attribute-add

# check if a direcotry exists if not
# https://www.decodingdevops.com/check-if-directory-exists-python-if-not-create/


def getExtension(stringA):
    a = Path(stringA)
    ris = a.name
    ris = ris.split('.')
    return ris[1]


def getName(stringA):
    a = Path(stringA)
    ris = a.name
    ris = ris.split('.')
    return ris[0]


def moveToBin(root, file_name, bin_path):
    root_as_path = Path(root)
    file_name_as_path = Path(file_name)
    bin_path_as_path = Path(bin_path)

    file_name_path = root_as_path/file_name
    i = 1
    dest_path = bin_path_as_path/file_name_as_path
    file_exists = os.path.isfile(dest_path)          # ../bin/file.txt
    while file_exists:
        # destination + name + str(i) + extension   in order to not have duplicates
        i += 1
        name = getName(file_name)  # name.extension
        number = str(i)
        point = '.'
        ext = getExtension(file_name)

        # creating the actual destination path adding the number
        name_with_number = Path(name + '(' + number + ')' + point + ext)
        dest_path = bin_path_as_path/name_with_number
        file_exists = os.path.isfile(dest_path)

    # moving the file from his original path to his destination path
    dest_path = str(dest_path)
    os.rename(file_name_path, dest_path)

    # shutil.move(file_name_path, bin_path)  #you need the full path to the file_name and the full path of the bin


def moveToSingleFotos(root, file_name, single_fotos_list, single_fotos_path):
    os.chdir(root)
    # ciao = os.getcwd()
    single_fotos_list.append(file_name)
    shutil.move(file_name, single_fotos_path)


if __name__ == '__main__':

    # while len(sys.argv) > 1 and len(sys.argv)<3 and not os.path.exists(sys.argv[1]) :
    #     print("Insert ONE valid path to start")

    # start_path_as_string= sys.argv[1]
    # start_path = Path (p)

    exclude = ['SingleFotos', 'Bin']
    extensions = ['jpg', 'png']

    bin_path = (r'C:\Users\lucas\Desktop\Foto\Bin')
    single_fotos_path = (r'C:\Users\lucas\Desktop\Foto\SingleFotos')

    start_path = Path(r'C:\Users\lucas\Desktop\Foto')

    single_fotos_list = []  # initialize a list just with the file names
    # single_fotos_paths = [] #initialize a list with the complete path name of the file

    for root, dirs, files in os.walk(str(start_path)):
        # https://stackoverflow.com/questions/19859840/excluding-directories-in-os-walk
        dirs[:] = [d for d in dirs if d not in exclude]
        for file_name in files:
            # filters all the images formats (formats has to be added)
            if getExtension(file_name) in extensions:
                if file_name in single_fotos_list:
                    # move the file in the bin directory and for every double saves it double.txt double1.txt double2.txt
                    moveToBin(root, file_name, bin_path)
                else:
                    # move the file in the single fotos directory
                    moveToSingleFotos(
                        root, file_name, single_fotos_list, single_fotos_path)

    print(single_fotos_list)

  