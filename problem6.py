

today = datetime.now().year
print(today)


age = raw_input(" whats your age ")
print(age)

retire = raw_input(" At what age would you like to retire ")
print(retire)

BestGuess = int(retire) - int(age)
print(" Yout have " + str(BestGuess) + " years left until you can retire ")

Result = today + BestGuess

print(" It is currently" + today +
      "you should be able to retire in " + str(Result))
