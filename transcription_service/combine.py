import os

input_path = "converted_files"
arr = []
final_text = ""

for file in os.listdir(input_path):
    arr.append(file)

arr.sort(key = lambda x: x.split("_")[1])

for item in arr:
    username = item.partition('_')[0]
    message = open(f"converted_files/{item}").read()
    final_text += f"{username} - {message}\n\n"

print(final_text)