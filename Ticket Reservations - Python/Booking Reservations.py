import random
import pickle
import os
import winsound
def message():
     print "Thank You"
class myError(Exception):
         pass
myerror1=myError("Invalid Passport number!!")
myerror2=myError("Invalid Date!!")
myerror3=myError("Invalid Time!!")     
class booking(myError):
     def __init__(self):
          self.type=""
          self.beg=""
          self.end=""
          self.no=0 #number of people travelling
          self.flight=""
          self.date=0
          self.month=0
          self.year=0
          self.time=0
          self.budget=0
          self.id=""
          self.c1=450
          self.c2=450
          self.c3=450
          self.c4=450
          self.c5=450
          self.c6=450
          self.c7=450
          self.c8=450
          self.c9=450
          self.c10=450
          self.c11=450
     def check(self,a):
          if len(a)==8:
               pass
          else:
               raise myerror1
          if a[1].isalpha:
               pass
          else:
               raise myerror1

     def check2(self,b):
          if b[2:4]=="01" or b[2:4]=="03" or b[2:4]=="05" or b[2:4]=="07" or b[2:4]=="08" or b[2:4]=="10" or b[2:4]=="12":
               if b[0:2]>="01" and b[0:2]<="31":
                    pass
               else:
                    raise myerror2
          elif b[2:4]=="04" or b[2:4]=="06" or b[2:4]=="09" or b[2:4]=="11":
               if b[0:2]>="01" and b[0:2]<="30":
                    pass
               else:
                    raise myerror2
          elif b[2:4]=="02":
               if b[0:2]>="01" and b[0:2]<="28":
                    pass
               else:
                    raise myerror2
          elif len(b)!=6:
               raise myerror2

     def check3(self,c):
          if c[0:2]>="00" and c[0:2]<="24" and c[2::]>="00" and c[2::]<="59":
               pass
          else:
               raise myerror3
               
     def datetime(self):
          self.name=raw_input("Enter your Name:")
          try:
               self.id=raw_input("Enter your Passport Number:")
               a=self.id
               self.check(a)
               self.date=raw_input("Enter the date of your trip(DDMMYYYY):")
               b=self.date
               self.check2(b)
               self.time=raw_input("Enter the time for your departure(HHMM):")
               c=self.time
               self.check3(c)
                    
          except myError,e: 
               print e.message
               self.datetime()      
               
     def specs(self):
        print"***************************************************************************************************************************************"
        print"***************************************************************************************************************************************"
        print"******************************            WELCOME TO THE 'QUICK TRACK' BOOKING RESERVATION PORTAL!!    ********************************"    
        print"******************************         WHERE THE BEST FLIGHTS ARE AVAILABLE TO YOU AT THE BEST OFFERS  ********************************"
        print"******************************                        AT YOUR PLACE AND YOUR TIME                      ********************************"
        print"***************************************************************************************************************************************"
        print"***************************************************************************************************************************************"
        print "\n\n\n\nChoose your travel class:"
        print "1-Economy class"
        print "2-Business class"
        print
        print
        ch=0
        while (ch!=1 or ch!=2):
            ch=input("Enter your choice:")
            if ch==1:
                 self.type="economy class"
                 break
            elif ch==2:
                 self.type="business class"
                 break
            else:
                 print"Incorrect Choice!!"
                 continue
                 
     def start(self):
       while True:
         print"***************************************************************************************************************************************"
         print"*********************************************************Departure Destination*********************************************************"
         print"***************************************************************************************************************************************"
         print"##OUR VALUABLE SERVICES ARE AVAILABLE FROM THE FOLLOWING DESTINATIONS"
         print "1-DUBAI"
         print "2-SHARJAH"
         print "3-NEW YORK"
         print "4-LONDON"
         print "5-CARDIFF"
         print "6-HYDERABAD"
         print "7-COCHIN"
         print "8-CALICUT"
         print "9-TOKYO"
         print "10-BRAZIL"
         print "11-BAYERN "
         start=input("Enter the destination from which you want to travel:")
         if start ==1:
              self.beg="Dubai"
              break
         elif start ==2:
              self.beg="Sharjah"
              break
         elif start ==3:
              self.beg="New York"
              break
         elif start ==4:
              self.beg="London"
              break
         elif start ==5:
              self.beg="Cardiff"
              break
         elif start ==6:
              self.beg="Hyderabad"
              break
         elif start ==7:
              self.beg="Cochin"
              break
         elif start ==8:
              self.beg="Calicut"
              break
         elif start ==9:
              self.beg="Tokyo"
              break
         elif start ==10:
              self.beg="Brazil"
              break
         elif start ==11:
              self.beg="Bayern"
              break
         else:
               print"wrong choice"
     def arrival(self):
       while True:
         print"***************************************************************************************************************************************"
         print"**********************************************************Arrival Destination**********************************************************"
         print"***************************************************************************************************************************************"
         print"##OUR VALUABLE SERVICES ARE AVAILABLE TO THE FOLLOWING DESTINATIONS"
         print "1-DUBAI"
         print "2-SHARJAH"
         print "3-NEW YORK"
         print "4-LONDON"
         print "5-CARDIFF"
         print "6-HYDERABAD"
         print "7-COCHIN"
         print "8-CALICUT"
         print "9-TOKYO"
         print "10-BRAZIL"
         print "11-BAYERN "
         start=input("Enter the destination to which you want to travel:")
         if start==1:
              self.end="Dubai"
              if self.end==self.beg:
                   print"ERROR 427356 CONDITION NOT POSSIBLE"
              else:
                    break
         elif start ==2:
              self.end="Sharjah"
              if self.end==self.beg:
                   print"ERROR 427356 CONDITION NOT POSSIBLE"
              else:
                    break
         elif start ==3:
              self.end="New York"
              if self.end==self.beg:
                   print"ERROR 427356 CONDITION NOT POSSIBLE"
              else:
                    break
         elif start ==4:
              self.end="London"
              if self.end==self.beg:
                   print"ERROR 427356 CONDITION NOT POSSIBLE"
              else:
                    break
         elif start ==5:
              self.end="Cardiff"
              if self.end==self.beg:
                   print"ERROR 427356 CONDITION NOT POSSIBLE"
              else:
                    break
         elif start ==6:
              self.end="Hyderabad"
              if self.end==self.beg:
                   print"ERROR 427356 CONDITION NOT POSSIBLE"
              else:
                    break
         elif start ==7:
              self.end="Cochin"
              if self.end==self.beg:
                   print"ERROR 427356 CONDITION NOT POSSIBLE"
              else:
                    break
         elif start ==8:
              self.end="Calicut"
              if self.end==self.beg:
                   print"ERROR 427356 CONDITION NOT POSSIBLE"
              else:
                    break
         elif start ==9:
              self.end="Tokyo"
              if self.end==self.beg:
                   print"ERROR 427356 CONDITION NOT POSSIBLE"
              else:
                    break
         elif start ==10:
              self.end="Brazil"
              if self.end==self.beg:
                   print"ERROR 427356 CONDITION NOT POSSIBLE"
              else:
                    break
              
         elif start ==11:
              self.end="Bayern"
              if self.end==self.beg:
                   print"ERROR 427356 CONDITION NOT POSSIBLE"
              else:
                    break
     
         else:
               print"wrong choice"
     def count(self,x):
          print "hello"
          if self.flight=="Emirates Airlines":
               c1=x-1
               print c1
          elif self.flight=="Etihad Airlines":
               self.c2=self.c2-1
          elif self.flight=="Jet Airways":
               self.c3=self.c3-1
          elif  self.flight=="Indigo Airlines":
               self.c4=self.c4-1
          elif  self.flight=="Air India":
               self.c5=self.c5-1
          elif self.flight=="Air Arabia ":
                self.c6=self.c6-1
          elif  self.flight=="Air India Express":
                self.c7=self.c7-1
          elif self.flight=="Air France ":
               self.c8=self.c8-1
          elif self.flight=="Lufthansa ":
               self.c9=self.c9-1
          elif  self.flight=="Turkish Airlines":
               self.c10=self.c10-1
          elif  self.flight=="Cathay Pacific":
               self.c11=self.c11-1
          else:
               print "wrong choice"
     def price(self,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11):
        while True:
           if self.type=="business class":
              print"***************************************************************************************************************************************"
              print"*************************************************** AVAILABLE AIRPLANES ***************************************************************"
              print"***************************************************************************************************************************************"
              print"_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ "
              print"S.NO|         AIRLINE            |        FARE          | NUMBER OF SEATS AVAILABLE  |"
              print"_ _ |_ _ _ _ _ _ _ _ _ _ _ _  _ _|_ _ _ _ _ _ _ _ _ _ _ |_ _ _ _ _ _ _ _ _ _ _ _ _ _ |"
              print "1)  | Emirates Airlines          |        $600          |            ",c1,"           |"
              print "2)  | Etihad Airlines            |        $500          |            ",c2,"           |"
              print "3)  | Jet Airways                |        $450          |            ",c3,"           |"
              print "4)  | Indigo Airlines            |        $560          |            ",c4,"           |"
              print "5)  | Air India                  |        $400          |            ",c5,"           |"
              print "6)  | Air Arabia                 |        $450          |            ",c6,"           |"
              print "7)  | Air India Express          |        $550          |            ",c7,"           |"
              print "8)  | Air France                 |        $600          |            ",c8,"           |"
              print "9)  | Lufthansa                  |        $620          |            ",c9,"           |"
              print"10) | Turkish Airlines           |        $370          |            ",c10,"           |"
              print"11) | Cathay Pacific             |        $520          |            ",c11,"           |"
              print"_ _ |_ _ _ _ _ _ _ _ _ _ _ _ _ _ |_ _ _ _ _ _ _ _ _ _ _ |_ _ _ _ _ _ _ _ _ _ _ _ _ _ |"
              ch=input("Enter your choice:")
              if ch==1:
                   self.flight="Emirates Airlines"
                   self.budget=600
                   print "Price= $",self.budget
                   if c1==0 or c1<0:
                        print"Seats are not available. Sorry for the incovenience!!"
                        c1=0
                   else:
                        ch=raw_input("Is your Booking Confirmed(Y/N)?")
                        if ch=="Y"or ch=="y":
                             print"Your Booking has been successful!!"
                             print"Hope you enjoyed our service and enjoy your flight with",self.flight
                             break
                        elif ch=="N"or ch=="n":
                             print"1-Make changes in Booking"
                             print"2-Switch to Economy Class"
                             print"3-Exit"
                             ch=input("Enter your choice:")
                             if ch==1:
                                  pass
                             elif ch==3:
                                   print "Thank You and Goodbye!!"
                                   exit()
                             elif ch==2:
                                  self.type="economy class"
                                  pass
                                  
              elif ch==2:
                   self.flight="Etihad Airlines"
                   self.budget=500
                   print "Price= $",self.budget
                   if c2==0 or c2<0:
                        print"Seats are not available. Sorry for the incovenience!!"
                        c2=0
                   else:
                        ch=raw_input("Is your Booking Confirmed(Y/N)?")
                        if ch=="Y"or ch=="y":
                             print"Your Booking has been successful!!"
                             print"Hope you enjoyed our service and enjoy your flight with",self.flight
                             break
                        elif ch=="N"or ch=="n":
                             print"1-Make changes in Booking"
                             print"2-Switch to Economy Class"
                             print"3-Exit"
                             ch=input("Enter your choice:")
                             if ch==1:
                                  pass
                             elif ch==3:
                                   print "Thank You and Goodbye!!"
                                   exit()
                             elif ch==2:
                                  self.type="economy class"
                                  pass
              elif ch==3:
                   self.flight="Jet Airways"
                   self.budget=450
                   print "Price= $",self.budget
                   if c3==0 or c3<0:
                        print"Seats are not available. Sorry for the incovenience!!"
                        c3=0
                   else:
                        ch=raw_input("Is your Booking Confirmed(Y/N)?")
                        if ch=="Y"or ch=="y":
                             print"Your Booking has been successful!!"
                             print"Hope you enjoyed our service and enjoy your flight with",self.flight
                             break
                        elif ch=="N"or ch=="n":
                             print"1-Make changes in Booking"
                             print"2-Switch to Economy Class"
                             print"3-Exit"
                             ch=input("Enter your choice:")
                             if ch==1:
                                  pass
                             elif ch==3:
                                   print "Thank You and Goodbye!!"
                                   exit()
                             elif ch==2:
                                  self.type="economy class"
                                  pass
              elif ch==4:
                   self.flight="Indigo Airlines"
                   self.budget=560
                   print "Price= $",self.budget
                   if c4==0 or c4<0:
                        print"Seats are not available. Sorry for the incovenience!!"
                        c4=0
                   else:
                        ch=raw_input("Is your Booking Confirmed(Y/N)?")
                        if ch=="Y"or ch=="y":
                             print"Your Booking has been successful!!"
                             print"Hope you enjoyed our service and enjoy your flight with",self.flight
                             break
                        elif ch=="N"or ch=="n":
                             print"1-Make changes in Booking"
                             print"2-Switch to Economy Class"
                             print"3-Exit"
                             ch=input("Enter your choice:")
                             if ch==1:
                                  pass
                             elif ch==3:
                                   print "Thank You and Goodbye!!"
                                   exit()
                             elif ch==2:
                                  self.type="economy class"
                                  pass
                             elif ch==3:
                                   self.price()
              elif ch==5:
                   self.flight="Air India"
                   self.budget=400
                   print "Price= $",self.budget
                   if c5==0 or c5<0:
                        print"Seats are not available. Sorry for the incovenience!!"
                        c5=0
                   else:
                        ch=raw_input("Is your Booking Confirmed?(Y/N)")
                        if ch=="Y"or ch=="y":
                             print"Your Booking has been successful!!"
                             print"Hope you enjoyed our service and enjoy your flight with",self.flight
                             break
                        elif ch=="N"or ch=="n":
                             print"1-Make changes in Booking"
                             print"2-Switch to Economy Class"
                             print"3-Exit"
                             ch=input("Enter your choice:")
                             if ch==1:
                                  pass
                             elif ch==3:
                                   print "Thank You and Goodbye!!"
                                   exit()
                             elif ch==2:
                                  self.type="economy class"
                                  pass
              elif ch==6: 
                   self.flight="Air Arabia "
                   self.budget=450
                   print "Price= $",self.budget
                   if c6==0 or c6<0:
                        print"Seats are not available. Sorry for the incovenience!!"
                        c6=0
                   else:
                        ch=raw_input("Is your Booking Confirmed(Y/N)?")
                        if ch=="Y"or ch=="y":
                             print"Your Booking has been successful!!"
                             print"Hope you enjoyed our service and enjoy your flight with",self.flight
                             break
                        elif ch=="N"or ch=="n":
                             print"1-Make changes in Booking"
                             print"2-Switch to Economy Class"
                             print"3-Exit"
                             ch=input("Enter your choice:")
                             if ch==1:
                                  pass
                             elif ch==3:
                                   print "Thank You and Goodbye!!"
                                   exit()
                             elif ch==2:
                                  self.type="economy class"
                                  pass
              elif ch==7:
                   self.flight="Air India Express"
                   self.budget=550
                   print "Price= $",self.budget
                   if c7==0 or c7<0:
                        print"Seats are not available. Sorry for the incovenience!!"
                        c7=0
                   else:
                        ch=raw_input("Is your Booking Confirmed(Y/N)?")
                        if ch=="Y"or ch=="y":
                             print"Your Booking has been successful!!"
                             print"Hope you enjoyed our service and enjoy your flight with",self.flight
                             break
                        elif ch=="N"or ch=="n":
                             print"1-Make changes in Booking"
                             print"2-Switch to Economy Class"
                             print"3-Exit"
                             ch=input("Enter your choice:")
                             if ch==1:
                                  pass
                             elif ch==3:
                                   print "Thank You and Goodbye!!"
                                   exit()
                             elif ch==2:
                                  self.type="economy class"
                                  pass
                                  
              elif ch==8:
                   self.flight="Air France "
                   self.budget=600
                   print "Price= $",self.budget
                   if c8==0 or c8<0:
                        print"Seats are not available. Sorry for the incovenience!!"
                        c8=0
                   else:
                        ch=raw_input("Is your Booking Confirmed(Y/N)?")
                        if ch=="Y"or ch=="y":
                             print"Your Booking has been successful!!"
                             print"Hope you enjoyed our service and enjoy your flight with",self.flight
                             break
                        elif ch=="N"or ch=="n":
                             print"1-Make changes in Booking"
                             print"2-Switch to Economy Class"
                             print"3-Exit"
                             ch=input("Enter your choice:")
                             if ch==1:
                                  pass
                             elif ch==3:
                                   print "Thank You and Goodbye!!"
                                   exit()
                             elif ch==2:
                                  self.type="economy class"
                                  pass
              elif ch==9:
                   self.flight="Lufthansa "
                   self.budget=620
                   print "Price= $",self.budget
                   if  c9==0 or c9<0:
                        print"Seats are not available. Sorry for the incovenience!!"
                        c9=0
                   else:
                        ch=raw_input("Is your Booking Confirmed(Y/N)?")
                        if ch=="Y"or ch=="y":
                             print"Your Booking has been successful!!"
                             print"Hope you enjoyed our service and enjoy your flight with",self.flight
                             break
                        elif ch=="N" or ch=="n":
                             print"1-Make changes in Booking"
                             print"2-Switch to Economy Class"
                             print"3-Exit"
                             ch=input("Enter your choice:")
                             if ch==1:
                                  pass
                             elif ch==3:
                                   print "Thank You and Goodbye!!"
                                   exit()
                             elif ch==2:
                                  self.type="economy class"
                                  pass
                                  
              elif ch==10:
                   self.flight="Turkish Airlines"
                   self.budget=370
                   print "Price= $",self.budget
                   if  c10==0 or c10<0:
                        print"Seats are not available. Sorry for the incovenience!!"
                        c10=0
                   else:
                        ch=raw_input("Is your Booking Confirmed(Y/N)?")
                        if ch=="Y"or ch=="y":
                             print"Your Booking has been successful!!"
                             print"Hope you enjoyed our service and enjoy your flight with",self.flight
                             break
                        elif ch=="N"or ch=="n":
                             print"1-Make changes in Booking"
                             print"2-Switch to Economy Class"
                             print"3-Exit"
                             ch=input("Enter your choice:")
                             if ch==1:
                                  pass
                             elif ch==3:
                                   print "Thank You and Goodbye!!"
                                   exit()
                             elif ch==2:
                                  self.type="economy class"
                                  pass
              elif ch==11:
                   self.flight="Cathay Pacific"
                   self.budget=520
                   print "Price= $",self.budget
                   if c11==0 or c11<0:
                        print"Seats are not available. Sorry for the incovenience!!"
                        c11=0
                        break
                   else:
                        ch=raw_input("Is your Booking Confirmed(Y/N)?")
                        if ch=="Y"or ch=="y":
                             print"Your Booking has been successful!!"
                             print"Hope you enjoyed our service and enjoy your flight with",self.flight
                             break
                        elif ch=="N"or ch=="n":
                             print"1-Make changes in Booking"
                             print"2-Switch to Economy Class"
                             print"3-Exit"
                             ch=input("Enter your choice:")
                             if ch==1:
                                  pass
                             elif ch==3:
                                   print "Thank You and Goodbye!!"
                                   exit()
                             elif ch==2:
                                  self.type="economy class"
                                  pass
           elif self.type=="economy class":
              print"***************************************************************************************************************************************"
              print"*************************************************** AVAILABLE AIRPLANES ***************************************************************"
              print"***************************************************************************************************************************************"
              print"_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ "
              print"S.NO|         AIRLINE            |        FARE          | NUMBER OF SEATS AVAILABLE  |"
              print"_ _ |_ _ _ _ _ _ _ _ _ _ _ _  _ _|_ _ _ _ _ _ _ _ _ _ _ |_ _ _ _ _ _ _ _ _ _ _ _ _ _ |"
              print "1)  | Emirates Airlines          |        $400          |            ",c1,"           |"
              print "2)  | Etihad Airlines            |        $500          |            ",c2,"           |"
              print "3)  | Jet Airways                |        $250          |            ",c3,"           |"
              print "4)  | Indigo Airlines            |        $160          |            ",c4,"           |"
              print "5)  | Air India                  |        $200          |            ",c5,"           |"
              print "6)  | Air Arabia                 |        $150          |            ",c6,"           |"
              print "7)  | Air India Express          |        $350          |            ",c7,"           |"
              print "8)  | Air France                 |        $400          |            ",c8,"           |"
              print "9)  | Lufthansa                  |        $420          |            ",c9,"           |"
              print"10) | Turkish Airlines           |        $170          |            ",c10,"           |"
              print"11) | Cathay Pacific             |        $220          |            ",c11,"           |"
              print"_ _ |_ _ _ _ _ _ _ _ _ _ _ _ _ _ |_ _ _ _ _ _ _ _ _ _ _ |_ _ _ _ _ _ _ _ _ _ _ _ _ _ |"
              ch=input("Enter your choice:")
              if ch==1:
                   self.flight="Emirates Airlines"
                   self.budget=400
                   print "Price= $",self.budget
                   if c1==0 or c1<0:
                        print"Seats are not available. Sorry for the incovenience!!"
                        c1=0
                   else:
                        ch=raw_input("Is your Booking Confirmed(Y/N)?")
                        if ch=="Y"or ch=="y":
                             print"Your Booking has been successful!!"
                             print"Hope you enjoyed our service and enjoy your flight with",self.flight
                             break
                        elif ch=="N"or ch=="n":
                             print"1-Make changes in Booking"
                             print"2-Switch to Business Class"
                             print"3-Exit"
                             ch=input("Enter your choice:")
                             if ch==1:
                                  pass
                             elif ch==3:
                                   print "Thank You and Goodbye!!"
                                   exit()
                             elif ch==2:
                                  self.type="business class"
                                  pass
                                  
              elif ch==2:
                   self.flight="Etihad Airlines"
                   self.budget=500
                   print "Price= $",self.budget
                   if c2==0 or c2<0:
                        print"Seats are not available. Sorry for the incovenience!!"
                        c2=0
                   else:
                        ch=raw_input("Is your Booking Confirmed(Y/N)?")
                        if ch=="Y"or ch=="y":
                             print"Your Booking has been successful!!"
                             print"Hope you enjoyed our service and enjoy your flight with",self.flight
                             break
                        elif ch=="N"or ch=="n":
                             print"1-Make changes in Booking"
                             print"2-Switch to Business Class"
                             print"3-Exit"
                             ch=input("Enter your choice:")
                             if ch==1:
                                  pass
                             elif ch==3:
                                   print "Thank You and Goodbye!!"
                                   exit()
                             elif ch==2:
                                  self.type="business class"
                                  pass
              elif ch==3:
                   self.flight="Jet Airways"
                   self.budget=250
                   print "Price= $",self.budget
                   if c3==0 or c3<0:
                        print"Seats are not available. Sorry for the incovenience!!"
                        c3=0
                   else:
                        ch=raw_input("Is your Booking Confirmed(Y/N)")
                        if ch=="Y"or ch=="y":
                             print"Your Booking has been successful!!"
                             print"Hope you enjoyed our service and enjoy your flight with",self.flight
                             break
                        elif ch=="N"or ch=="n":
                             print"1-Make changes in Booking"
                             print"2-Switch to Business Class"
                             print"3-Exit"
                             ch=input("Enter your choice:")
                             if ch==1:
                                  pass
                             elif ch==3:
                                   print "Thank You and Goodbye!!"
                                   exit()
                             elif ch==2:
                                  self.type="business class"
                                  pass
              elif ch==4:
                   self.flight="Indigo Airlines"
                   self.budget=160
                   print "Price= $",self.budget
                   if c4==0 or c4<0:
                        print"Seats are not available. Sorry for the incovenience!!"
                        c4=0
                   else:
                        ch=raw_input("Is your Booking Confirmed(Y/N)?")
                        if ch=="Y"or ch=="y":
                             print"Your Booking has been successful!!"
                             print"Hope you enjoyed our service and enjoy your flight with",self.flight
                             break
                        elif ch=="N"or ch=="n":
                             print"1-Make changes in Booking"
                             print"2-Switch to Business Class"
                             print"3-Exit"
                             ch=input("Enter your choice:")
                             if ch==1:
                                  pass
                             elif ch==3:
                                   print "Thank You and Goodbye!!"
                                   exit()
                             elif ch==2:
                                  self.type="business class"
                                  pass
              elif ch==5:
                   self.flight="Air India"
                   self.budget=200
                   print "Price= $",self.budget
                   if c5==0 or c5<0:
                        print"Seats are not available. Sorry for the incovenience!!"
                        c5=0
                   else:
                        ch=raw_input("Is your Booking Confirmed(Y/N)?")
                        if ch=="Y"or ch=="y":
                             print"Your Booking has been successful!!"
                             print"Hope you enjoyed our service and enjoy your flight with",self.flight
                             break
                        elif ch=="N"or ch=="n":
                             print"1-Make changes in Booking"
                             print"2-Switch to Business Class"
                             print"3-Exit"
                             ch=input("Enter your choice:")
                             if ch==1:
                                  pass
                             elif ch==3:
                                   print "Thank You and Goodbye!!"
                                   exit()
                             elif ch==2:
                                  self.type="business class"
                                  pass
              elif ch==6:
                   self.flight="Air Arabia "
                   self.budget=150
                   print "Price= $",self.budget
                   if c6==0 or c6<0:
                        print"Seats are not available. Sorry for the incovenience!!"
                        c6=0
                   else:
                        ch=raw_input("Is your Booking Confirmed(Y/N)?")
                        if ch=="Y"or ch=="y":
                             print"Your Booking has been successful!!"
                             print"Hope you enjoyed our service and enjoy your flight with",self.flight
                             break
                        elif ch=="N"or ch=="n":
                             print"1-Make changes in Booking"
                             print"2-Switch to Business Class"
                             print"3-Exit"
                             ch=input("Enter your choice:")
                             if ch==1:
                                  pass
                             elif ch==3:
                                   print "Thank You and Goodbye!!"
                                   exit()
                             elif ch==2:
                                  self.type="business class"
                                  pass

              elif ch==7:
                   self.flight="Air India Express"
                   self.budget=350
                   print "Price= $",self.budget
                   if c7==0 or c7<0:
                        print"Seats are not available. Sorry for the incovenience!!"
                        c7=0
                   else:
                        ch=raw_input("Is your Booking Confirmed(Y/N)?")
                        if ch=="Y"or ch=="y":
                             print"Your Booking has been successful!!"
                             print"Hope you enjoyed our service and enjoy your flight with",self.flight
                             break
                        elif ch=="N"or ch=="n":
                             print"1-Make changes in Booking"
                             print"2-Switch to Business Class"
                             print"3-Exit"
                             ch=input("Enter your choice:")
                             if ch==1:
                                  pass
                             elif ch==3:
                                   print "Thank You and Goodbye!!"
                                   exit()
                             elif ch==2:
                                  self.type="business class"
                                  pass
     
              elif ch==8:
                   self.flight="Air France "
                   self.budget=400
                   print "Price= $",self.budget
                   if c8==0 or c8<0:
                        print"Seats are not available. Sorry for the incovenience!!"
                        c8=0
                   else:
                        ch=raw_input("Is your Booking Confirmed(Y/N)?")
                        if ch=="Y"or ch=="y":
                             print"Your Booking has been successful!!"
                             print"Hope you enjoyed our service and enjoy your flight with",self.flight
                             break
                        elif ch=="N"or ch=="n":
                             print"1-Make changes in Booking"
                             print"2-Switch to Business Class"
                             print"3-Exit"
                             ch=input("Enter your choice:")
                             if ch==1:
                                  pass
                             elif ch==3:
                                   print "Thank You and Goodbye!!"
                                   exit()
                             elif ch==2:
                                  self.type="business class"
                                  pass
              elif ch==9:
                   self.flight="Lufthansa "
                   self.budget=420
                   print "Price= $",self.budget
                   if c9==0 or c9<0:
                        print"Seats are not available. Sorry for the incovenience!!"
                        c9=0
                   else:
                        ch=raw_input("Is your Booking Confirmed(Y/N)?")
                        if ch=="Y"or ch=="y":
                             print"Your Booking has been successful!!"
                             print"Hope you enjoyed our service and enjoy your flight with",self.flight
                             break
                        elif ch=="N"or ch=="n":
                             print"1-Make changes in Booking"
                             print"2-Switch to Business Class"  
                             print"3-Exit"
                             ch=input("Enter your choice:")
                             if ch==1:
                                  pass
                             elif ch==3:
                                   print "Thank You and Goodbye!!"
                                   exit()
                             elif ch==2:
                                  self.type="business class"
                                  pass
                                  
              elif ch==10:
                   self.flight="Turkish Airlines"
                   self.budget=170
                   print "Price= $",self.budget
                   if c10==0 or c10<0:
                        print"Seats are not available. Sorry for the incovenience!!"
                        c10=0
                   else:
                        ch=raw_input("Is your Booking Confirmed(Y/N)?")
                        if ch=="Y"or ch=="y":
                             print"Your Booking has been successful!!"
                             print"Hope you enjoyed our service and enjoy your flight with",self.flight
                             break
                        elif ch=="N"or ch=="n":
                             print"1-Make changes in Booking"
                             print"2-Switch to Business Class"
                             print"3-Exit"
                             ch=input("Enter your choice:")
                             if ch==1:
                                  pass
                             elif ch==3:
                                   print "Thank You and Goodbye!!"
                                   exit()
                             elif ch==2:
                                  self.type="business class"
                                  pass
              elif ch==11:
                   self.flight="Cathay Pacific"
                   self.budget=220
                   print "Price= $",self.budget
                   if c11==0 or c11<0:
                        print"Seats are not available. Sorry for the incovenience!!"
                        c11=0
                   else:
                        ch=raw_input("Is your Booking Confirmed(Y/N)?")
                        if ch=="Y"or ch=="y":
                             print"Your Booking has been successful!!"
                             print"Hope you enjoyed our service and enjoy your flight with",self.flight
                             break
                             
                             
                        elif ch=="N"or ch=="n":
                             print"1-Make changes in Booking"
                             print"2-Switch to Business Class"
                             print"3-Exit"
                             ch=input("Enter your choice:")
                             if ch==1:
                                  pass
                             elif ch==3:
                                   print "Thank You and Goodbye!!"
                                   exit()
                             elif ch==2:
                                  self.type="business class"
                                  pass
     
     def display1(self,i):
          print i,"\t",self.type,
     def display2(self):
          if len(self.name)>=8:
               print "\t",self.name,"\t",self.id,"\t",self.date,"\t",self.time,
          else:
               print "\t",self.name,"\t\t",self.id,"\t",self.date,"\t",self.time,
     def display3(self):
          if len(self.beg)<7:
              print "\t",self.beg,"\t",
          else:
             print "\t",self.beg,  
     def display4(self):
          if len(self.end)<7 or len(self.end)==7:
               print "\t",self.end,
          else:
               print "\t\t",self.end, 
     def display5(self):
           if len(self.end)<7 or len(self.end)==7:
                if len(self.flight)>6:
                   print  "\t\t",self.flight,"\t",self.budget,"\n"
                else:
                    print  "\t",self.flight,"\t",self.budget,"\n" 
     
         
          
