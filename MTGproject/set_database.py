from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog
import pyrebase
from datetime import datetime
def collectCard():
	listy = []
	cards = Card.where(set='ktk').where(subtypes='warrior,human').all()
	for card in cards:
		name = card.name
		mana_cost = card.mana_cost
		colors = card.colors
		types = card.type
		supertype = card.supertypes
		subtypes = card.subtypes
		text = card.text 
		power = card.power
		toughness = card.toughness
		cmc = card.cmc
		colourIdentit = card.color_identity
		print(colourIdentit)
def addToDatabase():
	config = {
	  "apiKey": " AIzaSyAThe5ILc3TGvV_rIxHKxbZfQfMTtdj1jQ ",
	  "authDomain": "deckcreator-d2ddf.firebaseapp.com",
	  "databaseURL": "https://my-application-a29f5.firebaseio.com/",
	  "storageBucket": "deckcreator-d2ddf.firebaseapp.com",
	  "serviceAccount": "/home/conner/Documents/clubhub-270013-9a21263094f2.json" #Not putting on github
	}


def main():
	collectCard()



if __name__ == '__main__':
	main()




		
