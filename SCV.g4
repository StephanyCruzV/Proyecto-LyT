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
ARRAY   : 'array';
MAT     : 'mat';
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

var_decl    : ID ':' data_type value_init ';'
            | ID ':' variable;

value_init  : ':=' value_literal
            | ':=' indexation
            | ;

funcs_decl  : func_decl funcs_decl
            | ;

func_decl   : FUNCTION ID arguments return_type IS vars_decl block;

arguments   : '(' args_list? ')';

args_list   : arg_list arg_list_continuation ;

arg_list_continuation   : ';' args_list
                        | ;

arg_list    : id_list ':' data_type;

id_list     : ID id_list_continuation;
    
id_list_continuation : ',' id_list
                        | ;

return_type : RETURN data_type
            | ;

block       : BEGIN stmts END ID ';';

stmts       : stmt stmts
            | ;

stmt        : assignation
            | if_block
            | loop_block
            | for_loop
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

for_loop    : FOR ID IN direction factor '..' factor LOOP stmts END LOOP ';' ;

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

dimensions_continuation : ',' CTE_INT dimensions_continuation
            | ;

//expression  :  EXPRESSION;

data_type   : INT
            | FLOAT
            | ARRAY
            | MAT;

value_literal   : CTE_INT
                | CTE_FLOAT 
                | indexation;

// -------------------------------------
// Expresion

expression	: rel_exp
		| num_exp 
		| bool_exp;

bool_exp 	: and_exp next_bool ;

next_bool 	: OR bool_exp 
		| ;

and_exp 	: not_exp next_and ;

next_and 	: AND and_exp
		| ;

not_exp 	: NOT bool_term
		| bool_term;

bool_term	: rel_exp
		| variable
		| '(' bool_exp ')' ;


rel_exp		: num_exp rel_operator num_exp ;

num_exp		: prod_exp sum_res ;

prod_exp	: factor prod_div ;

prod_div	: prod_op prod_exp
		| ;

sum_res		: sum_op num_exp
		| ;

factor	: '(' num_exp ')'
		| CTE_INT
		| CTE_FLOAT
		| variable 
		| func_call ;

prod_op	: '*'
		| '/' ;

sum_op	: '+'
		| '-' ;

rel_operator	: '='
		        | '<'
                | '>'
                | '<='
                | '>=' ;












