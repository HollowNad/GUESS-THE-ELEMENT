import random 

#DEFINING THE LIST OF ELEMENTS
def nad():
    print ("GUESS YOUR ELEMENTS ")
    
    element = [
        "Aurum",
        "Hydrogen",
        "Helium",
        "Carbon",
        "Nitrogen",
        "Oxygen",
        "Ferum",
        "Platinum",
        "Zink",
        "Calsium"]
        
    a = random.choice(element)

#GUESS THE ELEMENTS
    teka = None

    while a != teka:
        
        teka = str(input("\nGuess your element. "))
        
        if teka == a:
            print ("\nCongratulations!Your answer correct")
            
#HINTS IF THE ANSWER INCORRECT
        elif a == ("Aurum"):
            print("\nVery valuable")
        
        elif a == ("Hydrogen"):
            print("\nCombined with oxygen to create water.")
        
        elif a == ("Helium"):
            print("\nExample for Noble Gas")
        
        elif a == ("Carbon"):
            print("\nUsed to make a pencil.")
        
        elif a == ("Nitrogen"):
            print("\n78% in the air")
        
        elif a == ("Oxygen"):
            print ("\nUsed to create fire")
        
        elif a == ("Ferum"):
            print("\nOther name for iron")
        
        elif a == ("Platinum"):
            print ("\nHighly unreactive")
        
        elif a == ("Zink"):
            print("\nUsed to make roofs")
        
        elif a == ("Calsium"):
            print("\nExtracted by electrolysis")
        
        else:
            print("\nSorry incorrect answer.Please try again")

nad()