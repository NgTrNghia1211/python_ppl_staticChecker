// student ID: 2013873
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}
// ! program: decllist EOF;
program: decllist EOF ;// write your rule here

decllist: decl decllist | decl ;
decl: vardecl | funcdecl ;


// --2. Program Structure --> declaration
// ? vardecl - variable
vardecl: shortform_vardecl | fullform_vardecl ;
// ! --- short form: auto type ?
shortform_vardecl: idlist COLON (element_typ|AUTO) SEMI ;
// ! --- fullform: not yet compare number of vars and values 
// fullform_vardecl: idlist COLON element_typ EQUAL explist SEMI ;
fullform_vardecl: prefullform_vardecl SEMI ;
prefullform_vardecl: IDENTIFIER COMMA prefullform_vardecl COMMA expr | base_fullform;
base_fullform: IDENTIFIER COLON (element_typ|AUTO) EQUAL expr;
// a, b, c: integer = 3, 4 ,6;

idlist: IDENTIFIER COMMA idlist | IDENTIFIER ;
explist: expr COMMA explist | expr ; // * actually expprime in exercise

// ? vardecl - parameter
param: INHERIT? OUT? IDENTIFIER COLON (element_typ|AUTO) ;
paramsdecl: LB paramslist RB ;

// ! fundecl - blockstatement not yet
funcdecl: IDENTIFIER COLON FUNCTION return_type paramsdecl (INHERIT IDENTIFIER)? block_stmt ; 
paramslist: paramsprime | ;
paramsprime: param COMMA paramsprime | param ;

// ? not declared yet
return_type: element_typ | VOID | AUTO ;

// --6. expression
expr: relational_expr (BELONG) relational_expr | relational_expr; // * actually is string concatenation
relational_expr: logical_expr (EQOP | DIFOP | LT | GT | LE | GE) logical_expr | logical_expr ;
logical_expr: logical_expr (ANDOP | OROP) adding_expr | adding_expr ;
adding_expr: adding_expr (ADDOP | SUBOP) multiply_expr | multiply_expr;
multiply_expr: multiply_expr (MULOP | DIVOP | MODOP) ulogical_expr | ulogical_expr;
ulogical_expr: (NOTOP) ulogical_expr | sign_expr ;
sign_expr: (SUBOP) sign_expr | index_expr ;
index_expr: index_expr LSB explist RSB | operands ;
// index_expr: IDENTIFIER LSB explist RSB ;
funcall: IDENTIFIER LB funcall_list RB ;
funcall_list: explist | ;
operands: IDENTIFIER | INTLIT | FLOATLIT | STRINGLIT | boollit | funcall | LB expr RB | arraylit | funcall;

// --7. statement
// stmtlist: stmt stmtlist | ;
stmt: assg_stmt | if_stmt | for_stmt | while_stmt | break_stmt | continue_stmt | return_stmt | block_stmt | call_stmt | do_while_stmt ;
// --- Assign statement
assg_stmt: lhs EQUAL expr SEMI;
lhs: scalar_var | index_expr;
scalar_var: IDENTIFIER | index_expr;
// --- If statement
if_stmt: IF LB expr RB stmt (ELSE stmt)? ;
// tstmt: stmt;
// --- For statement
for_stmt: FOR LB scalar_var EQUAL init_expr COMMA conditional_expr COMMA update_expr RB stmt;
// for_expr
// 	:  ;
conditional_expr: expr ;
update_expr: expr ;
init_expr: expr ;
// --- While statement 
while_stmt: WHILE LB expr RB stmt ;
// --- Do-while statement
do_while_stmt: DO block_stmt WHILE LB expr RB SEMI ;
// --- Break statement
break_stmt: BREAK SEMI ;
// --- Continue statement
continue_stmt: CONTINUE SEMI ;
// --- RETURN statement
return_stmt: RETURN expr? SEMI ;
// --- Call statement
call_stmt: IDENTIFIER LB explist? RB SEMI ;
// --- Block statement
// block_stmt: LP (vardecl | stmt)* RP ;
block_stmt: LP block_stmt_prime_2 RP ;
block_stmt_prime_2: block_stmt_prime | ;
block_stmt_prime: (vardecl | stmt) block_stmt_prime | (vardecl | stmt);




// --3. Comment, Literals, Keywords ...
// comment
LINE_COMMENT: '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;

