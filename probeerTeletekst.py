try:
    def Nieuws():
        from bs4 import BeautifulSoup
        import urllib.request
        import requests
        import re
        import time
        import sys
        global slash
        global ding
        global ding1
        global ding2
        global ding3
        global ding4
        global ding5
        global ding6
        global ding7
        global ding8
        global ding9
        global ding10
        global ding11
        global ding12
        global ding13
        global ding14
        global ding15
        global ding16
        global ding17
        global ding18
        global ding19
        global ding20
        global ding21
        html = requests.get("https://teletekst-data.nos.nl/webplus?p=102-1").content
        #1 Recoding
        encoded_str = html.decode("ISO-8859-1")
        news_soup = BeautifulSoup(encoded_str, "html.parser")
        a_text = news_soup.find_all("span", class_="yellow")
        #2 REMOVING ALL UGLY TEXT
        y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
        sentence = " ".join(y)
        sentence = sentence[8:]
        sentence = sentence.replace("N.", "")
        sentence = sentence.replace("102", "")
        sentence = sentence.replace("103", "")
        sentence = sentence.replace("104", "")
        sentence = sentence.replace("105", "")
        sentence = sentence.replace("106", "")
        sentence = sentence.replace("109", "")
        sentence = sentence.replace("ticker 199", "")
        sentence = sentence.replace("107", "")
        sentence = sentence.replace("108", "")
        sentence = sentence.replace("sport", "")
        sentence = sentence.replace("110", "")
        sentence = sentence.replace("111", "")
        sentence = sentence.replace("112.", "")
        sentence = sentence.replace("113", "")
        sentence = sentence.replace("114", "")
        sentence = sentence.replace("115", "")
        sentence = sentence.replace("116", "")
        sentence = sentence.replace("117", "")
        sentence = sentence.replace("118", "")
        sentence = sentence.replace("119", "")
        sentence = sentence.replace("120", "")
        sentence = sentence.replace("121", "")
        sentence = sentence.replace("122", "")
        news = 0
        ding="/"
        ding1 = "/"
        ding2 = "/"
        ding3 = "/"
        ding4 = "/"
        ding5 = "/"
        ding6 = "/"
        ding7 = "/"
        ding8 = "/"
        ding9 = "/"
        ding10 = "/"
        ding11 = "/"
        ding12 = "/"
        ding13 = "/"
        ding14 = "/"
        ding15 = "/"
        ding16 = "/"
        ding17 = "/"
        ding18 = "/"
        ding19 = "/"
        ding20 = "/"
        ding21 = "/"
        slash = "/"
        sentenceSplit = filter(None, sentence.split("  "))
        for s in sentenceSplit :
            #SPLITTING THE HEADLINES INTO INDIVIDUAL LINES
            ding = (s.strip() + ".")
            ding = ding[:35]
            news += 1
            if news == 1:
                ding1 = ding
            elif news == 2:
                ding2 = ding
            elif news == 3:
                ding3 = ding
            elif news == 4:
                ding4 = ding
            elif news == 5:
                ding5 = ding
            elif news == 6:
                ding6 = ding
            elif news == 7:
                ding7 = ding
            elif news == 8:
                ding8 = ding
            elif news == 9:
                ding9 = ding
            elif news == 10:
                ding10 = ding
            elif news == 11:
                ding11 = ding
            elif news == 12:
                ding12 = ding
            elif news == 13:
                ding13 = ding
            elif news == 14:
                ding14 = ding
            elif news == 15:
                ding15 = ding
            elif news == 16:
                ding16 = ding
            elif news == 17:
                ding17 = ding
            elif news == 18:
                ding18 = ding
            elif news == 19:
                ding19 = ding
            elif news == 20:
                ding20 = ding
            elif news == 21:
                ding21 = ding
            elif news == 22:
                break
        return slash
        return ding
        return ding1
        return ding2
        return ding3
        return ding4
        return ding5
        return ding6
        return ding7
        return ding8
        return ding9
        return ding10
        return ding11
        return ding12
        return ding13
        return ding14
        return ding15
        return ding16
        return ding17
        return ding18
        return ding19
        return ding20
        return ding21
    Nieuws()
except:
    pass
