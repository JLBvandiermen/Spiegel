try:
    def Bus():
        from bs4 import BeautifulSoup
        import urllib.request
        import requests
        import re
        import time
        global tussenstuk1
        global tussenstuk2
        global tussenstuk3
        global tussenstuk4
        global tussenstuk5
        global tussenstuk6
        global tussenstuk7
        global tussenstuk8
        global tussenstuk9
        global tussenstuk10
        global bus1
        global bus2
        global bus3
        global bus4
        global bus5
        global bus6
        global bus7
        global bus8
        global bus9
        global bus10
        bus1=""
        bus2=""
        bus3=""
        bus4=""
        bus5=""
        bus6=""
        bus7=""
        bus8=""
        bus9=""
        bus10=""
        tussenstuk1=""
        tussenstuk2=""
        tussenstuk3=""
        tussenstuk4=""
        tussenstuk5=""
        tussenstuk6=""
        tussenstuk7=""
        tussenstuk8=""
        tussenstuk9=""
        tussenstuk10=""
        time1=0
        time2=0
        time3=0
        time4=0
        time5=0
        time6=0
        time7=0
        time8=0
        time9=0
        time10=0
        add1=""
        add2=""
        add3=""
        add4=""
        add5=""
        add6=""
        add7=""
        add8=""
        add9=""
        add10=""
        a1=""
        a2=""
        a3=""
        a4=""
        a5=""
        a6=""
        a7=""
        a8=""
        a9=""
        a10=""
        b1=""
        b2=""
        b3=""
        b4=""
        b5=""
        b6=""
        b7=""
        b8=""
        b9=""
        b10=""
        c1=""
        c2=""
        c3=""
        c4=""
        c5=""
        c6=""
        c7=""
        c8=""
        c9=""
        c10=""
        d1=""
        d2=""
        d3=""
        d4=""
        d5=""
        d6=""
        d7=""
        d8=""
        d9=""
        d10=""
        bij1 = ""
        bij2 = ""
        bij3 = ""
        bij4 = ""
        bij5 = ""
        bij6 = ""
        bij7 = ""
        bij8 = ""
        bij9 = ""
        bij10 = ""

        html = requests.get("https://9292.nl/utrecht/bushalte-europaplein-oost").content
        #1 Recoding
        unicode_str = html.decode("utf8")
        encoded_str = unicode_str.encode("ascii",'ignore')
        news_soup = BeautifulSoup(encoded_str, "html.parser")
        a_text = news_soup.find_all('td')
        #2 Removing
        y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
        zin = "".join(y)
        tel = 0
        zin = zin.replace("""





        """, "")
        zin = zin.replace("""

        """, "")
        zin = zin.replace("U-link 34", "")
        zin = zin.replace("apendorp", "")
        zin = zin.replace("Station", "")
        zin = zin.replace("Bus 10", "")
        zin = zin.replace("Bus", "")
        zin = zin.replace("U-OV", "")
        zin = zin.replace("P+R", "P")
        zin = zin.replace("Park", "P")
        zin = zin.replace("Zeist", "")
        zin = zin.replace("Lunetten", "Lunetten P")
        zin = zin.replace("via", "")
        zin = zin.replace("Amersfoort", "")
        zin = zin.replace("U-link", "")
        zinSplit = filter(None, zin.split("P"))
        for q in zinSplit :
            trein = (q.strip() + "")
            tel += 1
            if tel == 1:
                bus1 = trein
            elif tel == 2:
                bus2 = trein
            elif tel == 3:
                bus3 = trein
            elif tel == 4:
                bus4 = trein
            elif tel == 5:
                bus5 = trein#[:24]
            elif tel == 6:
                bus6 = trein
            elif tel == 7:
                bus7 = trein
            elif tel == 8:
                bus8 = trein
            elif tel == 9:
                bus9 = trein
            elif tel == 10:
                bus10 = trein
            elif tel == 11:
                break
        #FINDS THE DEPARTING HOUR(b) AND MINUTE(a)
        a1 = ''.join(x for x in bus1 if x.isdigit())
        b1 = a1[:2]
        a1 = a1[2:4]
        a2 = ''.join(x for x in bus2 if x.isdigit())
        b2 = a2[:2]
        a2 = a2[2:4]
        a3 = ''.join(x for x in bus3 if x.isdigit())
        b3 = a3[:2]
        a3 = a3[2:4]
        a4 = ''.join(x for x in bus4 if x.isdigit())
        b4 = a4[:2]
        a4 = a4[2:4]
        a5 = ''.join(x for x in bus5 if x.isdigit())
        b5 = a5[:2]
        a5 = a5[2:4]
        a6 = ''.join(x for x in bus6 if x.isdigit())
        b6 = a6[:2]
        a6 = a6[2:4]
        a7 = ''.join(x for x in bus7 if x.isdigit())
        b7 = a7[:2]
        a7 = a7[2:4]
        a8 = ''.join(x for x in bus8 if x.isdigit())
        b8 = a8[:2]
        a8 = a8[2:4]
        a9 = ''.join(x for x in bus9 if x.isdigit())
        b9 = a9[:2]
        a9 = a9[2:4]
        a10 = ''.join(x for x in bus10 if x.isdigit())
        b10 = a10[:2]
        a10 = a10[2:4]

        #FINDS THE DELAY
        c1 = ''.join(x for x in bus1 if x.isdigit())
        d1 = c1[2:4]
        c1 = c1[4:8]
        c2 = ''.join(x for x in bus2 if x.isdigit())
        d2 = c2[2:4]
        c2 = c2[4:8]
        c3 = ''.join(x for x in bus3 if x.isdigit())
        d3 = c3[2:4]
        c3 = c3[4:8]
        c4 = ''.join(x for x in bus4 if x.isdigit())
        d4 = c4[2:4]
        c4 = c4[4:8]
        c5 = ''.join(x for x in bus5 if x.isdigit())
        d5 = c5[2:4]
        c5 = c5[4:8]
        c6 = ''.join(x for x in bus6 if x.isdigit())
        d6 = c6[2:4]
        c6 = c6[4:8]
        c7 = ''.join(x for x in bus7 if x.isdigit())
        d7 = c7[2:4]
        c7 = c7[4:8]
        c8 = ''.join(x for x in bus8 if x.isdigit())
        d8 = c8[2:4]
        c8 = c8[4:8]
        c9 = ''.join(x for x in bus9 if x.isdigit())
        d9 = c9[2:4]
        c9 = c9[4:8]
        c10 = ''.join(x for x in bus10 if x.isdigit())
        d10 = c10[2:4]
        c10 = c10[4:8]

        #FINDS IF IT IS AN DELAY(-) OR A INCREASE (+)
        minus1 = bus1[7:8]
        minus2 = bus2[7:8]
        minus3 = bus3[7:8]
        minus4 = bus4[7:8]
        minus5 = bus5[7:8]
        minus6 = bus6[7:8]
        minus7 = bus7[7:8]
        minus8 = bus8[7:8]
        minus9 = bus9[7:8]
        minus10 = bus10[7:8]

        #TURNS THE EMPTY VARIABLE INTO A CALCULATABLE INT
        if c1 == "":
            c1 = 0
        if c2 == "":
            c2 = 0
        if c3 == "":
            c3 = 0
        if c4 == "":
            c4 = 0
        if c5 == "":
            c5 = 0
        if c6 == "":
            c6 = 0
        if c7 == "":
            c7 = 0
        if c8 == "":
            c8 = 0
        if c9 == "":
            c9 = 0
        if c10 == "":
            c10 = 0

        #CALCULATES THE ARRIVAL TIME(time) BY ADDING 14 MINUTES TO THE ARRIVAL MIN(a) AND SUBSTRACTING DELAY(c) IF DELAY OR NOT(minus)
        #IF THE ARRIVAL TIME(time) EXCEEDS 60 MIN THE HOUR(b) WILL INCREASE
        if a1 != "":
            if minus1 == "-":
                time1 = int(a1) + 14 - int(c1)
            elif minus1 == "+":
                time1 = int(a1) + 14 + int(c1)
            else:
                time1 = int(a1) + 14
            if time1 > 60:
                time1 = time1 - 60
                b1 = int(b1) + 1
        if a2 != "":
            if minus2 == "-":
                time2 = int(a2) + 14 - int(c2)
            elif minus2 == "+":
                time2 = int(a2) + 14 + int(c2)
            else:
                time2 = int(a2) + 14
            if time2 > 60:
                time2 = time2 - 60
                b2 = int(b2) + 1
        if a3 != "":
            if minus3 == "-":
                time3 = int(a3) + 14 - int(c3)
            elif minus4 == "+":
                time3 = int(a3) + 14 + int(c3)
            else:
                time3 = int(a3) + 14
            if time3 > 60:
                time3 = time3 - 60
                b3 = int(b3) + 1
        if a4 != "":
            if minus4 == "-":
                time4 = int(a4) + 14 - int(c4)
            elif minus4 == "+":
                time4 = int(a4) + 14 + int(c4)
            else:
                time4 = int(a4) + 14
            if time4 > 60:
                time4 = time4 - 60 
                b4 = int(b4) + 1
        if a5 != "":
            if minus5 == "-":
                time5 = int(a5) + 14 - int(c5)
            elif minus5 == "+":
                time5 = int(a5) + 14 + int(c5)
            else:
                time5 = int(a5) + 14
            if time5 > 60:
                time5 = time5 - 60
                b5 = int(b5) + 1
        if a6 != "":
            if minus6 == "-":
                time6 = int(a6) + 14 - int(c6)
            elif minus6 == "+":
                time6 = int(a6) + 14 + int(c6)
            else:
                time6 = int(a6) + 14
            if time6 > 60:
                time6 = time6 - 60
                b6 = int(b6) + 1
        if a7 != "":
            if minus7 == "-":
                time7 = int(a7) + 14 - int(c7)
            elif minus7 == "+":
                time7 = int(a7) + 14 + int(c7)
            else:
                time7 = int(a7) + 14
            if time7 > 60:
                time7 = time7 - 60
                b7 = int(b7) + 1
        if a8 != "":
            if minus8 == "-":
                time8 = int(a8) + 14 - int(c8)
            elif minus8 == "+":
                time8 = int(a8) + 14 + int(c8)
            else:
                time8 = int(a8) + 14
            if time8 > 60:
                time8 = time8 - 60
                b8 = int(b8) + 1
        if a9 != "":
            if minus9 == "-":
                time9 = int(a9) + 14 - int(c9)
            elif minus9 == "+":
                time9 = int(a9) + 14 + int(c9)
            else:
                time9 = int(a9) + 14
            if time9 > 60:
                time9 = time9 - 60
                b9 = int(b9) + 1
        if a10 != "":
            if minus10 == "-":
                time10 = int(a10) + 14 - int(c10)
            elif minus10 == "+":
                time10 = int(a10) + 14 + int(c10)
            else:
                time10 = int(a10) + 14
            if time10 > 60:
                time10 = time10 - 60
                b10 = int(b10) + 1
                        
        #MAKES THE HOUR TIME IN XX:XX FORMAT INSTEAD OF X:XX
        if time1 != "":
            if time1 < 10:
                add1 = "0"
        if time1 != "":
            if time1 > 10:
                add1 = ""
        if time2 != "":
            if time2 < 10:
                add2 = "0"
        if time2 != "":
            if time2 > 10:
                add2 = ""
        if time3 != "":
            if time3 < 10:
                add3 = "0"
        if time3 != "":
            if time3 > 10:
                add3 = ""
        if time4 != "":
            if time4 < 10:
                add4 = "0"
        if time4 != "":
            if time4 > 10:
                add4 = ""
        if time5 != "":
            if time5 < 10:
                add5 = "0"
        if time5 != "":
            if time5 > 10:
                add5 = ""
        if time6 != "":
            if time6 < 10:
                add6 = "0"
        if time6 != "":
            if time6 > 10:
                add6 = ""
        if time7 != "":
            if time7 < 10:
                add7 = "0"
        if time7 != "":
            if time7 > 10:
                add7 = ""
        if time8 != "":
            if time8 < 10:
                add8 = "0"
        if time8 != "":
            if time8 > 10:
                add8 = ""
        if time9 != "":
            if time9 < 10:
                add9 = "0"
        if time9 != "":
            if time9 > 10:
                add9 = ""
        if time10 != "":
            if time10 < 10:
                add10 = "0"
        if time10 != "":
            if time10 > 10:
                add10 = ""
                        
        #IF THE HOUR APPROACHES MIDNIGHT THE 24 IS TURNED INTO 00
        if b1 != "":
            if b1 == 24:
                b1 = "00"
        if b2 != "":
            if b2 == 24:
                b2 = "00"
        if b3 != "":
            if b3 == 24:
                b3 = "00"
        if b4 != "":
            if b4 == 24:
                b4 = "00"
        if b5 != "":
            if b5 == 24:
                b5 = "00"
        if b6 != "":
            if b6 == 24:
                b6 = "00"
        if b7 != "":
            if b7 == 24:
                b7 = "00"
        if b8 != "":
            if b8 == 24:
                b8 = "00"
        if b9 != "":
            if b9 == 24:
                b9 = "00"
        if b10 != "":
            if b10 == 24:
                b10 = "00"

        #MAKES THE MINUTE TIME IN XX:XX FORMAT INSTEAD OF XX:X
        if b1 != "": 
            if int(b1) < 10:
                bij1 = "0"
        if b1 != "":
            if "0" in str(b1):
                bij1 = ""
        if b2 != "":
            if int(b2) < 10:
                bij2 = "0"
        if b2 != "":
            if "0" in str(b2):
                bij2 = ""
        if b3 != "":
            if int(b3) < 10:
                bij3 = "0"
        if b3 != "":
            if "0" in str(b3):
                bij3 = ""
        if b4 != "":
            if int(b4) < 10:
                bij4 = "0"
        if b4 != "":
            if "0" in str(b4):
                bij4 = ""
        if b5 != "":
            if int(b5) < 10:
                bij5 = "0"
        if b5 != "":
            if "0" in str(b5):
                bij5 = ""
        if b6 != "":
            if int(b6) < 10:
                bij6 = "0"
        if b6 != "":
            if "0" in str(b6):
                bij6 = ""
        if b7 != "":
            if int(b7) < 10:
                bij7 = "0"
        if b7 != "":
            if "0" in str(b7):
                bij7 = ""
        if b8 != "":
            if int(b8) < 10:
                bij8 = "0"
        if b8 != "":
            if "0" in str(b8):
                bij8 = ""
        if b9 != "":
            if int(b9) < 10:
                bij9 = "0"
        if b9 != "":
            if "0" in str(b9):
                bij9 = ""
        if b10 != "":
            if int(b10) < 10:
                bij10 = "0"
        if b10 != "":
            if "0" in str(b10):
                bij10 = ""
                
        #THE EVENTUALLY CALCULATED EXPECTED TIME OF ARRIVAL
        tussenstuk1 = bij1 + str(b1) + ":" + add1 + str(time1) + " aankomst"
        tussenstuk2 = bij2 + str(b2) + ":" + add2 + str(time2) + " aankomst"
        tussenstuk3 = bij3 + str(b3) + ":" + add3 + str(time3) + " aankomst"
        tussenstuk4 = bij4 + str(b4) + ":" + add4 + str(time4) + " aankomst"
        tussenstuk5 = bij5 + str(b5) + ":" + add5 + str(time5) + " aankomst"
        tussenstuk6 = bij6 + str(b6) + ":" + add6 + str(time6) + " aankomst"
        tussenstuk7 = bij7 + str(b7) + ":" + add7 + str(time7) + " aankomst"
        tussenstuk8 = bij8 + str(b8) + ":" + add8 + str(time8) + " aankomst"
        tussenstuk9 = bij9 + str(b9) + ":" + add9 + str(time9) + " aankomst"
        tussenstuk10 = bij10 + str(b10) + ":" + add10 + str(time10) + " aankomst"

        #ALL OTHER TRAFFIC THAN THAT TO SCIENCE PARK IS FILTERED OUT
        if "Science" not in bus1:
            bus1 = ""
            tussenstuk1 = ""
        if "Science" not in bus2:
            bus2 = ""
            tussenstuk2 = ""
        if "Science" not in bus3:
            bus3 = ""
            tussenstuk3 = ""
        if "Science" not in bus4:
            bus4 = ""
            tussenstuk4 = ""
        if "Science" not in bus5:
            bus5 = ""
            tussenstuk5 = ""
        if "Science" not in bus6:
            bus6 = ""
            tussenstuk6 = ""
        if "Science" not in bus7:
            bus7 = ""
            tussenstuk7 = ""
        if "Science" not in bus8:
            bus8 = ""
            tussenstuk8 = ""
        if "Science" not in bus9:
            bus9 = ""
            tussenstuk9 = ""
        if "Science" not in bus10:
            bus10 = ""
            tussenstuk10 = ""

        if tussenstuk1 == "" and tussenstuk2 == "" and tussenstuk3 == "" and tussenstuk4 == "" and tussenstuk5 == "" and tussenstuk6 == "" and tussenstuk7 == "" and tussenstuk8 == "" and tussenstuk9 == "" and tussenstuk10 == "":
            tussenstuk1 = "Er is op dit moment geen reisinformatie beschikbaar"
        return tussenstuk1
        return tussenstuk2
        return tussenstuk3
        return tussenstuk4
        return tussenstuk5
        return tussenstuk6
        return tussenstuk7
        return tussenstuk8
        return tussenstuk9
        return tussenstuk10
        return bus1
        return bus2
        return bus3
        return bus4
        return bus5
        return bus6
        return bus7
        return bus8
        return bus9
        return bus10
    Bus()
except:
    pass

