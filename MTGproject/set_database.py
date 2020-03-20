
from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog
import pyrebase
from datetime import datetime
import re
def collectCard():
	keywords = ["Surveil", "enters", "dies", "Flash","Defender", "Deathtouch","enchant", "Enchant", "Equip", "Flying", "Indestructible", "Lifelink", "Cumulative", "Cycling", "Buyback", "Madness", "Morph", "facedown", "Storm", "Affinity", "Ninjutsu", "Dredge", "Wither", "Cascade", "Infect", "Miracle", "Extort", "Prowess", "Jump-Start", "Escape", "create", "Hexproof", "Shroud"]
	listy = []
	
	cards = Card.where(set='ktk').all()
	for card in cards:
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
			checker = "Empty"
		power = card.power
		toughness = card.toughness
		cmc = card.cmc
		colourIdentit = card.color_identity
		addToDatabase(colourIdentit, name, mana_cost, colors, types, subtypes, supertype, text, power, toughness, cmc, itsgot)

def addToDatabase(colourIdentit, name, mana_cost, colors, types, subtypes, supertype, text, power, toughness, cmc, itsgot):
	config = {
	  "apiKey": " AIzaSyAThe5ILc3TGvV_rIxHKxbZfQfMTtdj1jQ ",
	  "authDomain": "deckcreator-d2ddf.firebaseapp.com",
	  "databaseURL": "https://deckcreator-d2ddf.firebaseio.com",
	  "storageBucket": "deckcreator-d2ddf.appspot.com",
	  "serviceAccount": "/home/conner/Documents/deckcreator-d2ddf-6ce726e6fa03.json" #/home/ethan/Documents/QuarantineProject/deckcreator-d2ddf-6ce726e6fa03.json"
	}
	colourIdentit = "%20".join(colourIdentit)
	firebase = pyrebase.initialize_app(config)
	auth = firebase.auth()
	user = auth.sign_in_with_email_and_password("connerbehan1@gmail.com", "") ##Not putting on github
	db = firebase.database()
	data = {"CMC": cmc , "mana_cost" : mana_cost, "text" : text, "types": types, "subtypes" : subtypes, "power" : power, "toughness" : toughness, "keywords": itsgot}
	if colourIdentit == "":
		db.child("Colors").child("colorless").child(name).set(data, user['idToken'])
	else:
		db.child("Colors").child(colourIdentit).child(name).set(data, user['idToken'])


def main():
	collectCard()



if __name__ == '__main__':
	main()


		
