grammar MiGramatica;

// Regla principal: permite múltiples sentencias terminadas en ';'
programa: (sentencia ';')+ EOF ;

// Sentencias permitidas
sentencia
    : forStmt
    | asignacion  
    ;

// Regla para for
forStmt
    : 'for' '(' inicializacion ';' condicion ';' actualizacion ')' bloque # ForLoop
    ;

// Bloque de sentencias dentro del for
bloque
    : '{' (sentencia ';')* '}'
    ;

// Inicialización del for (Ej: i = 0)
inicializacion
    : ID '=' expresion 
    ;

// Condiciones dentro del for (Ej: i < 10)
condicion
    : ID op=('>' | '<' | '==' | '!=') INT  
    ;

// Actualización del for (Ej: i = i + 1)
actualizacion
    : ID '=' expresion 
    ;

// Asignaciones con ;
asignacion
    : ID '=' expresion 
    ;

// Expresiones matemáticas con prioridad de operadores
expresion
    : expresion op=('*'|'/') expresion     # MulDiv
    | expresion op=('+'|'-') expresion     # AddSub
    | INT                                  # Int
    | ID                                   # Variable
    | '(' expresion ')'                    # Parens
    ;

// Reglas léxicas
ID  : [a-zA-Z_][a-zA-Z_0-9]* ;  // Identificadores
INT : [0-9]+ ;                   // Números enteros
WS  : [ \t\r\n]+ -> skip ;       // Ignorar espacios en blanco