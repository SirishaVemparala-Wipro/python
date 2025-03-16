def count_vowels(string):
    
    vowels = "aeiouAEIOU"
    
    count = 0
    
    for char in string:
    
        if char in vowels:
    
            count += 1
    
    return count

text = input("enter text: ")

print("Vowel count:", count_vowels(text))
