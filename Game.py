#Sorry for spelling. Will fix

#Get name
def _getName():
    _Name = input("What is your name?  :")
    print("Helo " + _Name)

#section 1 out of 2
def _sec1():
    print("You stumble apon a cassle. You decide to check it out.")
    print("You can either walk around (1) or go through the cassle door (2)")
    _input = input("What wold you like to do? (1/2): ")
   
    
    if(_input == "1"): #walk around cassle
        print("you encounter a goblin")
        print("THE END!")
        _sec1()
    elif(_input == "2"): #go through gate
        _sec2()
    else:
        print("Sorry that dose not work. try again")
        _sec1()
        
#section 2 out of 2
def _sec2():
    #text
    print("the cassle door imediatly closes. You see the king standing at the base of a large stone thrown.")
    print("King: WHO ARE YOU?!?")
    print("")
    
    _input = input(" (1) you say 'JO, jomama' (2) you say a wanderer")
    
    if(_input == "1"):
        print("The gards swarm you. THE END")
        print("Try again")
        _sec2()
    
    elif(_input == "2"):
        print("You follow the king inside. He offers you a job. you take it. you live the rest of your life as the king's jester")
        print("THE END")
    else:
        print("Sorry that dose not work. try again")
        _sec2()
        
#call functions
_getName()

_sec1()
