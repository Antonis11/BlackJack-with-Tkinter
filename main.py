from tkinter import *
from random import shuffle

number = {"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"}
kind = {"♥", "♦", "♠", "♣"}

deck = []

def main():

    window = Tk()
    window.geometry("500x500")
    window.resizable(False, False)

    window.title("BlackJack")
    
    deck = [(n, k) for n in number for k in kind]
    shuffle(deck)
    
    
main()