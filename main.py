# from src.crew_inserimento.inserimento_crew import InserimentoCrew
# from src.crew_cancellazione.cancellazione_crew import CancellazioneCrew
# from crewai.flow import Flow, start, listen, router
# from models.models import DatiInserimento, DatiCancellazione, WeflaiState

# #config. Flow
# class WeflaiFlow(Flow[WeflaiState]):
    
#     @start()
#     def utente_sceglie(self):
#         self.state.scelta = input(f'''🛫🛩️🚁🛬✈️🛬🚁🛩️🛫
# Sono WEFLAI, quello che se non azzecchi la query non ci vAI!
# 🛫🛩️🚁🛬✈️🛬🚁🛩️🛫

# VUOI PRENOTARE O CANCELLARE UN VOLO?
# 1. PRENOTARE
# 2.CANCELLARE\n\n
# ''')

#         if self.state.scelta == '1':
#             nome= input("Inserisci il nome: ")
#             cognome= input("Inserisci il cognome: ")
#             email= input("Inserisci l'email: ")
#             citta_partenza= input("Inserisci la citta di partenza: ")
#             citta_arrivo= input("Inserisci la citta di arrivo: ")
#             data_partenza= input("Inserisci la data di partenza: ")
#             numero_documento= input("Inserisci il numero del documento: ")
#             # print("\nFormato richiesto: Nome, Cognome, Email, Citta Partenza, Citta Arrivo, Data Partenza, Numero Documento")
#             # self.state.query_utente = input("Inserisci i dati separati dalla virgola: ")

#             self.state.dati_inserimento = DatiInserimento(
#                 nome_utente=nome,
#                 cognome_utente=cognome,
#                 email_utente=email,
#                 citta_partenza=citta_partenza,
#                 citta_arrivo=citta_arrivo,
#                 data_partenza=data_partenza,
#                 numero_documento=numero_documento
#             )
#             # parti = self.state.query_utente.split(',')
#             # if len(parti) != 7:
#             #     print("ERRORE: Hai inserito pochi dati")
#             #     self.state.scelta = "Errore"
#             # else:
#                 # self.state.dati_inserimento = DatiInserimento(
#                 #     #nome=parti[0].strip(),
#                 #     nome=nome,
#                 #     cognome=parti[1].strip(),
#                 #     email=parti[2].strip(),
#                 #     citta_partenza=parti[3].strip(),
#                 #     citta_arrivo=parti[4].strip(),
#                 #     data_partenza=parti[5].strip(),
#                 #     numero_documento=parti[6].strip()
#                 # )
            
#         elif self.state.scelta == '2':
#             nome= input("Inserisci il nome: ")
#             cognome= input("Inserisci il cognome: ")
#             email= input("Inserisci l'email: ")
#             citta_partenza= input("Inserisci la citta di partenza: ")
#             citta_arrivo= input("Inserisci la citta di arrivo: ")
#             data_partenza= input("Inserisci la data di partenza: ")
#             numero_documento= input("Inserisci il numero del documento: ")
#             # print("\nFormato richiesto: Nome, Cognome, Email, Citta Partenza, Citta Arrivo, Data Partenza, Numero Documento")
#             # self.state.query_utente = input("Inserisci i dati separati dalla virgola: ")

#             self.state.dati_inserimento = DatiCancellazione(
#                 id_prenotazione
#                 nome_utente=nome,
#                 cognome_utente=cognome,
#             )
#                 # print("\nFormato richiesto: ID Prenotazione, Nome, Cognome")
#                 # self.state.query_utente = input("Inserisci i dati separati dalla virgola: ")
                
#                 # parti = self.state.query_utente.split(',')
#                 # if len(parti) < 3:
#                 #      print("ERRORE: Hai inserito pochi dati")
#                 #      self.state.scelta = "Errore"
#                 # else:
#                 #     self.state.dati_cancellazione = DatiCancellazione(
#                 #         id_prenotazione=int(parti[0].strip()), # Converto in int
#                 #         nome_utente=parti[1].strip(),
#                 #         cognome_utente=parti[2].strip()
#                 #     )
        
#         #return self.state.scelta

#     #smisto
#     @router(utente_sceglie)
#     def smistaments(self):
#         if self.state.scelta == '1':
#             return "percorso_prenotazione"
#         elif self.state.scelta == '2':
#             return "percorso_cancellazione"
#         else:
#             return "percorso_errore"


#     # @listen('percorso_prenotazione')
#     # def percorso_prenotazione(self):
#     #     inputs = self.state.dati_inserimento.model_dump()
#     #     result = InserimentoCrew().crew().kickoff(inputs=inputs)
#     #     print('PROCESSO COMPLETATO')
#     #     return result
#     @listen('percorso_prenotazione')
#     def percorso_prenotazione(self):
#         inputs = self.state.dati_inserimento.model_dump()
#         #print(f'PRINT DELL\'INPUTS (self.state.dati_inserimento.model_dump():\n{inputs}')
#         #inputs['query_utente'] = self.state.query_utente
#         #print(f'PRINT DELL\'INPUTS (self.state.query_utente):\n{inputs['query_utente']}')
#         result = InserimentoCrew().crew().kickoff(inputs=inputs)
#         print(inputs)
#         #return result

