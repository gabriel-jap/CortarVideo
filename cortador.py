import csv
from moviepy.editor import VideoFileClip


VIDEO: str = r"Recursos\w_LSA_202209_04_r720P.mp4"
TABLA: str = r"Recursos\Tiempos - 1_0.csv"

RUTA_DESTINO: str = "Clips/"
PREFIJO: str = "prueba"
EXTENSION: str = ".mp4"

class subclip():
    def __init__(self, nombre:str, inicio:int, final:int) -> None:
        self.nombre = nombre
        self.inicio = inicio
        self.final = final
        self.clip: VideoFileClip
    def aplicar_corte(self, original: VideoFileClip):
        self.clip = original.subclip(self.inicio,self.final)

def a_segundos(duracion: str) -> int:
    "Funcion que recibe una duracion en formato MM:SS y devuelve la cantidad de segundos que corresponde a esa duración"
    minutos,segundos=duracion.split(":")
    minutos=int(minutos)
    segundos=int(segundos)
    return minutos*60+segundos

def nombre_archivo(archivo:dict)->str:
    "Crea el nombre del archivo segun el formato"
    return f"{PREFIJO}_{archivo['No']} {archivo['Nombre']}"

def obtener_parametros(ruta: str):
    """
    Dada una ruta a un archivo .csv, crea una lista con objetos subclip sin procesar, pero con la información para hacerlo

    Input
        ruta (str): La ruta a un archivo .csv
    Output
        una list con tantos objetos subclip como filas halla en el csv
    """
    output:list[subclip]=[]
    with open(ruta, mode ='r')as FILE:
        DICT_FILE = csv.DictReader(FILE)
        for line in DICT_FILE:
            inicio=a_segundos(line["Inicio"])
            final=a_segundos(line['Final'])
            nombre = nombre_archivo(line)
            output.append(subclip(nombre,inicio,final))
    return output

if __name__=="__main__":
    clips = obtener_parametros(TABLA)
    with VideoFileClip(VIDEO) as ORIGINAL:
        for corte in clips:
            corte.aplicar_corte(ORIGINAL)
            corte.clip.write_videofile(RUTA_DESTINO+corte.nombre+EXTENSION)
            corte.clip.close()