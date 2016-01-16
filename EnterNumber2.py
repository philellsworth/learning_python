'''
    This Module May Have Bugs in It.  Your Missions, should you decide to accept them:
      (1) Find And Fix Bugs
      (2) Document & Comment
      (3) Make It Better
      (4) Send Improvements Back To Base
'''      
'''
    This Module:
     * Defines Variables
     * Defines Functions
     * Calls Functions To Test Them
       (Calls Are Commented Out After Testing)
'''
### Python Provides a "Not A Number" facility:
NaN = float ( 'nan' ) # Let's Make One that we can return whenever we want
## And Run A few testers to see what it does.
print ("a = float ('nan')")
a = float ( 'nan' )
print ( 'a', a, sep=": " )
print ("b = float ('nan')")
b = float ( 'nan' )
print ( 'b:', b, sep=": " )
print ('type(a)', type(a))
print ('type(b)', type(a))
print ("a == b", a == b , sep=": ")
print ("a == a", a == a , sep=": ")
print ("float ('nan') == float ('nan')", float ('nan') == float ('nan') , sep=": ")
print ("type(float('nan'))", type(float('nan')), sep=": ")
print ('type (NaN)' , type (NaN) , sep=": ")
print ('NaN == NaN' , NaN == NaN , sep=": ")

'''
What's Happening Here!?!?!?
One of the properties of NaN is that comparisons and equality tests using them are always false
'cat' will never be greater than, less than, equal to 1. and 'cat' will never be greater than, less than, or equal to 'cat'.
greater than, less than, and equal to only make sense with numbers to python.
'''

'''
But we can test whether a variable of type float is not a number
'''
from math import isnan # math.isnan(x): Return True if x is a NaN (not a number), and False otherwise.

'''
Let's define a function that guarantees a passed-in (argument) variable is a number
 And gracefully handles arguments that are not recognisable as numbers
'''

def IsNum ( TestVar ) :
    '''
        Return floating point number if TestVar can be converted
        to a floating point number. Otherwise, return "Not A Number"
    '''
    # Try to use built in function float() to convert TestVar to float
    # If conversion attempt fails, intercept error reporting
    # and return a non-unique special value that is "Not a Number"
    try : 
        FloatVar = float ( TestVar )
        return FloatVar
    except :
        return NaN

'''
Call Function Multiple times to test all possibilities
These calls to print():
   (1)Output text indicating the call
   (2) Then make the call and output its return value.
NOTE that the call executes and returns before the print statement gets executed
'''
#print ('IsNum ( 1     )' , IsNum ( 1     ) )
#print ('IsNum ( 1.0   )' , IsNum ( 1.0   ) )
#print ('IsNum ( 1 / 2 )' , IsNum ( 1 / 2 ) )
#print ("IsNum ( 'cat' )" , IsNum ( 'cat' ) )

# These are variables definitions not function definitions (How Do You Know?)
NumPrompt     = 'Num?: '
QuitNumPrompt = 'Num?  or "q(uit)": '

# Let's Keep Getting Input From the User until he enters something Python recognises as a number
def GetNumFromUser ():
    TestNum = NaN
    while ( isnan( TestNum ) ) :
        print ('Here')
        TestNum = IsNum ( input ( NumPrompt ) )
    return TestNum

# Call Function to Test It    
#print ('GetNumFromUser()' , GetNumFromUser() )

# But what if he wants to stop entering numbers?
def GetUserNumOrQuit () :
    TestNum = NaN
    while ( isnan( TestNum ) ) :
        UserResponse = input ( QuitNumPrompt ) 
        if ( UserResponse == 'q' ) :
            return UserResponse
        TestNum = IsNum ( UserResponse )
    return TestNum

# Call Function to Test It    
#print ('GetUserNumOrQuit()' , GetUserNumOrQuit() )

# But what if he's a smart guy and knows that Control-C means Quit to Python

def KbdIntGetUserNumOrQuit() :
    try :
        return GetUserNumOrQuit ()
    except KeyboardInterrupt :
        print ('Ouch! Control-C - Quit' )
        return 'Ctrl-C' # Why???
