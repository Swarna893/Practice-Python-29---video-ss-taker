# Practice-Python-29---video-ss-taker

from moviepy.editor import *

clip = VideoFileClip("jawan.mp4").subclip(00, 1)

clip = clip.margin(60)
var = clip.write_videofile("new_margin.mp4")
