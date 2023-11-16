A discord bot that can listen in on a voice call and record and transcribe the entire call.

This works using two different serviecs:

  One is the actual bot, which can listen to commands and perform actions based off of those commands. This is written in javascript through a node image from docker. It then sends these files to the transcription service.

  The other service is a transcription service, which recieves the audio stream in TCP packets and converts them to wav format to transcribe onto a txt file. The transcription service used is huggingface's small whisper model. Hoping to inscrease it to medium in the future for more accurate   transcriptions.
