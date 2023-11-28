from config import AVOIDED_WORDS

# Helps with filetering out garbage
def validTranscription(text):
    valid = False
    words = text.split()
    if words not in AVOIDED_WORDS and len(words) > 2:
        valid = True
    return valid