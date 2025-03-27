grammar MiGramatica;

programa
    : (sentencia ';')+ EOF
    ;

sentencia
    : forStmt
    | asignacion
    ;

forStmt
    : 'for' '(' inicializacion ';' condicion ';' actualizacion ')' (bloque | sentencia) # ForLoop
    ;


bloque
    : '{' (sentencia ';')* '}'
    | sentencia
    ;

inicializacion
    : ID '=' expresion
    ;

condicion
    : expresion op=('>' | '<' | '==' | '!=') expresion
    ;

actualizacion
    : ID '=' expresion
    ;

asignacion
    : ID '=' expresion
    ;

expresion
    : expresion op=('*'|'/') expresion     # MulDiv
    | expresion op=('+'|'-') expresion     # AddSub
    | INT                                  # Int
    | ID                                   # Variable
    | '(' expresion ')'                    # Parens
    ;

ID  : [a-zA-Z_][a-zA-Z_0-9]* ;
INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;
