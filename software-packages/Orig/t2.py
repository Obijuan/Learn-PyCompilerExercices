# t2.py tokenizer                    
import sys, time   # sys needed to access cmd line args and sys.exit()

class Token:
   def __init__(self, line, column, category, lexeme):
      self.line = line         # source program line number of the token
      self.column = column     # source program column in which token starts
      self.category = category # category of the token
      self.lexeme = lexeme     # token in string form

# global variables 
trace = True       # controls token trace
grade = False      # controls grade display
source = ''        # receives entire source program
sourceindex = 0    # index into the source code in source
line = 0           # current line number 
column = 0         # current column number
tokenlist = []     # list of tokens created by tokenizer
token = None       # current token
prevchar = '\n'    # '\n' in prevchar signals start of new line
blankline = True   # reset to False if line not blank
instring = False   # True when processing a string
parenlevel = 0     # nesting level of parentheses

# constants that represent token categories
EOF           = 0      # end of file
PRINT         = 1      # 'print' keyword
UNSIGNEDINT   = 2      # unsigned integer
NAME          = 3      # identifier that is not a keyword
ASSIGNOP      = 4      # '=' assignment operator
LEFTPAREN     = 5      # '('
RIGHTPAREN    = 6      # ')'
PLUS          = 7      # '+'
MINUS         = 8      # '-'
TIMES         = 9      # '*'
NEWLINE       = 10     # end of line
ERROR         = 11     # if not any of the above, then error

# new keywords
NONE          = 12     # 'None' keyword
TRUE          = 13     # 'True' keyword
FALSE         = 14     # 'False' keyword
PASS          = 15     # 'pass' keyword
IF            = 16     # 'if' keyword
ELSE          = 17     # 'else' keyword
WHILE         = 18     # 'while' keyword

# new types
UNSIGNEDFLOAT = 19     # number with a decimal point
STRING        = 20     # string delimited by single quotes

# relational operators category numbers
EQUAL         = 21     # '=='
NOTEQUAL      = 22     # '!='
LESSTHAN      = 23     # '<'
LESSEQUAL     = 24     # '<='
GREATERTHAN   = 25     # '>'
GREATEREQUAL  = 26     # '>='

# new arithmetic operators
DIV           = 27     # '/'  floating point divide

# new punctuation      
COMMA         = 28     # ','
COLON         = 29     # ':'

# Python indentation

INDENT        = 30     # indentation
DEDENT        = 31     # outdentation 

# displayable names for each token category
catnames = ['EOF', 'print', 'UNSIGNEDINT', 'NAME', 'ASSIGNOP',
            'LEFTPAREN', 'RIGHTPAREN', 'PLUS', 'MINUS',
            'TIMES', 'NEWLINE','ERROR', 'NONE', 'TRUE', 'FALSE',
            'PASS', 'IF', 'ELSE', 'WHILE', 'UNSIGNEDFLOAT',
            'STRING', 'EQUAL', 'NOTEQUAL', 'LESSTHAN', 'LESSEQUAL',
            'GREATERTHAN', 'GREATEREQUAL', 'DIV',
            'COMMA', 'COLON', 'INDENT','DEDENT']

keywords = {'print':PRINT, 'None':NONE,'True':TRUE, 
            'False':FALSE, 'pass':PASS, 'if':IF, 'else':ELSE, 
            'while':WHILE}

smalltokens = {'=':ASSIGNOP, '==':EQUAL, '<':LESSTHAN, 
               '<=':LESSEQUAL, '>':GREATERTHAN, '>=':GREATEREQUAL,
               '!':ERROR, '!=':NOTEQUAL, '(':LEFTPAREN, 
               ')':RIGHTPAREN, '+':PLUS, '-':MINUS, '*':TIMES,
               '\n':NEWLINE, '':EOF, ',':COMMA , ':':COLON, '/':DIV}

#################
# main function #
#################
# main() reads source file and calls tokenizer
def main():
   global source

   if len(sys.argv) == 2:      # check if two cmd line args
      try:
         infile = open(sys.argv[1], 'r')
         source = infile.read()   # read source code
      except IOError:
         print('Cannot read input file ' + sys.argv[1])
         sys.exit(1)
   else:
      print('Wrong number of command line arguments')
      print('Format: python t2.py <infile>')
      sys.exit(1)

   if source[-1] != '\n':   # add newline to end if missing
      source = source + '\n'

   if grade:
      print(time.strftime('%c') + '%34s' % 'YOUR NAME HERE')
      print('Tokenizer = ' + sys.argv[0])
      print('Input file  = ' + sys.argv[1])

   if trace:
      print('------------------------------------------- Token trace')
      print('Line  Col Category    Lexeme\n')

   try:
      tokenizer()    # tokenize source code in source

   # on an error, display an error message
   # token is the token object on which the error was detected
   except RuntimeError as emsg: 
     # output slash n in place of newline
     lexeme = token.lexeme.replace('\n', '\\n')
     print('\nError on '+ "'" + lexeme + "'" + ' line ' +
        str(token.line) + ' column ' + str(token.column))
     print(emsg.args[0]) # message from RuntimeError object