# Call Function to Test It    
#print ('KbdIntGetUserNumOrQuit()' , KbdIntGetUserNumOrQuit() )
'''
Now that we have user management out of the way, lets define a few predicates
a Predicate for Blahness returns true for x if x is a blah, false otherwise
'''
def IsInteger ( Num ):
    '''Return True if Num is (a Mathematical) Integer, Otherwise return False'''
    # Test for Mathematical Integer-ness, not python int-ness
    return ( Num % 1 ) == 0

# Call Function to Test It    
##print ('IsInteger( -3   )'   , IsInteger ( -3   )  , sep=": ")
##print ('IsInteger( -2   )'   , IsInteger ( -2   )  , sep=": ")
##print ('IsInteger( -1   )'   , IsInteger ( -1   )  , sep=": ")
##print ('IsInteger(  0   )'   , IsInteger (  0   )  , sep=": ")
##print ('IsInteger(  1   )'   , IsInteger (  1   )  , sep=": ")
##print ('IsInteger(  2   )'   , IsInteger (  2   )  , sep=": ")
##print ('IsInteger(  3   )'   , IsInteger (  3   )  , sep=": ")
##print ('IsInteger(  0.5 )'   , IsInteger (  0.5 )  , sep=": ")

def IsOdd( Num ) :
    '''Return True if Num is Mathematically Odd, Otherwise return False'''
    # Test for Mathematical Odd-ness
    return ( Num % 2 ) == 1
##print ('IsOdd( -3   )'   , IsOdd ( -3   )  , sep=": ")
##print ('IsOdd( -2   )'   , IsOdd ( -2   )  , sep=": ")
##print ('IsOdd( -1   )'   , IsOdd ( -1   )  , sep=": ")
##print ('IsOdd(  0   )'   , IsOdd (  0   )  , sep=": ")
##print ('IsOdd(  1   )'   , IsOdd (  1   )  , sep=": ")
##print ('IsOdd(  2   )'   , IsOdd (  2   )  , sep=": ")
##print ('IsOdd(  3   )'   , IsOdd (  3   )  , sep=": ")
##print ('IsOdd(  0.5 )'   , IsOdd (  0.5 )  , sep=": ")
def IsEven( Num ) :
    '''Return True if Num is Mathematically Even, Otherwise return False'''
    # Test for Mathematical Even-ness
    return IsInteger(Num) and ( Num % 2 ) == 0
##print ('IsEven( -3   )'   , IsEven ( -3   )  , sep=": ")
##print ('IsEven( -2   )'   , IsEven ( -2   )  , sep=": ")
##print ('IsEven( -1   )'   , IsEven ( -1   )  , sep=": ")
##print ('IsEven(  0   )'   , IsEven (  0   )  , sep=": ")
##print ('IsEven(  1   )'   , IsEven (  1   )  , sep=": ")
##print ('IsEven(  2   )'   , IsEven (  2   )  , sep=": ")
##print ('IsEven(  3   )'   , IsEven (  3   )  , sep=": ")
##print ('IsEven(  0.5 )'   , IsEven (  0.5 )  , sep=": ")

def IsPrime( Num ):
    '''Return True if Num is Prime, Otherwise Return False'''
    # make sure Num is a positive integer
    if ( not IsInteger( Num ) ) :
        return False
    
    Num = abs ( int ( Num ) )
    # 0 and 1 are not primes
    if Num < 2:
        return False
    # 2 is the only even prime number
    if Num == 2 : 
        return True    
    # all other even numbers are not primes
    if IsEven ( Num ): 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range ( 3 , int ( Num ** 0.5 ) + 1 , 2 ):
        if Num % x == 0 :
            return False
    return True

##print ('IsPrime(1.2): ', IsPrime(1.2))
##print ('IsPrime(1.5): ', IsPrime(1.5))
##print ('IsPrime(0): '  , IsPrime(0))
##print ('IsPrime(1): '  , IsPrime(1))
##print ('IsPrime(2): '  , IsPrime(2))
##print ('IsPrime(3): '  , IsPrime(3))
##print ('IsPrime(4): '  , IsPrime(4))
##print ('IsPrime(5): '  , IsPrime(5))
##print ('IsPrime(6): '  , IsPrime(6))
##print ('IsPrime(7): '  , IsPrime(7))
##print ('IsPrime(9): '  , IsPrime(9))
##print ('IsPrime(15): ' , IsPrime(15))

