# Interactive character creator in Python for Fallout
# Uses SPECIAL system

# import libraries
import math
import pickle

# starting character info
choice = None
genetics = None
background = None
Traits = []
traitn = 1
Perks = []
perkn = 0

# starting resistances
rres = 0
pres = 0
fres = 0
dres = 0
cres = 0
eres = 0

# starting karma
karma = 0

# starting tag skills
tags = 3

# raw stat values
strev = 5
percv = 5
enduv = 5
charv = 5
intev = 5
agilv = 5
luckv = 5
# stat value
statv = {'stre': 5, 'perc': 5, 'endu': 5, 'char': 5, 'inte': 5, 'agil': 5, 'luck': 5}
# raw stat bonus
streb = 1
percb = 1
endub = 1
charb = 1
inteb = 1
agilb = 1
luckb = 1
# stat bonus
statb = {'stre': 1, 'perc': 1, 'endu': 1, 'char': 1, 'inte': 1, 'agil': 1, 'luck': 1}
# raw skill value
bartv = 0
biggv = 0
enerv = 0
explv = 0
lockv = 0
mediv = 0
melev = 0
pilov = 0
repav = 0
sciev = 0
smalv = 0
sneav = 0
speev = 0
steav = 0
survv = 0
unarv = 0
# skill value
skils = {'bart': 0, 'bigg': 0, 'ener': 0, 'expl': 0, 'lock': 0, 'medi': 0, 'mele': 0, 'pilo': 0, 'repa': 0, 'scie': 0, 'smal': 0, 'snea': 0, 'spee': 0, 'stea': 0, 'surv': 0, 'unar': 0}

# stat bonus
def stat_bonus():
    for stat in statv.keys():
        if statv[stat] < 5:
            statb[stat] = 0
        elif statv[stat] > 4 and statv[stat] < 8:
            statb[stat] = 1
        elif statv[stat] > 7 and statv[stat] < 10:
            statb[stat] = 2
        elif statv[stat] == 10:
            statb[stat] = 3
        else:
            print 'Error! Stat cannot be zero!'

# dependent variables
hp = (statv['endu'] + statv['stre']) * 5
hr = statb['endu'] + 1
ud = statb['stre'] + 1
sp = statb['inte'] + 1
cw = (statv['stre'] * 10) + 30

# initialize constants
POOL = 5

