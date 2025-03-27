from MiGramaticaVisitor import MiGramaticaVisitor

class EvalVisitor(MiGramaticaVisitor):
    def __init__(self):
        self.variables = {}

    def visitPrograma(self, ctx):
        """Visita todas las sentencias del programa"""
        for sentencia in ctx.sentencia():
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

    def visitAddSub(self, ctx):
        """Manejo de suma y resta"""
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        return left + right if ctx.op.text == '+' else left - right

    def visitMulDiv(self, ctx):
        """Manejo de multiplicación y división entera"""
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        return left * right if ctx.op.text == '*' else left // right  

    def visitParens(self, ctx):
        """Manejo de paréntesis"""
        return self.visit(ctx.expresion())

    def visitForStmt(self, ctx):
        """Manejo del bucle for"""
        print("\n🔄 Iniciando FOR...")

        # Ejecutar inicialización del for
        self.visit(ctx.inicializacion())
        print(f"📌 Inicialización: i = {self.variables.get('i', 0)}")

        # Evaluar condición y ejecutar bloque
        while self.visit(ctx.condicion()):
            print(f"🔍 Iteración: i = {self.variables.get('i', 0)}, x = {self.variables.get('x', 0)}")

            # Ejecutar sentencias dentro del bloque
            for stmt in ctx.bloque().sentencia():
                self.visit(stmt)

            # Ejecutar la actualización
            self.visit(ctx.actualizacion())
            print(f"📊 Después de actualización: i = {self.variables['i']}, x = {self.variables['x']}")

        print("🛑 Fin del FOR\n")

    def visitCondicionSimple(self, ctx):
        """Evaluación de la condición del for"""
        var = ctx.ID().getText()
        value = self.variables.get(var, 0)
        cmp_value = int(ctx.INT().getText())
        op = ctx.op.text

        resultado = False
        if op == '>':
            resultado = value > cmp_value
        elif op == '<':
            resultado = value < cmp_value
        elif op == '==':
            resultado = value == cmp_value
        elif op == '!=':
            resultado = value != cmp_value

        print(f"🔎 Evaluando condición: {var} {op} {cmp_value} → {resultado}")
        return resultado
