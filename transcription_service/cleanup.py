import os

converted_files = "converted_files"
pcm = "pcm"
wav = "wav"

for filename in os.listdir(converted_files):
    file = os.path.join(converted_files, filename)
    os.remove(file)

for filename in os.listdir(pcm):
    file = os.path.join(pcm, filename)
    os.remove(file)

for filename in os.listdir(wav):
    file = os.path.join(wav, filename)
    os.remove(file)

