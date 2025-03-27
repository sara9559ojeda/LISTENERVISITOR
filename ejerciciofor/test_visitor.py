from antlr4 import *
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser
from EvalVisitor import EvalVisitor

def test_visitor(input_code):
    print("\n🔍 Probando código con EvalVisitor...\n")
    
    # Crear el flujo de entrada
    input_stream = InputStream(input_code)
    lexer = MiGramaticaLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MiGramaticaParser(tokens)

    # Generar el árbol de sintaxis
    tree = parser.programa()

    # Ejecutar el Visitor
    visitor = EvalVisitor()
    resultado = visitor.visit(tree)

    print("\n📦 Variables al final:", resultado, visitor, tree)
    print("\n✅ Prueba finalizada.")

if __name__ == "__main__":
    test_code = "z = 0; for (i = 0; i < 3; i = i + 1) { z = z + 2; };"
    test_visitor(test_code)


