import datetime

def store_confession(confession):
    # Get the current date and time for the timestamp
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Append the confession to a file
    with open("confessions.txt", "a") as file:
        file.write(f"[{timestamp}] {confession}\n")
    
    print("Thank you for your confession. It has been saved anonymously.")

def main():
    print("Welcome to the Confession Box.")
    print("You can share your secrets anonymously.")
    print("Type 'exit' to quit at any time.")
    
    while True:
        # Prompt the user for a confession
        confession = input("What's your confession? ")
        
        # Exit condition
        if confession.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Store the confession
        store_confession(confession)

if __name__ == "__main__":
    main()
