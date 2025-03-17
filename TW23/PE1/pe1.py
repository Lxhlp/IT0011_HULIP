def count_words(statement):
    # Exclude these words
    exclude_words = {'and', 'but', 'or', 'nor', 'for', 'so', 'yet', 'a', 'an', 'the', 'of'}
    
    words = statement.split()
    
    # Filter out excluded words and count words
    word_count = {}
    for word in words:
        if word.lower() not in exclude_words:
            word_count[word] = word_count.get(word, 0) + 1
    
    lowercase_words = {word: count for word, count in word_count.items() if word.islower()}
    uppercase_words = {word: count for word, count in word_count.items() if not word.islower()}
    
    # Sort words in ascending order
    sorted_lowercase = sorted(lowercase_words.items())
    sorted_uppercase = sorted(uppercase_words.items())
    
    sorted_words = sorted_lowercase + sorted_uppercase
    
    total_filtered_words = sum(word_count.values())
    for word, count in sorted_words:
        print(f"{word.ljust(10)} - {count}")
    print(f"Total words filtered: {total_filtered_words}")

print("**************************************")
print("Welcome to the word counter program!")
print("**************************************")
statement = input("Enter a string statement: ")
print("\nWord count result:")
count_words(statement)