#     @listen('percorso_cancellazione')
#     def percorso_cancellazione(self):
#         inputs = self.state.dati_cancellazione.model_dump()
#         result = CancellazioneCrew().crew().kickoff(inputs=inputs)
#         print('PROCESSO PARTITO')
#         return result

#     @listen('percorso_errore')
#     def gestione_errore(self):
#         print('ERRORE')
#         return 'Errore'

# #DALL
# if __name__ == '__main__':
#     WeflaiFlow().kickoff()


# '''PER FRANCO IL MALATINO MONELLINO'''
# # Riassunto del Flusso Dati:

# # L'utente scrive stringa e ilFlow (main.py) la passa in DatiInserimento() o DatiCancellazione() (Pydantic).

# # Flow usa .model_dump() e trasforma il pydantic in un Dizionario Python.

# # CrewAI .kickoff() prende il dizionario e tramite le chiavi utilizza direttamente i valori nel file YAML ({valore}).

# # In questo modo gli agenti eseguono il lavoro con dati precisi e si riduce sensibilmente la possibilità di minchiate.

# # Fino a ritornarci il risultato imposta in base alla diversa crew utilizzata.

from src.crew_inserimento.inserimento_crew import InserimentoCrew
from src.crew_cancellazione.cancellazione_crew import CancellazioneCrew
from crewai.flow import Flow, start, listen, router
from models.models import DatiInserimento, DatiCancellazione, WeflaiState

class WeflaiFlow(Flow[WeflaiState]):
    
    @start()
    def utente_sceglie(self):
        self.state.scelta = input(f'''🛫🛩️🚁🛬✈️🛬🚁🛩️🛫
  Sono WEFLAI.
  VUOI PRENOTARE O CANCELLARE UN VOLO?
  1. PRENOTARE
  2. CANCELLARE\n\n''')

        if self.state.scelta == '1':
            print("--- INSERIMENTO DATI PRENOTAZIONE ---")
            self.state.dati_inserimento = DatiInserimento(
                nome_utente=input("Inserisci il nome: "),
                cognome_utente=input("Inserisci il cognome: "),
                email_utente=input("Inserisci l'email: "),
                citta_partenza=input("Inserisci la citta di partenza: "),
                citta_arrivo=input("Inserisci la citta di arrivo: "),
                data_partenza=input("Inserisci la data di partenza (YYYY-MM-DD): "),
                numero_documento=input("Inserisci il numero del documento: ")
            )
            
        elif self.state.scelta == '2':
            print("--- INSERIMENTO DATI CANCELLAZIONE ---")
            # Richiediamo l'ID, se l'utente non lo sa, lascia vuoto
            id_input = input("Inserisci ID Prenotazione (premi invio se non lo sai): ")
            id_valido = int(id_input) if id_input.isdigit() else None
            
            self.state.dati_cancellazione = DatiCancellazione(
                id_prenotazione=id_valido,
                nome_utente=input("Inserisci il nome: "),
                cognome_utente=input("Inserisci il cognome: ")
            )

    @router(utente_sceglie)
    def smistaments(self):
        if self.state.scelta == '1':
            return "percorso_prenotazione"
        elif self.state.scelta == '2':
            return "percorso_cancellazione"
        else:
            return "percorso_errore"

    @listen('percorso_prenotazione')
    def esegui_prenotazione(self):
        # Trasformiamo il Pydantic in dict per passarlo a CrewAI
        inputs = self.state.dati_inserimento.model_dump()
        print(f"DEBUG INPUTS: {inputs}") 
        # Kickoff con i dati specifici
        result = InserimentoCrew().crew().kickoff(inputs=inputs)
        print('\n--- BIGLIETTO GENERATO ---\n')
        print(result)
        # Salva il risultato nello state e termina
        self.state.response_finale = str(result)
        print("\n✅ OPERAZIONE COMPLETATA. Il programma termina.")
        return "completato"

    @listen('percorso_cancellazione')
    def esegui_cancellazione(self):
        inputs = self.state.dati_cancellazione.model_dump()
        print(f"DEBUG INPUTS: {inputs}")
        result = CancellazioneCrew().crew().kickoff(inputs=inputs)
        print('\n--- ESITO CANCELLAZIONE ---\n')
        print(result)
        # Salva il risultato nello state e termina
        self.state.response_finale = str(result)
        print("\n✅ OPERAZIONE COMPLETATA. Il programma termina.")
        return "completato"

    @listen('percorso_errore')
    def gestione_errore(self):
        print('Scelta non valida.')

if __name__ == '__main__':
    flow = WeflaiFlow()
    flow.kickoff()