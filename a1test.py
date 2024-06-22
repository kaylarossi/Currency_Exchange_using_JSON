"""
Test script for module a1

When run as a script, this module invokes several procedures that
test the various functions in the module a1.


"""
import introcs
import a1

def testA():
    """
    Test procedure to test splitting functions
    """
    #test printing val before space
    result=a1.before_space('4.502 Euros')
    introcs.assert_equals('4.502',result)
    result1=a1.before_space('Kayla Rossi')
    introcs.assert_equals('Kayla',result1)

    #test printing val after space
    result=a1.after_space('4.502 Euros')
    introcs.assert_equals('Euros',result)
    result1=a1.after_space('Kayla Rossi')
    introcs.assert_equals('Rossi',result1)

    pass

def testB():
    """
    Test procedure for Part B of testing a JSON
    """
    result=a1.first_inside_quotes('A "B C" D')
    introcs.assert_equals('B C',result)
    result1=a1.first_inside_quotes('A "B C" D "E F" G')
    introcs.assert_equals('B C',result1)
    result2=a1.first_inside_quotes('he"ll"o')
    introcs.assert_equals('ll',result2)




    pass



#testA()
testB()
#testC()
#testD()
print('Module a1 passed all tests.')
