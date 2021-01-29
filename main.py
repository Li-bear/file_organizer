import os


def read_folder(ruta):
    content = os.listdir(ruta)
    print(content)


if __name__ == '__main__':
    read_folder('/Users/ALLIS/Downloads')
