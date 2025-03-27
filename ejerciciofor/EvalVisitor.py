from MiGramaticaVisitor import MiGramaticaVisitor

class EvalVisitor(MiGramaticaVisitor):
    def __init__(self):
        self.variables = {}

    def visitPrograma(self, ctx):
        """Visita todas las sentencias del programa"""
        for sentencia in ctx.sentencia():
            print(f"➡️ Visitando sentencia: {sentencia.getText()}")
            self.visit(sentencia)
        return self.variables

    def visitAssign(self, ctx):
        """Manejo de asignaciones"""
        var = ctx.ID().getText()
        value = self.visit(ctx.expresion())
        self.variables[var] = value
        print(f"📝 Asignación: {var} = {value}")
        return value

    def visitInt(self, ctx):
        """Retorna un número entero"""
        return int(ctx.getText())

    def visitVariable(self, ctx):
        """Manejo de variables, asumiendo 0 si no están inicializadas"""
        var = ctx.getText()
        if var not in self.variables:
            print(f"⚠️ Variable '{var}' no inicializada. Se asume 0.")
            self.variables[var] = 0  # Asignación predeterminada
        return self.variables[var]

    def visitForStmt(self, ctx):
        """Manejo del bucle for"""
        print("\n🔄 Iniciando FOR...")

    # Ejecutar inicialización del for
        self.visit(ctx.inicializacion())
        print(f"📌 Inicialización: i = {self.variables.get('i', 0)}")

    # Evaluar condición y ejecutar bloque
        while self.visit(ctx.condicion()):
            print(f"🔍 Iteración: i = {self.variables.get('i', 0)}, z = {self.variables.get('z', 0)}")

        # ✅ Ejecutar el bloque del for
            if ctx.bloque():
                for stmt in ctx.bloque().sentencia():
                    print(f"▶️ Ejecutando sentencia en bloque: {stmt.getText()}")
                    self.visit(stmt)
            elif ctx.sentencia():
                print(f"▶️ Ejecutando sentencia única: {ctx.sentencia().getText()}")
                self.visit(ctx.sentencia())

        # ✅ Ejecutar la actualización
            print(f"🛠️ Ejecutando actualización: {ctx.actualizacion().getText()}")
            self.visit(ctx.actualizacion())

            print(f"📊 Después de actualización: i = {self.variables['i']}, z = {self.variables['z']}")

        print("🛑 Fin del FOR\n")

