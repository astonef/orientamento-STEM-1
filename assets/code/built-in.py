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