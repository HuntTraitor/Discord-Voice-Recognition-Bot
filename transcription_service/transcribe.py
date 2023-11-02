from transformers import pipeline
import os

device = "cpu"

pipe = pipeline(
  "automatic-speech-recognition",
  model="openai/whisper-small",
  chunk_length_s=30,
  device=device,
)

input_dir = "wav"
output_dir = "converted_files"

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith(".wav"):
        input_path = os.path.join(input_dir, filename)

        transcription = pipe(input_path, batch_size=8)["text"]

        output_filename = os.path.splitext(filename)[0] + ".txt"
        output_path = os.path.join(output_dir, output_filename)

        with open(output_path, "w") as output_file:
            output_file.write(transcription)
        
        print(f"Transcribed {filename} and saved to {output_filename}")