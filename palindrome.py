def isPalindrome(string):
    left_pos=0
    right_pos=len(string)
    
    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False
        left_pos += 1
        
            
                
    
    right_pos -= 1
    return True
print("is this 	palindrome")
print(isPalindrome("nitin"))