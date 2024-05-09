%{
#include <stdio.h>   // for printf()
#include <string.h>  // for strcpy()
#include <ctype.h>   // for isdigit
char input[80];      // global array that holds the input string
int yyparse();       // prototype
%}

%token DIGIT   // indictes DIGIT is a token
%left '+'      // indicates + and * are left associative and
%left '*'      // * has higher precedence than +

%%
Q: E          {printf("%d\n", $1);} // display expr value
   ;                                // indicates end of Q productions
E: E '+' E    {$$ = $1 + $3;}       // assign left side the sum
   | E '*' E  {$$ = $1 * $3;}       // assign left side the product
   | DIGIT                          // assign left side the right
   ;                                // indicates end of E productions

%%
int main(int argc, char *argv[])
{
   strcpy(input, argv[1]);         // copy input string to input array
   return yyparse();               // call  yyparse()
}
int yylex()
{
   static int i = 0;               // i retains value between calls
   if (isdigit(input[i]))         
   {                                  
      yylval = input[i++] - '0';   // if digit, return in value in yylval
      return DIGIT;                // return token category via return stmt
   }   
   return input[i++];
}
void yyerror(char *p)
{
   printf("%s\n", p);             // displays error message it is passed
}