s=booking()        
class file(booking):
   def book (self,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11):
          k=open("class.dat",'wb')
          k1=open("datetime.dat",'wb')
          k2=open("destination.dat",'wb')
          k3=open("arrival.dat",'wb')
          k4=open("price.dat",'wb')  
          s.specs()
          pickle.dump(s,k)
          s.datetime()
          pickle.dump(s,k1)
          s.start()
          pickle.dump(s,k2)
          s.arrival()
          pickle.dump(s,k3)
          s.price(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11)
          pickle.dump(s,k4)
          k1.close()
          k2.close()
          k3.close()
          k4.close()
          k.close()
          if s.flight=="Emirates Airlines":
               return 1
          elif s.flight=="Etihad Airlines":
               return 2
          elif s.flight=="Jet Airways":
               return 3
          elif  s.flight=="Indigo Airlines":
                 return 4
          elif  s.flight=="Air India":
               return 5
          elif s.flight=="Air Arabia ":
                return 6
          elif  s.flight=="Air India Express":
                return 7
          elif s.flight=="Air France ":
               return 8
          elif s.flight=="Lufthansa ":
               return 9
          elif  s.flight=="Turkish Airlines":
               return 10
          elif  s.flight=="Cathay Pacific":
               return 11
          

   def add(self,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11):
          k=open("class.dat",'ab')
          k1=open("datetime.dat",'ab')
          k2=open("destination.dat",'ab')
          k3=open("arrival.dat",'ab')
          k4=open("price.dat",'ab')
          s.specs()
          pickle.dump(s,k)
          s.datetime()
          pickle.dump(s,k1)
          s.start()
          pickle.dump(s,k2)
          s.arrival()
          pickle.dump(s,k3)
          s.price(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11)
          pickle.dump(s,k4)
          k1.close()
          k2.close()
          k3.close()
          k4.close()
          k.close()
          if s.flight=="Emirates Airlines":
               return 1
          elif s.flight=="Etihad Airlines":
               return 2
          elif s.flight=="Jet Airways":
               return 3
          elif  s.flight=="Indigo Airlines":
                 return 4
          elif  s.flight=="Air India":
               return 5
          elif s.flight=="Air Arabia ":
                return 6
          elif  s.flight=="Air India Express":
                return 7
          elif s.flight=="Air France ":
               return 8
          elif s.flight=="Lufthansa ":
               return 9
          elif  s.flight=="Turkish Airlines":
               return 10
          elif  s.flight=="Cathay Pacific":
               return 11
     
   
   def display(self):
          k=open("class.dat",'rb')
          k1=open("datetime.dat",'rb')
          k2=open("destination.dat",'rb')
          k3=open("arrival.dat",'rb')
          k4=open("price.dat",'rb')
          i=1
          print "SNO","\t","type","\t\t","name","\t\t","id","\t\t","date","\t\t","time","\t","departure","\t","arrival","\t\t","flight","\t\t","budget"
          try:
               while True:
                    s=pickle.load(k)
                    s1=pickle.load(k1)
                    s2=pickle.load(k2)
                    s3=pickle.load(k3)
                    s4=pickle.load(k4)
                    s.display1(i)
                    s1.display2()
                    s2.display3()
                    s3.display4()
                    s4.display5()
                    i=i+1
          except EOFError:
               k.close()
               k1.close()
               k2.close()
               k3.close()
               k4.close()
   def delete(self,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11):
          passid=raw_input("enter the passport id")
          k=open("class.dat",'rb')
          k1=open("datetime.dat",'rb')
          k2=open("destination.dat",'rb')
          k3=open("arrival.dat",'rb')
          k4=open("price.dat",'rb')
          f=open("newrec.dat",'wb')
          f1=open("newrec1.dat",'wb')
          f2=open("newrec2.dat",'wb')
          f3=open("newrec3.dat",'wb')
          f4=open("newrec4.dat",'wb')
          status=0  #flag variable
          s=booking()
          try:
               while True:
                    s=pickle.load(k)
                    s1=pickle.load(k1)
                    s2=pickle.load(k2)
                    s3=pickle.load(k3)
                    s4=pickle.load(k4)
                    if s1.id!=passid:
                         pickle.dump(s,f)
                         pickle.dump(s1,f1)
                         pickle.dump(s2,f2)
                         pickle.dump(s3,f3)
                         pickle.dump(s4,f4)
                    else:
                         status=1
          except EOFError:
               k.close()
               k1.close()
               k2.close()
               k3.close()
               k4.close()
               f.close()
               f1.close()
               f2.close()
               f3.close()
               f4.close()
          if status==1:
               print "record deleted"
          else:
               print "record not found"
          os.remove("class.dat")
          os.remove("datetime.dat")
          os.remove("destination.dat")
          os.remove("arrival.dat")
          os.remove("price.dat")
          os.rename("newrec.dat","class.dat")
          os.rename("newrec1.dat","datetime.dat")
          os.rename("newrec2.dat","destination.dat")
          os.rename("newrec3.dat","arrival.dat")
          os.rename("newrec4.dat","price.dat")
          if s4.flight=="Emirates Airlines":
               return 1
          elif s4.flight=="Etihad Airlines":
               return 2
          elif s4.flight=="Jet Airways":
               return 3
          elif  s4.flight=="Indigo Airlines":
                 return 4
          elif  s4.flight=="Air India":
               return 5
          elif s4.flight=="Air Arabia ":
                return 6
          elif  s4.flight=="Air India Express":
                return 7
          elif s4.flight=="Air France ":
               return 8
          elif s4.flight=="Lufthansa ":
               return 9
          elif  s4.flight=="Turkish Airlines":
               return 10
          elif  s4.flight=="Cathay Pacific":
               return 11
          


   def modify(self,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11):
         passid=raw_input("Enter the Passport number:")
         k=open("class.dat",'rb')
         k1=open("datetime.dat",'rb')
         k2=open("destination.dat",'rb')
         k3=open("arrival.dat",'rb')
         k4=open("price.dat",'rb')
         f=open("newrec.dat",'wb')
         f1=open("newrec1.dat",'wb')
         f2=open("newrec2.dat",'wb')
         f3=open("newrec3.dat",'wb')
         f4=open("newrec4.dat",'wb')
         status=0
         try:
             while True:
                    s=pickle.load(k)
                    s1=pickle.load(k1)
                    s2=pickle.load(k2)
                    s3=pickle.load(k3)
                    s4=pickle.load(k4)
                    if s.id==passid:
                          s.specs()
                          pickle.dump(s,f)
                          s1.datetime()
                          pickle.dump(s1,f1)
                          s2.start()
                          pickle.dump(s2,f2)
                          s3.arrival()
                          pickle.dump(s3,f3)
                          s4.price(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11)
                          pickle.dump(s4,f4)
                          status=1
                    else:
                       pickle.dump(s,f)
                       pickle.dump(s1,f1)
                       pickle.dump(s2,f2)
                       pickle.dump(s3,f3)
                       pickle.dump(s4,f4)
         except EOFError:
                   k.close()
                   k1.close()
                   k2.close()
                   k3.close()
                   k4.close()
                   f.close()
                   f1.close()
                   f2.close()
                   f3.close()
                   f4.close()
         if status==1:
               print "record modified"
         else:
               print "record not found"
         os.remove("class.dat")
         os.remove("datetime.dat")
         os.remove("destination.dat")
         os.remove("arrival.dat")
         os.remove("price.dat")
         os.rename("newrec.dat","class.dat")
         os.rename("newrec1.dat","datetime.dat")
         os.rename("newrec2.dat","destination.dat")
         os.rename("newrec3.dat","arrival.dat")
         os.rename("newrec4.dat","price.dat")
                         
                    
