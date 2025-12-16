f = input("Hey, how are you feeling today? (happy, sad, angry, excited): ").lower()

match f:
    case "happy":
        print("Love that! Hold onto that good energy and let it carry you through the day.")
    case "sad":
        print("I'm really sorry you're feeling low. Be gentle with yourself—better moments will come.")
    case "angry":
        print("That sounds tough. Take a breath, step back for a moment, and give yourself some space.")
    case "excited":
        print("That's awesome! Ride that wave of excitement and make something great out of it.")
    case _:
        print("Thanks for sharing. Whatever you're feeling right now, you're doing your best, and that matters.")