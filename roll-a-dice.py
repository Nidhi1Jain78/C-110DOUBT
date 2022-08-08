import random
print("Do you want to roll the dice? Type y for yes and n for no.")
response=input("Enter your response")
def dice(response):
    if response=="y":
        no=random.randint(1,6)
        if no==1:
            print("[-----]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[-----]")
        elif no==2:
            print("[-----]")
            print("[     ]")
            print("[0   0]")
            print("[     ]")
            print("[-----]")
        elif no==3:
            print("[-----]")
            print("[  0  ]")
            print("[  0  ]")
            print("[  0  ]")
            print("[-----]")
        elif no==4:
            print("[-----]")
            print("[  0  ]")
            print("[0   0]")
            print("[  0  ]")
            print("[-----]")
        elif no==5:
            print("[-----]")
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]")
            print("[-----]")
        elif no==6:
            print("[-----]")
            print("[0   0]")
            print("[0   0]")
            print("[0   0]")
            print("[-----]")
        else:
            print("Press again")

    else:
        print("You have pressed n for no")


dice(response)
print("y for rolling the dice and n to exit")


   

