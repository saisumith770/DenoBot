import random

def welcome_message(name):
    greetings = [
        f"Welcome {name}👋",
        f"{name} has joined!🎉",
        f"{name} just landed🚀",
        f"{name} hopped on board"
    ]
    return random.choice(greetings)