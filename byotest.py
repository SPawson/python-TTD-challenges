def test_are_equal(actual,expected):
    assert expected == actual,"Expected {0}, instead got {1}".format(expected,actual)
    
def test_not_equal(a,b):
    assert a != b, "Did not expect {0}, but got {1}".format(a,b)
    
def test_is_in(collection,item):
    assert item in collection, "{0} does not contain the item {1}".format(collection,item)
    
def test_isnt_in(collection,item):
    assert item not in collection, "{0} does contain the item {1}".format(collection,item)

def between(min,max,value):
    if value >= min and value <= max:
        return True
    else:
        return False
        
def test_between(min,max,value):
    assert between(min,max,value) == True, "The number {0} is not between {1} and {2}".format(value,min,max)
