def spel():

    index = 0
    number =1
    totalt_rätt_svar = 0

    for key in frågor: 
        print("\n",number,">",key) # will print question from the dictionary
        number+=1
        print()
        for i in svar[index]:
            print(i)   # will print all the options for prespective question

        index+=1
        user_svar = int(input("Svar>: "))
        
        
        fråga = frågor.get(key)   # will get the value from dictionary fro prespectve question
        totalt_rätt_svar += kolla_svar(fråga, user_svar)# #taking the return value from Kolla_svar() and increment it by 1

    visa_resultat(totalt_rätt_svar)

    print("\n\nVill du spela igen(ya eller nej):")
    input1 = input("> ")
    if input1 == "ja":
        spel()
    else:
        print("hej dååååååå")


      
       
           

def kolla_svar(rätt_svar, user_svar):
    
    if user_svar <= 3 and user_svar >= 1:
        if rätt_svar == user_svar:  # checking the value from dictionary  with the input value
            print("\n****det är rätt****")
            return 1
        else:
            print("\n***Det är fel svar***")
            return 0
    else:
        print("FEL Siffra.")
        user_svar = int(input("Pröva igen: "))
        return kolla_svar(rätt_svar, user_svar)
    
    
def visa_resultat(totalt_rätt_svar):
    print("\n\nHär är din resultaten\n")
    resultat = int((totalt_rätt_svar/len(frågor))*100)
    print(f"Du har totalt {totalt_rätt_svar} rätt svar.")
    print(resultat,"%")


frågor = {'''Vad skriver följande rad kod ut i terminalen?
    print("Hello World!")''': 1, 
    """Vad skriver följande rad kod ut i terminalen?
print(f"{type(5)} {type(1.52)} {type('hej')} {type(True)}")""":1,
"""\nVilken klass/typ blir följande variabel?
variabelnamn = 'text här'""":3,
"""fruits = ["apple", "banana", "cherry"]
vilken kommand måste skriva för att tabort "banana" från fruits.""":2,

"""fruits = ("apple", "banana", "cherry")
vilken data type är den?""":3,

"""i = 0
while i < 6:
i += 1
if i == 3:
    continue
print(i)
vad ska printa i terminalen?\n\n""":3}


svar=[("1. Hello World!","2. HELLO WORLD","3. Hello     World"),
    ("1. <class 'int'> <class 'float'> <class 'str'> <class 'bool'>", "2. <nåt> <som> <jag> <inte> <vet>", "3. 5,1.42,hej, True"),
    ("1. int", "2. float", "3. ingen av de"),
    ("1. fruits.pop()","2. fruits.remove('banana')","3. fruits.clear()"),
    ("1. list", "2. dictionary", "3. tuples"),
    ("1. 1,2,3,4,5,6", "2. 1,2,3","3. 1,2,4,5,6")]


spel()