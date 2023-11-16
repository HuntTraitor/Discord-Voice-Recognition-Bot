from transformers import pipeline

def transcribe(pipe, data, username):

    output_file = "transcription.txt"
    transcription = pipe(data, batch_size=8)["text"]

    with open(output_file, 'a') as output_file:
        output_file.write(f"{username}: {transcription}\n")