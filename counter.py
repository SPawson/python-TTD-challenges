def capital_counter(message):
    count = 0
    
    for c in message:
        if c.isupper():
            count+= 1
    return count
    
var = capital_counter("Hello My Name Is Sam")

testMessage = "Hello My Name Is Samuel J Pawson"
testMessageAmount = capital_counter(testMessage)


assert capital_counter("") == 0, "Empty message"
assert capital_counter("AD") == 2, "Counting more than one upper"
assert capital_counter("ad") == 0, "counting upper when there is none"
assert capital_counter("@$%^") == 0, "Special chars counted"
assert capital_counter(testMessage) == testMessageAmount, "Not all uppers counted"

print("All tests complete")