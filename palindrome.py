#this program is to check whether the given statement is palindrome or not

#method_1
string = "abcdcba"
reversed = ''.join(reversed(string))
if string == reversed:
    print("The above stated string is palindrome")
else:
    print("The above stated string is not palindrome")


#method_2

string = input("Enter to check if it palindrome or not:")
length = len(string)
reverse = ''
print(string)
for i in range(length - 1, -1, -1):
    reverse += string[i]
if string == reverse:
        print("the above stated string is palindrome")
else:
    print("the above stated string is not plaindrome")









