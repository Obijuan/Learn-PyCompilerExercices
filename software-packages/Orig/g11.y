// ========================================== part 1a
%{
// include files
#include <stdio.h>  // for I/O functions
#include <string.h> // for strcmp(), strdup()
#include <ctype.h>  // for isdigit(), isalpha()
#include <stdlib.h> // for exit()

// global variables
char *symtab[100];      // symbol table
int symval[100];        // symbol table
char yytext[100];       // holds lexeme
int currentChar = -1;   // forces read of first line of source program
int currentColumn;
int currentLine;
int i, ii; 
int nextIndex;   // index of next available slot in symbol table
FILE* inFile;    // file pointer for input file

// function prototypes
int yyparse();
int getNextChar();
int yylex();
int enter(char *);
int getValue(char *);
void yyerror(char *);
%}

// ========================================== part 1b
%token ID
%token UNSIGNED
%token PRINT
%left '+'  // indicates left associative
%left '*'  // indicates * higher precedence than +

%%  // ====================================== part 2
program:
   statementList
;
//------------------------------
statementList:
   statementList statement
 |
   statement
;
//------------------------------
statement:
   assignmentStatement
 |
   printStatement
;
//------------------------------
assignmentStatement:
   ID
   { ii = enter(yytext); }  // enter lexeme into symbol table
   '='
   expr {symval[ii] = $4; } // store its value in symbol table
   '\n'
;
//------------------------------
printStatement:
   PRINT
   '(' 
   expr { printf("%d\n", $3); } 
   ')'
   '\n'
;
//------------------------------
expr:
   expr '+' expr { $$ = $1 + $3; }
 |
   expr '*' expr { $$ = $1 * $3; }
 |
   factor { $$ = $1; }
;
//------------------------------
factor:
   '+' factor { $$ = $2; }
 |
   '-' factor { $$ = -$2; }
 |
   UNSIGNED { $$ = $1; }
 |
   ID { $$ = getValue(yytext); } // get value of lexeme in yytext
;

%%  // ====================================== part 3
int main(int argc, char *argv[])
{
  // open file whose name given on command line
  inFile = fopen(argv[1], "r");  // open for input
  return yyparse();
}
//------------------------------------
// enter or find ID in symbol table, return index
int enter(char *p) // p points to ID
{
   i = 0;
   while (i < nextIndex && strcmp(p, symtab[i]))
      i++;
   // i < nextIndex if ID in symbol table
   if (i < nextIndex)
      return i;
   // add ID to symbol table
   // strdup allocates memory for ID
   // and copies ID there
   symtab[nextIndex] = strdup(p);
   return nextIndex++;
}
//------------------------------------
// returns value of ID
int getValue(char *p)
{
   i = 0;
   // search for ID
   while (i < nextIndex && strcmp(p, symtab[i]))
      i++;
   if (i < nextIndex)
      return symval[i];   // found it at index i
   // symbol not in symbol table so no value
   printf("name '%s' on line %d column %d is not defined\n", 
           p, currentLine, currentColumn);
   exit(1);  // terminate the program
}
//------------------------------------
// returns next character on current line
int getNextChar()
{
  // input retains values 
  // between calls of getNextChar() 
  // because of keyword static 
  static char input[100];

  if (currentChar == '\n' || currentChar == -1)  // need next line?
  {
    if (fgets(input, sizeof(input), inFile))     // true if more lines
    {
      currentLine++;
      currentColumn = 0;
    }
    else  // at EOF
    {
      return 0;
    }
  }
  return input[currentColumn++];
}
//------------------------------------
// lexer (i.e., tokenizer)
int yylex()
{
  int category;

  // skip space and tab
  while (currentChar == ' ' || currentChar == '\t' 
         || currentChar == -1 )  // -1 forces read of first line of source code
    currentChar = getNextChar();

  // check for EOF
  if (currentChar == 0)
  {
    strcpy(yytext, "<EOF>");  // give EOF a lexeme
    category = 0;
  }

  else  // check for unsigned int
  if (isdigit(currentChar))
  {
    i = 0;
    do  // store lexeme in yytext
    {
      yytext[i++] = currentChar;
      currentChar = getNextChar();
    } while (isdigit(currentChar));
    yytext[i] = '\0';
    // convert ASCII string in yytest to int
    sscanf(yytext, "%d", &yylval);
    category = UNSIGNED;
  }

  else  // check for identifier
  if (isalpha(currentChar) || currentChar == '_')
  {
    i = 0;
    do  // store lexeme in yytext
    {
      yytext[i++] = currentChar;
      currentChar = getNextChar();
    } while (isalpha(currentChar) || currentChar == '_' || isdigit(currentChar));
    yytext[i] = '\0';  // terminate string with null char
    // check if keyword
    if (!strcmp(yytext, "print"))
      category = PRINT;
    else  // not a keyword so category is ID
      category = ID;
  }

  else  // do this if preceding cases do not apply
  {
    // use character itself as its category value
    category = currentChar;
    yytext[0] = currentChar;
    yytext[1] = '\0';  // terminate string with null char
    currentChar = getNextChar();  // always read one char beyond end of token
  }

  return category;
}
//------------------------------------
void yyerror(char *p)
{
   printf("%s %s '%s' %s %d %s %d\n", p, "on", yytext,
          "on line", currentLine, "column", currentColumn);
}
