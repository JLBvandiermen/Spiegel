from bs4 import BeautifulSoup
import urllib.request
import requests
import re
import time

def nieuws():
    html = requests.get("https://nu.nl").content
    source = urllib.request.urlopen('https://nu.nl').read()
    soup = BeautifulSoup(source,'lxml')
    #1 Recoding
    unicode_str = html.decode("utf8")
    encoded_str = unicode_str.encode("ascii",'ignore')
    news_soup = BeautifulSoup(encoded_str, "html.parser")
    a_text = news_soup.find_all('span')
    #2 Removing
    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
    bad_chars = [",", ".", "'", "\"", "(", ")", ":", "$", "&", "-", "“", "’",
                             "—", "”", "?", ";", "1","2","3","4","5","6","7","8", "9", "0",
                             "#", "[", "]", "‘", "–", "<title>","</title>","|"]

    sent = " ".join(y)
    sentence = sent[230:]
    news = 0
    sentenceSplit = filter(None, sentence.split("  "))
    for s in sentenceSplit :
        print(s.strip() + ".")
        time.sleep(5)
        news += 1
        if news == 11:
            time.sleep(1800)
            nieuws()
        
nieuws()
