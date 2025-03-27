from antlr4 import *
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser
from MyListener import MyListener
from antlr4.tree.Tree import ParseTreeWalker

def test_listener(input_code):
    # Crear el flujo de entrada
    input_stream = InputStream(input_code)
    lexer = MiGramaticaLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MiGramaticaParser(tokens)

    # Generar el árbol de sintaxis
    tree = parser.programa()

    # Ejecutar el Listener
    walker = ParseTreeWalker()
    listener = MyListener()
    walker.walk(listener, tree)
if __name__ == "__main__":  # <- Corregido el error en "_main"
    test_code = "for (i = 0; i < 10; i = i + 1) { x = x + 1; }"
    print("Probando código con test_listener...")
    test_listener(test_code)
    print("Prueba finalizada.")