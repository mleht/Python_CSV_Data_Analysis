import csv

print()
print("-------------------------")
print("""This dataset is public available for research. The details are described in [Cortez and Morais, 2007]. 
P. Cortez and A. Morais. A Data Mining Approach to Predict Forest Fires using Meteorological Data. 
In J. Neves, M. F. Santos and J. Machado Eds., New Trends in Artificial Intelligence, 
Proceedings of the 13th EPIA 2007 - Portuguese Conference on Artificial Intelligence, December, 
Guimaraes, Portugal, pp. 512-523, 2007. APPIA, ISBN-13 978-989-95618-0-9. 
Available at: http://www.dsi.uminho.pt/~pcortez/fires.pdf""")
print("-------------------------")
print()

forestfires = open("forestfires.csv", "r")
next(forestfires)

weekdays = []
temperatures = []  
rhlist = []

for row in csv.reader(forestfires):
    weekday = row[3]
    weekdays.append(weekday)
    temp = float(row[8])
    temperatures.append(temp)
    rh = int(row[9])
    rhlist.append(rh)
   
forestfires.close()      

temp_average = sum(temperatures)/len(temperatures)
rh_average = sum(rhlist)/len(rhlist)

print("Forest fires / week day")
print(f"Mon: {weekdays.count('mon')}")
print(f"Tue: {weekdays.count('tue')}")
print(f"Wed: {weekdays.count('wed')}")
print(f"Thu: {weekdays.count('thu')}")
print(f"Fir: {weekdays.count('fri')}")
print(f"Sat: {weekdays.count('sat')}")
print(f"Sun: {weekdays.count('sun')}")
print()
print(f"Min temperature before fire: {min(temperatures)} Celsius degrees")
print(f"Max temperature before fire: {max(temperatures)} Celsius degrees")
print(f"Average temperature before fire: {round(temp_average,1)} Celsius degrees")
print()
print(f"Min relative humidity {min(rhlist)} %")
print(f"Max relative humidity {max(rhlist)} %")
print(f"Average relative humidity {int(rh_average)} %")


