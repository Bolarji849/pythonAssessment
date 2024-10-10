def get_vowel(word):
	
	for character in "aeiou":

		if word == character:
			return True
		
	
	return False

print(get_vowel("f"))
