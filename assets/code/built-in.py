# Sezione: Operazioni di base e stampa [1-3]
# 1 - Stampa "Hello, World!" nella console
'''
print('Hello, World!)
'''
# 2 - Assegna una variabile
'''
x = 'Hello, World!'
'''
# 3 - Stampa la variabile
'''
x = 'Hello, World!'
print(x)
'''
# Sezione: Condizioni e logica [4]
# 4 - Usa implicazione logica per stampare in console
'''
x = 2

if x > 3:
  print(x)
else:  
  print ("Hello, World!")
'''
# Sezione: Funzioni di base [5,6]
# 5 - Crea una funzione
'''
def saluto(nome):
    print("Hello, " + nome + "!")
    
saluto("Agata")
'''

# 6 - Crea una funzione con ritorno di valore

'''
def somma (a, b):
    return a + b

risultato = somma(4,6)

print(risultato)
'''
# Sezione: Parametri opzionali e argomenti variabili [7,8]
# 7 - Crea una funzione con variabile opzionale
'''
def saluto_opzionale(nome, messaggio = "Ciao"):
    print(f"{messaggio}, {nome}!")

saluto_opzionale("Marco")
saluto_opzionale("Andrea", "Salve")
'''
#8 - Crea una funzione con argomenti variabili
'''
def esplora(*luoghi):
  for luogo in luoghi:
    print(f"Agata visita prima {luogo}. Poi si dirige verso {luogo}. Infine va verso {luogo}")
   

esplora('la scogliera', 'la barriera corallina', 'una nuova spiaggia')
'''
# Sezione: Selezione e combinazione di elementi [9,10]
#9 - Funzione con selezione di elementi ordinati
'''
def esplora_uno(*luoghi):
  primo_luogo = luoghi[0]
  print(f"Agata visita prima {primo_luogo}. Poi si dirige verso {primo_luogo}. Infine va verso {primo_luogo}.")

esplora_uno('la scogliera', 'la barriera corallina', 'una nuova spiaggia')      
'''

# 10 - Funzione con combinazione di elementi 
'''
def esplora(*luoghi):
    print(f"Agata visita prima {luoghi[0]}. Poi si dirige verso {luoghi[1]}. Infine va verso {luoghi[2]}.")

esplora('la scogliera', 'la barriera corallina', 'una nuova spiaggia')
'''
#Sezione: Iterazione e parola chiave
#11 - Funzione con iterazione sugli elementi
'''
def esplora(*luoghi):
    print("Agata esplora i seguenti luoghi:")
    for luogo in luoghi:
        print(luogo)

esplora('la scogliera', 'la barriera corallina', 'una nuova spiaggia')
'''

#12 - Funzione con argomenti di parola chiave (**kwargs)
'''
def esplora_con_dettagli(**dettagli):
    for luogo, descrizione in dettagli.items():
        print(f"Agata visita {luogo}: {descrizione}")

esplora_con_dettagli(
    Napoli="una scogliera ripida e rocciosa",
    Corallolandia="una barriera piena di coralli colorati",
    Ostia="una spiaggia con sabbia finissima"
)
'''

# Tipi di dati e operatori aritmetici

'''
# Tipi di dati
eta = 15  # int
altezza = 1.65  # float
nome = "Stefano"  # string
is_student = True  # boolean

# Stampa delle variabili
print("Età:", eta)
print("Altezza:", altezza)
print("Nome:", nome)
print("Sei uno studente?", is_student)

# Operazioni aritmetiche
somma = eta + 5
print("Somma dell'età e 5:", somma)

moltiplicazione = altezza * 2
print("Il doppio dell'altezza:", moltiplicazione)

sottrazione = eta - 3
print("Età meno 3:", sottrazione)

divisione = altezza / 2
print("Altezza divisa per 2:", divisione)
'''

# Liste, Tuple, Dizionari
'''
# Liste
frutti = ["mela", "banana", "ciliegia"]
frutti.append("arancia")  # Aggiungi un frutto
frutti.remove("banana")  # Rimuovi un frutto
print("Lista aggiornata dei frutti:", frutti)

# Tuple
colori = ("rosso", "verde", "blu")
print("Colori nella tupla:", colori)

# Dizionari
studenti = {"Luca": 14, "Marta": 15}
studenti["Giulia"] = 16  # Aggiungi uno studente
studenti["Luca"] = 15  # Modifica l'età di uno studente
print("Dizionario aggiornato degli studenti:", studenti)

'''

# Cicli for e while
'''
# Ciclo for su una lista
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeri:
    print("Numero:", numero)

# Contare numeri maggiori di 10
numeri_grandi = [3, 8, 15, 1, 22, 9]
count = 0
for numero in numeri_grandi:
    if numero > 10:
        count += 1
print("Numeri maggiori di 10:", count)

# Ciclo while per cercare un nome
nomi = ["Anna", "Marco", "Luca", "Sara"]
index = 0
while index < len(nomi):
    if nomi[index] == "Luca":
        print("Nome trovato:", nomi[index])
        break
    index += 1
'''

# Input dall'utente
'''
# 1. Chiedi il nome all'utente
nome = input("Inserisci il tuo nome: ")
print(f"Benvenuto, {nome}!")

# 2. Calcolatore interattivo
numero1 = int(input("Inserisci il primo numero: "))
numero2 = int(input("Inserisci il secondo numero: "))
somma = numero1 + numero2
print(f"La somma di {numero1} e {numero2} è: {somma}")

# 3. Gioco del numero segreto
numero_segreto = 7
tentativo = int(input("Indovina il numero segreto (tra 1 e 10): "))

if tentativo == numero_segreto:
    print("Complimenti! Hai indovinato il numero segreto!")
else:
    print("Spiacente, il numero è sbagliato. Riprova!")

'''