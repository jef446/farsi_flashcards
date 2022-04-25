'''
from googlesearch import search

query = "google translate"

for j in search(query, tld="co.in", num=10, stop=10,pause=2):
	print(j)
'''
'''
import requests

URL="https://translate.google.co.uk/"
page = requests.get(URL)

f=open("initial","w")
f.write(page.text)
f.close()


URL="https://translate.google.co.uk/?sl=en&tl=fa&text=hello&op=translate"
page = requests.get(URL)
f=open("search","w")
f.write(page.text)
f.close()
'''
'''
translator = Translator()
class UnsortedAttributes(HTMLFormatter):
    def attributes(self, tag):
        for k, v in tag.attrs.items():
            yield k, v
'''
'''
from googletrans import Translator

#while Translating==True:
translator = Translator()
text="mi casa"

translator.detect(text)
'''
from translations import verbs
farsimap={
"Auto Verbs":verbs,
"Adjectives":{
"something":"something",
},
"Adverbs":{
"something":"something",
},
"Articles":{
"something":"something",
},
"Conjunctions":{
"something":"something",
},
"Interjections":{
"something":"something",
},
"Nouns":{
"something":"something",
},
"Prepositions":{
"something":"something",
},
"Pronouns":{
"something":"something",
},
"Verbs":{
"to add":"اضافه کردن",
"to agree":"برای موافقت",
"to allow":"اجازه دادن",
"to appear":"ظاهر شدن",
"to ask":"پرسیدن",
"to be":"بودن",
"to become":"شدن",
# "to begin":"",
# "to believe":"",
# "to bring":"",
# "to build":"",
# "to buy":"",
# "to call":"",
# "to carry":"",
# "to change":"",
# "to come":"",
# "to consider":"",
# "to continue":"",
# "to create":"",
# "to decide":"",
# "to describe":"",
# "to develop":"",
# "to die":"",
# "to do":"",
# "to draw":"",
# "to except":"",
# "to fall":"",
# "to feel":"",
# "to find":"",
# "to follow":"",
# "to get":"",
# "to give":"",
# "to go":"",
# "to happen":"",
"to have":"داشتن",
},
"Modal Verbs":{
"something":"something",
},
}
'''
print('Import succesful')

print(farsimap.keys())
print(farsimap["Verbs"])
'''
