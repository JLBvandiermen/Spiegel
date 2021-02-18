from __future__ import print_function
from flask import Flask, render_template, request
from importlib import reload
import time
import random 
import operator
import statistics
import probeerStock2
import probeerWeer
import probeerTeletekst
import probeerAgenda
import spiegelpi
import probeerUithof
global calender1 
while True:

    global ding
    global sentenceSplit
    global tram

    try:
        app = Flask(__name__)
        #The home page
        @app.route('/')
        def index():
            global calc
            global stonk
            global avarage
            global bewolking
            global regen
            global maxtemp
            global temp
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
            global calender
            global calender1
            global calender2
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
                
            #AANDELEN
            try:
                reload(probeerStock2)
                probeerStock2.aandelen()
            except:
                stonk=""
                avarage="Er is geen data"
                pass
                
            #INPIREREND
            inspirerend=""
            myList = ["You look good today!", "You're rocking those trousers!", "Nice hair!", "Use that smile!", "Have a blessed day!", "I like you", "If you were a pokemon, I would choose you", "Everywhere I look I am reminded of your love", "There is no one who is insignificant in the purpose of God", "The best thing about the future is that it comes only one day at a time", "I can do all things through Christ who gives me strength", "If God is for us, who can be against us?", "love covers over a multitude of sins", "Above all else, guard your heart, for everything you do flows from it", "Don't let anyone look down on you because you are young", "God will be with you wherever you go", "My God turns my darkness into light", "Those who hope in the Lord will renew their strength", "I can do all this through him who gives me strength", "This is the day the Lord has made", "You can't go back to start again, but today you can make a new ending", "Too many of us are not living our dreams because we are living our fears", "Bravery is not he who doesn't feel afraid, but he who conquers that fear"]
            inspirerend = random.choice(myList)

            #TELETEKST
            try:
                reload(probeerTeletekst)
                probeerTeletekst.Nieuws()
            except:
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
                pass
                
            #UITHOF 
            try:
                reload(probeerUithof)
                probeerUithof.Bus()
            except:
                bus1 ="Er is geen data"
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
                pass
                
            #WEER
            try:
                reload(probeerWeer)
                probeerWeer.Weer()
            except:
                bewolking = ""
                regen = "-"
                maxtemp = "-"
                temp = "-"
                
            #CALENDER
            try:
                reload(probeerAgenda)
                probeerAgenda.Agenda()
            except:
                calender = ""
                calender1 = ""
                calender2 = ""
                
            return render_template("home.html", slash=probeerTeletekst.slash, test=probeerTeletekst.ding, test1=probeerTeletekst.ding1, test2=probeerTeletekst.ding2, test3=probeerTeletekst.ding3, test4=probeerTeletekst.ding4, test5=probeerTeletekst.ding5, test6=probeerTeletekst.ding6, test7=probeerTeletekst.ding7, test8=probeerTeletekst.ding8, test9=probeerTeletekst.ding9, test10=probeerTeletekst.ding10, test11=probeerTeletekst.ding11,test12=probeerTeletekst.ding12,test13=probeerTeletekst.ding13,test14=probeerTeletekst.ding14,test15=probeerTeletekst.ding15,test16=probeerTeletekst.ding16,test17=probeerTeletekst.ding17, test18=probeerTeletekst.ding18, test19=probeerTeletekst.ding19, test20=probeerTeletekst.ding20, test21=probeerTeletekst.ding21, bus1=probeerUithof.bus1, bus2=probeerUithof.bus2, bus3=probeerUithof.bus3, bus4=probeerUithof.bus4, bus5=probeerUithof.bus5, bus6=probeerUithof.bus6, bus7=probeerUithof.bus7, bus8=probeerUithof.bus8, bus9=probeerUithof.bus9, bus10=probeerUithof.bus10, tussenstuk1=probeerUithof.tussenstuk1, tussenstuk2=probeerUithof.tussenstuk2, tussenstuk3=probeerUithof.tussenstuk3, tussenstuk4=probeerUithof.tussenstuk4, tussenstuk5=probeerUithof.tussenstuk5, tussenstuk6=probeerUithof.tussenstuk6, tussenstuk7=probeerUithof.tussenstuk7, tussenstuk8=probeerUithof.tussenstuk8, tussenstuk9=probeerUithof.tussenstuk9, tussenstuk10=probeerUithof.tussenstuk10, temp=probeerWeer.temp, maxtemp=probeerWeer.maxtemp, regen=probeerWeer.regen, bewolking=probeerWeer.bewolking, inspirerend=inspirerend, calender=probeerAgenda.calender, calender1=probeerAgenda.calender1, calender2=probeerAgenda.calender2, stonk=probeerStock2.stonk, avarage=probeerStock2.avarage)

        #Starts the program
        if __name__ == '__main__':
            app.run(debug=True , port=80, host='0.0.0.0')
    except: #ConnectionError as e:
        reload(spiegelpi)
        spiegelpi.Fail()
         
