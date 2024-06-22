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
    result2=a1.before_space('"ok":false, "lhs":"",')
    introcs.assert_equals('"ok":false,',result2)

    #test printing val after space
    result=a1.after_space('4.502 Euros')
    introcs.assert_equals('Euros',result)
    result1=a1.after_space('Kayla Rossi')
    introcs.assert_equals('Rossi',result1)

    pass

def testB():
    """
    Test procedure for Part B of testing a JSON
    Test proc for lhs json
    Test proc for rhs JSON
    """
    result=a1.first_inside_quotes('A "B C" D')
    introcs.assert_equals('B C',result)
    result1=a1.first_inside_quotes('A "B C" D "E F" G')
    introcs.assert_equals('B C',result1)
    result2=a1.first_inside_quotes('he"ll"o')
    introcs.assert_equals('ll',result2)

    result_lhs=a1.get_lhs('{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }')
    introcs.assert_equals('1 Bitcoin',result_lhs)
    result_lhs1=a1.get_lhs('{ "ok":true, "lhs":"2.5 United States Dollars", "rhs":"64.375 Cuban Pesos", "err":"" }')
    introcs.assert_equals('2.5 United States Dollars',result_lhs1)

    result_rhs=a1.get_rhs('{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }')
    introcs.assert_equals('9916.0137 Euros',result_rhs)
    result_rhs1=a1.get_rhs('{ "ok":true, "lhs":"2.5 United States Dollars", "rhs":"64.375 Cuban Pesos", "err":"" }')
    introcs.assert_equals('64.375 Cuban Pesos',result_rhs1)

    result_err=a1.has_error('{ "ok":false, "lhs":"", "rhs":"", "err":"Currency amount is invalid." }')
    introcs.assert_equals(True,result_err)
    result_err1=a1.has_error('{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }')
    introcs.assert_equals(False,result_err1)


    pass

def testC():
    """
    Test proc to return JSON string
    """
    result=a1.currency_response('USD','CUP','2.5')
    introcs.assert_equals('{ "ok":true, "lhs":"2.5 United States Dollars", "rhs":"64.375 Cuban Pesos", "err":"" }',result)
    result1=a1.currency_response('USD','BIF','1')
    introcs.assert_equals('{ "ok":true, "lhs":"1 United States Dollar", "rhs":"2047 Burundian Francs", "err":"" }',result1)
    result2=a1.currency_response('AAA','ZZZ','5')
    introcs.assert_equals('{ "ok":false, "lhs":"", "rhs":"", "err":"Source currency code is invalid." }',result2)

    pass

def testD():
    """
    Test proc for currencies and exchange
    """
    result=a1.is_currency('USD')
    introcs.assert_equals(True,result)
    result1=a1.is_currency('AAA')
    introcs.assert_equals(False,result1)

    result_exch=a1.exchange('USD','CUP',2.5)
    introcs.assert_equals(64.375, result_exch)
    result_exch1=a1.exchange('USD','AOA',1.0)
    introcs.assert_floats_equal(428.1788, result_exch1)



    pass

testA()
testB()
testC()
testD()
print('Module a1 passed all tests.')
