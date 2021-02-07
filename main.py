import os
import shutil


def create_folder(path_downloads, key):
    path_downloads += '/' + key
    try:
        os.mkdir(path_downloads)
    except OSError:
        print(f"La carpeta {key} ya existe")
    else:
        print("Se ha creado el directorio: %s " % path_downloads)


def read_folder(ruta, dic_file):
    content = os.listdir(ruta)   # lee
    print(content)
    for archivo in content:
        if archivo[-4::] == ".exe":
            dic_file['Descargables'].append(archivo)
        elif archivo[-4::] == ".pdf":
            dic_file['PDF'].append(archivo)
        elif archivo[-4::] == ".zip":
            dic_file['ZIP'].append(archivo)
        elif archivo[-4::] == ".png" or archivo[-4::] == ".jpg":
            dic_file['Imagenes'].append(archivo)
    print(dic_file)
    return dic_file


def move_tofolfer(path_downloads, type_file):
    for file in dic_file[type_file]:
        shutil.move(path_downloads + '/' + file, path_downloads + '/' + type_file)

if __name__ == '__main__':
    user_path = os.environ['USERPROFILE'] # Obtiene el camino del usuario
    path_downloads = user_path + '/Downloads'
    dic_file = {'Descargables': [], "PDF": [], "ZIP": [], "Imagenes" : []}
    dic_file = read_folder(path_downloads, dic_file) # Lee los archivos de la carpeta downloads
    for key in dic_file.keys():
        create_folder(path_downloads, key)
    for type_file in dic_file.keys():
        move_tofolfer(path_downloads, type_file)

    print("El proceso ha terminado con exito")