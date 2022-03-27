grammar SCV;

// Tokens

// Reserved Keywords
FUNCTION   : 'function';
RETURN  : 'return';
IF      : 'if';
ELSE    : 'else';
LOOP    : 'loop';
BREAK   : 'break';
AND     : 'and';
OR      : 'or';
NOT     : 'not';
VAR     : 'var';
INT     : 'int';
FLOAT   : 'float';
BEGIN   : 'begin';
END     : 'end';
FOR     : 'for';
WHILE   : 'while';
REVERSE : 'reverse';
EXIT    : 'exit';
THEN    : 'then';
IS      : 'is';
IN      : 'in';


EXPRESSION : 'expression';

// Built-in procedures
PRINT : 'print';
READ    : 'read';


SQRT    : 'sqrt';
POW     : 'pow';
LOG     : 'log';
MOD     : 'mod';
ABS     : 'abs';


// Literals
fragment DIGIT  : [0-9];
fragment DIGITS : DIGIT+;
fragment LETTER : [A-Za-z]+;
fragment SIGN   : '-';

CTE_INT     : SIGN? DIGITS;
CTE_FLOAT   : SIGN? DIGITS ('.' DIGITS)?;
ID          : LETTER (LETTER | DIGIT | '_')*;
WS          : [ \n\t\r] -> skip;
COMMENT     : '#|' .*? '|#' -> skip;

// Syntax

program     : vars_decl funcs_decl;

vars_decl   : var_decl vars_decl
            | ;

var_decl    : ID ':' data_type value_init ';';

value_init  : ':=' value_literal
            | ;

funcs_decl  : func_decl funcs_decl
            | ;

func_decl   : FUNCTION ID arguments return_type IS vars_decl block;

arguments   : '(' args_list ')';

args_list   : arg_list arg_list_continuation ;

arg_list_continuation   : ';' args_list
                        | ;

arg_list    : id_list ':' data_type;

id_list     : ID id_list_continuation;
    
id_list_continuation : ',' id_list
                        | ;

return_type : RETURN data_type;

block       : BEGIN stmts END ID ';';

stmts       : stmt stmts
            | ;

stmt        : assignation
            | if_block
            | loop_block
            | EXIT ';'
            | RETURN expression ';'
            | built_in_func
            | func_call ;

assignation : variable ':=' expression ';';

if_block    : IF expression THEN stmts alter END IF ';';

alter       : ELSE else_block
            | ;

else_block  : if_block
            | stmts ;

loop_block  : while_block
            | for_loop ;

while_block : WHILE expression LOOP stmts END LOOP ';' ;

for_loop    : FOR ID IN direction CTE_INT '..' CTE_INT LOOP stmts END LOOP ';' ;

direction   : REVERSE
            | ;

built_in_func : PRINT '(' id_list ')' ';'
            | variable ':=' READ '()' ';' ;

func_call   : ID '(' params ')' ';' ;

params      : ID params_continuation
            | ID
            | ;

params_continuation : ',' ID
            | ;

variable    : ID indexation ;

indexation  : '[' dimensions ']'
            | ;

dimensions  : CTE_INT dimensions_continuation ;

dimensions_continuation : ',' CTE_INT
            | ;

expression  :  EXPRESSION;

data_type   : INT
            | FLOAT;

value_literal   : CTE_INT
                | CTE_FLOAT ;
