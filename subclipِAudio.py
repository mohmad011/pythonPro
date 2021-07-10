import moviepy.editor as mp
import os

nameInput = input('Enter Name Input File\n')
nameOutput = input('Enter Name Output File\n')

# Converts into more readable format
def convert(seconds):
    hours = seconds // 3600
    seconds %= 3600
    mins = seconds // 60
    seconds %= 60
    return hours, mins, seconds

clip = mp.AudioFileClip(os.path.join(nameInput))

# Contains the duration of the video in terms of seconds
video_duration = int(clip.duration)
hours, mins, secs = convert(video_duration)


time = input('Do Want Enter Time As a Seconds ? ( y or n )\n')

if time == 'y':
	start = input('Enter Start Point\n') or 1
	end = input('Enter End Point\n') or secs
	endAud = int(end) + 1
	
else:
	print('For Start Point')
	Hours1 = (input('Enter Hours...\n')) or 0
	Mints1 = (input('Enter Mints...\n')) or 1
	Sec1 = (input('Enter Secs...\n')) or 1
	print('For End Point')
	Hours2 = (input('Enter Hours...\n')) or 0
	Mints2 = (input('Enter Mints...\n')) or 1
	Sec2 = (input('Enter Secs...\n')) or 1

	start = (int(Hours1) * 60 * 60) + (int(Mints1) * 60) + int(Sec1)
	endAud = ((int(Hours2) * 60 * 60) + (int(Mints2) * 60) + int(Sec2))



# clip = mp.VideoFileClip(os.path.join(nameInput))

new  = clip.subclip(t_start=start, t_end=endAud)

# new.audio.write_audiofile(nameOutput)

if not os.path.exists('SaveAudio'):
    os.mkdir('SaveAudio')

new.write_audiofile('SaveAudio/' + nameOutput)

# new.write_videofile(nameOutput)