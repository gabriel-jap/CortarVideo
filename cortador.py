from moviepy.editor import VideoFileClip
from constants import RUTA_DEL_VIDEO_ENTERO, RUTA_DESTINO,RUTA_DESTINO_DE_LISTA

class subclip():
    """
    Objetos encargados de almacenar unir los subclips creados con la información de su corte, así como el nombre que deben de tener al ser guardados

    Input
        nombre(str): el nombre con el que se debe de guardar el archivo
        inicio y fin: numero de segundo en el que se debe de hacer el corte

    Metodos
        aplicar_corte: se le pasa un video y corta los segundos indicados. El clip se guarda en el atributo 'clip'
    """

    def __init__(self, nombre: str, sec_inicio: int, sec_final: int) -> None:
        self.nombre = nombre
        self.inicio = sec_inicio
        self.final = sec_final

    def aplicar_corte(self, original: VideoFileClip, ruta_de_destino: str):
        if "IMG" in self.nombre:
            original.save_frame(str(ruta_de_destino)+self.nombre+".jpeg", t=float(self.inicio)+1)
        else:
            original.subclip(self.inicio, self.final).write_videofile(
                ruta_de_destino+self.nombre+".mp4")

def listado(path:str)-> list[subclip]:
    output = []
    with open(path,"r") as list:
        for no,element in enumerate(list):
            titulo,inicio,final = element.split(",")
            output.append(subclip(nombre=str(no)+" "+titulo, sec_inicio=inicio, sec_final=final))
    return output

if __name__ == "__main__":
    errores = []
    with VideoFileClip(RUTA_DEL_VIDEO_ENTERO) as ORIGINAL:
        for corte in listado(RUTA_DESTINO_DE_LISTA):
            try:
                corte.aplicar_corte(ORIGINAL, RUTA_DESTINO)
            except Exception as e:
                errores.append((corte.nombre, e))
        print(errores)
