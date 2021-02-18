from bs4 import BeautifulSoup
import urllib.request
import datetime
import re
try:
    def Agenda():
        import pickle
        import os.path
        from googleapiclient.discovery import build
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.auth.transport.requests import Request
        import functools 
        import operator
        import datetime
        global calender
        global calender1
        global calender2
        global datumdag1
        global datumdag
        global dedatum
        SCOPES = ['https://www.googleapis.com/auth/calendar.readonly'] 
        creds = None
        calenderr = 0
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        service = build('calendar', 'v3', credentials=creds)
        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        #print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                            maxResults=10, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])
        if not events:
            calender = 'No upcoming events found.'
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            start = str(start)
            #REMOVING ALL UGLY TEXT
            start = start.replace("T", " ")
            start = start.replace("+02:00", " ")
            start = start.replace(":00", ".")
            start = start.replace("+01", " ")
            start = start.replace("..", ":00")
            start = start.replace(".", "")
            startSplit = filter(None, start.split("  "))
            for s in startSplit :
                calenderr += 1
                if calenderr == 1:
                    calendera = str(start), event['summary']
                    calender = "".join(calendera)
                elif calenderr == 2:
                    calendera = str(start), event['summary']
                    calender1 = "".join(calendera)
                elif calenderr == 3:
                    calendera = str(start), event['summary']
                    calender2 = "".join(calendera)
                elif calenderr == 4:
                    break
        #print(calender)
        #print(calender1)
        #print(calender2)
        def calenderschoon(calender):
            datum = calender.replace(" ", "-")
            datum = datum.split("-")
            datumdag = datum[2:3]
            datumdag = " ".join(datumdag)
        def removezero(datumdag):
            global datumdag1
            if datumdag == "01":
                datumdag1 = datumdag.replace("0","")
            elif datumdag == "02":
                datumdag1 = datumdag.replace("0","")
            elif datumdag == "03":
                datumdag1 = datumdag.replace("0","")
            elif datumdag == "04":
                datumdag1 = datumdag.replace("0","")
            elif datumdag == "05":
                datumdag1 = datumdag.replace("0","")
            elif datumdag == "06":
                datumdag1 = datumdag.replace("0","")
            elif datumdag == "07":
                datumdag1 = datumdag.replace("0","")
            elif datumdag == "08":
                datumdag1 = datumdag.replace("0","")
            elif datumdag == "09":
                datumdag1 = datumdag.replace("0","")
            else:
                pass
            return datumdag1
        def wanneerdag(datumdag1, vandaag, morgen, overmorgen, datum):
            global dedatum
            if datumdag1 == vandaag:
                datum.pop(0)
                datum.pop(0)
                datum.pop(0)
                wanneer = " ".join(datum)
                dedatum = ("Vandaag: " + wanneer)
            elif datumdag1 == morgen:
                datum.pop(0)
                datum.pop(0)
                datum.pop(0)
                wanneer = " ".join(datum)
                dedatum = ("Morgen: " + wanneer)
            elif datumdag1 == overmorgen:
                datum.pop(0)
                datum.pop(0)
                datum.pop(0)
                wanneer = " ".join(datum)
                dedatum = ("Overmogen: " + wanneer)
            else:
                print("helaas")
            return dedatum
        
        vandaag = datetime.datetime.now()
        vandaag = vandaag.strftime("%D")
        vandaag = str(vandaag)
        vandaag = vandaag.split("/")
        vandaag = vandaag[1:2]
        vandaag = " ".join(vandaag)
        vandaag = str(int(vandaag) + 1 - 1)
        morgen = str(int(vandaag) + 1)
        overmorgen = str(int(morgen) + 1)

        datum = calender.replace(" ", "-")
        datum = datum.split("-")
        datumdag = datum[2:3]
        datumdag = " ".join(datumdag)
        removezero(datumdag)
        wanneerdag(datumdag1, vandaag, morgen, overmorgen, datum)
        calender = dedatum

        datum = calender1.replace(" ", "-")
        datum = datum.split("-")
        datumdag = datum[2:3]
        datumdag = " ".join(datumdag)
        removezero(datumdag)
        wanneerdag(datumdag1, vandaag, morgen, overmorgen, datum)
        calender1 = dedatum

        datum = calender2.replace(" ", "-")
        datum = datum.split("-")
        datumdag = datum[2:3]
        datumdag = " ".join(datumdag)
        removezero(datumdag)
        wanneerdag(datumdag1, vandaag, morgen, overmorgen, datum)
        calender2 = dedatum
        
        return calender
        return calender1
        return calender2
    Agenda()
    print(calender)
    print(calender1)
    print(calender2)
except:
    pass
