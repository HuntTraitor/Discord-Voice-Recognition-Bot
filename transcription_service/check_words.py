AVOIDED_WORDS = [
    "MBC 뉴스 이덕영입니다.",
    "지금까지 신선한 경제였습니다."
]

# Helps with filetering out garbage
def validTranscription(text):
    valid = False
    words = text.split()
    if words not in AVOIDED_WORDS and len(words) > 2:
        valid = True
    return valid