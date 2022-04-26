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
#### SOLUTION
import time
import requests
import html
import random
from lxml import html as parser

from adjectives import adjectives
from adverbs import adverbs
from articles import articles
from conjunctions import conjunctions
from interjections import interjections
from modal_verb import modal_verbs
from nouns import nouns
from prepositions import prepositions
from pronouns import pronouns
from verbs import verbs

list_of_dicts = ["adjectives", "adverbs", "articles", "conjunctions", "interjections", "modal_verbs", "nouns", "prepositions", "pronouns", "verbs"]
list_of_words = [adjectives, adverbs, articles, conjunctions, interjections, modal_verbs, nouns, prepositions, pronouns, verbs]
lists_2_trans=[]
for i in range(0,len(list_of_words)):
    lists_2_trans.append(list(list_of_words[i].keys()))

user_agents=[#'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
'Mozilla/5.0 (X11; Linux i686; rv:99.0) Gecko/20100101 Firefox/99.0',
'Mozilla/5.0 (Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0',
'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:99.0) Gecko/20100101 Firefox/99.0',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0',
'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0',]


for iii in range(0,len(lists_2_trans)):
    list_to_translate=lists_2_trans[iii]
    print(list_to_translate)
    for i in range(0,len(list_to_translate)):
        columns=list_to_translate[i].split()
        search_me=""
        for j in range(0,len(columns)):
            if j == len(columns)-1:
                search_me+=columns[j]
            else:
                search_me+=columns[j]+'+'
        print(search_me,type(search_me))
        headers={'User-Agent':random.choice(user_agents)}
        URL="https://www.google.com/search?q=%22"+search_me+"%22+translate+to+persian&client=ubuntu&channel=fs&ei=9PliYrXYCYepgAbHiqroAw&ved=0ahUKEwi1oveTrKj3AhWHFMAKHUeFCj0Q4dUDCA4&uact=5&oq=%22i+am+here%22+translate+to+persian&gs_lcp=Cgdnd3Mtd2l6EAM6BwgAEEcQsAM6BQgAEKIEOgUIABCRAjoKCAAQsQMQgwEQQzoLCAAQgAQQsQMQgwE6DgguEIAEELEDEMcBEKMCOg4ILhCABBCxAxDHARDRAzoLCC4QgAQQsQMQgwE6CAgAEIAEELEDOgoILhCxAxDUAhBDOgQILhBDOgcILhCxAxBDOgsILhCABBDHARCvAToOCC4QgAQQsQMQxwEQrwE6CAguEIAEENQCOgUIABCABDoKCAAQkQIQRhD_AToECAAQAzoFCC4QgAQ6CggAEIAEEEYQ_wE6BggAEBYQHjoICCEQFhAdEB46BwghEAoQoAFKBAhBGABKBAhGGABQ9QtYtYMBYM-FAWgHcAF4AYABnAWIAdU3kgEMNC4yOC4zLjEuMC4ymAEAoAEByAEIwAEB&sclient=gws-wiz"
        image_URL="https://www.google.com/search?q="+search_me+"&client=ubuntu&hs=Nxt&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj4mriK3Kn3AhVNeMAKHccDDIYQ_AUoAXoECAEQAw&biw=1920&bih=944&dpr=1#imgrc=u3Q2KHasDPX2BM"
        page = requests.get(URL,headers=headers)
        print("URL",URL)
        ####image_page = requests.get(image_URL,headers=headers)
        tree = parser.fromstring(page.content)
        ####image_tree = parser.fromstring(image_page.content)
        translation = tree.xpath('//pre[@id="tw-target-text"]/span[@class="Y2IQFc"]/text()')
        print(translation)
        if i == 2:
            break
        #image_dl_link=image_tree.xpath('//div[@class="mJxzWe"]')
        #image_dl_link=image_tree.xpath('//div[@class="isv-r PNCib MSM1fd BUooTd"]')
        #image_dl_link=image_tree.xpath('//img[@class="rg_i Q4LuWd"]')
        ####image_dl_link=image_tree.xpath('//a[@class="wXeWr islib nfEiy"]')
        ####image_dl_link=image_tree.xpath('//a[@href]')
        ####print(image_dl_link[0].values()[0])
        ####f=open("search","w")
        ####f.write(image_page.text)
        ####f.close()
        ####print(dir(image_dl_link[0]))
        ####print(image_dl_link[0])
        ####print(image_dl_link[0].keys())
        ####print(image_dl_link[0].values())
        #print(image_dl_link[0].resolve_base_ref)
        #print(image_dl_link[0].get("data-iid"))
        if i == 0:
            f=open(list_of_dicts[iii]+"_scraped.py","w")
            f.write(list_of_dicts[iii]+"={\n")
        else:
            f=open(list_of_dicts[iii]+"_scraped.py","a")

        write_me = '\"' + list_to_translate[i] + '\"' + ' : \"' +str(translation).strip("'[]") + '\",\n'
        f.write(write_me)


        if i == (len(list_to_translate)-1):
            f.write("}\n")
        f.close()
        #s=input("Ctrl+C to end")

        time.sleep(float(random.choice([3,4,5,6,7,8,9,10])))

###

'''
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'}
URL="https://www.google.com/search?q=%22to+run%22+translate+to+persian&client=ubuntu&channel=fs&ei=9PliYrXYCYepgAbHiqroAw&ved=0ahUKEwi1oveTrKj3AhWHFMAKHUeFCj0Q4dUDCA4&uact=5&oq=%22i+am+here%22+translate+to+persian&gs_lcp=Cgdnd3Mtd2l6EAM6BwgAEEcQsAM6BQgAEKIEOgUIABCRAjoKCAAQsQMQgwEQQzoLCAAQgAQQsQMQgwE6DgguEIAEELEDEMcBEKMCOg4ILhCABBCxAxDHARDRAzoLCC4QgAQQsQMQgwE6CAgAEIAEELEDOgoILhCxAxDUAhBDOgQILhBDOgcILhCxAxBDOgsILhCABBDHARCvAToOCC4QgAQQsQMQxwEQrwE6CAguEIAEENQCOgUIABCABDoKCAAQkQIQRhD_AToECAAQAzoFCC4QgAQ6CggAEIAEEEYQ_wE6BggAEBYQHjoICCEQFhAdEB46BwghEAoQoAFKBAhBGABKBAhGGABQ9QtYtYMBYM-FAWgHcAF4AYABnAWIAdU3kgEMNC4yOC4zLjEuMC4ymAEAoAEByAEIwAEB&sclient=gws-wiz"
page = requests.get(URL,headers=headers)
tree = parser.fromstring(page.content)
html_string = html.unescape(page.text)
print(html_string)
print(tree)
id="tw-target-text-container"
thinga = tree.xpath('//div[@id="tw-target-text-container"]')
print(thinga)
thinga = tree.xpath('//pre[@id="tw-target-text"]/span[@class="Y2IQFc"]/text()')
print(thinga)

'''
