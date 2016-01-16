import sys
def TellMeTheType( pVal ):
    print ('The type for ' , pVal , 'is ' , type(pVal))
def GiveMeValueInfo ( pTst ) :
    try :
        a = 1 / 0
        print  ( 'Value' , 'pTst' , 'Info:' )
        if pTst == 3 :
            print ('\t it is equal to 3')
        elif pTst == 'cat' :
            print ('\t is cat')
        else :
            print ('\t nothing of interest')
    except :
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print ('\t there was a problem inside GiveMeValueInfo on line:', exc_traceback.tb_lineno)
        traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)

if __name__ == '__main__' :
    try :
        lst = (3,4, 5, 6 ,7 ,10, 'cat')
        for elt in lst :
            print ('Running TellMeTheType for value' , elt )
            TellMeTheType ( elt )
    except :
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print ('\t there was a problem running GiveMeValueInfo on line:', exc_traceback.tb_lineno)
##try:
##    if b == 3 :
##        print ('yes')
##        print ('it is')
##    else :
##        print ('
##
##except IndexError:
##    exc_type, exc_value, exc_traceback = sys.exc_info()
##    print "*** print_tb:"
##    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
##    print "*** print_exception:"
##    traceback.print_exception(exc_type, exc_value, exc_traceback,
##                              limit=2, file=sys.stdout)
##    print "*** print_exc:"
##    traceback.print_exc()
##    print "*** format_exc, first and last line:"
##    formatted_lines = traceback.format_exc().splitlines()
##    print formatted_lines[0]
##    print formatted_lines[-1]
##    print "*** format_exception:"
##    print repr(traceback.format_exception(exc_type, exc_value,
##                                          exc_traceback))
##    print "*** extract_tb:"
##    print repr(traceback.extract_tb(exc_traceback))
##    print "*** format_tb:"
##    print repr(traceback.format_tb(exc_traceback))
##    print "*** tb_lineno:", exc_traceback.tb_lineno
