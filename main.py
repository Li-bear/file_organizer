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


def read_folder(ruta, dic_file):  # Mejorar esta función
    content = os.listdir(ruta)  # lee
    for archivo in content:
        if archivo[-4::] == ".exe":
            dic_file['Descargables'].append(archivo)
        elif archivo[-4::] == ".pdf":
            dic_file['PDF'].append(archivo)
        elif archivo[-4::] == ".zip":
            dic_file['ZIP'].append(archivo)
        elif archivo[-4::] == ".png" or archivo[-4::] == ".jpg" or archivo[-4::] == ".gif":
            dic_file['Imagenes'].append(archivo)
        elif archivo[-4::] == ".mp4":
            dic_file["Videos"].append(archivo)
        elif archivo[-4::] == ".mp3":
            dic_file["Audio"].append(archivo)
    return dic_file


def move_tofolfer(path_downloads, type_file):
    for file in dic_file[type_file]:
        shutil.move(path_downloads + '/' + file, path_downloads + '/' + type_file)


if __name__ == '__main__':
    #path_downloads = os.environ['USERPROFILE']  #Obtiene el camino del usuario hacia descargas
    path_downloads = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')
    # Buscar solucion para computadores donde la carpeta de descargas se encuentra en otro lugar

    dic_file = {'Descargables': [], "PDF": [], "ZIP": [], "Imagenes": [], "Videos": [], "Audio": []}
    dic_file = read_folder(path_downloads, dic_file)  # Lee los archivos de la carpeta downloads
    for key in dic_file.keys():
        create_folder(path_downloads, key)
    for type_file in dic_file.keys():
        move_tofolfer(path_downloads, type_file)

    #TODO: problemas cuando los archivos tienen el mismo nombre
