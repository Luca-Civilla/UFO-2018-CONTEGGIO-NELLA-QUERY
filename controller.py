import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model



    def handle_graph(self, e):
        try:
            int(self._view._txtAnno.value)
            int(self._view._txtGiorni.value)
        except ValueError:
            return self._view.create_alert("ERRORE VALORI NON NUMERICI")
        anno = int(self._view._txtAnno.value)
        giorni = int(self._view._txtGiorni.value)
        if anno<1906 or anno> 2014:
            return self._view.create_alert("ERRORE ANNO NON IDONEO, VALORI COMPRESI TRA 1906 E 2014")
        if giorni<1 or giorni>180:
            return self._view.create_alert("ERRORE NUMRO GIORNI NON IDONEO, VALORI COMPRESI TRA 1 E 180")

        self._model.buildGraph(anno,giorni)
        nodi,archi = self._model.graphDetails()

        self._view.txt_result.controls.append(ft.Text(f"GRAFO CREATO CORRETTAMENTE CON {nodi} NODI E {archi} ARCHI"))
        lista = self._model.sommaPesiArchi()
        for ee in lista:
            self._view.txt_result.controls.append(ft.Text(f"{ee[0].Name}--con somma {ee[1]}"))

        self._view.update_page()