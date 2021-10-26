import sys
valor = {
    'item' : 'Breastplate of Valor',
    'physical prots' : 65,
    'magical prots' : False,
    'damage mit' : False,
    'mana' : 300,
    'mp5' : 10,
    'cooldown' : .2,
    'hp5' : False,
    'health' : False,
    'movement' : False,
    'physical power' : False,
    'magical power' : False, 
    'passive' : False,
    'attack speed' : False,
    'percent pen' : False,
    'flat pen' : False,
    'lifesteal' : False,
    'crit' : False,
    'CCR' : False
    }
genjis = {
    'item' : "Genji's Guard",
    'physical prots' : False,
    'magical prots' : 70,
    'damage mit' : False,
    'mana' : False,
    'mp5' : 40,
    'cooldown' : .1,
    'hp5' : False,
    'health' : 150,
    'movement' : False,
    'physical power' : False,
    'magical power' : False, 
    'passive' : 'When you take Magical Damage from Abilities your cooldowns are reduced by 3s. This can only occur once every 30s.',
    'attack speed' : False,
    'percent pen' : False,
    'flat pen' : False,
    'lifesteal' : False,
    'crit' : False,
    'CCR' : False
    }
bulwark = {
    'item' : 'Bulwark of Hope',
    'physical prots' : False,
    'magical prots' : 80,
    'damage mit' : False,
    'mana' : False,
    'mp5' : False,
    'cooldown' : False,
    'hp5' : False,
    'health' : 250,
    'movement' : False,
    'physical power' : False,
    'magical power' : False, 
    'passive' : 'When you take damage and are below 40% Health, you gain a Shield with health equal to 15 percent of your Maximum Health for 20s. Can only occur once every 60s.',
    'attack speed' : False,
    'percent pen' : False,
    'flat pen' : False,
    'lifesteal' : False,
    'crit' : False,
    'CCR' : .2
    }
failnot = {
    'item' : 'Fail-not',
    'physical prots' : False,
    'magical prots' : False,
    'damage mit' : False,
    'mana' : False,
    'mp5' : False,
    'cooldown' : .2,
    'hp5' : False,
    'health' : False,
    'movement' : False,
    'physical power' : 40,
    'magical power' : False, 
    'passive' : 'When your Ultimate ability has finished casting, your next ability or basic attack within 8s that damages an enemy god marks them, increasing the chance you and your allies can land a Critical Strike by 20 percent for 10 seconds. This can only occur once every 45 seconds.',
    'attack speed' : False,
    'percent pen' : .1,
    'flat pen' : False,
    'lifesteal' : False,
    'crit' : .1,
    'CCR' : False
    }
soul = {
    'item' : 'Soul Gem',
    'physical prots' : False,
    'magical prots' : False,
    'damage mit' : False,
    'mana' : False,
    'mp5' : False,
    'cooldown' : .1,
    'hp5' : False,
    'health' : 150,
    'movement' : False,
    'physical power' : False,
    'magical power' : 80, 
    'passive' : 'On successful hit of an Ability you gain 1 stack. At 4 Stacks your next Ability that damages an enemy God will deal bonus damage equal to 25% of your Magical power to each God hit, and will heal yourself and allies within 20 units for 30 percent of your Magical Power and will consume the 4 stacks.',
    'attack speed' : False,
    'percent pen' : False,
    'flat pen' : False,
    'lifesteal' : .12,
    'crit' : False,
    'CCR' : False
    }
jotunn = {
    'item' : 'Jotunn\'s Wrath',
    'physical prots' : False,
    'magical prots' : False,
    'damage mit' : False,
    'mana' : 150,
    'mp5' : False,
    'cooldown' : .2,
    'hp5' : False,
    'health' : False,
    'movement' : False,
    'physical power' : 45,
    'magical power' : False, 
    'passive' : False,
    'attack speed' : False,
    'percent pen' : False,
    'flat pen' : 10,
    'lifesteal' : False,
    'crit' : False,
    'CCR' : False
    }
hyrdras = {
    'item' : 'Hydra\'s Lament',
    'physical prots' : False,
    'magical prots' : False,
    'damage mit' : False,
    'mana' : False,
    'mp5' : 10,
    'cooldown' : .1,
    'hp5' : False,
    'health' : False,
    'movement' : False,
    'physical power' : 40,
    'magical power' : False, 
    'passive' : 'For 8s after using an ability, your next Basic Attack will deal an additional 40 percent damage. Abilities that function like basic attacks do not benefit from this. PASSIVE - This item grants 2.5 MP5 per 10 percent of your missing Mana.',
    'attack speed' : False,
    'percent pen' : False,
    'flat pen' : False,
    'lifesteal' : False,
    'crit' : False,
    'CCR' : False
    }
