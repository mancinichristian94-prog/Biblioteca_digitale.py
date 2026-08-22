"""
Progetto: Gestione Biblioteca Digitale
Sistema per gestire libri, utenti e prestiti.

"""
 
# =========================================================
# PARTE 1 - Variabili e tipi di dati
# =========================================================
 
titolo = "Il Signore degli Anelli"      # stringa
copie = 5                                # intero
prezzo_medio = 19.90                     # float
disponibile = True                       # booleano
 
print("=== PARTE 1: Variabili e tipi di dati ===")
print(f"Titolo: {titolo} (tipo: {type(titolo).__name__})")
print(f"Copie disponibili: {copie} (tipo: {type(copie).__name__})")
print(f"Prezzo medio: {prezzo_medio} EUR (tipo: {type(prezzo_medio).__name__})")
print(f"Disponibile: {disponibile} (tipo: {type(disponibile).__name__})")
print()
 
 
# =========================================================
# PARTE 2 - Strutture dati
# =========================================================
 
# Lista di titoli
titoli_libri = [
    "Il Signore degli Anelli",
    "1984",
    "Il Nome della Rosa",
    "Fahrenheit 451",
    "Cronache del Ghiaccio e del Fuoco"
]
 
# Dizionario titolo -> copie disponibili
copie_disponibili = {
    "Il Signore degli Anelli": 5,
    "1984": 3,
    "Il Nome della Rosa": 2,
    "Fahrenheit 451": 4,
    "Cronache del Ghiaccio e del Fuoco": 1
}
 
# Set di utenti registrati
utenti_registrati = {"Mario Rossi", "Luca Bianchi", "Anna Verdi"}
 
print("=== PARTE 2: Strutture dati ===")
print("Lista titoli:", titoli_libri)
print("Dizionario copie disponibili:", copie_disponibili)
print("Set utenti registrati:", utenti_registrati)
print()
 
 
# =========================================================
# PARTE 3 - Classi e OOP
# =========================================================
 
class Libro:
    def __init__(self, titolo, autore, anno, copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili
 
    def info(self):
        return (f"'{self.titolo}' di {self.autore} ({self.anno}) "
                f"- Copie disponibili: {self.copie_disponibili}")
 
 
class Utente:
    def __init__(self, nome, eta, id_utente):
        self.nome = nome
        self.eta = eta
        self.id_utente = id_utente
 
    def scheda(self):
        print(f"ID Utente: {self.id_utente} | Nome: {self.nome} | Età: {self.eta}")
 
 
class Prestito:
    def __init__(self, utente, libro, giorni):
        self.utente = utente
        self.libro = libro
        self.giorni = giorni
 
    def dettagli(self):
        print("--- Dettagli Prestito ---")
        print(f"Utente: {self.utente.nome} (ID: {self.utente.id_utente})")
        print(f"Libro: {self.libro.titolo} di {self.libro.autore}")
        print(f"Durata prestito: {self.giorni} giorni")
        print(f"Copie rimanenti dopo il prestito: {self.libro.copie_disponibili}")
        print("-------------------------")
 
 
# =========================================================
# PARTE 4 - Funzionalità
# =========================================================
 
def presta_libro(utente, libro, giorni):
    """
    Verifica la disponibilità del libro:
    - se disponibile, riduce le copie e crea un oggetto Prestito
    - altrimenti stampa un messaggio di errore
    """
    if libro.copie_disponibili >= 1:
        libro.copie_disponibili -= 1
        nuovo_prestito = Prestito(utente, libro, giorni)
        print(f"Prestito effettuato: '{libro.titolo}' a {utente.nome} per {giorni} giorni.")
        return nuovo_prestito
    else:
        print(f"ERRORE: nessuna copia disponibile per '{libro.titolo}'.")
        return None
 
 
if __name__ == "__main__":
    print("=== PARTE 3 e 4: Classi, OOP e Funzionalità ===\n")
 
    # Creazione oggetti Libro
    libro1 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1954, 5)
    libro2 = Libro("1984", "George Orwell", 1949, 3)
    libro3 = Libro("Il Nome della Rosa", "Umberto Eco", 1980, 1)
 
    # Creazione oggetti Utente
    utente1 = Utente("Mario Rossi", 28, "U001")
    utente2 = Utente("Luca Bianchi", 34, "U002")
    utente3 = Utente("Anna Verdi", 22, "U003")
 
    print("Schede utenti registrati:")
    utente1.scheda()
    utente2.scheda()
    utente3.scheda()
    print()
 
    print("Informazioni libri (prima dei prestiti):")
    for l in (libro1, libro2, libro3):
        print(l.info())
    print()
 
    # Simulazione di almeno 3 prestiti
    print("Simulazione prestiti:")
    prestiti = []
    prestiti.append(presta_libro(utente1, libro1, 14))
    prestiti.append(presta_libro(utente2, libro2, 7))
    prestiti.append(presta_libro(utente3, libro3, 10))
    # Quarto tentativo per testare il caso "nessuna copia disponibile"
    prestiti.append(presta_libro(utente1, libro3, 5))
    print()
 
    # Elenco aggiornato delle copie disponibili
    print("Elenco aggiornato copie disponibili:")
    for l in (libro1, libro2, libro3):
        print(f"- {l.titolo}: {l.copie_disponibili} copie")
    print()
 
    # Dettagli di ogni prestito effettuato
    print("Dettagli di tutti i prestiti effettuati:")
    for p in prestiti:
        if p is not None:
            p.dettagli()