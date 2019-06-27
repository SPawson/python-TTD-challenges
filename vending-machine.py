from byotest import*


#Get change function
def get_change(amount):
    if amount == 0:
        return []
    else:
        return [amount]
        
#Tests
test_are_equal(get_change(0),[])
test_are_equal(get_change(1),[1])
test_are_equal(get_change(2),[2])
test_are_equal(get_change(5),[5])
test_are_equal(get_change(10),[10])
test_are_equal(get_change(20),[20])
test_are_equal(get_change(50),[50])
test_are_equal(get_change(100),[100])

print("All tests passed!")