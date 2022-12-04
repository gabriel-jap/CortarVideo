import csv
from moviepy.editor import VideoFileClip


VIDEO: str = r"Recursos\w_LSA_202209_04_r720P.mp4"
TABLA: str = r"Recursos\Tiempos - 1_0.csv"

RUTA_DESTINO: str = "Clips/"
PREFIJO: str = "prueba"
EXTENSION: str = ".mp4"


VIDEO_ORIGINAL=VideoFileClip(VIDEO)
class response():
    def __init__(self, exito: bool, clip: VideoFileClip, error: str = "") -> None:
        self.exito = exito
        self.clip = clip
        self.error = error

def a_segundos(duracion: str) -> int:
    "Funcion que recibe una duracion en formato MM:SS y devuelve la cantidad de segundos que corresponde a esa duración"
    minutos,segundos=duracion.split(":")
    minutos=int(minutos)
    segundos=int(segundos)
    return minutos*60+segundos

def nombre_archivo(archivo:dict)->str:
    "Crea el nombre del archivo segun el formato"
    return f"{PREFIJO}_{archivo['No']} {archivo['Nombre']}"

def cortar_video(original: VideoFileClip, segundo_inicio: int, segundo_fin: int) -> response:
    "Crea un objeto con un fragmento del video original"
    try:
        clip=original.subclip(segundo_inicio,segundo_fin)
    except Exception as e:
        return response(False,original, str(e))
    else:
        return response(True,clip)

with open(TABLA, mode ='r')as FILE:
    DICT_FILE = csv.DictReader(FILE)
    resultado: list[bool] =[]
    for line in DICT_FILE:
        inicio=a_segundos(line["Inicio"])
        final=a_segundos(line['Final'])
        nombre = nombre_archivo(line)
        corte = cortar_video(VIDEO_ORIGINAL,inicio,final)
        if corte.exito:
            corte.clip.write_videofile(RUTA_DESTINO+nombre+EXTENSION)
            resultado.append(True)
        else:
            resultado.append(False)
            print(f"Error en archivo: {nombre}\nError: {corte.error}")

if all(resultado):
    print("Cortes realizados con exito")
