year = int (input("gebe hier das aktuelle jahr ein: "))

if (year % 400 == 0):
	print("dieses jahr ist ein schaltjahr")
elif(year % 4 == 0 and year % 100 != 0):
	print("dieses jahr ist ein schaltjahr")
else:
	print("dieses Jahr ist kein schaltjahr")
