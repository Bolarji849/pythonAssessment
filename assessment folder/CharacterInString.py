



def count_characters_in_string(word):
    return len(word)



def main():
	user_input = input("Enter a word   ")
	character_count = count_characters_in_string(user_input)

	print(f"The number of characters in '{user_input}' is {character_count}.")





main()
