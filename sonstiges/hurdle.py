def hurdle():
    print("A")
    
def turtle():
    print("B")
    
def pinky():
    print("C")
    
def multFunc(name_der_funktion,zahl):
    for _ in range(zahl):
        name_der_funktion()
        
        
    
multFunc(hurdle,6)
multFunc(turtle,3)
multFunc(pinky,11)