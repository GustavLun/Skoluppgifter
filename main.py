#Task 1
print ("Hello, world")
print (" This program was made by Gustav ")

#Task3
Ticket_Price = 100  # biljettpris
Total_Cash_Amount = 200  # pengar på fickan
print(f"Det blir {Total_Cash_Amount - Ticket_Price}  kronor över.")
Exchange = (Total_Cash_Amount - Ticket_Price) / 2
print(f"Varje person får  {Exchange} över efter att 2 biljetter köpts av värdet 50SEK/Biljett")
print (input("Press any key for next script"))

#Task4 1A

Heltal_1 = int(input(" Skriv ett heltal "))
Heltal_2 = int(input(" Skriv ett till heltal"))
print(f"Summan av de två talen blir {Heltal_1 + Heltal_2}" )
print (input("Press any key for next script"))

#Task4 2A
jacket_price = 2000
rea_procent = 0.75
print(f"Jackans kostnad är 2000Sek, men efter avdragen rabatt kostar den {jacket_price * rea_procent} SEK")
print (input("Press any key for next script"))


#Task4 2B
jacket_price = 2000
rea_procent = int (input(" Skriv in önskad procentrabatt i heltal ")) #Finns inget som hindrar användaren från att skriva ett heltal
print(f"Jackans kostnad efter avdragen rabatt är {round(jacket_price * (1- rea_procent / 100))} SEK") #round agerar som avrundning
print (input("Press any key for next script"))

# Task5 1A
Distance_Between_Cities= 470
Estimated_Speed = int(input("Hur många KM/H kör du?"))
print(f" Det kommer ta dig {round(Distance_Between_Cities / Estimated_Speed ,2)} Timmar att köra till destinationen")
print (input("Press any key for next script"))

#Task 5 1B
Distance_Between_Cities= 470
Estimated_Speed = int(input("Hur många KM/H kör du?"))
print(f" Det kommer ta dig {round((Distance_Between_Cities / Estimated_Speed) * 60 ,0)} minuter att köra att köra till destinationen")
print (input("Press any key for next script"))

#Task 5 1C

Estimated_Speed = int(input("Hur många KM/H kör du?"))
Driving_Time= 470 / Estimated_Speed
Time_Hours = int (Driving_Time) # Sätter totala tiden i timmar en egen variabel
Time_Minutes = (int((Driving_Time -Time_Hours) * 60)) # Variabel som tar bort hela timmar och räknar om decimalerna av kvarvarande timmar i minuter
print(f"Det kommer ta {Time_Hours} Timmar och {Time_Minutes})minuter till din destination")
print (input("Press any key for next script"))


#Task 5 2
import math
X=(float(input("Skriv längden på sida X av triangeln")))
B=float(input("Skriv längden på sida B av triangeln"))
C=float (math.sqrt(X**2 + (B**2)))
print("Hypotenusan är", (round(C ,2)))
print (input("Press any key for next script"))

#Task 5 3A
from datetime import timedelta, datetime
print(datetime.now().timestamp())
print (input("Press any key for next script"))

#Task 5 3B
Today=datetime.now()
Days_Ahead=int(input(" Skriv antal dagar framåt för att få dess datum "))
Futuredate = Today + timedelta(days=Days_Ahead)
print("Om ",Days_Ahead , "Dagar är det den" , Futuredate.strftime(("%Y-%m-%d")))

print (input( "Press any key to exit "))