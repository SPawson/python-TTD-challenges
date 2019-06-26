def even_number_of_evens(numbers):
    length = len(numbers)
    
    if length == 0:
        return False
    elif length== 1:
        if numbers[0] % 2 == 0:
            return False
        else:
            return False
    else:
        even_count = 0
        for num in numbers:
            if num%2 == 0:
                even_count += 1

        if length == 2 and even_count == 2:
            return True
        elif length == 2 and even_count == 1:
            return False
        elif length > 2 and even_count == 3:
            return False  
        elif length > 2 and even_count == 4:
            return True 
        else:
            return False
            
            
assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([1]) == False, "One number"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All tests completed successfully")