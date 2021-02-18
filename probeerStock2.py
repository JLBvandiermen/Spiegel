try:
    def aandelen():
        from bs4 import BeautifulSoup
        import urllib.request
        import requests
        import re
        import time
        import random
        import sys
        import statistics
        import datetime
        global stonk
        global calc
        global avarage
        x = datetime.datetime.now()
        z = x.strftime("%H")
        avarage = list()
        if True:#9 <= int(z) < 21:
            stonk = list()
            def stonks(stockname, stockbuyprice):
                global stonk
                global calc
                stock = " ".join(y)
                stock = stock.replace(",","")
                stock = (((float(stock)-stockbuyprice)/stockbuyprice)*100)
                stock = str(round(stock, 2))
                calc = stock
                avarage.append(calc)
                stock = (stockname) + ": " + (stock) + "%"
                stonk.append(stock)
                return stonk
                #print(stock)
            with open("C:/Users/jonat/Dropbox/PI/stock.txt", mode='r') as vcf:
                try:
                    NASDAQ = vcf.readline()
                    NASDAQ = float(NASDAQ.replace("NASDAQ=",""))
                except:
                    pass
                try:
                    GOOGLE = vcf.readline()
                    GOOGLE = float(GOOGLE.replace("GOOGLE=",""))
                except:
                    pass
                try:
                    AMAZON = vcf.readline()
                    AMAZON = float(AMAZON.replace("AMAZON=",""))
                except:
                    pass
                try:
                    APPLE = vcf.readline()
                    APPLE = float(APPLE.replace("APPLE=",""))
                except:
                    pass
                try:
                    FACEBOOK = vcf.readline()
                    FACEBOOK = float(FACEBOOK.replace("FACEBOOK=",""))
                except:
                    pass
                try:
                    INTEL = vcf.readline()
                    INTEL = float(INTEL.replace("INTEL=",""))
                except:
                    pass
                try:
                    MICROSOFT = vcf.readline()
                    MICROSOFT = float(MICROSOFT.replace("MICROSOFT=",""))
                except:
                    pass
                try:
                    NETFLIX = vcf.readline()
                    NETFLIX = float(NETFLIX.replace("NETFLIX=",""))
                except:
                    pass
                try:
                    NIKE = vcf.readline()
                    NIKE = float(NIKE.replace("NIKE=",""))
                except:
                    pass
                try:
                    NVIDIA = vcf.readline()
                    NVIDIA = float(NVIDIA.replace("NVIDIA=",""))
                except:
                    pass
                try:
                    QUALCOMM = vcf.readline()
                    QUALCOMM = float(QUALCOMM.replace("QUALCOMM=",""))
                except:
                    pass
                try:
                    TESLA = vcf.readline()
                    TESLA = float(TESLA.replace("TESLA=",""))
                except:
                    pass
                try:
                    ASML = vcf.readline()
                    ASML = float(ASML.replace("ASML=",""))
                except:
                    pass
                try:
                    BOEING = vcf.readline()
                    BOEING = float(BOEING.replace("BOEING=",""))
                except:
                    pass
                try:
                    ARCELORMITTAL = vcf.readline()
                    ARCELORMITTAL = float(ARCELORMITTAL.replace("ARCELORMITTAL=",""))
                except:
                    pass
                try:
                    AKZONOBEL = vcf.readline()
                    AKZONOBEL = float(AKZONOBEL.replace("AKZONOBEL=",""))
                except:
                    pass
                try:
                    AHOLD = vcf.readline()
                    AHOLD = float(AHOLD.replace("AHOLD=",""))
                except:
                    pass
                try:
                    ABNAMRO = vcf.readline()
                    ABNAMRO = float(ABNAMRO.replace("ABNAMRO=",""))
                except:
                    pass
                try:
                    HEINEKEN = vcf.readline()
                    HEINEKEN = float(HEINEKEN.replace("HEINEKEN=",""))
                except:
                    pass
                try:
                    ING = vcf.readline()
                    ING = float(ING.replace("ING=",""))
                except:
                    pass
                try:
                    KPN = vcf.readline()
                    KPN = float(KPN.replace("KPN=",""))
                except:
                    pass
                try:
                    PHILIPS = vcf.readline()
                    PHILIPS = float(PHILIPS.replace("PHILIPS=",""))
                except:
                    pass
                try:
                    UNILEVER = vcf.readline()
                    UNILEVER = float(UNILEVER.replace("UNILEVER=",""))
                except:
                    pass
                try:
                    SHELL = vcf.readline()
                    SHELL = float(SHELL.replace("SHELL=",""))
                except:
                    pass
                try:
                    KLM = vcf.readline()
                    KLM = float(KLM.replace("KLM=",""))
                except:
                    pass
                try:
                    VIRGINGALACTIC = vcf.readline()
                    VIRGINGALACTIC = float(VIRGINGALACTIC.replace("VIRGINGALACTIC=",""))
                except:
                    pass
                try:
                    DELTAAIRLINES = vcf.readline()
                    DELTAAIRLINES = float(DELTAAIRLINES.replace("DELTAAIRLINES=",""))
                except:
                    pass
                try:
                    ALIBABA = vcf.readline()
                    ALIBABA = float(ALIBABA.replace("ALIBABA=",""))
                except:
                    pass
                try:
                    MCDONALDS = vcf.readline()
                    MCDONALDS = float(MCDONALDS.replace("MCDONALDS=",""))
                except:
                    pass
                try:
                    COCACOLA = vcf.readline()
                    COCACOLA = float(COCA-COLA.replace("COCACOLA=",""))
                except:
                    pass
                try:
                    VOLVO = vcf.readline()
                    VOLVO = float(VOLVO.replace("VOLVO=",""))
                except:
                    pass
                try:
                    NN = vcf.readline()
                    NN = float(NN.replace("NN=",""))
                except:
                    pass
                try:
                    AMD = vcf.readline()
                    AMD = float(AMD.replace("AMD=",""))
                except:
                    pass
                try:
                    GOLD = vcf.readline()
                    GOLD = float(GOLD.replace("GOLD=",""))
                except:
                    pass
                try:
                    BEYONDMEAT = vcf.readline()
                    BEYONDMEAT = float(BEYONDMEAT.replace("BEYONDMEAT=",""))
                except:
                    pass
                

            #STOCK STOCK STOCK STOCK STOCK STOCK STOCK
            if isinstance(KLM, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/AF.PA?p=AF.PA&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Klm", KLM)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(SHELL, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/RDSA.AS?p=RDSA.AS&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Shell", SHELL)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(UNILEVER, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/UNA.AS?p=UNA.AS&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Unilever", UNILEVER)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(PHILIPS, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/PHIA.AS?p=PHIA.AS&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Philips", PHILIPS)
                    except:
                        pass
                else:
                    pass
            else: pass
            if isinstance(HEINEKEN, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/HEIA.AS?p=HEIA.AS&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Heineken", HEINEKEN)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(KPN, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/KPN.AS?p=KPN.AS&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("KPN", KPN)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(ING, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/INGA.AS?p=INGA.AS&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("ING", ING)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(ABNAMRO, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/ABN.AS?p=ABN.AS&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("ABN-AMRO", ABNAMRO)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(AHOLD, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/AD.AS?p=AD.AS&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Ahold", AHOLD)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(AKZONOBEL, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/AKZA.AS?p=AKZA.AS&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Akzonobel", AKZONOBEL)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(ARCELORMITTAL, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/MT.AS?p=MT.AS&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Arcelormittal", ARCELORMITTAL)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(BOEING, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/BA?p=BA&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Boeing", BOEING)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(ASML, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/ASML.AS?p=ASML.AS&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("ASML", ASML)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(TESLA, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Tesla", TESLA)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(QUALCOMM, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/QCOM?p=QCOM&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Qualcomm", QUALCOMM)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(NVIDIA, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/NVDA?p=NVDA&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Nvidia", NVIDIA)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(ASML, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/NKE?p=NKE&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Nike", NIKE)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(NETFLIX, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/NFLX?p=NFLX&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Netflix", NETFLIX)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(MICROSOFT, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Microsoft", MICROSOFT)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(INTEL, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/INTC?p=INTC&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Intel", INTEL)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(FACEBOOK, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/FB?p=FB&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Facebook", FACEBOOK)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(APPLE, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Apple", APPLE)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(AMAZON, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Amazon", AMAZON)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(GOOGLE, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Google", GOOGLE)
                    except:
                        print('nay')
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(NASDAQ, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/%5EIXIC?p=^IXIC&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Nasdaq", NASDAQ)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(VIRGINGALACTIC, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/SPCE?p=SPCE&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Virgin Galatic", VIRGINGALACTIC)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(DELTAAIRLINES, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/DAL?p=DAL&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Delta Air Lines", DELTAAIRLINES)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            if isinstance(ALIBABA, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/BABA?p=BABA&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Alibaba", ALIBABA)
                    except:
                        pass
                else:
                    pass
            if isinstance(MCDONALDS, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/MCD?p=MCD&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("MCdonald's", MCDONALDS)
                    except:
                        pass
                else:
                    pass
            if isinstance(COCACOLA, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/KO?p=KO&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("CocaCola", COCACOLA)
                    except:
                        pass
                else:
                    pass
            if isinstance(VOLVO, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/VOLV-B.ST?p=VOLV-B.ST&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Volvo", VOLVO)
                    except:
                        pass
                else:
                    pass
            if isinstance(NN, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/NN.AS?p=NN.AS&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("NN", NN)
                    except:
                        pass
                else:
                    pass
            if isinstance(AMD, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/AMD?p=AMD&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("AMD", AMD)
                    except:
                        pass
                else:
                    pass
            if isinstance(GOLD, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/GC=F?p=GC=F&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("Goud", GOLD)
                    except:
                        pass
                else:
                    pass
            if isinstance(BEYONDMEAT, float):
                if True:#14 <= int(z) <= 21:
                    html = requests.get("https://finance.yahoo.com/quote/BYND?p=BYND&.tsrc=fin-srch").content
                    #1 Recoding
                    unicode_str = html.decode("ISO-8859-1")
                    encoded_str = unicode_str.encode("ascii",'ignore')
                    news_soup = BeautifulSoup(encoded_str, "html.parser")
                    a_text = news_soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                    #2 Removing
                    y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                    try:
                        stonks("BeyondMeat", BEYONDMEAT)
                    except:
                        pass
                else:
                    pass
            else:
                pass
            stonk = "\n".join(stonk)
            #print(stonk)
        else:
            pass
        float_list= list()
        for item in avarage:
            float_list.append(float(item))
        avarage = round(statistics.mean(float_list), 3)
        avarage = "Average: " + (str(avarage)) + "%"
        return stonk
        return avarage
    aandelen()
except:
    pass
#print(stonk)
#print(avarage)