f=file()
c1=c2=c3=c4=c5=c6=c7=c8=c9=c10=c11=450
while True:
     print
     print"***************************************************************************************************************************************"
     print"***************************************************************************************************************************************"
     print"*************************************************      1 - MAKE A BOOKING         *****************************************************"
     print"*************************************************      2 - ADD A NEW RESERVATION  *****************************************************"
     print"*************************************************      3 - SHOW BOOKING           *****************************************************"
     print"*************************************************      4 - CANCEL THE BOOKING     *****************************************************"
     print"*************************************************      5 - EDIT THE RESERVATION   *****************************************************"
     print"*************************************************      6 - EXIT                   *****************************************************"
     print"***************************************************************************************************************************************"
     print"***************************************************************************************************************************************"
     ch=input("Enter your choice:")     
     if ch==1:
          winsound.Beep(500,500)
          p=f.book(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11)
          if p==1:
               c1=c1-1
          elif p==2:
               c2=c2-1
          elif p==3:
               c3=c3-1
          elif p==4:
               c4=c4-1
          elif p==5:
               c5=c5-1
          elif p==6:
               c6=c6-1
          elif p==7:
               c7=c7-1
          elif p==8:
               c8=c8-1
          elif p==9:
               c9=c9-1
          elif p==10:
               c10=c10-1
          elif p==11:
               c11=c11-1
          

     elif ch==2:
          winsound.Beep(500,500)
          p=f.add(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11)
          if p==1:
               c1=c1-1
          elif p==2:
               c2=c2-1
          elif p==3:
               c3=c3-1
          elif p==4:
               c4=c4-1
          elif p==5:
               c5=c5-1
          elif p==6:
               c6=c6-1
          elif p==7:
               c7=c7-1
          elif p==8:
               c8=c8-1
          elif p==9:
               c9=c9-1
          elif p==10:
               c10=c10-1
          elif p==11:
               c11=c11-1
          
 
          
     elif ch==3:
          f.display()
          winsound.Beep(500,500)
     elif ch==4:
          winsound.Beep(500,500)
          p=f.delete(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11)
          if p==1 and  c1!=450:
               c1=c1+1
          elif p==2 and c2!=450:
               c2=c2+1
          elif p==3 and c3!=450:
               c3=c3+1
          elif p==4 and c4!=450:
               c4=c4+1
          elif p==5 and c5!=450:
               c5=c5+1
          elif p==6 and c6!=450:
               c6=c6+1
          elif p==7 and c7!=450:
               c7=c7+1
          elif p==8 and c8!=450:
               c8=c8+1
          elif p==9 and c9!=450:
               c9=c9+1
          elif p==10 and c10!=450:
               c10=c10+1
          elif p==11 and c11!=450:
               c11=c11+1
          
     elif ch==5:
          winsound.Beep(500,500)
          f.modify(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11)
     elif ch==6:
          print "Thank you for using our services!!"
          winsound.Beep(2000,1500)
          exit()
          
          
