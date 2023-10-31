A discord bot that can listen in on a voice call and record and transcribe the entire call.

This works using two different serviecs:

  One is the actual bot, which can listen to commands and perform actions based off of those commands. This is written in javascript through a node image from docker. It then sends these files to the transcription service.

  The other service is a transcription service, which recieves .pcm files and converts them into .wav files and then uses openai/whisper transcription tool to transcribe these files into .txt files
