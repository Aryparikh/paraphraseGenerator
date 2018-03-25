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

languages = ["ar", "sq", "be", "bg" "af", "ca", "zh-CN", "zh-TW", "hr",
             "cs", "da", "nl", "et", "en", "tl", "fi", "fr", "gl", "de",
             "el", "iw", "hi", "hu", "is", "id", "ga", "it", "ja", "ko",
             "lv", "lt", "mk", "ms", "mt", "no", "fa", "pl", "pt", "ro",
             "ru", "sr", "sk", "sl", "es", "sw", "sv", "th", "tr", "uk",
             "vi", "cy", "yi"]



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

