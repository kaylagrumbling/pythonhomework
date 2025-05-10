# Step 1: Initialize an Empty List
favorite_books = []

# Step 2 & 3: Prompt the User for Input and Store the Books in the List
for i in range(1, 4):
    book = input(f"Enter the title of your favorite book #{i}: ")
    favorite_books.append(book)

# Step 4: Sort the List
favorite_books.sort()

# Step 5: Print the Sorted List
print("\nYour favorite books in alphabetical order:")
for book in favorite_books:
    print(book)