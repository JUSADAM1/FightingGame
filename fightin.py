
import random
import time
import os

# -----------------------------------Variables----------------------------------- #
enemy_name = ''
enemy_race = ''
enemy_hitpoints = 50
enemy_armorclass = 1
enemy_attack = 6
races = ['human', 'orc', 'goblin', 'dwarf', 'troll', 'elf', 'halfling', 'gnome']
usr_name = ''
usr_race = ''
usr_hitpoints = 50
usr_armorclass = 1
usr_attack = 7
race_human = {'HP_Mod': 3, 'AC_Mod': 0, 'ATK_Mod': 1}
race_orc = {'HP_Mod': 7, 'AC_Mod': 4, 'ATK_Mod': 3}
race_goblin = {'HP_Mod': 4, 'AC_Mod': 2, 'ATK_Mod': 2}
race_dwarf = {'HP_Mod': 6, 'AC_Mod': 4, 'ATK_Mod': 3}
race_troll = {'HP_Mod': 3, 'AC_Mod': 3, 'ATK_Mod': 2}
race_elf = {'HP_Mod': 8, 'AC_Mod': 2, 'ATK_Mod': 2}
race_halfling = {'HP_Mod': 6, 'AC_Mod': 4, 'ATK_Mod': 2}
race_gnome = {'HP_Mod': 6, 'AC_Mod': 4, 'ATK_Mod': 2}
RACE_STATS = [race_human, race_orc, race_goblin, race_dwarf, race_troll, race_elf, race_halfling, race_gnome]

trashtalk = ['Do you even lift???', 'Who\'s this guy?']
enemy_miss = ['*crys*', '*rages*', 'Who said you could move!', 'WOW!', 'Whoops', 'NO!', 'You got away this time!',
              'I\'ll get you next time', 'I have failed you mother!', '*Sits in silence thinking about life*',
              'That\'s not fair!', 'Bruh...']
KILLS = -1
# ------------------------------------------------------------------------------- #
os.system("color 17")


# Setting User Stats
def usr_stats(race):
    global usr_hitpoints
    global usr_armorclass
    global usr_attack
    if race == 'human':
        usr_hitpoints += race_human['HP_Mod']
        usr_armorclass += race_human['AC_Mod']
        usr_attack += race_human['ATK_Mod']
    elif race == 'orc':
        usr_hitpoints += race_orc['HP_Mod']
        usr_armorclass += race_orc['AC_Mod']
        usr_attack += race_orc['ATK_Mod']
    elif race == 'goblin':
        usr_hitpoints += race_goblin['HP_Mod']
        usr_armorclass += race_goblin['AC_Mod']
        usr_attack += race_goblin['ATK_Mod']
    elif race == 'dwarf':
        usr_hitpoints += race_dwarf['HP_Mod']
        usr_armorclass += race_dwarf['AC_Mod']
        usr_attack += race_dwarf['ATK_Mod']
    elif race == 'troll':
        usr_hitpoints += race_troll['HP_Mod']
        usr_armorclass += race_troll['AC_Mod']
        usr_attack += race_troll['ATK_Mod']
    elif race == 'elf':
        usr_hitpoints += race_elf['HP_Mod']
        usr_armorclass += race_elf['AC_Mod']
        usr_attack += race_elf['ATK_Mod']
    elif race == 'halfling':
        usr_hitpoints += race_halfling['HP_Mod']
        usr_armorclass += race_halfling['AC_Mod']
        usr_attack += race_halfling['ATK_Mod']
    elif race == 'gnome':
        usr_hitpoints += race_gnome['HP_Mod']
        usr_armorclass += race_gnome['AC_Mod']
        usr_attack += race_gnome['ATK_Mod']
    else:
        None


