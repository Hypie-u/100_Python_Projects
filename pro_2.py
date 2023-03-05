print("total tip calculatur")
persons = int(input("how many people buy bill"))
viuw = float(input("total bill is how much"))
tip = int(input("how much tip woudl you like to 10,12,15?"))
billtip = (tip / 100 * viuw + viuw) / persons
print(f"totaly needes money {billtip}")
