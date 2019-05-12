# list that contains gold and bp for 2 players.
gold=[20,20]
bp=[20,20]

print ("player 1 has",gold[0],"gold")
print ("player 2 has",gold[1],"gold")

print ("player 1 has",bp[0],"BP")
print ("player 2 has",bp[1],"BP")

sans=["skeleton","normal attack:bones, and a single gaster blaster",]
store = [sans]
print (store)

stamina=[1000,1000]

#pyshical state of the charater that if its stunned, electrified or sleepy.
states = {
    "sleepy": "recharge stamina until",
    "stunned": "can't move for 5 secs",
    "electrified": "stunned and taking dmg for 10 secs",
    "normal": "your taking 0 dmg unless player does dmg and your not stunned unless player is stunned, etc",
    "force": "the your heavy and opponent controls your movement for 5 secs",
    "KR": "dot damage,damages the opponent over time. the daamages lasts for 5 secs and each sec is 2 dmg"
}
# a lazy skeleton but very strong! he cost 100 gold, and he has many skills.
sans={
    "name": "SANS",
    "type": "skeleton that makes puns",
    "battack": "bones and gaster blaster",
    "battack_dmg":10,
    "battack_state": "KR",
    "sattack": "gaster plater barrage",
    "sattack_dmg":20,
    "sattack1": "blue soul",
    "sattack1_dmg":5,
    "sattack1_state": "force"
}

#a cute little foe but very dangerous! he has annoying attacks to ;D
pikachu={
    "name": "PIKACHU",#key value
    "type": "pokemon",
    "battack3": "iron tail",
    "battack3_dmg":50,
    "battack3_state": "stunned",
    "battack4": "lightning ball",
    "battack4_dmg":50,
    "battack4_state": "electrified",
    "sattack3": "lightning dash",
    "sattack3_dmg":100,
    "sattack3_states": "electrified",
    "sattack4": "lightning barrage",
    "sattack4_dmg":100,
    "sattack4_state": "electrified"
}

print(pikachu)
print(pikachu["battack3"],pikachu["battack3_dmg"], pikachu["battack3_state"] )
print(sans["battack"],sans["battack_dmg"],sans ["battack_state"])

#bone=["ghghghgh","sans","pikachu","battack","gaster blaster","papyrus"] #i added a system where it check like its say if "900" in bone it mean if its there do that else mean if not do that

#for x in pikachu,pikachu.values():
    #print(x)
#bone=[900]
#if "900" in bone:
   # print("yes it exist")
#else:
    #print("no")
    

# i added input statment that stores the names for the players
print("HELLO THIS GAME IS ABOUT FIGHT PLAYER ONE CHOOSE YOUR NAME")
x=input("choose name: ")
print("hello", x,"welcome to the game")
print("NOW YOUR TURN PLAYER TWO!")
y=input("choose name: ")
print("hello", y,"welcome to the game")

print(pikachu)
print(pikachu["battack3"],pikachu["battack3_dmg"], pikachu["battack3_state"] )
print(sans["battack"],sans["battack_dmg"],sans ["battack_state"])

print("HELLO THIS GAME IS ABOUT FIGHT PLAYER ONE CHOOSE YOUR NAME")
x=input("choose name: ")
print("hello", x,"welcome to the game")
print("NOW YOUR TURN PLAYER TWO!")
y=input("choose name: ")
print("hello", y,"welcome to the game")

s=input("choose your charater type in pikachu to be pikachu and or type something else to be sans: ")
if s=="pikachu":
    print("your now pikachu")
else:
    print("you're now sans")
# added charater selection
p=input("choose your charater player 2 type in pikachu to be pikachu or type in somthing else to be sans: ")
if p=="pikachu":
    print("you're now pikachu")
else:
    print("you're now sans")

    
    
    
    
    
 
 
 
q=input("type in sattack1 to use your sattack but if you type in something else you use your battack")
if q=="sattack1":
    print("player 2 has 100 hp!")
else:
    print("player 2 has 150 HP!")
e=input("YOUR TURN PLAYER2! type in sattack 2 to use your sattack and type in something else to use your battack!")
if e=="sattack2":
    print("player1 has 100 hp")
else:
    print("player1 has 150 HP!")
q=input("type in sattack1 to use your sattack but if you type in something else you use your battack")
if q=="sattack1":
    print("player 2 has 0 hp!")
    print("player 2 has fallen")
else:
    print("player 2 has 100 HP!")
e=input("YOUR TURN PLAYER2! type in sattack 2 to use your sattack and type in something else to use your battack!")
if e=="sattack2":
    print("player1 has 0 hp")
    print("player 1 has fallen!")
else:
    print("player1 has 100 HP!")
q=input("NOW YOU CAN ONLY USE BATTACKS TYPE IN battack1 or just type in a random word to use it!")
if q=="battack1":
    print("player2 has 50 HP!")
else:
    print("player2 has 50 HP!")
e=input("NOW YOU CAN ONLY USE BATTACKS TYPE IN battack2 or just type in a random word to use it!")
if e=="battack2":
    print("player1 has 50 HP!")
else:
    print("player1 has 50 HP!")
q=input("NOW YOU CAN ONLY USE BATTACKS TYPE IN battack1 or just type in a random word to use it!")
if q=="battack2":
    print("player2 has 0 HP!")
    print("player2 has fallen!")
else:
    print("player2 has 0 HP!")
    print("player2 has fallen!")
e=input("NOW YOU CAN ONLY USE BATTACKS TYPE IN battack2 or just type in a random word to use it!")
if e=="battack2":
    print("player1 has  0 HP!")
    print("player1 has fallen!")
else:
    print("player1 has  0 HP!")
    print("player1 has fallen!")
