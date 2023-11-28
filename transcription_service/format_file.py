import os

def format(file_path):
    with open(file_path, 'r') as f:
        final_text = ''
        avoided_words = [
            "MBC 뉴스 이덕영입니다.",
            "지금까지 신선한 경제였습니다."
        ]
        for line in f:
            timestamp_start, remaining = line.split(" - ", 1)
            remaining, timestamp_end = remaining.split(" = ", 1)
            name, remaining_check = remaining.split(': ', 1)
            name, text = remaining.split(": ", 1)

            words = remaining.split()

            if remaining_check not in avoided_words and len(words) > 2:
                final_text += f"{name}: {text}\n\n"

    directory, filename = os.path.split(file_path)
    with open(os.path.join(directory, 'formatted_' + filename), 'a+') as f:
        f.write(final_text)

format("transcription_service/transcriptions/1167939648530694165--2023-11-27 20:57:35.txt.txt")