'''
Whenever we define a predicate, we have to define a report
'''

def IntegerReport( Num ) :
    if ( IsInteger( Num ) ):
        print ( Num , 'Is An Integer' )
    else :
        print ( Num , 'Is NOT An Integer' )

#print ('IntegerReport(3)', IntegerReport ( 3 ) )

def OddReport( Num ):
    if ( IsOdd( Num ) ):
        print ( Num , 'Is Odd' )
    else :
        print ( Num , 'Is NOT Odd' )

#print ('OddReport(1.2)', OddReport (1.2) )

def EvenReport ( Num ) :
    if ( IsEven( Num ) ):
        print ( Num , 'Is Even' )
    else :
        print ( Num , 'Is NOT Even' )

#print ('EvenReport(1.2)', EvenReport (1.2) )

def PrimeReport ( Num ) :
    if ( IsPrime ( Num ) ) :
        print ( Num , 'Is Prime' )
    else :
        print ( Num , 'Is NOT Prime' )

#print ('PrimeReport(1.2)', PrimeReport (1.2) )

           
# Finally!  Our Tool for generating Number Reports!
def ReportOnNumber( Num ) :
    print ('Your Number is: ' , Num )
    IntegerReport ( Num )
    OddReport     ( Num )
    EvenReport    ( Num )
    PrimeReport   ( Num )

#print ('ReportOnNumber(3)' , ReportOnNumber ( 3 ) )
# And A Tool to Generate Them for as many numbers as we care to enter!
def LoopingPrompt () :
    while True :
        strUserResponse = KbdIntGetUserNumOrQuit()
        if strUserResponse == 'q' :
            print('Quitting, Per Your Request (Thanks for Not Using Control-C)!')
            return    
        if strUserResponse == 'Ctrl-C' :
            print('Quitting, Per Your Request (Thanks for Using Control-C)!')
            return
        ReportOnNumber( strUserResponse )    

# Call Function to Test It
#print ('LoopingPrompt()' , LoopingPrompt() )


# But We're Smarter than That!  Let's Make A file of the inputs
# And define a function that process the file

def LoopThroughNumFile () :
    Name = 'Numbers.txt'
    try :  # Generate an Exception of Python Fails to Open The File
        File = open ( Name , 'r')
    except IOError : # Output Error Information
        print('Cannot Open', Name )
    else : # No Exception in Attempting To Open The Named File
        List = File.readlines()
        File.close()
        print(  Name, 'Has', len ( List ) , 'Lines' )
        ## for LineText in List : - What We Are Not Doing.  We Want The Line Number As Well!
        for LineNum , LineText in enumerate ( List ) :
            #print ('LineText' , LineText , 'Type' , type ( LineText ) )
            try :
                Num = float ( LineText )
            except :
                print ( 'Line Number', LineNum + 1 , "Is BAD:" , LineText, end='' )
            else:
                ReportOnNumber ( Num )
                
# Call Function to Test It
#print ('LoopThroughFile()',LoopThroughFile())
Dict={}
def LoopThroughCfgFile():
    Name = 'Config.txt'
    try :  # Generate an Exception of Python Fails to Open The File
        File = open ( Name , 'r')
    except IOError : # Output Error Information
        print('Cannot Open', Name )
    else : # No Exception in Attempting To Open The Named File...
        ListOfLines = File.readlines()
        File.close()
        print(  Name, 'Has', len ( ListOfLines ) , 'Lines' )
        ## for LineText in List : - What We Are Not Doing.  We Want The Line Number As Well!
        for LineNum , LineText in enumerate ( ListOfLines ) :
            if LineText[0] != '\n' :
                CleanLine = LineText.replace('\n','')
                print ('CleanLine: (' , CleanLine , ')' , sep='' , end=': ' )
                if ( CleanLine[0] == '['):
                    Key=CleanLine.replace('[','').replace(']','')
                    Val=[] # Start an Empty Value List
                    Dict[Key] = Val
                    print ('Key: (' , Key , ')' , sep='')
                else:
                     print ('Not a Key')
                     Val.append(CleanLine)
                     
print ('LoopThroughCfgFile()',LoopThroughCfgFile())
print ('Dict' , Dict)
