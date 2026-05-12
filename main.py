#Task 1
print ("Hello, world")
print (" THis program was made by Gustav ")

#Task3
Ticket_Price = 100  # biljettpris
Total_Cash_Amount = 200  # pengar på fickan
print(f"Det blir {Total_Cash_Amount - Ticket_Price}  kronor över.")
Exchange = (Total_Cash_Amount - Ticket_Price) / 2
print(f"Varje person får  {Exchange}")

#Task4 1A

Heltal_1 = int(input(" Skriv ett heltal "))
Heltal_2 = int(input(" Skriv ett till heltal"))
print(f"Summan av de två talen blir {Heltal_1 + Heltal_2}" )

#Task4 2A
jacket_price = 2000
rea_procent = 0.75
print(f"Jackans kostnad efter avdragen rabatt är {jacket_price * rea_procent} SEK")


#Task4 2B
jacket_price = 2000
rea_procent = int (input(" Skriv in önskad procentrabatt i heltal ")) #Finns inget som hindrar användaren från att skriva ett heltal
print(f"Jackans kostnad efter avdragen rabatt är {round(jacket_price * (1- rea_procent / 100))} SEK") #round agerar som avrundning

# Task5 1A
Distance_Between_Cities= 470
Estimated_Speed = int(input("Hur många KM/H kör du?"))
print(f" Det kommer ta dig {round(Distance_Between_Cities / Estimated_Speed ,2)} Timmar att köra")

#Task 5 1B
Distance_Between_Cities= 470
Estimated_Speed = int(input("Hur många KM/H kör du?"))
print(f" Det kommer ta dig {round((Distance_Between_Cities / Estimated_Speed) * 60 ,0)} minuter att köra")

#Task 5 1C

Estimated_Speed = int(input("Hur många KM/H kör du?"))
Driving_Time= 470 / Estimated_Speed
Time_Hours = int (Driving_Time) # Sätter totala tiden i timmar en egen variabel
Time_Minutes = (int((Driving_Time -Time_Hours) * 60)) # Variabel som tar bort hela timmar och räknar om decimalerna av kvarvarande timmar i minuter
print(f"Det kommer ta dig  {Time_Hours} Timmar och {Time_Minutes})minuter till din destination")

input ("Press enter to exit")
#Task 5 2

