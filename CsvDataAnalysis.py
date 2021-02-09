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

qty_mon = 0
qty_tue = 0
qty_wed = 0
qty_thu = 0
qty_fri = 0
qty_sat = 0
qty_sun = 0
min_temp = 100.00
max_temp = 0.00
temp_sum = 0.00
rows = 1
rh_sum = 0
min_rh = 100
max_rh = 0

for row in csv.reader(forestfires):
    temp = float(row[8])
    if temp > max_temp:
        max_temp = temp
    if temp < min_temp:
        min_temp = temp
    temp_sum = temp_sum + temp       
    weekday = row[3]     
    if weekday == "mon":
        qty_mon = qty_mon + 1
    if weekday == "tue":
        qty_tue = qty_tue + 1
    if weekday == "wed":
        qty_wed = qty_wed + 1
    if weekday == "thu":
        qty_thu = qty_thu + 1
    if weekday == "fri":
        qty_fri = qty_fri + 1
    if weekday == "sat":
        qty_sat = qty_sat + 1
    if weekday == "sun":
        qty_sun = qty_sun + 1 
    rh = int(row[9])
    if rh > max_rh:
        max_rh = rh
    if rh < min_rh:
        min_rh = rh
    rh_sum = rh_sum + rh
    rows = rows + 1        

rh_average = rh_sum / rows
temp_average = temp_sum / rows
forestfires.close()      

print("Forest fires / week day")

print(f"Mon: {qty_mon}")
print(f"Tue: {qty_tue}")
print(f"Wed: {qty_wed}")
print(f"Thu: {qty_thu}")
print(f"Fri: {qty_fri}")
print(f"Sat: {qty_sat}")
print(f"Sun: {qty_sun}")
print()
print(f"Min temperature before fire: {min_temp} Celsius degrees")
print(f"Max temperature before fire: {max_temp} Celsius degrees")
print(f"Average temperature before fire: {round(temp_average,1)} Celsius degrees")
print()
print(f"Min relative humidity {min_rh} %")
print(f"Max relative humidity {max_rh} %")
print(f"Average relative humidity {int(rh_average)} %")

