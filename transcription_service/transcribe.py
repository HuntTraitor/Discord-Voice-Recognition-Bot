from transformers import pipeline

def transcribe(data):
    device = "cpu"

    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-small",
        chunk_length_s=30,
        device=device
    )

    output_file = "transcription.txt"
    transcription = pipe(data, batch_size=8)["text"]

    with open(output_file, 'a') as output_file:
        output_file.write(transcription + "\n")