# CortarVideo

## Instalación
Para que el proyecto funcione antes hay que seguir 2 pasos:
- obtener un ffprobe.exe para que sirva de motor para la App. Recomiendo descargarlo de un lugar seguro como el link oficial https://ffmpeg.org/download.html
- Luego colocarlo en la misma carpeta que los archivos python y crear ahí mismo una carpeta **Clips**

## Uso
- Primero, colocaremos l video a cortar en la carpeta Clips.
- Luego, habra que editar constants.py de forma de que el nombre de la variable ```nombre_del_video``` contenga el nombre del archivo y su extensión, tal que:
 ```nombre_del_video = "video_de_ejemplo.mp4"```
- Luego se ejecutará  ```list_chapters.py```. Ahora en la carpeta  ```Clips``` habrá un archivo  ```Tiempos.csv```. La primera columna representa al titulo que tendrá el subclip, la segunda a el inicio del clip en segundos, y la tercera a el fin del clip en segundos.
- Haga los cambios que guste, y luego ejecute  ```cortador.py```. Luego de que termine, encontrará los clips en la carpeta  ```Clips```.
 
 > NOTA:
 > Aquellos clips que tengan en el titulo "IMG" se cortará la imagen del frame de un segundo siguiente a el segundo inicio
