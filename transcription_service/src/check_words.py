from config import AVOIDED_WORDS

# Helps with filetering out garbage
def validTranscription(text):
    words = text.split()
    if words not in AVOIDED_WORDS and len(words) > 2:
        print(f"Passed word: {words}")
        return True
    print(f"Avoided word: {words}")
    return False