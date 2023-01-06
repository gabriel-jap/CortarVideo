from moviepy.editor import VideoFileClip, concatenate_videoclips
clip1 = VideoFileClip("08_08 parr6A.mp4") #5 seconds video
clip2 = VideoFileClip("08_08 parr6B.mp4") #10 seconds video
final_clip = concatenate_videoclips([clip1,clip2])
final_clip.write_videofile("08_08 parr6.mp4") #16 seconds video
final_clip.close()