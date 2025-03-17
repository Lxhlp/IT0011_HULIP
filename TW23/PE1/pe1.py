# Excluded words
exclude_words = {'and', 'but', 'or', 'nor', 'for', 'so', 'yet', 'a', 'an', 'the', 'of'}

print("**************************************")
print("Welcome to the word counter program!")
print("**************************************")
statement = input("Enter a string statement: ")

# Split into words
words = statement.split()

# Filter out excluded words and count words
word_count = {}
for word in words:
    if word.lower() not in exclude_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

# Separate lowercase and uppercase words
lowercase_words = {}
uppercase_words = {}
for word, count in word_count.items():
    if word.islower():
        lowercase_words[word] = count
    else:
        uppercase_words[word] = count

# Sort words in ascending order
sorted_lowercase = sorted(lowercase_words.items())
sorted_uppercase = sorted(uppercase_words.items())

sorted_words = sorted_lowercase + sorted_uppercase

# Count number of words 
total_filtered_words = sum(word_count.values())

print("\nWord count result:")
for word, count in sorted_words:
    print(f"{word.ljust(10)} - {count}")
print(f"Total words filtered: {total_filtered_words}")