# Setting Enemy Stats
def enemy_stats(race):
    global enemy_hitpoints
    global enemy_armorclass
    global enemy_attack
    global ENEMY_STATS
    if race == 'human':
        enemy_hitpoints += race_human['HP_Mod']
        enemy_armorclass += race_human['AC_Mod']
        enemy_attack += race_human['ATK_Mod']
    elif race == 'orc':
        enemy_hitpoints += race_orc['HP_Mod']
        enemy_armorclass += race_orc['AC_Mod']
        enemy_attack += race_orc['ATK_Mod']
    elif race == 'goblin':
        enemy_hitpoints += race_goblin['HP_Mod']
        enemy_armorclass += race_goblin['AC_Mod']
        enemy_attack += race_goblin['ATK_Mod']
    elif race == 'dwarf':
        enemy_hitpoints += race_dwarf['HP_Mod']
        enemy_armorclass += race_dwarf['AC_Mod']
        enemy_attack += race_dwarf['ATK_Mod']
    elif race == 'troll':
        enemy_hitpoints += race_troll['HP_Mod']
        enemy_armorclass += race_troll['AC_Mod']
        enemy_attack += race_troll['ATK_Mod']
    elif race == 'elf':
        enemy_hitpoints += race_elf['HP_Mod']
        enemy_armorclass += race_elf['AC_Mod']
        enemy_attack += race_elf['ATK_Mod']
    elif race == 'Halfling':
        enemy_hitpoints += race_halfling['HP_Mod']
        enemy_armorclass += race_halfling['AC_Mod']
        enemy_attack += race_halfling['ATK_Mod']
    elif race == 'gnome':
        enemy_hitpoints += race_gnome['HP_Mod']
        enemy_armorclass += race_gnome['AC_Mod']
        enemy_attack += race_gnome['ATK_Mod']
    else:
        None
    ENEMY_STATS = {'NAME': enemy_name, 'HITPOINTS': enemy_hitpoints, 'ARMORCLASS': enemy_armorclass,
                   'ATTACK': enemy_attack, 'RACE': enemy_race, 'BLOCK': 'false'}


# Print Out Text!
def slowtext(u):
    for i in u:
        time.sleep(.03)
        print(i, end='')
    nl()


# Makes a new line
def nl():
    print('\n')


# Generates An Enemy
def genEnemy():
    #generates the AI player race
    global enemy_race
    #generates the names
    global enemy_name
    #adds the stats given to AI
    #so it knows what stats to use for what races it is using
    global enemy_stats
    #The time in which the AI and the program moves itself
    #also sets the time limit between attacks
    global slowtext
    #A friend of mine who I play Dungeons and Dragons with helped me pick so names out
    male_names = ['Grosssmash', 'Dogplunder', 'Greenfoot', 'Shriekvenger', 'Redface', 'Cruelanger',
                  'Redspark', 'Traphammer', 'Cruelvenger', 'Inatheyiu', 'Thaleriu', 'Scatinoo',
                  'Hexaneskiu', 'Stingtansol', 'Herinon', 'Fretharum', 'Matun', 'Funochun', 'Awdpio', 'Wardov',
                  'Laridan', 'Cilired', 'Borewin', 'Gwiratha', 'Falenidd', 'Galeamos', 'Morlune', 'Miriawan', 'Higo',
                  'Foli', 'Voilir',
                  'Dumli', 'Glegnus', 'Fulin', 'Febur', 'Gagan', 'Noiin', 'Toimli', 'Huginn', 'Jengo', 'Zobogo',
                  'Trojahsus', 'Galjin',
                  'Chesuk', 'Baba', 'Mezilalor', 'Zic', 'Maji', 'Texmon']
    #AI player races choice
    enemy_race = random.choice(races)
    #Plus the random name
    enemy_name = random.choice(male_names)
    #plus the AI stats depending upon who he or she uses it.
    enemy_stats(enemy_race)


# Initiate Users Character
#User Interface
#STILL IN THE WORKS
def user_char():
#STILL A WORK IN PROGRESS
    global usr_name
    global usr_race
    global USER_CHARARCTER_STATS

    print('-'*90)
    print('-'*90)
    print(' __     __     ______     __         ______     ______     __    __     ______    ')
    print('/\ \  _ \ \   /\  ___\   /\ \       /\  ___\   /\  __ \   /\ "-./  \   /\  ___\   ')
    print('\ \ \/ ".\ \  \ \  __\   \ \ \____  \ \ \____  \ \ \/\ \  \ \ \-./\ \  \ \  __\   ')
    print(' \ \__/".~\_\  \ \_____\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \ \_\  \ \_____\ ')
    print('  \/_/   \/_/   \/_____/   \/_____/   \/_____/   \/_____/   \/_/  \/_/   \/_____/ ')
    print('*'*90)
    print(' ______   __         ______     __  __     ______     ______                      ')
    print('/\  == \ /\ \       /\  __ \   /\ \_\ \   /\  ___\   /\  == \                     ')
    print('\ \  _-/ \ \ \____  \ \  __ \  \ \____ \  \ \  __\   \ \  __<                     ')
    print(' \ \_\    \ \_____\  \ \_\ \_\  \/\_____\  \ \_____\  \ \_\ \_\                   ')
    print('  \/_/     \/_____/   \/_/\/_/   \/_____/   \/_____/   \/_/ /_/                   ')
    print('-'*90)
    print('The GOD of this program was not sober when he made it so have fun')
    print('-'*90)
    print('In this game you the player will be battling against another race which is randomly generated.')
    print('THE GAME IS TIMED SO IF YOU DO NOT REACT FAST ENOUGH YOU WILL LOOSE!!!!')
    print('The game only gets harder as you beat other players')
    usr_name = input('Please Type your Character Name:  ')
    racechoice = True
    while racechoice == True:
        slowtext("Pick a race: 'Human', 'Orc', 'Goblin', 'Dwarf', 'Troll', 'Elf', 'Halfling', or 'Gnome'")
        usr_race = input('Race:  ')
        for i in races:
            if usr_race.lower() == i.lower():
                usr_race = i
                racechoice = False
                break
            else:
                None
    usr_stats(usr_race)
