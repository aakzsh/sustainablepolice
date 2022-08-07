from better_profanity import profanity

def is_abusive(text):
    return profanity.contains_profanity(text)

