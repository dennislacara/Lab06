import flet as ft
from UI.view import View
from model.model import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view
        self.listaAuto = []
        self.listaAutoxModello = []

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value # uso il setter del responsabile
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.input_responsabile.value = '' # pulisco il campo di scrittura del responsabile
        self._view.update()

    # Altre Funzioni Event Handler
    def lista_automobili(self, e):
        self.listaAuto = Autonoleggio.get_automobili(self._model)
        self._view.aggiornaListaAuto(self.listaAuto)

    def cerca(self, modello):
        self.listaAutoxModello = Autonoleggio.cerca_automobili_per_modello(self._model, modello)
        self._view.aggiornaListaxModello(self.listaAutoxModello)
    # TODO
