import csv
from moviepy.editor import VideoFileClip

# Ruta al archivo del video a cortar
VIDEO: str = r"Recursos/16.mp4"
# Tabla con la información de los cortes
TABLA: str = r"Recursos\Tiempos.csv"
# Prefijo de todos los archivos creados
PREFIJO: str = "W"

# Carpeta en la que guardar los clips
RUTA_DESTINO: str = "Clips"+"/"


class subclip():
    """
    Objetos encargados de almacenar unir los subclips creados con la información de su corte, así como el nombre que deben de tener al ser guardados

    Input
        nombre(str): el nombre con el que se debe de guardar el archivo
        inicio y fin: numero de segundo en el que se debe de hacer el corte

    Metodos
        aplicar_corte: se le pasa un video y corta los segundos indicados. El clip se guarda en el atributo 'clip'
    """

    def __init__(self, nombre: str, inicio: int, final: int) -> None:
        self.nombre = nombre
        self.inicio = inicio
        self.final = final

    def aplicar_corte(self, original: VideoFileClip, nombre: str):
        if self.inicio == self.final:
            original.save_frame(nombre+".jpeg", t=self.inicio)
        else:
            original.subclip(self.inicio, self.final).write_videofile(
                nombre+".mp4")


def a_segundos(duracion: str) -> int:
    "Funcion que recibe una duracion en formato MM:SS y devuelve la cantidad de segundos que corresponde a esa duración"
    minutos, segundos = duracion.split(":")
    minutos = int(minutos)
    segundos = int(segundos)
    return minutos*60+segundos


def nombre_archivo(archivo: dict) -> str:
    "Crea el nombre del archivo segun el formato"
    return f"{PREFIJO}_{archivo['No']} {archivo['Nombre']}"


def obtener_parametros(ruta: str) -> list[subclip]:
    """
    Dada una ruta a un archivo .csv, crea una lista con objetos subclip sin procesar, pero con la información para hacerlo

    Input
        ruta (str): La ruta a un archivo .csv
    Output
        una list con tantos objetos subclip como filas halla en el csv
    """
    output: list[subclip] = []
    with open(ruta, mode='r')as FILE:
        DICT_FILE = csv.DictReader(FILE)
        for line in DICT_FILE:
            inicio = a_segundos(line["Inicio"])
            final = a_segundos(line['Final'])
            nombre = nombre_archivo(line)
            output.append(subclip(nombre, inicio, final))
    return output


if __name__ == "__main__":
    clips = obtener_parametros(TABLA)
    nombreError = []
    with VideoFileClip(VIDEO) as ORIGINAL:
        for corte in clips:
            try:
                corte.aplicar_corte(ORIGINAL, RUTA_DESTINO+corte.nombre)
            except Exception as e:
                nombreError.append((corte.nombre, e))
                break
            print(nombreError)
