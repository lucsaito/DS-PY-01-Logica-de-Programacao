
"""
To play the game it's necessary to install the beautifulsoup4 and the unicode libraries!
Para rodar o programa é necessário instalar a biblioteca beautifulsoup4 e a biblioteca unidecode!
""";

# Setting environment:
from bs4 import BeautifulSoup
from urllib.request import urlopen
import random
import unidecode

# Getting list of words:
url = "https://g1.globo.com/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

text = soup.get_text().split()
word_list = []

for item in text:
    if item.isalpha():
        if len(item) > 6:
                word_list.append(item.lower())

word_list = list(set(word_list))      

# Functions used
def guess_verification():
    if unidecode.unidecode(guess) == unaccented_secret:
        return("end")
    elif unidecode.unidecode(guess) == "arrego":
        return("arrego")
    else:
        for item in unaccented_secret:
            if guess == item:
                return("continue")
        else:
            return
          
def update_word():
    for item in range(len(unaccented_secret)):
        if unidecode.unidecode(guess) == unaccented_secret[item]:
            word_visual[item] = (secret[item] + " ")
    return word_visual
  
def update_missing_digits():    
    missing_digits = 0
    for item in word_visual:
        if item == "_ ":
            missing_digits += 1
    return missing_digits
  
def arrego_function():
    for item in range(len(word_visual)):
        if word_visual[item] == "_ ":
            word_visual[item] = (secret[item] + " ")
            return word_visual
          


# Global variables:
secret = random.choice(word_list)
unaccented_secret = unidecode.unidecode(secret)
game = "start"
lives = 6
arrego = 0
wrong_words = []
missing_digits = -1

word_visual = []
for item in range(len(secret)):
    word_visual.append("_ ")

# Game greetings
print(f"It's the hangmans game!\n")
print(f"Try to guess the hidden word: {'_ '*len(secret)} \n")
print(f"-> Here's a tip: the word has {len(secret)} digits!")
print(f"-> If you don't know what to guess, type 'arrego' for a tip! (use it only once) \n")

# Main game body
while game != "end":
    if missing_digits != 0:
        guess = input("Type here your guess: ").lower()
        while not (len(guess) > 5 or len(guess) == 1):
            guess = input("Enter a valid guess: a").lower() 
    
        game = guess_verification()
    
    elif missing_digits == 0:
        game = "end"
    
    if game == "end":
        print("Congratulations! You made it! You guessed the hidden word correctly!! \n")
        print(f"The hidden word was: {secret}")
        break
        
    elif game == "continue":
        word_visual = update_word()
        missing_digits = update_missing_digits()
        if missing_digits == 0:
            continue
        print("\nYou are on the right track! ")
        print(f"The hidden word is: {''.join(word_visual)} \n")
        print(f"You still have to guess {missing_digits} digits! You have {lives} lives. \n")
        
    elif game == "arrego":
        if arrego == 0:
            word_visual = arrego_function()
            missing_digits = update_missing_digits()
            arrego = 1
            
        print("\nYou arregated!! Here's your tip!")
        print(f"The hidden word is: {''.join(word_visual)} \n")
        print(f"You have {lives} lives. \n")
        
    else:
        wrong_words.append(guess)
        print(f"\nThe hidden word doesn't have '{wrong_words}': {''.join(word_visual)}")
        lives -= 1
        if lives > 0:
            print(f"Now you have {lives} lives! \n")
        else:
            print("You ran out of lives!")
            print(f"The hidden word was: {secret}")
            game = "end"
            break  

