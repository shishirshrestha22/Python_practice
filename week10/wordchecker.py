#program to check palindrome and anagram
#An anagram is when two words contain the same letters in the same quantity, but arranged in a different order.
class WordChecker:
    def __init__(self,word):
        self.word = word
    
    def palindrome(self):
        return self.word == self.word[::-1]#------------------------->> logic to check palindrome
    def anagram(self,word):
        return sorted(self.word.lower()) == sorted(word.lower())#---------------------->> logic to check anagram

def main():
    word = input("Enter a word: ")
    checker = WordChecker(word)

    while True:
        print("\n1.Check Palindrome")
        print("2. Check Anagram")
        print("3. exit")

        choice = input("ENter your choice: ")

        if  choice == "1":
            if checker.palindrome():
                print("It is palindrome")
            else:
                print("Not palindrome")

        elif choice == "2":
            other = input("ENter another word: ")
            if checker.anagram(other):
                print("It is anagram")
            else:
                print("It is not anagram")
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":#------------------------>> this line prevents this file/code to run directly while imported 
    main()
        