####################
# tokenizer        #
####################
def tokenizer():
   global token, instring
   curchar = ' '                       # prime curchar with space
   indentstack = [1]

   while True:
      # skip whitespace but not newlines
      while curchar != '\n' and curchar.isspace():
         curchar = getchar() # get next char from source program

      # construct and initialize token
      token = Token(line, column, None, '')  

      if curchar.isdigit() or curchar == '.': 
         token.category = UNSIGNEDINT
         if curchar == '.':
            token.category = UNSIGNEDFLOAT
         while True:
            token.lexeme += curchar
            curchar = getchar()
            if token.category == UNSIGNEDINT and curchar == '.':
               token.category = UNSIGNEDFLOAT
            elif not curchar.isdigit():
               break

      elif curchar == "'":
         instring = True
         while True:
            curchar = getchar()
            if curchar == '' or curchar == '\n':
               raise RuntimeError('Unterminated string')
            if curchar == "'":
               curchar = getchar()
               token.category = STRING
               instring = False
               break
            if curchar == '\\':
               curchar = getchar()
               if curchar == 'n':
                  token.lexeme += '\n'
               elif curchar == 't':
                  token.lexeme += '\t'
               elif curchar == '\n':
                  pass
               else:
                  token.lexeme += curchar
            else:
               token.lexeme += curchar

      elif curchar.isalpha() or curchar == '_':
         while True:
            token.lexeme += curchar
            curchar = getchar()
            if not curchar.isalnum() and curchar != '_':
               break
         # determine if lexeme is a keyword or name of variable
         if token.lexeme in keywords:
            token.category = keywords[token.lexeme]
         else:
            token.category = NAME

      elif curchar in smalltokens:
         save = curchar
         curchar = getchar()
         twochar = save + curchar
         if twochar in smalltokens:
            token.category = smalltokens[twochar]
            token.lexeme = twochar
            curchar = getchar()
         else: 
            token.category = smalltokens[save]
            token.lexeme = save
      else:
         token.category = ERROR    # invalid token 
         token.lexeme = curchar    # save lexeme
         raise RuntimeError('Invalid token')
      
      # check for change in indentation when starting a new line
      if len(tokenlist) == 0 or tokenlist[-1].category == NEWLINE:
         if indentstack[-1] < token.column:         # indentation
            indentstack.append(token.column)
            indenttoken = Token(token.line, token.column, INDENT, '{')
            tokenlist.append(indenttoken)
            if trace:
               print("%3s %4s  %-14s %s" % (str(indenttoken.line), 
                  str(indenttoken.column), catnames[indenttoken.category], 
                  indenttoken.lexeme))
         elif indentstack[-1] > token.column:       # dedentation
            while True:
               dedenttoken = Token(token.line, token.column, DEDENT, '}') 
               tokenlist.append(dedenttoken)
               indentstack.pop()
               if trace:
                  print("%3s %4s  %-14s %s" % (str(dedenttoken.line), 
                     str(dedenttoken.column), catnames[dedenttoken.category], 
                     dedenttoken.lexeme))
               if indentstack[-1] == token.column:
                  break
               elif indentstack[-1] < token.column:
                  raise RuntimeError('Indentation error')
      
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
      return ''                   # str char signals end of source

   c = source[sourceindex] # get next char in the source program
   sourceindex += 1        # increment sourceindex to next character
   column += 1             # increment column number

   if c == '#' and not instring:      # skip over comment
      while True:
         c = source[sourceindex]
         sourceindex += 1
         if c == '\n':
            break

   if not c.isspace():     # if c not whitespace then line not blank
      blankline = False    # indicate line not blank
   prevchar = c            # save current character

   # if at end of blank line, return space in place of '\n'
   if c == '\n' and blankline:
      return ' '
   else:
      return c             # return character to tokenizer()

####################
# start of program #
####################
main()
if grade:
   # display language processor's source code
   print('------------------------------------------- ' + sys.argv[0])
   print(open(sys.argv[0]).read())