malice = {
    'item' : 'Malice',
    'physical prots' : False,
    'magical prots' : False,
    'damage mit' : False,
    'mana' : False,
    'mp5' : False,
    'cooldown' : .2,
    'hp5' : False,
    'health' : False,
    'movement' : False,
    'physical power' : 40,
    'magical power' : False, 
    'passive' : 'Successfully Hitting an Enemy God with a Critical Strike will subtract 3s from all of your abilities currently on Cooldown, except your Ultimate ability. This effect can only happen once every 5s.',
    'attack speed' : False,
    'percent pen' : False,
    'flat pen' : False,
    'lifesteal' : False,
    'crit' : .25,
    'CCR' : False
    }
soul_eater = {
    'item' : 'Soul Eater',
    'physical prots' : False,
    'magical prots' : False,
    'damage mit' : False,
    'mana' : False,
    'mp5' : False,
    'cooldown' : .1,
    'hp5' : False,
    'health' : False,
    'movement' : False,
    'physical power' : 35,
    'magical power' : False, 
    'passive' : 'Abilites heal 20 percent of damage done.',
    'attack speed' : False,
    'percent pen' : .1,
    'flat pen' : False,
    'lifesteal' : .1,
    'crit' : False,
    'CCR' : False
    }
sov = {
    'item' : 'Sovereignty',
    'physical prots' : 60,
    'magical prots' : False,
    'damage mit' : False,
    'mana' : False,
    'mp5' : False,
    'cooldown' : .2,
    'hp5' : 35,
    'health' : 250,
    'movement' : False,
    'physical power' : False,
    'magical power' : False, 
    'passive' : False,
    'attack speed' : False,
    'percent pen' : False,
    'flat pen' : False,
    'lifesteal' : False,
    'crit' : False,
    'CCR' : False
    }
mystical = {
    'item' : 'Mystical Mail',
    'physical prots' : 40,
    'magical prots' : False,
    'damage mit' : False,
    'mana' : False,
    'mp5' : False,
    'cooldown' : False,
    'hp5' : False,
    'health' : 200,
    'movement' : False,
    'physical power' : False,
    'magical power' : False, 
    'passive' : 'ALL enemies are dealt 30(+1 per level)Magical Damage per second.',
    'attack speed' : False,
    'percent pen' : False,
    'flat pen' : False,
    'lifesteal' : False,
    'crit' : False,
    'CCR' : .2
    }
midgardian = {
    'item' : 'Midgardian Mail',
    'physical prots' : 40,
    'magical prots' : False,
    'damage mit' : False,
    'mana' : False,
    'mp5' : False,
    'cooldown' : False,
    'hp5' : False,
    'health' : 300,
    'movement' : False,
    'physical power' : False,
    'magical power' : False, 
    'passive' : 'Enemies that successfully land a basic attack on you have their Movement Speed and Attack Speed reduced by 8 percent for 2 seconds. This effect can stack up to 3 times and can stack with other item slow effects.',
    'attack speed' : False,
    'percent pen' : False,
    'flat pen' : False,
    'lifesteal' : False,
    'crit' : False,
    'CCR' : False
    }
emperor = {
    'item' : 'Emperor\'s Armor',
    'physical prots' : 60,
    'magical prots' : False,
    'damage mit' : False,
    'mana' : False,
    'mp5' : False,
    'cooldown' : False,
    'hp5' : False,
    'health' : 250,
    'movement' : False,
    'physical power' : False,
    'magical power' : False, 
    'passive' : 'Damageable enemy structures within 55 units have their Attack Speed reduced by 30%. Damageable allied structures within 55 units have their Attack Speed increased by 40%.',
    'attack speed' : False,
    'percent pen' : False,
    'flat pen' : False,
    'lifesteal' : False,
    'crit' : False,
    'CCR' : False
    }
exe = {
    'item' : 'The Executioner',
    'physical prots' : False,
    'magical prots' : False,
    'damage mit' : False,
    'mana' : False,
    'mp5' : False,
    'cooldown' : False,
    'hp5' : False,
    'health' : False,
    'movement' : False,
    'physical power' : 35,
    'magical power' : False, 
    'passive' : 'Basic Attacks against an enemy reduce your target\'s Physical Protection by 7 percent for 3 seconds (max. 4 Stacks).',
    'attack speed' : .2,
    'percent pen' : False,
    'flat pen' : False,
    'lifesteal' : False,
    'crit' : False,
    'CCR' : False
    }
