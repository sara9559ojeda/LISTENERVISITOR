from MiGramaticaListener import MiGramaticaListener

class MyListener(MiGramaticaListener):
    def exitForLoop(self, ctx):
        print(" Se detectó un ciclo FOR")
        print(f"  - Inicialización: {ctx.inicializacion().getText()}")
        print(f"  - Condición: {ctx.condicion().getText()}")
        print(f"  - Actualización: {ctx.actualizacion().getText()}")

    def exitAsignacion(self, ctx):
        print(" Asignación detectada:", ctx.getText())

    def exitCondicion(self, ctx):
        print("Condición detectada:", ctx.ID().getText(), ctx.op.text, ctx.INT().getText())