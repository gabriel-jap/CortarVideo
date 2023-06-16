import subprocess
import json
import os.path

from constants import RUTA_DESTINO_DE_LISTA,RUTA_DEL_VIDEO_ENTERO

def get_timestamps (video: str) -> list[dict] :
        listado = list()
        exe_out=subprocess.run([os.path.join("Recursos","ffprobe.exe"),"-i", video ,"-print_format", "json", "-show_chapters", "-loglevel", "error"],capture_output=True)
        chapters = json.loads(exe_out.stdout)["chapters"]
        for nro,chapter in enumerate(chapters,start=1):
            start = chapter["start_time"]
            end = chapter["end_time"]
            title = (str(chapter["tags"]["title"])
                    .replace("Ilustración ","IMG_")
                    .replace("Subtítulo ","Sub_")
                    .replace("Título","titulo")
                    .replace("R? ","rep_")
                    .replace("? ","Q_")
                    .replace("§ ","parr_")
                    .replace(". ","_")
                    .replace(":","_")
                    .replace(",","_")
                    )
            listado.append({"nro":nro,"titulo":title,"startSec":start,"endSec":end})
        return listado

def show_timestamps (listado: list[dict]) -> str:
    csv = ""
    for chapter in listado:
        csv = csv + (",".join([chapter["titulo"],chapter["startSec"],chapter["endSec"]])) + "\n"
    return csv

def save_timestamps(texto:str,ruta_y_nombre: str):
    with open(ruta_y_nombre,"w") as out:
        out.write(texto)


if __name__ == "__main__":
     lista = get_timestamps(RUTA_DEL_VIDEO_ENTERO)
     text = show_timestamps(lista)
     save_timestamps(text,RUTA_DESTINO_DE_LISTA)