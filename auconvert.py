import sys
import os
sys.path.append(os.path.abspath("/usr/local/lib/python3.7/site-packages"))
import glob
from pydub import AudioSegment

video_dir = 'content/'  # Path where the videos are located
extension_list = ('*.mp4', '*.flv')

os.chdir(video_dir)
for extension in extension_list:
    for video in glob.glob(extension):
        #mp3_filename = os.path.splitext(os.path.basename(video))[0] + '.mp3'
        #AudioSegment.from_file(video).export(mp3_filename, format='mp3')
        flac_filename = os.path.splitext(os.path.basename(video))[0] + '.flac'
        audio = AudioSegment.from_file(video)
        audio = audio.set_channels(1)
        audio.export(flac_filename, format='flac')
