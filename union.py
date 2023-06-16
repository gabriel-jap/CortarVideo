from moviepy.editor import VideoFileClip, concatenate_videoclips
from constants import RUTA_DESTINO

clip1 = ""
clip2 = ""

final_clip = concatenate_videoclips([VideoFileClip(RUTA_DESTINO+clip1),VideoFileClip(RUTA_DESTINO+clip2)])
final_clip.write_videofile("W_3 parr3.mp4") #16 seconds video
final_clip.close()