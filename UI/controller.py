import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        anno = int(self._view._txtAnno.value)
        if anno < 1816 or anno > 2016:
            self._view._txt_result.controls.clear()
            self._view.create_alert("Attenzione, anno non valido!")
            self._view.update_page()
            return


        self._model.buildGraph(anno)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text("Grafo creato correttamente."))
        self._view._ddStato.disabled = False
        self._view._btnStatiRagg.disabled = False
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.getInfoConn()} componenti connesse."))
        self._view.update_page()

        for c in self._model.getInfoNodi():
            self._view._txt_result.controls.append(ft.Text(f"{c[0]} -- {c[1]} vicini"))
            self._view.update_page()

    def fillStato(self):
        stati = self._model.getStati()
        for s in stati:
            self._view._ddStato.options.append(ft.dropdown.Option(s))
            self._view.update_page()

    def handleStatiRagg(self, e):
        stato = self._view._ddStato.value

        if stato is None:
            self._view._txt_result.controls.clear()
            self._view.create_alert("Attenzione, inserire uno stato!")
            self._view.update_page()
            return

        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Gli Stati raggiungibili da {stato} sono:"))

        statiRagg = self._model.getDFSNodesFromEdges(stato)

        for sr in statiRagg:
            self._view._txt_result.controls.append(ft.Text(f"{sr}"))
            self._view.update_page()









