from transformers import pipeline

# Transcribe data using the pipeline from handle_packet
def transcribe(pipe, data, username, filename):
    output_file = f"transcriptions/{filename}"
    transcription = pipe(data, batch_size=8)["text"]

    with open(output_file, 'a+') as output_file:
        output_file.write(f"{username}: {transcription}\n")