def es_palindromo(x):
    s = x [::-1]
    return (x == s)

palabra = input ("Ingrese una palabra:  ")
QPalindromos = 0
QNoPalindromos = 0
while palabra != "bye":
    if es_palindromo(palabra):
        print ("La palabra ", palabra," es un palindromo")
        QPalindromos = QPalindromos + 1
    else:
        print ("La palabra ", palabra, "no es un palindromo")
        QNoPalindromos = QNoPalindromos + 1
    palabra = input ("Ingrese una palabra:  ")

print("saliste del ciclo")
print("Total Palindromos", QPalindromos)
print("Total No Palindromos", QNoPalindromos)