#GETS USERS CHARACTER NAME, STATS OF RACES AND THE AMOUNT OF DAMAGE.
#TECHNICALLY PRINTS ALL THAT AND THE
    USER_CHARARCTER_STATS = {'NAME': usr_name, 'HITPOINTS': usr_hitpoints, 'ARMORCLASS': usr_armorclass,
                             'ATTACK': usr_attack, 'RACE': usr_race, 'BLOCK': 'false', 'KILLS': KILLS}


# Roll A Random Number
def roll():
    global roll_number
    roll_number = random.randrange(1, 21)
    return roll_number


def Forfeit():
    global forfeit
    roll1 = roll()
    roll2 = roll()
    roll3 = roll()
    if roll1 == roll2 and roll2 == roll3:
        slowtext('*%s decided to kill you*' % ENEMY_STATS['NAME'])
        forfeit = True
    else:
        None


# User Attacks or Misses
def userAttack():
    global USER_CHARARCTER_STATS
    global ENEMY_STATS
    global slowtext
    if ENEMY_STATS['HITPOINTS'] <= 0:
        slowtext('Enemy Is Dead!')
        USER_CHARARCTER_STATS['KILLS'] += 1
    else:
        roll()
        # Hit
        if ENEMY_STATS['HITPOINTS'] <= 0:
            slowtext('Enemy is Dead!')
            USER_CHARARCTER_STATS['KILLS'] += 1
        elif roll_number >= ENEMY_STATS['ARMORCLASS']:
            ENEMY_STATS['HITPOINTS'] -= ENEMY_STATS['ATTACK']
            slowtext(('%s was hit! -%s ') % (ENEMY_STATS['NAME'], ENEMY_STATS['ATTACK']))
            slowtext(('%s has %s hitpoints!') % (ENEMY_STATS['NAME'], ENEMY_STATS['HITPOINTS']))
        else:
            slowtext('*You Missed!*')


# Enemy Attacks or Misses
def enemyAttack():
    global USER_CHARARCTER_STATS
    global ENEMY_STATS
    global slowtext
    roll()
    # Hit
    if USER_CHARARCTER_STATS['HITPOINTS'] <= 0:
        slowtext('You Died!')
    elif roll_number >= USER_CHARARCTER_STATS['ARMORCLASS']:
        USER_CHARARCTER_STATS['HITPOINTS'] -= ENEMY_STATS['ATTACK']
        slowtext(('You were hit! -%s ') % (ENEMY_STATS['ATTACK']))
        slowtext(('You have %s hitpoints!') % (USER_CHARARCTER_STATS['HITPOINTS']))
    elif roll_number < USER_CHARARCTER_STATS['ARMORCLASS']:
        slowtext(('*%s Missed*') % (ENEMY_STATS['NAME']))
        slowtext(('%s: %s') % (ENEMY_STATS['NAME'], random.choice(enemy_miss)))
    else:
        None


# Print Out Battle Stats
def printBattleStats():
    global slowtext
    print('       |Battle Stats|')
    print(('Name:          %s vs %s') % (usr_name, enemy_name))
    print(('Hitpoints:     %s        %s') % (USER_CHARARCTER_STATS['HITPOINTS'], ENEMY_STATS['HITPOINTS']))
    print(('ArmorClass:    %s         %s') % (USER_CHARARCTER_STATS['ARMORCLASS'], ENEMY_STATS['ARMORCLASS']))
    print(('Race:          %s     %s') % (USER_CHARARCTER_STATS['RACE'].upper(), ENEMY_STATS['RACE'].upper()))
    print(('Attack:        %s         %s') % (USER_CHARARCTER_STATS['ATTACK'], ENEMY_STATS['ATTACK']))


