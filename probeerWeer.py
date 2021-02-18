try:
    def Weer():
        from bs4 import BeautifulSoup
        import urllib.request
        import requests
        import re
        import time
        import random
        import sys
        global bewolking
        global regen
        global maxtemp
        global temp
        #HUIDIGE TEMP DE BILT
        html = requests.get("https://teletekst-data.nos.nl/webplus?p=705-2").content
        #1 Recoding
        unicode_str = html.decode("ISO-8859-1")
        encoded_str = unicode_str.encode("ascii",'ignore')
        news_soup = BeautifulSoup(encoded_str, "html.parser")
        a_text = news_soup.find_all("span", class_="green")
        #2 Removing
        y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
        temp = " ".join(y)
        temp=(temp[44:temp.index("De Bilt") + len("De Bilt")-18:])
        temp = temp.replace("                 ","")
        temp = temp.replace("  ","")
        temp = temp.replace("`","")

        #MAX TEMP DE BILT
        html = requests.get("https://teletekst-data.nos.nl/webplus?p=705-3").content
        #1 Recoding
        unicode_str = html.decode("ISO-8859-1")
        encoded_str = unicode_str.encode("ascii",'ignore')
        news_soup = BeautifulSoup(encoded_str, "html.parser")
        a_text = news_soup.find_all("span", class_="cyan")
        #2 Removing
        y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
        maxtemp = " ".join(y)
        maxtemp = maxtemp[140:-110]
        maxtemp = maxtemp.replace("                 ","")
        maxtemp = maxtemp.replace("  ","")
        maxtemp = maxtemp.replace("`","")

        #REGEN DE BILT
        html = requests.get("https://teletekst-data.nos.nl/webplus?p=705-3").content
        #1 Recoding
        unicode_str = html.decode("ISO-8859-1")
        encoded_str = unicode_str.encode("ascii",'ignore')
        news_soup = BeautifulSoup(encoded_str, "html.parser")
        a_text = news_soup.find_all("span", class_="cyan")
        #2 Removing
        y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
        regen = " ".join(y)
        regen = regen[146:-100]
        regen = regen.replace("  ","")
        regen = regen.replace("                 ","")
        regen = regen.replace("`","")

        #BEWOLKT DE BILT
        #mogelijke woorden: nevel, geheel bewolkt, droog, onbewolkt, regen, buien,
        #onweer, hagel, zwaar bewolkt, heiig, licht bewolkt, regenbui,
        html = requests.get("https://teletekst-data.nos.nl/webplus?p=705-2").content
        #1 Recoding
        unicode_str = html.decode("ISO-8859-1")
        encoded_str = unicode_str.encode("ascii",'ignore')
        news_soup = BeautifulSoup(encoded_str, "html.parser")
        a_text = news_soup.find_all("span", class_="cyan")
        #2 Removing
        y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
        bewolking = " ".join(y)
        bewolking = bewolking[109:-150]
        bewolking = bewolking.replace("  ","")
        bewolking = bewolking.replace("                 ","")
        wolken = ["nevel", "bewolkt", "heiig"]
        regenen = ["regen", "buien", "onweer", "regenbui", "motregen"]
        sneeuw = ["sneeuw", "motsneeuw", "ijzel"]
        if any(x in bewolking for x in wolken):
            bewolking = "wolken"
        elif any(x in bewolking for x in regenen):
            bewolking = "regen"
        elif any(x in bewolking for x in sneeuw):
            bewolking = "sneeuw"
        return bewolking
        return regen
        return maxtemp
        return temp
    Weer()
except:
    pass
