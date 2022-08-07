from langdetect import detect


def checklang(tweet):
    if detect(tweet) == 'en':
        return True
    return False

