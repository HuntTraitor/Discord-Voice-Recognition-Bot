import whisper
import os

input_dir = "wav"
output_dir = "converted_files"

os.makedirs(output_dir, exist_ok=True)

model = whisper.load_model("tiny")

for filename in os.listdir(input_dir):
    if filename.endswith(".wav"):
        input_path = os.path.join(input_dir, filename)

        result = model.transcribe(input_path, fp16=False)
        transcription = result["text"]

        output_filename = os.path.splitext(filename)[0] + ".txt"
        output_path = os.path.join(output_dir, output_filename)

        with open(output_path, "w") as output_file:
            output_file.write(transcription)
        
        print(f"Transcribed {filename} and saved to {output_filename}")
