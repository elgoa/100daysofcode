Bill_without_tip = int(input("Geben sie hier den vollständigen Rechnungsbetrag an: €"))
number_of_people = int(input("Geben sie hier an wieviele Personen sich die Rechnung teilen: "))
Bill_one_person = Bill_without_tip / number_of_people
print(Bill_one_person)
Tip_valid = False
while Tip_valid is False:
	Tip = int(input("Geben sie hier an ob sie 10, 12 oder 15 % Trinkgeld geben wolle: %"))
	if Tip not in (10, 12, 15):
		print ("Trinkgeld nicht gültig")
	else:
		Tip_valid = True
Tip = Bill_one_person * (Tip / 100)
print(Tip)
One_person_pay = Bill_one_person + Tip
print (f"Jede Person muss {One_person_pay}€ bezahlen")

