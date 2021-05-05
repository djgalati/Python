import pickle

story = {
    'Intro':{
		    'Text': [
			      "You wake up from a wonderful nap flying high through blue skies over the Pacific only to hear a baby crying and all of sudden loud alrams start screaming into your ears! The plane jumps, rocks everyone all through the cabin sending luggage everywhere. You become numb from fear, sticking your head between your legs as the plane starts to lose altitude. You try to remain concious but the g forces and lack of oxygen make you black out and the last thing you see is a mother screaming and trying to save her child."
                    ],
          'Actions': [
          ]
	  },
	  'Crash Site': {
		    'Text': [
            "When you wake up, you find you are up to your waist in water. You look around and find you are alone. You are the only survivor. The plane has crashed a few meters away from the coast of an unknown island. The plane is slowly sinking."
		    ],
		    'Actions': [
            ('Grab batteries', '1'),
            ("Grab first-aid kit", '2'),
			      ("Salvage plane radio system", '3'),
			      ("Leave the Crash Site", 'Move')
		    ]	
	  },
	  'Beach':{
		    'Text':[
			      "As you wade back through the water onto dry land, you gather as many items as you can find and pack them into a bag. You have matches, a bottle of water, a flare gun, and some food. This will only last you so long. Now you must survive at all cost!"
		    ],
		    'Actions':[
			      ("Start campfire", '1'),
			      ("Enter shelter", '2'),
			      ("Leave the Beach", 'Move')
		    ]
	  },
	  'Fishing Area':{
		    'Text':[
			      "As you look to explore the island for more supplies, you look into the jungle and feel a hard sense of fear. It feels much safer staying on the beach, so you decide to head north sticking to the sand. After walking a mile you happen upon a lagoon full of tropical looking fish, which means food!"
		    ],
		    'Actions':[
			      ("Start fishing", '1'),
			      ("Leave the Fishing Area", 'Move')
		    ]
	  },
          'Abandoned Campsite':{
		    'Text':[
			      "After catching some fish for food, you feel a little more secure. You have fire and food capabilites now. The will to explore this unknown island compels you to continue, you again head north! \nYou now have entered an abanonded campsite.... \nWere there other people here before you? \nMaybe this island isn't as desserted as you think..."
		    ],
		    'Actions':[
			      ("Grab Food", '1'),
			      ("Leave the Campsite", 'Move')
		    ]
	  },
          'Empty Land':{
		    'Text':[
			      "After searching the campsite for food, you realize th area has a dark vibe. You see two skeletons draped in torn and weathered clothing... You searhch the long dead bodies and find nothing but expired hot dogs and moldy buns. You relaize there is nothing here for you but death staring you in the face...you decide to explore west into the jungle! \nAfter navigating the thick jungle for what seems like hours you break out into a large clearing of land. There is nothing here, seems strange, not even a blade of grass..."
		    ],
		    'Actions':[
			      ("Leave the Empty Land", 'Move')
		    ]
	  },
          'Bunker':{
		    'Text':[
			      "As your exploring the empty, dusty land, you trip over something and fall hard. You get up quickly wiping the dust and blood from your face. What could have possibly tripped you in this desolate spit of land.... \nYou look down and see a large metallic handle...that looks like it is attached to and door? \nIt takes every last ounce of strength you have to lift this handle and pull the underground door open.  \nA dark maw containingg a rusty ladder faces you! What could such a place contain? Death maybe? Rescue maybe? Either way you decide to climb in..."
		    ],
		    'Actions':[
			      ("Take torn island map", '1'),
			      ("Leave the Bunker", 'Move')
		    ]
	  },
          'Secret Island':{
		    'Text':[
			      "After searhcing the dark and dank hallways of what looks like the remants of German Nazi WWII munitions bunker, you find a torn map of the island that is missing peices but you notice another smaller island off south east of the beach you washed up on. Where the island is depicted you see an image if a radio. Thinking there may be a radio on the island you backtrack the way you came returning to the beach. You then head south turning turning the corner of the island to see the off shore island on the horizon. Having no boat you must swim...the water looks rough and the distance long but if there is a radio for rescue, you must try... \n\n After nearly drowning, you somehow make it to the Secret Island where all seems silent...a little too silent..."
		    ],
		    'Actions':[
			      ("Grab Coconut", '1'),
			      ("Leave the Secret Island", 'Move')
		    ]
	  },
          'Hidden Cave':{
		    'Text':[
			      "You enter the silent, eery jungle, where you find another trail that looks human made. You wearily foolow the trail, now hearing loud roars from the trees you start running! Up ahead you see a rock wall, as you get closer you see the entrance to a darkened cave. The roars seem to be getting closer every second, you decide to enter the hidden cave!"
		    ],
		    'Actions':[
			      ("Grab tool", '1'),
			      ("Leave the Cave", 'Move')
		    ]
	  },
          'Graveyard':{
		    'Text':[
			      "Sprinting through the cave with reckless abanoned you evevtully pop out into another clearing sorrounded by rock. As you slow down to catch your breath you notice what looks like an ancient graveyard..."
		    ],
		    'Actions':[
			      ("Inspect tombstone", '1'),
			      ("Leave the Graveyard", 'Move')
		    ]
	  },
          'Biohazard Area':{
		    'Text':[
			      "After you explore the graveyard you look for anything that might contain the 'supposed' radio. Searching graves leads to findning nothing but bones, you have hit a dead end... \nYou decide this was a giant waste of time and have to head back to the beach. It is now starting to get dark, you must make it back to the beach as fast as possible. \nYou again run back into the cave and out through the dark jungle, swim back to the main island and head north again towards the beach you started upon.. \nYou make a fire, cook some fish and decide to rest for the night.  \nAs your falling asleep by the fire you remeber there was an area of the map you found missing. You decide to to that area to explore first thing in the morning. \nAs you awake the sense of hopelessness tries to take you over. What is this island and where did everyone go? \nAccording to the map, the missing is directly of the beach so you head thata way. Again feeling safer you stick to the sand, after a hour of walking you start to notice the jungle in the area looks infected and dieing. Through the dying foliage you see what looks like a work site of some sort that is covered in a misty haze. As you approach the hazardous site you notice just a single oil barrell standing alone"
		    ],
		    'Actions':[
			      ("Open Barrel", '1'),
			      ("Leave the Biohazard Area", 'Move')
		    ]
	  },
          'END':{
		    'Text':[
			      "HAHA when you opened that barrel, A zombie ate you, You have completed the game, Goodbye"
		    ],
		    'Actions':[
		    ]
	  }
}

with open('Test.ch', 'wb') as chapter:
  pickle.dump(story, chapter)
