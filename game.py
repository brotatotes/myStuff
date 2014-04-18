#!/usr/bin/python
import time

inventory = []
money = 0
health = 100
mana = 0
thankful_passenger = False

def Invalid():
	print "I can't understand that."

def wait(n):
	time.sleep(n)
	#pass

def start():
	print "You wake up as your eyes ease open. It's very dim. You have no idea where you are."
	print "Your back aches as you try to sit up, probably from laying on the hard, rough, rock ground beneath you."
	print "You feel the humidity and smell a slightly unpleasant odor that surrounds you."
	print "As you look around, you notice that all the light, what little of it there is, is coming from a single point in the distance."
	while 1:
		next1 = raw_input("What do you do? A: Get up and walk toward the dim light and risk your safety. B: Go back to sleep. ")
		if next1.lower() == "a":
			print "As you stand up, your head bangs against some sort of ceiling. This 'room' is a lot smaller than you thought."
			print "You stoop down and inch toward the light."
			wait(5)
			print "The closer you get, the more you can make out your surroundings."
			wait(5)
			print "Soon it becomes clear that you are in some sort of a cave. You keep going. At this point the ceiling has dropped so low that you end up crawling toward what you hope is the entrance."
			wait(5)
			print "Your head peeks out through a hole that you judge can just barely fit you through."
			print "You see mountains around you covered in light green vegetation for miles."
			print "As your eyes scan the landscape, you spot an unnatural trail perhaps 30 feet away."
			while 1:
				next2 = raw_input("What do you do? A: Go to the trail. B: crawl back into your cave, where it's safe. ")
				if next2.lower() == "a":
					print "You push yourself out of the cave and trek toward the trail..."
					wait(3)
					trail()
				elif next2.lower() == "b":
					back_into_cave()
				else:
					Invalid()
		elif next1.lower() == "b":
			print "You feel rather drowsy and can't help but lay your head back down..."
			wait(3)
			print "Zzzz"
			wait(3)
			print "Zzzz"
			wait(3)
			start()
		else:
			print "Please enter 'A' or 'B'."

def back_into_cave():
	print "You go back into the cave."
	wait(3)
	print "You think about going to the trail."
	wait(3)
	while 1:
		next3 = raw_input("What do you do? A: Go to the trail. B: crawl back into your cave, where it's safe. ")
		if next3.lower() == "a":
			print "You push yourself out of the cave and trek toward the trail..."
			wait(3)
			trail()
		elif next3.lower() == "b":
			back_into_cave()
		else:
			Invalid()

def trail():
	print "You arrive at the trail. There are no signs as far as you can see. You don't really know where the trail goes, or which direction you should go."
	while 1:
		next4 = raw_input("What do you do? A: Walk along the trail eastward. B: Walk along the trail westward. C: Go back to the cave, where it's safe. ")
		if next4.lower() == "a":
			print "You head along the trail eastward..."
			trail_east_forest()
		elif next4.lower() == "b":
			print "You head along the trail westward..."
			trail_west_town()
		elif next4.lower() == "c":
			print "What a wimp."
			back_into_cave()	
		else:
			Invalid()

def walk_along_trail():
	print "You begin walking along the dirt path."
	wait(2)

def trail_east_forest():
	walk_along_trail()
	print "You can see the flat landscape beginning to recede into a forest in the distance."
	wait(2)
	print "Along the way you run into a rather clumsy young fellow carring a bag, going the opposite direction you're going."
	wait(2)
	print "As he walks past you, he accidentally drops his bag to the ground, spilling its contents."
	print "It was mostly clothing, but you also notice a few books and a quill or too - nothing extraordinary."
	wait(3)
	while 1:
		next5 = raw_input("What do you do? A: Help him gather his things. B: The forest is just ten minutes away! Keep walking. ")
		if next5.lower() == "a":
			wait(1)
			thankful_passenger()
			break
		elif next5.lower() == "b":
			break
		else:
			Invalid()
	forest()

def thankful_passenger():
	print "You help him gather his things. He give you an odd but grateful look. 'Thanks,' he mutters, as he scampers off."
	print "You shrug and continue on your way."
	thankful_passenger = True
	wait(2)


def trail_west_town():
	walk_along_trail()
	#UNFINISHED METHOD

def forest():
	print "You have arrived at the forest. A terrifying sight awaits you. A corpse lies against a tree with markings scratched into its bark. It reads 'DANGER'."
	#UNFINISHED METHOD




























start()

	