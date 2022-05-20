import shutil
import os


def main():
    os.chdir('FilesToSort')
    print("Starting directory is: {}".format(os.getcwd()))
    extensions_folder = {}

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension = filename.split(".")[1]
        if extension not in extensions_folder:
            folder_name = input("What category would you like to sort {} files into? ".format(extension))
            extensions_folder[extension] = folder_name

            try:
                os.mkdir(folder_name)
            except FileExistsError:
                pass

        shutil.move(filename, (f"{extensions_folder[extension]}/" + filename))


main()