asi = {
    'item' : 'Asi',
    'physical prots' : False,
    'magical prots' : False,
    'damage mit' : False,
    'mana' : False,
    'mp5' : False,
    'cooldown' : False,
    'hp5' : False,
    'health' : False,
    'movement' : False,
    'physical power' : 25,
    'magical power' : False, 
    'passive' : 'If you drop below 35% Health, you gain an additional 30% Physical Lifesteal for 5 seconds. Can only occur once every 15 seconds.',
    'attack speed' : .25,
    'percent pen' : False,
    'flat pen' : 15,
    'lifesteal' : .2,
    'crit' : False,
    'CCR' : False
    }
pythag = {
    'item' : 'Pythagorem\'s Timepiece',
    'physical prots' : False,
    'magical prots' : False,
    'damage mit' : False,
    'mana' : False,
    'mp5' : False,
    'cooldown' : False,
    'hp5' : False,
    'health' : 200,
    'movement' : False,
    'physical power' : False,
    'magical power' : 70, 
    'passive' : ' Allied gods within 70 units have their Magical Lifesteal increased by 12 percent and their Magical Power increased by 30 or their Physical Lifesteal increased by 10 percent and their Physical Power increased by 20.',
    'attack speed' : False,
    'percent pen' : .1,
    'flat pen' : False,
    'lifesteal' : .24,
    'crit' : False,
    'CCR' : False
    }
heart = {
    'item' : 'Heartseeker',
    'physical prots' : False,
    'magical prots' : False,
    'damage mit' : False,
    'mana' : 200,
    'mp5' : 20,
    'cooldown' : False,
    'hp5' : False,
    'health' : False,
    'movement' : False,
    'physical power' : 65,
    'magical power' : False, 
    'passive' : False,
    'attack speed' : False,
    'percent pen' : .1,
    'flat pen' : False,
    'lifesteal' : False,
    'crit' : False,
    'CCR' : False
    }
def get_item(prompt):
    item = input(prompt)
    while item.lower() != 'quit':
        if item == 'sov':
            return sov
        if item == 'valor':
            return valor
        if item == 'genjis':
            return genjis
        if item == 'bulwark':
            return bulwark
        if item == 'failnot':
            return failnot
        if item == 'soul':
            return soul
        if item == 'jotunn':
            return jotunn
        if item == 'hydras':
            return hyrdras
        if item == 'malice':
            return malice
        if item == 'soul_eater':
            return soul_eater
        if item == 'mystical':
            return mystical
        if item == 'midgardian':
            return midgardian
        if item == 'emperor':
            return emperor
        if item == 'exe':
            return exe
        if item == 'asi':
            return asi
        if item == 'pythag':
            return pythag
        if item == 'heartseeker':
            return heart
        else:
            print('That item is either not in the database or has a typo')
            item = input(prompt)
    else:
        sys.exit()
def attacked(mprot, pprot):
    yorn = input('Would you like to be attacked? Yes or No? ')
    while yorn.lower() != 'quit':
        if yorn == 'yes':
            morp = input('Is the attack magical or physical? ')
            while morp.lower() != 'quit':
                if morp == 'magical':
                    dam = int(input('Please enter damage value '))
                    return (100 * dam) / (mprot + 100)
                if morp == 'physical':
                    dam = int(input('Please enter damage value '))
                    return (100 * dam) / (pprot + 100)
                else:
                    print('Please select magical or physical')
                    morp = input('Is the attack magical or physical? ')
            else:
                sys.exit()
        if yorn == 'no':
            break
    else:
        print('Please emter a valid response. ')
        yorn = input('Would you like to be attacked? Yes or No? ')
def damtest(mprot, pprot):
    again = input('Would you like to be attacked? yes or no? ')
    while again == 'yes':
        print(f'You take {special_attack(mprot, pprot):.2f} damage.')
        again = input('Would you like to be attacked? ')
def special_attack(mprot, pprot):
    morp = input('Is the attack magical or physical? ')
    while morp.lower() != 'quit':
        if morp == 'magical':
            dam = int(input('Please enter damage value '))
            return (100 * dam) / (mprot + 100)
        if morp == 'physical':
            dam = int(input('Please enter damage value '))
            return (100 * dam) / (pprot + 100)
        else:
            print('Please select magical or physical')
            morp = input('Is the attack magical or physical? ')
    else:
        sys.exit()
