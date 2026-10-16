from strumento import Strumento
from operator import attrgetter
from prestito import Prestito

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self._nome = nome
        self._responsabile = responsabile
        self.strumenti = []
        self.prestiti = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        with open(file_path, "r") as infile:
            lines = infile.readlines()
            for line in lines:
                word = line.strip().split(",")
                codice = word[0]
                tipo = word[1]
                marca = word[2]
                anno_acquisto = int(word[3])
                valore = float(word[4])
                strumento = Strumento(codice, tipo, marca, anno_acquisto, valore)
                self.strumenti.append(strumento)


    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        n = len(self.strumenti) +1
        codice = f"S{str(n)}"
        strumento = Strumento(codice, tipo, marca, anno_acquisto, valore)
        self.strumenti.append(strumento)
        return strumento

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        self.strumenti.sort(key=attrgetter("marca"))
        return self.strumenti

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        strumento_trovato = None
        for strumento in self.strumenti:
            if id_strumento == strumento.codice:
                strumento_trovato = strumento
        if strumento_trovato is None:
            raise Exception(f"Lo strumento {id_strumento} non è presente nel sistema")

        for p in self.prestiti:
            if id_strumento == p.id_strumento:
                raise Exception(f"Lo strumento {id_strumento} è già in prestito")

        n = len(self.prestiti) + 1
        id_prestito = f"P{n}"
        prestito = Prestito(id_prestito, data, id_strumento, cognome_allievo)
        self.prestiti.append(prestito)
        return prestito


    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        for p in self.prestiti:
            if id_prestito == p.id_prestito:
                self.prestiti.remove(p)
                return
        raise Exception(f"Il prestito {id_prestito} non esiste")
