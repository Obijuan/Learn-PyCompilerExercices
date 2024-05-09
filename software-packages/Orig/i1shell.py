# i1shell.py parser
import sys, time   # sys needed to access cmd line args and sys.exit()

class Token:
   def __init__(self, line, column, category, lexeme):
      self.line = line         # srce program line number of the token
      self.column = column     # srce program col in which token starts
      self.category = category # category of the token
      self.lexeme = lexeme     # token in string form

# globals 
trace = False        # controls token trace
grade = False        # set to True to create output to be graded
source = ''          # receives entire source program
sourceindex = 0      # index into the source code in source
line = 0             # current line number 
column = 0           # current column number
tokenlist = []       # list of tokens created by tokenizer
tokenindex = -1      # index of current token in tokens
token = None         # current token
prevchar = '\n'      # '\n' in prevchar signals start of new line
blankline = True     # reset to False if line is not blank
operandstack = []    # holds operands and results of operations
symtab = {}          # holds values of variables

# constants that represent token categories
EOF           = 0    # end of file
PRINT         = 1    # 'print' keyword
UNSIGNEDINT   = 2    # unsigned integer
NAME          = 3    # identifier that is not a keyword
ASSIGNOP      = 4    # '=' assignment operator
LEFTPAREN     = 5    # '('
RIGHTPAREN    = 6    # ')'
PLUS          = 7    # '+'
MINUS         = 8    # '-'
TIMES         = 9    # '*'
NEWLINE       = 10   # end of line
ERROR         = 11   # if not any of the above, then error

# displayable names for each token category
catnames = ['EOF', 'print', 'UNSIGNEDINT', 'NAME', 'ASSIGNOP',
            'LEFTPAREN', 'RIGHTPAREN', 'PLUS', 'MINUS',
            'TIMES', 'NEWLINE','ERROR']

# keywords and their token categories}
keywords = {'print': PRINT}

# one-character tokens and their token categories
smalltokens = {'=':ASSIGNOP, '(':LEFTPAREN, ')':RIGHTPAREN,
               '+':PLUS, '-':MINUS, '*':TIMES, '\n':NEWLINE, '':EOF}

#################
# main function #
#################
# main() reads input file and calls tokenizer()
def main():
   global source

   if len(sys.argv) == 2:   # check if correct number of cmd line args
      try:
         infile = open(sys.argv[1], 'r')
         source = infile.read()  # read source program
      except IOError:
         print('Cannot read input file ' + sys.argv[1])
         sys.exit(1)
   else:
      print('Wrong number of command line arguments')
      print('Format: python i1.py <infile>')
      sys.exit(1)

   if source[-1] != '\n':  # add newline to end if missing
      source = source + '\n'

   if grade:
      print(time.strftime('%c') + '%34s' % 'YOUR NAME HERE')
      print('Interpreter = ' + sys.argv[0])
      print('Input file  = ' + sys.argv[1])

   if trace:
      print('------------------------------------------- Token trace')
      print('Line  Col Category    Lexeme\n')

   try:
      tokenizer()    # tokenize source code in source
      if grade or trace:
         print('------------------------------------------- Program output')
      parser()

   # on an error, display an error message
   # token is the token object on which the error was detected
   except RuntimeError as emsg: 
      # output slash n in place of newline
      lexeme = token.lexeme.replace('\n', '\\n')
      print('\nError on '+ "'" + lexeme + "'" + ' line ' +
         str(token.line) + ' column ' + str(token.column))
      print(emsg)      # message from RuntimeError object
      sys.exit(1)
 
