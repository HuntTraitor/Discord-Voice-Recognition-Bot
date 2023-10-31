import sys
import os
import wave

input_dir = "pcm"
output_dir = "wav"

if not os.path.exists(input_dir):
    os.makedirs(output_dir)

for filename in os.listdir(input_dir):
    if filename.endswith(".pcm"):
        print("test")
        input_filepath = os.path.join(input_dir, filename)
        output_filename = os.path.join(output_dir, os.path.splitext(filename)[0]+'.wav')

        with open(input_filepath, 'rb') as pcmfile:
            pcmdata = pcmfile.read()
        
        with wave.open(output_filename, 'wb') as wavfile:
            wavfile.setparams((2,2,44100,0,'NONE','NONE'))
            wavfile.writeframes(pcmdata)