def hit(ypen, yppen, tpprot, tmprot):
    hon = ('Would you like to attack someone? yes or no? ')
    while hon.lower() != 'quit':
        if hon == 'yes':
            your_attack = input('What type of damage are you? magical or physical? ')
            while your_attack.lower() != 'quit':
                if your_attack == 'magical':
                    dam = int(input('How much damage are you dealing? '))
                    prots = tmprot * (1 - yppen) - ypen
                    print(f'Before penetration you deal {(100 * dam) / (tmprot + 100)} damage.')
                    return (100 * dam) / (prots + 100)
                if your_attack == 'physical':
                    dam = int(input('How much damage are you dealing? '))
                    prots = tpprot * (1 - yppen) - ypen
                    print(f'Before penetration you deal {(100 * dam) / (tpprot + 100)} damage.')
                    return (100 * dam) / (prots + 100)
                else:
                    print('Please select magical or physical')
                    your_attack = input('What type of damage are you? magical or physical? ')
            else:
                sys.exit()
        if hon =='no':
            break
        else:
            print('Please emter a valid response. ')
            hon = input('Would you like to attack someone? yes or no? ')
def user_menu():
    print('Welcome to the Smite Calculator would you please enter the items you would like on your character')
    print('The items currently listed are valor, genjis, bulwark, failnot, soul, jotunn, hydras, malice, soul_eater, sov, mystical, midgardian, emperor, exe, asi, pythag, heartseeker')
    yitem1 = get_item('Please enter your first item ')
    yitem2 = get_item('Please enter your second item ')
    yitem3 = get_item('Please enter your third item ')
    yitem4 = get_item('Please enter your fourth item ')
    yitem5 = get_item('Please enter your fifth item ')
    yitem6 = get_item('Please enter your sixth item ')
    phys_prots = yitem1['physical prots'] + yitem2['physical prots'] + yitem3['physical prots'] + yitem4['physical prots'] + yitem5['physical prots'] + yitem6['physical prots']
    magic_prots = yitem1['magical prots'] + yitem2['magical prots'] + yitem3['magical prots'] + yitem4['magical prots'] + yitem5['magical prots'] + yitem6['magical prots']
    phys_power = yitem1['physical power'] + yitem2['physical power'] + yitem3['physical power'] + yitem4['physical power'] + yitem5['physical power'] + yitem6['physical power']
    attack_speed = yitem1['attack speed'] + yitem2['attack speed'] + yitem3['attack speed'] + yitem4['attack speed'] + yitem5['attack speed'] + yitem6['attack speed']
    cooldown = yitem1['cooldown'] + yitem2['cooldown'] + yitem3['cooldown'] + yitem4['cooldown'] + yitem5['cooldown'] + yitem6['cooldown']
    ccr = yitem1['CCR'] + yitem2['CCR'] + yitem3['CCR'] + yitem4['CCR'] + yitem5['CCR'] + yitem6['CCR']
    flatpen = yitem1['flat pen'] + yitem2['flat pen'] + yitem3['flat pen'] + yitem4['flat pen'] + yitem5['flat pen'] + yitem6['flat pen']
    ppen = yitem1['percent pen'] + yitem2['percent pen'] + yitem3['percent pen'] + yitem4['percent pen'] + yitem5['percent pen'] + yitem6['percent pen']
    print('The build is')
    print(yitem1['item'])
    print(yitem2['item'])
    print(yitem3['item'])
    print(yitem4['item'])
    print(yitem5['item'])
    print(yitem6['item'])
    print(f'The physical protections are {phys_prots:.2f}')
    print(f'The magical protections are {magic_prots:.2f}')
    print(f'The physical power is {phys_power:.2f}')
    print(f'The attack speed is {attack_speed:.2f} (this is as a percent but decimal form so 1.00 is 100 percent)')
    print(f'The cooldown is {cooldown:.2f}')
    print(f'The crowd control reduction is {ccr:.2f}')
    print(f'The flat penetration is {flatpen:.2f}')
    print(f'The percent penetration is {ppen:.2f}')
    damtest(magic_prots, phys_prots)
    spicy = input('Continue? ')
    while spicy.lower() != 'quit':
        if spicy == 'yes':
            titem1 = get_item('Please enter their first item ')
            titem2 = get_item('Please enter their second item ')
            titem3 = get_item('Please enter their third item ')
            titem4 = get_item('Please enter their fourth item ')
            titem5 = get_item('Please enter their fifth item ')
            titem6 = get_item('Please enter their sixth item ')
            tphys_prots = titem1['physical prots'] + titem2['physical prots'] + titem3['physical prots'] + titem4['physical prots'] + titem5['physical prots'] + titem6['physical prots']
            tmagic_prots = titem1['magical prots'] + titem2['magical prots'] + titem3['magical prots'] + titem4['magical prots'] + titem5['magical prots'] + titem6['magical prots']
            attack_value =  hit(flatpen, ppen, tphys_prots, tmagic_prots) 
            print(f'After penetration you hit the enemy for {attack_value:.2f} damage')
if __name__ == '__main__':
  user_menu()

