# spbt.py backtracking parser
# Grammar:
#    <S> -> <A><C>
#    <A> -> 'a''b'
#    <C> -> 'c'<C>
#    <C> -> 'd'
import sys   # needed to access command line arg

#global variables
tokenindex = -1
curchar = ''

def main():
   parser()      # call the parser

def parser():
   advance()   # prime curchar with first character
   if S():
      if curchar == '': 
         print('String in language')
      else:
         print('Garbage following string')
   else:
      print('String not in language')

def S():
   return A() and C()

def A():
   return consume('a') and consume('b')

def C():
   global tokenindex
   save = tokenindex
   if C1():
      return True
   else:                  # backtrack if C1() doesn't work
      tokenindex = save
      return C2()
def C1():
   return consume('c') and C()
def C2():
   return consume('d')

def advance():
   global tokenindex, curchar
   tokenindex += 1    # move tokenindex to next token
   # check for null string or end of string
   if len(sys.argv) < 2 or tokenindex >= len(sys.argv[1]):
      curchar = ''    # signal the end by returning ''
   else:
      curchar = sys.argv[1][tokenindex]

def consume(expected):
   if expected == curchar:
      advance()
      return True
   else:
      return False

main()