while choice != 0:

    print("""
    =========================
    Fallout Character Creator
    Copyright RobCo Ind. 2077
    =========================

    Please select an option:
    0 - Quit
    1 - Create new character

    """)

    choice = input("Choice: ")
    #print()

    if choice == 0:
        print("Goodbye!")
        break

    elif choice == 1:
        pool = 5
        print("""
        
        STEP ONE: NAME YOUR CHARACTER
        
        """)

        name = raw_input("\nYour name: ")
        #while name  == "":
        #    name = raw_input("Your name: ")
        cname = name.capitalize()

        print("""

        STEP TWO: DETERMINE STATS

        """)

        print("\nCurrent stats:\n")

        print "Strength: %s" % (statv['stre'])
        print "Perception: %s" % (statv['perc'])
        print "Endurance: %s" % (statv['endu'])
        print "Charisma: %s" % (statv['char'])
        print "Intelligence: %s" % (statv['inte'])
        print "Agility: %s" % (statv['agil'])
        print "Luck: %s" % (statv['luck'])

        while pool > 0:
            
            print "You have %s points to spend." % (pool)

            addsub = raw_input("\n(A)dd or (S)ubtract a stat point? (A/S): ")
            #print()

            if addsub == "A":
                print("""
                Choose a stat to add a point:

                1 - Strength
                2 - Perception
                3 - Endurance
                4 - Charisma
                5 - Intelligence
                6 - Agility
                7 - Luck
                
                """)
                statc = input("Stat: ")
                #print()

                if statc == 1:
                    strev += 1
                    statv['stre'] = strev
                    pool -= 1
                    print "Strength: %s" % (statv['stre'])
                    continue
                elif statc == 2:
                    percv += 1
                    statv['perc'] = percv
                    pool -= 1
                    print "Perception: %s" % (statv['perc'])
                    continue
                elif statc == 3:
                    enduv += 1
                    statv['endu'] = enduv
                    pool -= 1
                    print "Endurance: %s" % (statv['endu'])
                    continue
                elif statc == 4:
                    charv += 1
                    statv['char'] = charv
                    pool -= 1
                    print "Charisma: %s" % (statv['char'])
                    continue
                elif statc == 5:
                    intev += 1
                    statv['inte'] = intev
                    pool -= 1
                    print "Intelligence: %s" % (statv['inte'])
                    continue
                elif statc == 6:
                    agilv += 1
                    statv['agil'] = agilv
                    pool -= 1
                    print "Agility: %s" % (statv['agil'])
                    continue
                elif statc == 7:
                    luckv += 1
                    statv['luck'] = luckv
                    pool -= 1
                    print "Luck: %s" % (statv['luck'])
                    continue
                else:
                    print("\nYou fucked it up! Shit, man...")
                    continue

            elif addsub == "S":
                print("""
                Choose a stat to subtract a point:

                1 - Strength
                2 - Perception
                3 - Endurance
                4 - Charisma
                5 - Intelligence
                6 - Agility
                7 - Luck

                """)
                statc = input("Stat: ")
                #print()

                if statc == 1:
                    strev -= 1
                    statv['stre'] = strev
                    pool += 1
                    print "Strength: %s" % (statv['stre'])
                    continue
                elif statc == 2:
                    percv -= 1
                    statv['perc'] = percv
                    pool += 1
                    print "Perception: %s" % (statv['perc'])
                    continue
                elif statc == 3:
                    enduv -= 1
                    statv['endu'] = enduv
                    pool += 1
                    print "Endurance: %s" % (statv['endu'])
                    continue
                elif statc == 4:
                    charv -= 1
                    statv['char'] = charv
                    pool += 1
                    print "Charisma: %s" % (statv['char'])
                    continue
                elif statc == 5:
                    intev -= 1
                    statv['inte'] = intev
                    pool += 1
                    print "Intelligence: %s" % (statv['inte'])
                    continue
                elif statc == 6:
                    agilv -= 1
                    statv['agil'] = agilv
                    pool += 1
                    print "Agility: %s" % (statv['agil'])
                    continue
                elif statc == 7:
                    luckv -= 1
                    statv['luck'] = luckv
                    pool += 1
                    print "Luck: %s" % (statv['luck'])
                    continue
                else:
                    print("\nYou fucked it up! Shit, man...")
                    continue
            else:
                print("\nYou fucked it up! Shit, man...")
                continue
        else:
            print("\nBase stats selected:\n")
            print "Strength: %s" % (statv['stre'])
            print "Perception: %s" % (statv['perc'])
            print "Endurance: %s" % (statv['endu'])
            print "Charisma: %s" % (statv['char'])
            print "Intelligence: %s" % (statv['inte'])
            print "Agility: %s" % (statv['agil'])
            print "Luck: %s" % (statv['luck'])

        print("""
        
        STEP THREE: DETERMINE GENETICS
        
            1 - Pure Strain Human
                ( +2 stat points )
            2 - Wasteland Human
                ( +2 chem and rad resist )
            3 - Ghoul
                ( Heal x2 when irradiated,
                  +4 chem resist, -1 Str,
                  -1 Agl, -1 Chr )
            4 - Super Mutant
                ( Rad resist of 10, +1 DR,
                  +2 Str, -2 Agl, -2 Chr )
            5 - Abomination
                ( Rad resist of 10, +2 DR,
                  -1 to all skills )
            6 - Inorganic
                ( Poison, rad resist of 10,
                  +2 DR, -2 all skills except
                  tag skills, Luck of 5 )

        """)

        genec = input("Choose your genetic species: ")
        #print()

        if genec == 1:
            print("You chose Pure Strain Human.")
            
            genetics = "Pure Strain Human"
            
            freepoints = 2
            
            while freepoints > 0:
                print "\nYou have %s points to spend." % (freepoints)
                print "\nCurrent stats: \n"
                print "Strength: %s" % strev
                print "Perception: " % percv
                print "Endurance: %s" % enduv
                print "Charisma: %s" % charv
                print "Intelligence: %s" % intev
                print "Agility: %s" % agilv
                print "Luck: %s" % luckv

                print("""
                You may select one stat at a time.

                1 - Strength
                2 - Perception
                3 - Endurance
                4 - Charisma
                5 - Intelligence
                6 - Agility
                7 - Luck

                """)
                statc = input("Choose a stat to increase: ")
                #print()

                if statc == 1:
                    strev += 1
                    statv['stre'] = strev
                    freepoints -= 1
                    print "Strength: %s" % (statv['stre'])
                elif statc == 2:
                    percv += 1
                    statv['perc'] = percv
                    freepoints -= 1
                    print "Perception: %s" % (statv['perc'])
                elif statc == 3:
                    enduv += 1
                    statv['endu'] = enduv
                    freepoints -= 1
                    print "Endurance: %s" % (statv['endu'])
                elif statc == 4:
                    charv += 1
                    statv['char'] = charv
                    freepoints -= 1
                    print "Charisma: %s" % (statv['char'])
                elif statc == 5:
                    intev += 1
                    statv['inte'] = intev
                    freepoints -= 1
                    print "Intelligence: %s" % (statv['inte'])
                elif statc == 6:
                    agilv += 1
                    statv['agil'] = agilv
                    freepoints -= 1
                    print "Agility: %s" % (statv['agil'])
                elif statc == 7:
                    luckv += 1
                    statv['luck'] = luckv
                    freepoints -= 1
                    print "Luck: %s" % (statv['luck'])
                else:
                    print "\nYou fucked up! Shit, man!"
                    continue
            else:
                break

        elif genec == 2:
            print "You chose Wasteland Human."

            genetics = "Wasteland Human"

            cres += 2
            rres += 2
                
        elif genec == 3:
            print("You chose Ghoul.")

            genetics = "Ghoul"

            cres += 4

            strev -= 1
            statv['stre'] = strev
            agilv -= 1
            statv['agil'] = agilv
            charv -= 1
            statv['char'] = charv

        elif genec == 4:
            print("You chose Super Mutant.")

            genetics = "Super Mutant"

            rres = 10
            dres += 1

            strev += 2
            statv['stre'] = strev
            agilv -= 2
            statv['agil'] = agilv
            charv -= 2
            statv['char'] = charv

        elif genec == 5:
            print("You chose Abomination.")

            abomname = raw_input("Name your Abomination Species: ")
            #print()

            genetics = abomname

            rres = 10
            dres += 2

            for skilv in int(["bartv", "biggv", "enerv", "explv", "lockv", "mediv", "melev",  "pilov", "repav", "sciev", "smalv", "sneav", "speev", "steav", "survv", "unarv"]):
                skilv -= 1    

        elif genec == 6:
            print("You chose Inorganic.")

            inorgname = raw_input("Name your Inorganic Robot Species: ")
            #print()
            
            genetics = inorgname

            pres = 10
            rres = 10
            dres += 2
        
            for skilv in int(["bartv", "biggv", "enerv", "explv", "lockv", "mediv", "melev",  "pilov", "repav", "sciev", "smalv", "sneav", "speev", "steav", "survv", "unarv"]):
                skilv -= 2
            
            luckv = 5
            statv['luck'] = luckv

        else:
            print("\nYou fucked up! Shit, man.")

        if genetics == "Pure Strain Human":
            print("""
            
            STEP FOUR: DETERMINE BACKGROUND

            1 - Vault Dweller
                ( +1 Science, +1 Speech )
            2 - Elite Order
                ( +1 tag skill, +1 Energy Weapons )
            
            """)
        
        else:
            print("""
        
            STEP FOUR: DETERMINE BACKGROUND
        
            1 - Vault Dweller
                ( +1 Science, +1 Speech )
            2 - Elite Order
                ( +1 tag skill, +1 Energy Weapons )
            3 - Settler
                ( +1 Barter, +1 Repair )
            4 - Wastelander
                ( +1 Sneak, +1 Lockpick )
            5 - Tribal
                ( +1 Survival, +1 Melee )
            6 - Raider
                ( -4 Karma, + Chem Tolerant trait)
            7 - Experimental
                ( Choose 2 extra starting Perks )
            8 - Mysterious
                ( Create your own )

            """)

        bgrdc = input("Choose your background: ")
        #print()

        if bgrdc == 1:
            print("You chose Vault Dweller")

            background = "Vault Dweller"

            skils['scie'] += 1
            skils['spee'] += 1

        elif bgrdc == 2:
            print("You chose Elite Order")

            background = "Elite Order"

            tags += 1

            skils['ener'] += 1

        elif bgrdc == 3:
            print("You chose Settler")

            background = "Settler"

            skils['bart'] += 1
            skils['repa'] += 1

        elif bgrdc == 4:
            print("You chose Wastelander")

            background = "Wastelander"

            skils['snea'] += 1
            skils['lock'] += 1

        elif bgrdc == 5:
            print("You chose Tribal")

            background = "Tribal"

            skils['surv'] += 1
            skils['mele'] += 1

        elif bgrdc == 6:
            print("You chose Raider")

            background = "Raider"

            karma -= 4

            Traits.append('Chem Tolerant')

        elif bgrdc == 7:
            print("You chose Experimental")
            
            background = "Experimental"

            perkn = 2
            
            while perkn > 0:
                print("""
                Select a perk from the following list:

                1 - Black Widow (female)
                2 - Lady Killer (male)
                3 - Cherchez La Femme (female)
                4 - Confirmed Bachelor (male)
                5 - Gun Nut
                6 - Little Leaguer
                7 - Thief
                8 - Swift Learner
                9 - Intense Training

                """)

                xperk = input("Choose your experimental perk: ")
                #print()

                if xperk == 1:
                    Perks.append('Black Widow')
                    perkn -= 1
                    continue
                elif xperk == 2: 
                    Perks.append('Lady Killer')
                    perkn -= 1
                    continue
                elif xperk == 3:
                    Perks.append('Cherchez La Femme')
                    perkn -= 1
                    continue
                elif xperk == 4:
                    Perks.append('Confirmed Bachelor')
                    perkn -= 1
                    continue
                elif xperk == 5:
                    Perks.append('Gun Nut')
                    perkn -= 1
                    continue
                elif xperk == 6:
                    Perks.append('Little Leaguer')
                    perkn -= 1
                    continue
                elif xperk == 7:
                    Perks.append('Thief')
                    perkn -= 1
                    continue
                elif xperk == 8:
                    Perks.append('Swift Learner')
                    perkn -= 1
                    continue
                elif xperk == 9:
                    Perks.append('Intense Training')
                    perkn -= 1
                    continue
                else:
                    print("You fucked up! Shit, man.")
                    continue
            else:
                break

        elif brgdc == 8:
            print("You chose Mysterious")

            background = "Mysterious"

        else:
            print("You fucked up! Shit, man.")

    else:
        break