# General Battle Template
def battle():
    global genEnemy
    #YES IT TALKS TRASH
    global trashtalk
    global userAttack
    global enemyAttack
    global printBattleStats
    global slowtext
    global USER_CHARARCTER_STATS
    global ENEMY_STATS
    global forfeit
    # Generate an enemy
    genEnemy()
    # ----------------------------------------------------------------------------#

    # Battle Settings
    slowtext(('Your opponent is %s') % (ENEMY_STATS['NAME']))
    slowtext(('%s: %s') % (ENEMY_STATS['NAME'], random.choice(trashtalk)))
    printBattleStats()
    slowtext("Type in 'options' to see what you can do!")
    slowtext(('Queen: %s goes first') % (ENEMY_STATS['NAME']))
    time.sleep(3)
    slowtext('Begin!')

    # ----------------------------------------------------------------------------#

    # Sets Forfeit To False
    forfeit = False

    # ----------------------------------------------------------------------------#

    time.sleep(2)

    # ----------------------------------------------------------------------------#
    loop1 = True
    # Battle
    while loop1 == True:
        if USER_CHARARCTER_STATS['HITPOINTS'] <= 0:
            slowtext('You Died')
            loop1 = False
            break
        elif ENEMY_STATS['HITPOINTS'] <= 0:
            slowtext('%s Died!' % ENEMY_STATS['NAME'])
            loop1 = False
            break
        else:
            print('----------------------------------------------------------')
            # Enemy Undo Block
            if ENEMY_STATS['BLOCK'] == 'true':
                slowtext('*%s\'s Block Broke*' % ENEMY_STATS['NAME'])
                ENEMY_STATS['BLOCK'] = 'false'
            # Enemy Decides what to do!
            decide_move = roll()
            if decide_move > 4:
                decide_move = 'hit'
            else:
                decide_move = 'block'
                ENEMY_STATS['BLOCK'] = 'true'
            # ----------------------------------------------------------------------------#

            if decide_move == 'hit':
                slowtext(('%s attacked!') % (ENEMY_STATS['NAME']))
                if USER_CHARARCTER_STATS['BLOCK'] == 'true':
                    slowtext(('*%s was blocked*') % (USER_CHARARCTER_STATS['NAME']))
                else:
                    enemyAttack()
            elif decide_move == 'block':
                slowtext(('%s blocked this turn') % (ENEMY_STATS['NAME']))
                slowtext('*No damage*')
                enemy_block = 'true'
            time.sleep(10)
            print('----------------------------------------------------------')
            if USER_CHARARCTER_STATS['BLOCK'] == 'true':
                slowtext('*Your Block Broke*')
                USER_CHARARCTER_STATS['BLOCK'] = 'false'
            if usr_hitpoints <= 0:
                None
            else:
                slowtext("'Your Turn!'")
                move = input('Move: ')
                move = move.lower()
                # Options
                if move.startswith('o'):
                    print('Moves:  Hit         Block')
                    print(('Damage: %s    Blocks all damage ') % (USER_CHARARCTER_STATS['ATTACK']))
                    print('                 that turn')
                # Hit
                elif move.startswith('h'):
                    if ENEMY_STATS['BLOCK'] == 'true':
                        slowtext(('*%s was blocked*') % (ENEMY_STATS['NAME']))
                        slowtext('*No damage*')
                        pass
                    else:
                        userAttack()
                # Block
                elif move.startswith('b'):
                    USER_CHARARCTER_STATS['BLOCK'] = 'true'
                    slowtext('You blocked!')
                # Forfeit
                elif move.startswith('f'):
                    forfeit = True
                    Forfeit()
                # Else
                else:
                    slowtext('You did nothing this turn')
                    pass
                time.sleep(10)

                # ----------------------------------------------------------------------------#


def quickPlay():
    global USER_CHARARCTER_STATS
    global slowtext
    slowtext("Loading Quickplay!")
    time.sleep(5)
    slowtext("You are on \"Quick Play Mode!\"")
    slowtext("Defeat as many enemies as you can!")
    slowtext("Good Luck!")
    time.sleep(5)
    while USER_CHARARCTER_STATS['HITPOINTS'] > 0:
        USER_CHARARCTER_STATS['KILLS'] += 1
        battle()
        if USER_CHARARCTER_STATS['HITPOINTS'] > 0:
            USER_CHARARCTER_STATS['KILLS'] += 1
            slowtext("Hitpoints Left: %s" % USER_CHARARCTER_STATS['HITPOINTS'])
            nextBattle = input("For next battle enter anything:  ")
            USER_CHARARCTER_STATS['HITPOINTS'] += 60
            slowtext("+60 hitpoints")
        else:
            slowtext("You Have Died In QuickPlay")
            break

#QUICK TOTORIAL
def tutorial():
    print("        -----------")
    print("       |What to do!|")
    print("        -----------")
    print("Type in \"hit\" to hit")
    print("Type in \"block\" to block")
    print("Type in \"options\" for options")
    print("         -----------")
    print("       |Descriptions:|")
    print("         -----------")
    print("Hit: Does X amount of damage")
    print("Block: Blocks all damage for that turn")
    print("Options: Allows you to see ability descriptions")
    time.sleep(10)


user_char()
tutorial()

quickPlay()
os.system("pause")









