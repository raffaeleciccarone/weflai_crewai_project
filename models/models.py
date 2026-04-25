from pydantic import BaseModel
from typing import Optional

#config. pydantic
#ricordati di aggiungere option che poi rincoglionisce
class DatiInserimento(BaseModel):
    nome_utente: Optional[str] = None
    cognome_utente: Optional[str] = None
    email_utente: Optional[str] = None
    citta_partenza: Optional[str] = None
    citta_arrivo: Optional[str] = None
    data_partenza: Optional[str] = None
    numero_documento: Optional[str] = None  
    
class DatiCancellazione(BaseModel):
    id_prenotazione: Optional[int] = None
    nome_utente: Optional[str] = None
    cognome_utente: Optional[str] = None

class WeflaiState(BaseModel):
    scelta:str = ''
    query_utente:str = ''
    response_finale:str = ''
    dati_inserimento:Optional[DatiInserimento] = None
    dati_cancellazione:Optional[DatiCancellazione] = None

#formattazione output
class TicketOutput(BaseModel):
    id_prenotazione:int = 0
    id_volo:int = 0
    numero_documento:str = ''
    nome_utente:str = ''
    cognome_utente:str = ''
    email_utente:str = ''