import moviepy.editor as mp
import os

start = input('Enter Start Point\n')
end = input('Enter End Point\n')

clip = mp.VideoFileClip(os.path.join('a.mp4'))

new = clip.subclip(t_start=start, t_end=(end))

# new.audio.write_audiofile('c3.mp3')

new.write_videofile('c3.mp4')