// keywords
AUTO: 'auto' ;
BREAK: 'break' ;
BOOLEAN: 'boolean' ;
DO: 'do' ;
ELSE: 'else' ;
FALSE: 'false' ;
FLOAT: 'float' ;
FOR: 'for' ;
FUNCTION: 'function' ;
IF: 'if' ;
INTEGER: 'integer' ;
RETURN: 'return' ;
STRING: 'string' ;
TRUE: 'true' ;
WHILE: 'while' ;
VOID: 'void' ;
OUT: 'out' ;
CONTINUE: 'continue' ;
OF: 'of' ;
INHERIT: 'inherit' ;
ARRAY: 'array' ;

// operators
ADDOP: '+' ;
SUBOP: '-' ;
MULOP: '*' ;
DIVOP: '/' ;
MODOP: '%' ;
NOTOP: '!' ;
ANDOP: '&&' ;
OROP: '||' ;
EQOP: '==' ;
DIFOP: '!=' ;
LT: '<' ; // less than
GT: '>' ; // greater than
LE: '<=' ; // less equal
GE: '>=' ; // greater equal
BELONG: '::' ;

// separator
LSB: '[' ;
RSB: ']' ;
LP: '{' ;
RP: '}' ;
LB: '(' ;
RB: ')' ;
DOT: '.' ;
COMMA: ',' ;
SEMI: ';' ;
COLON: ':' ;
EQUAL: '=' ;


// literals
boollit: TRUE | FALSE ;

IDENTIFIER: NONDIGIT (NONDIGIT | DIGIT)*;


INTLIT: '0' 
	  | NONZERO DIGIT* ('_' DIGIT+)* {self.text = self.text.replace("_", "")} ;

FLOATLIT: ( INTLIT DOT DIGIT+ 
		| INTLIT EXPONENT
		| INTLIT DOT DIGIT+ EXPONENT ) 
		| DOT DIGIT+ EXPONENT {self.text = self.text.replace("_", "")};

// STRINGLIT:
// 	'"' STRING_CHAR* '"' {
//     self.text = self.text[1:-1]
// };

STRINGLIT
    : '"' CHAR* '"'
    {
        self.text = self.text[1:-1]
    };

fragment CHAR
    : '\\' [bfrnt"'\\]
    | ~[\r\n\\"]
    ;

arraylit: LP (arrayprime_2) RP | arrayprime;
arrayprime_2: arrayprime COMMA arrayprime_2 | arrayprime ;
arrayprime: LP explist RP ;
// arrayexpr: (atyp COMMA arrayexpr) | atyp;
// atyp: boollit | INTLIT | FLOATLIT | STRINGLIT;

// fragment
fragment BOOL: 'true' | 'false';
fragment DIGIT: [0-9] ;
fragment NONZERO: [1-9] ;
fragment NONDIGIT: [a-zA-Z_] ;
fragment EXPONENT: [Ee] [+-]? DIGIT+;
// fragment STRING_CHAR: ~[\b\t\n\f\r'\\] | ESC_SEQ;
// fragment ESC_SEQ: '\\' [btnfr"'\\];
// fragment ESC_ILLEGAL: '\\' ~[btnfr"\\] | '\\';

// --4. Types
// --- ATOMIC TYPE
bool_typ: BOOLEAN ;
int_typ: INTEGER ;
float_typ: FLOAT ;
string_typ: STRING | BELONG;
element_typ: bool_typ | int_typ | float_typ | string_typ | array_typ ;
// --- ARRAY TYPE
array_typ: ARRAY dimension_list OF type_in_array;
type_in_array: bool_typ | int_typ | float_typ | string_typ ;
dimension_list: LSB dimension_prime RSB ;
dimension_prime: INTLIT COMMA dimension_prime | INTLIT ;
// --- VOID TYPE -- AUTO TYPE
void_typ: VOID ;
auto_typ: AUTO ;


WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines

// UNCLOSE_STRING: '"' STRING_CHAR* {
//     raise UncloseString(self.text[1:])
// };
// ILLEGAL_ESCAPE: '"' STRING_CHAR* ESC_ILLEGAL {
//     raise IllegalEscape(self.text[1:])
// };
UNCLOSE_STRING: '"' CHAR* ([\r\nEOF] | ~'"')
{
	err_char = ['\r','\n',EOFError]
	if self.text[-1] in err_char:
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE: '"' CHAR* ('\\' ~[btnfr"\\] | ~'\\')
{
	raise IllegalEscape(self.text[1:])
};

ERROR_CHAR: . {raise ErrorToken(self.text)};
// UNCLOSE_STRING: .;
// ILLEGAL_ESCAPE: .;