import os

# Deletes all files associated with the guildID
def delete_files(guildId):
    directory_path = os.path.abspath('/app/transcriptions')

    for file in os.listdir(directory_path):
        if not file.startswith('.'):
            id, timestamp = file.split('--')
            if id == guildId:
                try:
                    os.remove(f"{directory_path}/{file}")
                except OSError as e:
                    print(f"Error deleting {file}: {e}")