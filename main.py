from tkinter import *
from tkinter import messagebox
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

def player(window, hand, on_stand_callback):
    player_hand_frame = Frame(window)
    player_hand_frame.place(relx=0.5,rely=0.87, anchor=CENTER)

    first = deck.pop()
    second = deck.pop()
    hand.add(first)
    hand.add(second)
    
    player = Label(player_hand_frame, text="Player")
    player.pack(side="top", padx=5)

    cards_frame = Frame(player_hand_frame) 
    cards_frame.pack(side="top")

    first_card = Label(cards_frame, text=first)
    first_card.pack(side="left", padx=2)

    second_card = Label(cards_frame, text=second)
    second_card.pack(side="left", padx=2)

    val = hand_value(hand)
    value = Label(player_hand_frame, text=f"Value: {val}")
    value.pack(side="top")
    
    if (val == 21):
        messagebox.showinfo(title="Info message",message="You win!")

    buttonHit = Button(window, text="Hit", command=lambda: clickHit(hand, cards_frame, value))
    buttonStand = Button(window, text="Stand", command=lambda: clickStand(hand, on_stand_callback, buttonHit, buttonStand))
    
    buttonHit.place(relx=0.45, width=50, rely=1.0, anchor="s") 
    buttonStand.place(relx=0.55, width=50, rely=1.0, anchor="s") 

def clickHit(hand, cards_frame, value):
    global score
    another = deck.pop()
    hand.add(another)

    another_card = Label(cards_frame, text=another)
    another_card.pack(side="left", padx=2)
    
    val = hand_value(hand)
    value.config(text=f"Value: {val}")

    if (val == 21):
        messagebox.showinfo(title="Info message",message="You win!")
    elif (val >= 21):
        messagebox.showinfo(title="Info message",message="You lose!")

def clickStand(hand, callback, buttonHit, buttonStand):
    final_value = hand_value(hand)
    buttonHit.config(state=DISABLED)
    buttonStand.config(state=DISABLED)
    callback(final_value)

def computer(window, hand, player_value):
    computer_hand_frame = Frame(window)
    computer_hand_frame.place(relx=0.5,rely=0.1, anchor=CENTER)

    first = deck.pop()
    second = deck.pop()
    hand.add(first)
    hand.add(second)
    
    computer = Label(computer_hand_frame, text="Computer")
    computer.pack(side="top", padx=5)

    cards_frame = Frame(computer_hand_frame) 
    cards_frame.pack(side="top")

    first_card = Label(cards_frame, text=first)
    first_card.pack(side="left", padx=2)

    second_card = Label(cards_frame, text=second)
    second_card.pack(side="left", padx=2)

    val = hand_value(hand)
    value = Label(computer_hand_frame, text=f"Value: {val}")
    value.pack(side="top")

    while val < player_value:
        another = deck.pop()
        hand.add(another)

        another_card = Label(cards_frame, text=another)
        another_card.pack(side="left", padx=2)
        
        val = hand_value(hand)
        value.config(text=f"Value: {val}")
        
    if val > 21:
        messagebox.showinfo(title="Info message",message="Computer lose!")  
    elif (val == 21 or val >= player_value):
        messagebox.showinfo(title="Info message",message="Computer win!")


def on_stand(window, final_value):
        computer_hand = set()
        computer(window, computer_hand, player_value=final_value)

def main():
    global deck 

    window = Tk()
    window.geometry("500x500")
    window.resizable(False, False)

    window.title("BlackJack")
    
    deck = [(n, k) for n in number for k in kind]
    shuffle(deck)

    player_hand = set()
    player(window, player_hand, lambda final_value: on_stand(window, final_value))
    
    window.mainloop()


main()