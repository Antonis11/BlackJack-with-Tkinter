from tkinter import *
from random import shuffle

number = {"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"}
kind = {"♥", "♦", "♠", "♣"}

deck = []

def hand_value(hand):
    value = 0
    ace = False
    for card in hand:
        if( card[0] == "J" or card[0] == "Q" or card[0] == "K" ):
            value += 10
        elif(card[0] == "A"):
            ace = True
            value += 1
        else:
            value += card[0]

    if ace and value + 10 <= 21:
        value += 10
    
    return value

def main():

    window = Tk()
    window.geometry("500x500")
    window.resizable(False, False)

    window.title("BlackJack")
    
    deck = [(n, k) for n in number for k in kind]
    shuffle(deck)

    window.mainloop()
    

main()