####################
# tokenizer        #
####################
def tokenizer():
   global token
   curchar = ' '          # prime curchar with space

   while True:
      # skip whitespace but not newlines
      while curchar != '\n' and curchar.isspace():
         curchar = getchar() # get next char from source program

      # construct and initialize token
      token = Token(line, column, None, '')  

      if curchar.isdigit():               # start of unsigned int?
         token.category = UNSIGNEDINT     # save category of token
         while True:
            token.lexeme += curchar       # append curchar to lexeme
            curchar = getchar()           # get next character
            if not curchar.isdigit():     # break if not a digit
               break

      elif curchar.isalpha() or curchar == '_':   # start of name?
         while True:
            token.lexeme += curchar       # append curchar to lexeme
            curchar = getchar()           # get next character
            # break if not letter, '_', or digit
            if not (curchar.isalnum() or curchar == '_'):
               break

         # determine if lexeme is a keyword or name of variable
         if token.lexeme in keywords:
            token.category = keywords[token.lexeme]
         else:
            token.category = NAME

      elif curchar in smalltokens:
         token.category = smalltokens[curchar]      # get category
         token.lexeme = curchar
         curchar = getchar()       # move to first char after the token

      else:                         
         token.category = ERROR    # invalid token 
         token.lexeme = curchar
         raise RuntimeError('Invalid token')
      
      tokenlist.append(token)      # append token to tokens list
      if trace:                    # display token if trace is True
         print("%3s %4s  %-14s %s" % (str(token.line), 
            str(token.column), catnames[token.category], token.lexeme))

      if token.category == EOF:    # finished tokenizing?
         break

# getchar() gets next char from source and adjusts line and column
def getchar():
   global sourceindex, column, line, prevchar, blankline

   # check if starting a new line
   if prevchar == '\n':    # '\n' signals start of a new line
      line += 1            # increment line number                             
      column = 0           # reset column number
      blankline = True     # initialize blankline

   if sourceindex >= len(source): # at end of source code?
      column = 1                  # set EOF column to 1
      prevchar = ''               # save current char for next call
      return ''                   # null str signals end of source

   c = source[sourceindex] # get next char in the source program
   sourceindex += 1        # increment sourceindex to next character
   column += 1             # increment column number
   if not c.isspace():     # if c not whitespace then line not blank
      blankline = False    # indicate line not blank
   prevchar = c            # save current character

   # if at end of blank line, return space in place of '\n'
   if c == '\n' and blankline:
      return ' '
   else:
      return c             # return character to tokenizer()

####################
# parser functions #
####################
# advances to the next token in the list tokens
def advance():
   global token, tokenindex 
   tokenindex += 1
   if tokenindex >= len(tokenlist):
      raise RuntimeError('Unexpected end of file')
   token = tokenlist[tokenindex]

# advances if current token is the expected token
def consume(expectedcat):
   if (token.category == expectedcat):
      advance()
   else:
     raise RuntimeError('Expecting ' + catnames[expectedcat])

# top level function of parser
def parser():
   advance()     # advance so token holds first token
   program()     # call function corresponding to start symbol
   # will token.category ever not equal EOF here?
   if token.category != EOF:
      raise RuntimeError('Expecting end of file')

def program():
   while token.category in [NAME, PRINT]:
      stmt()

def stmt():
   simplestmt()
   consume(NEWLINE)

def simplestmt():
   if token.category == NAME:
      assignmentstmt()
   elif token.category == PRINT:    
      printstmt() 
   else:
      raise RuntimeError('Expecting statement')

def assignmentstmt():
   left = token.lexeme       
   advance()
   consume(ASSIGNOP) 
   expr()

def printstmt():
   advance()
   consume(LEFTPAREN)
   expr()
   consume(RIGHTPAREN)

def expr():   
   term()
   while token.category == PLUS:
      advance()
      term()

def term():
   global sign
   sign = 1
   factor()
   while token.category == TIMES:
      advance()
      sign = 1
      factor()

def factor():
   global sign
   if token.category == PLUS:
      advance()
      factor()
   elif token.category == MINUS:
      sign = -sign
      advance()
      factor()
   elif token.category == UNSIGNEDINT:
      advance()
   elif token.category == NAME:
      advance()
   elif token.category == LEFTPAREN:
      savesign = sign
      advance()
      expr()
      consume(RIGHTPAREN)
   else:
      raise RuntimeError('Expecting factor')

####################
# start of program #
####################
main()
if grade:
   # display interpreter source code
   print('------------------------------------------- ' + sys.argv[0])
   print(open(sys.argv[0]).read())
