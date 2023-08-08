# Excercise 1
#TODO: def function
    #TODO: Computation
    #TODO: Print result

#TODO: input1
#TODO: input2

#function call

# Excercise 2
def testVowel(value,vowel):
    final = [each for each in value if each in vowel]
    print(len(final))
    print("Vowels are ",final)

# Driver Code for string and vowel char

value = "This nutritious fruit offers multiple health benefits. Apples may lower your chance of developing cancer, diabetes, and heart disease.Research says apples may also help you lose weight while improving your gut and brain health."
vowel = 'AaEeIiOoUu'
testVowel(value,vowel)

#Excercise 3

def fact(n): # with argument

    if (n == 1 or n == 0):
        return 1
    else:
        return (n * fact(n - 1))
print("Welcome!")

num = 5
result = fact(num)
print("Factorial of", num, "is", result)
