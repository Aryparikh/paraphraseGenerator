"""
@Author : Aryamaan Parikh

Takes a paraphrase.
Passes it into mtranslate
Translates into every language available from english/source language
Stores translated sentences in list
Calls google API again
Translates back into english/source language
You've got a much larger set of paraphrases !

Note :
What about indian languages ? Use them if you want to scale your data even higher.


USAGE :

sent = ["What a wonderful day to go for a ride in the park"]
sentMany = ["What a wonderful day to go for a ride in the park","It is not everyday that you encounter such weather."]

opSent = paragen(sent)
opSentMany = paragen(sentMany)

"""
import mtranslate
from googletrans import Translator
import re

languages = ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs',
             'bg', 'ca', 'ceb', 'zh-CN', 'zh-TW', 'co', 'hr', 'cs', 'da',
             'nl', 'en', 'eo', 'et', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 
             'el', 'gu', 'ht', 'ha', 'haw', 'he', 'hi', 'hmn', 'hu', 'is', 
             'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 
             'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 
             'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'ny', 'ps', 
             'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 
             'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 
             'tl', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'uz', 'vi', 
             'cy', 'xh', 'yi', 'yo', 'zu']

#105 Languages ! Remember to make a [(resultantList)] after paraphrasing, to avoid redundancy !


def paragen(engList):
    keyPhs = engList
    translatedPhrases =[]
    paraphrases = []
    for t in keyPhs:
        for value in languages:
            buf = mtranslate.translate(t,value,"en") # Why faulty ? - Depends on t + Py Version !
            print buf
            translatedPhrases.append(buf)

    # # ALTERNATIVE
    # translating=Translator()
    # for t in keyPhs:
    #     for value in languages:
    #         buf = translating.translate(t,value,"en").text
    #         translatedPhrases.append(buf)



    
    #translatedPhrases contains strings of phrases of different languages.
    for x in translatedPhrases:
        translator = Translator()
        v = translator.translate(x,"en").text
        print(v)
        paraphrases.append(v)

    oP = []
    for t in paraphrases:
        if t != '':
            t = t.lower()
            t = u''.join(t).encode('utf-8')
            t = re.sub('[^a-zA-Z0-9.]',' ', t)
            t = re.sub('[\s]+', ' ', t)
            oP.append(t)
    #        if this doesnt work
    #       oP.append(str(t))


    oP = oP[1:]
    print(oP)
    return oP

