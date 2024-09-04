# Sieb des Eratosthenes
import os
os.system("cls")

# Funktionen


# Initialisierung
trennzeichen = "#" * 20
checkNumber = int(input("Gib eine Zahl ein: "))
checkNumbers = list(range(4 , checkNumber + 1))
primeNumbers = [2, 3]

if "__main__" == __name__:
    print(trennzeichen *3 + "###")
    print(trennzeichen + " Sieb des Eratosthenes " + trennzeichen )
    print(trennzeichen *3 + "###")
    print()


    for number in checkNumbers:

        tempList = []
        for prime in primeNumbers:
            calc = number % prime
            tempList.append(calc)
        
        if not 0 in tempList:
            primeNumbers.append(number)
            
            
    if checkNumber in primeNumbers:
        print(f"{checkNumber} ist eine Primzahl")
    
    else:
        print(f"{checkNumber} ist KEINE Primzahl")