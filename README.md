# WEFLAI 🛫

**WEFLAI** è un sistema basato su intelligenza artificiale (costruito con **CrewAI**) che permette agli utenti di interagire con un database aeroportuale tramite un flusso conversazionale.

Il progetto utilizza agenti autonomi per gestire due operazioni principali:
1. **Prenotazione Voli (`InserimentoCrew`)**: Cerca i voli disponibili nel database PostgreSQL e inserisce la prenotazione, generando infine un biglietto in formato JSON.
2. **Cancellazione Voli (`CancellazioneCrew`)**: Ricerca e identifica in modo sicuro le prenotazioni esistenti (tramite ID o nome/cognome) ed esegue la cancellazione dal database.

### Caratteristiche
- Utilizza **CrewAI Flows** per gestire lo smistamento delle scelte dell'utente.
- Interagisce direttamente con il database tramite tool SQL customizzati.
- Validazione e gestione dello stato tramite **Pydantic**.

### Come avviarlo
1. Assicurati di avere un database PostgreSQL attivo e configurato.
2. Crea un file `.env` e inserisci le tue chiavi (es. `OLLAMA_API_KEY`).
3. Installa le dipendenze: `pip install -r requirements.txt`
4. Avvia il programma: `python main.py`
