import json
import urllib.request

def makeAPICall(pokemon):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
    headers={'User-Agent':user_agent,}
    request=urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data = response.read() # The data u need
    jsonData = json.loads(data)
    print(jsonData)
    moves = jsonData.get("moves")

    move = moves[0]
    moveDictionary = move["move"]
    print(moveDictionary["name"])

#makeAPICall("ditto")

strategies = {"Ditto": ["Moves: Transform; Ability: Imposter; Item: Choice Scarf; "
         "Analysis: Ditto's main usage is for extremely stat boosted opponents, simply send out Ditto since "
         "Imposter will automatically transform into the opponent, with choice scarf and the same stat boosts,"
         "Ditto should be able to over power most of the opponent's pokemon by using their own strategy against them!"],
"Durant": ["Moves: Iron Head, Rock Slide, X-Scissor, Thunder Wave; Ability: Hustle; Item: Zoom Lens; Durant's "
        "capabilities lie within physical strength and speed, Hustle adding onto the strength but decrasing accuracy,"
        "in this case we use the Zoom Lens to regain that accuracy. With the combination of moves, and thunder wave"
        "to decrease speed or lose a turn, the opponent's pokemon may not stand a chance! If you have a pokemon with"
        "hone claws and baton pass alongside this monster ant, then you're chances of winning are pretty high!"],
"Bruxish": ["Moves: Psychic Fangs, Aqua Jet, Ice Fang, Swords Dance; Ability: Strong Jaw; Item: Focus Sash; "
            "Like a Durant, this pokemon's capabilities are within its physical strength and speed. However, the"
            "difference lies within its move pool, being more diverse, and Strong Jaws, allowing the fang moves to"
            "increase in damage. A focus sash is probably a smart choice for a Swords Dance to boost your physical"
            "Attack, leaning you more to victory. While Aqua Jet, a priority move, will go before most moves that have"
            "less of a priority!"],
"Kabutops": ["Moves: Aqua Jet, Stone Edge, Swords Dance, Ariel Ace; Ability: Swift Swim; Item: Life Orb; Kabutops"
             "Itself is pretty weak, only good in physical offense and defense, but can easily be beaten with special"
             "attacks. In order to utilize Kabutops to the fullest, have a Drizzle pokemon on your team out in front,"
             "especially if it could set up some hazards on the opponents side. With Drizzle, rain will be summoned,"
             "allowing Kabutops to utilize a speed boost from Swift Swim. If you're able to obtain a Swords Dance"
             "without a death, I suggest it. However if not, utilize the moment to deal extra damage, especially since"
             "the Life Orb on Kabutops gives it an extra boost for a price of a bit of HP."],
"Drapion" : ["Moves: Earthquake, Cross Poison, Ice Fang, Swords Dance; Ability: Battle Armor; Item: Air Balloon; "
             "Drapion is already a tank in itself, being it's only real weakness being Ground-type moves, counter this"
             "with Air Balloon, though it's a one time trick, be warned. Use this to your advantage to get Swords Dance"
             "in, and then attack, specifically with Cross Poison, it might not have as much damage as Poison Jab, but"
             "with a high critical chance the 10 damage reduction is all good. Other moves are for coverage, such as"
             "Ice Fang for Ground, Flying etc., and Earthquake for Rock, Steel Electric, etc."],
"Yanmega": ["Move: Protect, Bug Buzz, Toxic, Air Slash; Ability: Speed Boost; Item: Life Orb; To be honest, this "
            "set may seem a little odd, but used in certain predicaments I think Yanmega can definitely help drain"
            "your opponents health. Most people may believe you're going to protect first because of Speed Boost,"
            "use this chance to poison the opponent with Toxic, then Protect, if you're trying to bank on luck double"
            "protect, if not use whichever move is more opportunistic, with the Life Orb, Yanmega should definitely"
            "be a fantastic asset."],
"Galvantula": ["Moves: Thunder, Bug Buzz, Sticky Web, Thunder Wave; Ability Compound Eyes; Item: Life Orb; Galvantula"
               "Is an incredible pokemon! It's prevolution is adorable, it's fast and, yeah no that's absolute bias."
               "In reality it is actually decent, able to use Thunder Wave to cut down speed and give paralysis,"
               "Thunder is now increased with accuracy thanks to Compound Eyes. Bug Buzz will be able to have STAB and"
               "coverage in case you're fighting a ground type. Alongside Sticky Web which is a speed hazard, a "
               "Galvantuala should be a terrific asset on your team!"]}

pokemon = {1: "Ditto", 2: "Durant", 3: "Bruxish", 4: "Kabutops", 5: "Drapion", 6: "Yanmega", 7: "Galvantula"}

moves = {"Ditto": "ditto", "Durant": "durant", "Bruxish": "bruxish", "Kabutops": "kabutops",
         "Drapion": "drapion", "Yanmega": "yanmega", "Galvantula": "galvantula"}

def displayStrategy(key):
    pokeinfo = pokemon.get(key)
    strategy = strategies.get(pokeinfo)
    pokemoves = moves.get(pokeinfo)
    learnset = makeAPICall(pokemoves)
    print(strategy)
    print(learnset)


def getSearchKey():
    count = 1
    for key in strategies:
        print(count, ") ", key)
        count +=1
    selection = input("Select the placement number of the Pokemon you'd like to view:")
    return selection


#make sure selection is valid (digit between 1-???)

while True:
    try:
        key = int(getSearchKey())
        if key >=1 and key <= len(strategies):
            displayStrategy(key)
        else:
            print(key, " not a valid pokemon")

    except:
        print("Dude, a number please, not letters")
