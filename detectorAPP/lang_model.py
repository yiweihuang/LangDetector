import pycld2 as cld2

# Language detect
def LangDetect(sent):
    result = {}
    isReliable, textBytesFound, details = cld2.detect(sent, bestEffort=1)
    if details[0][0] != 'Unknown':
        if details[0][0] == 'ChineseT':
            result['lang'] = "Traditional Chinese"
        elif details[0][0] == 'Chinese':
            result['lang'] = "Simplified Chinese"
        else:
            result['lang'] = details[0][0].capitalize()
    else:
        result['lang'] = "Unknown language"
    return result
