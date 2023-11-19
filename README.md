A discord bot that can listen in on a voice call and record and transcribe the entire call.

This works using two different serviecs:

  One is the actual bot, which can listen to commands and perform actions based off of those commands. This is written in javascript through a node image from docker. It then sends these files to the transcription service.

  The other service is a transcription service, which recieves the audio stream in TCP packets and converts them to wav format to transcribe onto a txt file. The transcription service used is huggingface's small whisper model. Hoping to inscrease it to medium in the future for more accurate   transcriptions.



To setup this file, the first thing you want to do is fill out a .env using your discord credentials. These can be found via discord developer portal.

Next, if using pyright, its good to make a pyrightconfig.json file inside the trasncription_service folder that has:
{
  "venvPath": "/path/to/virtual/environments",
  "venv": "your_virtual_environment_name"
}
included. This ensures your interperater can read the imports. I will update this in the future to have a seperate volume with venv so you don't have to run
pip install -r requirements.txt inside of your venv locally.
