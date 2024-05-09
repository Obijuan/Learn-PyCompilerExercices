# p2shell.py parser
import sys, time   # sys needed to access cmd line args and sys.exit()

class Token:
   def __init__(self, line, column, category, lexeme):
      self.line = line         # source program line number of the token
      self.column = column     # source program column in which token starts
      self.category = category # category of the token
      self.lexeme = lexeme     # token in string form

# global variables 
trace = False      # controls token trace
grade = False      # set to True to create output to be graded
source = ''        # receives entire source program
sourceindex = 0    # index into source
line = 0           # current line number 
column = 0         # current column number
tokenlist = []     # list of tokens created by tokenizer
tokenindex = -1    # index of current token in tokens
token = None       # current token
prevchar = '\n'    # '\n' in prevchar signals start of new line
blankline = True
instring = False
parenlevel = 0

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

#new types
UNSIGNEDFLOAT = 19     # number with a decimal point
STRING        = 20     # string delimited by single quotes

# relational operators
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

#Python indentation

INDENT        = 30     # indentation
DEDENT        = 31     # outdentation 

# displayable names for each token category
catnames = ['EOF', 'PRINT', 'UNSIGNEDINT', 'NAME', 'ASSIGNOP',
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
def main():
   global source

   if len(sys.argv) == 2:
      try:
         infile = open(sys.argv[1], 'r')
         source = infile.read()   # read source code
      except IOError:
         print('Cannot read input file ' + sys.argv[1])
         sys.exit(1)
   else:
      print('Wrong number of command line arguments')
      print('Format: python p2.py <infile>')
      sys.exit(1)

   if source[-1] != '\n':
      source = source + '\n'

   if grade:
      print(time.strftime('%c') + '%34s' % 'YOUR NAME HERE')
      print('Parser      = ' + sys.argv[0])
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
     print(emsg)         # message from RuntimeError object
     sys.exit(1)

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

      if curchar.isdigit() or curchar == '.':  # unsigned int or float?
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

      elif curchar == "'":                     # string?
         instring = True
         while True:
            curchar = getchar()
            if curchar == '' or curchar == '\n':
               raise RuntimeError('Unterminated string')
            if curchar == "'":     # end of string
               curchar = getchar() # move past the end of the string 
               token.category = STRING
               instring = False    # now not in string so set to False
               break
            if curchar == '\\':    # escape sequence
               curchar = getchar()
               if curchar == 'n':
                  token.lexeme += '\n'   # insert newline char
               elif curchar == 't':
                  token.lexeme += '\t'   # insert tab char
               elif curchar == '\n':
                  pass
               else:
                  token.lexeme += curchar
            else:
               token.lexeme += curchar

      elif curchar.isalpha() or curchar == '_':  # keyword or name
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
       
      # check for change in indentation
      if len(tokenlist) == 0 or tokenlist[-1].category == NEWLINE:
         if indentstack[-1] < token.column:         # indentation
            indentstack.append(token.column)
            indenttoken = Token(token.line, token.column, INDENT, '{')
            tokenlist.append(indenttoken)
            if trace:                    # display token if trace is True
               print("%3s %4s  %-14s %s" % (str(indenttoken.line), 
                  str(indenttoken.column), catnames[indenttoken.category], 
                  indenttoken.lexeme))
         elif indentstack[-1] > token.column:       # dedentation
            while True:
               dedenttoken = Token(token.line, token.column, DEDENT, '}') 
               tokenlist.append(dedenttoken)
               indentstack.pop()
               if trace:                 # display token if trace is True
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
      return ''                   # null str signals end of source

   c = source[sourceindex] # get next char in the source program
   sourceindex += 1        # increment sourceindex to next character
   column += 1             # increment column number

   if c == '#' and not instring:  # skip over comment
      while True:
         if sourceindex >= len(source):
            return ''
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
# parser functions #
####################
def advance():
   global token, tokenindex 
   tokenindex += 1
   if tokenindex >= len(tokenlist):
      raise RuntimeError('Unexpected end of file')
   token = tokenlist[tokenindex]

def consume(expectedcat):
   if (token.category == expectedcat):
      advance()
   else:
     raise RuntimeError('Expecting ' + catnames[expectedcat])

def parser():
   advance()     # advance to first token
   program()
   # will token.category ever not equal EOF here?
   if token.category != EOF:
      raise RuntimeError('Expecting end of file')

def program():
   pass          # missing code

def stmt():
   pass          # missing code

def simplestmt():
   pass          # missing code

def compoundstmt():
   pass          # missing code

def assignmentstmt():
   pass          # missing code

def printstmt():
   pass          # missing code
    
def passstmt():
   pass          # missing code

def whilestmt():
   pass          # missing code
    
def ifstmt():
   pass          # missing code

def codeblock():
   pass          # missing code

def relexpr():
   pass          # missing code
      
def expr():
   pass          # missing code
         
def term():
   pass          # missing code

def factor():
   pass          # missing code

####################
# start of program #
####################
main()
if grade:
   # display language processor's source code
   print('------------------------------------------- ' + sys.argv[0])
   print(open(sys.argv[0]).read())
