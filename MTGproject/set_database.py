
from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog
import pyrebase
from datetime import datetime
import re
from multiprocessing import Process
import time


def collectCard(setcodes, user, db, auth):
	start_time = time.time()
	keywords = ["Surveil", "enters", "dies", "Flash","Defender", "Deathtouch","enchant", "Enchant", "Equip", "Flying", "Indestructible", "Lifelink", "Cumulative", "Cycling", "Buyback", "Madness", "Morph", "facedown", "Storm", "Affinity", "Ninjutsu", "Dredge", "Wither", "Cascade", "Infect", "Miracle", "Extort", "Prowess", "Jump-Start", "Escape", "create", "Hexproof", "Shroud"]
	listy = []
	print("started")
	for code in setcodes:
		code = code.strip()
		cards = Card.where(set=code).all()
		print("cards collected")
		for card in cards:
			if (time.time() - start_time) > 3400:
				user = auth.refresh(user['refreshToken'])
				start_time = time.time()
				print("reset")
			itsgot = []
			name = card.name
			mana_cost = card.mana_cost
			colors = card.colors
			types = card.type
			supertype = card.supertypes
			subtypes = card.subtypes
			text = card.text 
			if text != "" and text != " " and text != "None":
				word = re.sub("[^a-zA-Z]+", " ", str(text))
				checker = word.split(" ")

				for word in keywords:
					if word in checker:
						itsgot.append(word)
			else:
				text = "Empty"
			power = card.power
			toughness = card.toughness
			cmc = card.cmc
			colourIdentit = card.color_identity
			addToDatabase(colourIdentit, name, mana_cost, colors, types, subtypes, supertype, text, power, toughness, cmc, itsgot, user, db)

def addToDatabase(colourIdentit, name, mana_cost, colors, types, subtypes, supertype, text, power, toughness, cmc, itsgot, user, db):

	colourIdentit = "%20".join(colourIdentit)
 ##Not putting on github
	
	data = {"CMC": cmc , "mana_cost" : mana_cost, "text" : text, "types": types, "subtypes" : subtypes, "power" : power, "toughness" : toughness, "keywords": itsgot, "colourIdentit" : colourIdentit}
	checkcreature = types.split(" ")

	if "Legendary" in supertype and "Creature" in checkcreature :
		print("Legendary")
		if colourIdentit == "":
			db.child("Commanders").child("colorless").child(name).set(data, user['idToken'])
		else:
			db.child("Commanders").child(colourIdentit).child(name).set(data, user['idToken'])
	if colourIdentit == "" or colourIdentit == " ":
		db.child("Colors").child("colorless").child(name).set(data, user['idToken'])
	else:
		db.child("Colors").child(colourIdentit).child(name).set(data, user['idToken'])


def main():
	
	config = {
	  "apiKey": " AIzaSyAThe5ILc3TGvV_rIxHKxbZfQfMTtdj1jQ ",
	  "authDomain": "deckcreator-d2ddf.firebaseapp.com",
	  "databaseURL": "https://deckcreator-d2ddf.firebaseio.com",	
	  "storageBucket": "deckcreator-d2ddf.appspot.com",
	  "serviceAccount": "/home/conner/Documents/deckcreator-d2ddf-6ce726e6fa03.json" #/home/ethan/Documents/QuarantineProject/deckcreator-d2ddf-6ce726e6fa03.json"
	}
	firebase = pyrebase.initialize_app(config)
	auth = firebase.auth()
	user = auth.sign_in_with_email_and_password("connerbehan1@gmail.com", "12345678")
	sets = open("setCodes.txt", "r")
	line = sets.readlines()
	db = firebase.database()
	print(len(line))
	##41 - 53 is complete
	firstbunch = line[177:220]
	secondbunch = line[221:250]
	thirdbunch = line[251:280]
	fourthbunch = line[281:310]

	p1 = Process(target=collectCard, args=(firstbunch,user, db, auth,  ))
	p2 = Process(target=collectCard, args=(secondbunch,user, db, auth,  ))
	p3 = Process(target=collectCard, args=(thirdbunch,user, db, auth,  ))
	p4 = Process(target=collectCard, args=(fourthbunch,user, db, auth,  ))

	p1.start()	
	p2.start()
	p3.start()
	p4.start()
	p1.join()
	p2.join()
	p3.join()
	p4.join()





if __name__ == '__main__':
	main()