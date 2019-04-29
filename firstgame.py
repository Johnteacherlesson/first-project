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
}
# a lazy skeleton but very strong! he cost 100 gold, and he has many skills.
sans={
    "name": "SANS",
    "type": "skeleton that makes puns",
    "battack": "bones and gaster blaster",
    "battack_dmg":10,
    "sattack": "gaster plater barrage",
    "sattack_dmg":20,
    "sattack1": "blue soul"
    "sattack1_dmg":5,
    "sattack1_state": "force"
}

###a cute little foe but very dangerous! he has annoying attacks to ;D
PIKACHU={
    "name": "PIKACHU",
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
