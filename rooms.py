rooms = {
    "lobby": {
        "description": "You are in a grand hall with a chandelier hanging from the ceiling. Shockingly, it is empty. You see an arched doorway to four directions.",
        "directions": {
            "north" : "treasury",
            "south" : "library",
            "east" : "reserved armory",
            "west" : "statue"
        },
        "items" : ["pamphlet", "key"]
},
    "treasury": {
        "description" : "You are in a room with chests full of gold and jewels.",
        "directions" : {
            "north" : "nothing",
            "south" : "lobby",
            "east" : "nothing",
            "west" : "nothing"
    },
        "items" : ["bag of gold", "ruby necklace"]   
},
    "library" : {
        "description" : "There is a huge collection of books here.",
        "directions" : {
            "north" : "lobby",
            "south" : "nothing",
            "east" : "door",
            "west" : "nothing"
        },
        "items" : ["red scroll"]
    },
    "reserved armory" : {
        "description" : "You see a collection of weapons and armor. As you look around, you cannot avoid feeling unease remembering how each of these weapons were used in battle.",
        "directions" : {
            "north" : "nothing",
            "south" : "nothing",
            "east" : "nothing",
            "west" : "lobby"
        },
        "items" : [""]
    },
    "statue" : {
        "description" : "There is a statue of King Medhias here. It looks like it has something in its hand. When you checked closer, you see that it is a silver dagger",
        "directions" : {
            "north" : "nothing",
            "south" : "nothing",
            "east" : "lobby",
            "west" : "nothing"
        },
        "items" : ["silver dagger"]
    },
}