def intro():
    print("Hey! I'm Penelope")

def process_input(solution):
     greeting = ["hi", "hello", "what's up", "hello", "wessup", "wassup", "hey"]
     goodbye = ["bye", "see ya", "kick rocks", "goodbye"]

     if is_valid_input(solution, greeting):
         say_greeting()

     elif is_valid_input(solution, goodbye):
         say_goodbye()

     else:
         say_default()

def say_greeting():
    print("Hey There!")

def say_goodbye():
    print("Goodbye!")

def say_default():
    print("Greet me some other way :(.")

def is_valid_input(user_input, valid_responses):
    for item in valid_responses:
        if user_input == item:
            return True
    return False

def main():
    intro()
    while True:
        answer = input("(Say something)")
        answer = answer.lower()

        process_input(answer)

def outro():
    print("Goodbye!")


if __name__ == "__main__":
  main()
