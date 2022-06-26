#Sorry for spelling. Will fix

#Get name
def _getName():
    _Name = input("What is your name?  :")
    print("Hello " + _Name)

#section 1 out of 2
def _sec1():
    print("You stumble upon a castle. You decide to check it out.")
    print("You can either walk around (1) or go through the castle door (2)")
    _input = input("What wold you like to do? (1/2): ")
   
    
    if(_input == "1"): #walk around castle
        print("You encounter a goblin")
        print("THE END!")
        _sec1()
    elif(_input == "2"): #go through gate
        _sec2()
    else:
        print("Sorry that does not work. Try again")
        _sec1()
        
#section 2 out of 2
def _sec2():
    #text
    print("The castle door immediately closes. You see the king standing at the base of a large stone throne.")
    print("King: WHO ARE YOU?!?")
    print("")
    
    _input = input(" (1) you say 'I am the King' (2) You say a wanderer")
    
    if(_input == "1"):
        print("The guards swarm you. THE END")
        print("Try again")
        _sec2()
    
    elif(_input == "2"):
        print("You follow the king inside. He offers you a job. You take it. You live the rest of your life as the king's jester")
        print("THE END")
    else:
        print("Sorry that does not work. Try again")
        _sec2()
        
#call functions
_getName()

_sec1()
