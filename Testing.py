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
            sys.exit()
    else:
        print('Please emter a valid response. ')
        yorn = input('Would you like to be attacked? Yes or No? ')
def damask(mprot, pprot):
    while True:
        print(f'You take {attacked(mprot, pprot):.2f} damage.')
        again = input('Would you like to be attacked again? ')
        if again == 'yes':
            again = True
            break
        if again == 'no':
            again = False
            break
def damloop(mprot,pprot):
    loop = input('Would you like to be attacked again? ')
    if loop == 'yes':
        while True:
            print(f'You take {attacked(mprot, pprot):.2f} damage.')
            again = input('Would you like to be attacked again? ')
            if again == 'yes':
                again = True
                break
            if again == 'no':
                again = False
                break
    if loop == 'no':
        sys.exit()
def user_menu():
    print('Welcome to the Smite Calculator would you please enter the items you would like on your character')
    print('The items currently listed are valor, genjis, bulwark, failnot, soul, jotunn, hydras, malice, soul_eater, sov, mystical, midgardian, emperor, exe, asi, pythag')
    item1 = get_item('Please enter your first item ')
    item2 = get_item('Please enter your second item ')
    item3 = get_item('Please enter your third item ')
    item4 = get_item('Please enter your fourth item ')
    item5 = get_item('Please enter your fifth item ')
    item6 = get_item('Please enter your sixth item ')
    phys_prots = item1['physical prots'] + item2['physical prots'] + item3['physical prots'] + item4['physical prots'] + item5['physical prots'] + item6['physical prots']
    magic_prots = item1['magical prots'] + item2['magical prots'] + item3['magical prots'] + item4['magical prots'] + item5['magical prots'] + item6['magical prots']
    phys_power = item1['physical power'] + item2['physical power'] + item3['physical power'] + item4['physical power'] + item5['physical power'] + item6['physical power']
    attack_speed = item1['attack speed'] + item2['attack speed'] + item3['attack speed'] + item4['attack speed'] + item5['attack speed'] + item6['attack speed']
    cooldown = item1['cooldown'] + item2['cooldown'] + item3['cooldown'] + item4['cooldown'] + item5['cooldown'] + item6['cooldown']
    ccr = item1['CCR'] + item2['CCR'] + item3['CCR'] + item4['CCR'] + item5['CCR'] + item6['CCR']
    print('The build is')
    print(item1['item'])
    print(item2['item'])
    print(item3['item'])
    print(item4['item'])
    print(item5['item'])
    print(item6['item'])
    print(f'The physical protections are {phys_prots:.2f}')
    print(f'The magical protections are {magic_prots:.2f}')
    print(f'The physical power is {phys_power:.2f}')
    print(f'The attack speed is {attack_speed:.2f} (this is as a percent but decimal form so 1.00 is 100 percent)')
    print(f'The cooldown is {cooldown:.2f}')
    print(f'The crowd control reduction is {ccr:.2f}')
    damaged = attacked(magic_prots, phys_prots)
    print(f'You take {damaged:.2f} damage.')
    damask(magic_prots, phys_prots)

if __name__ == '__main__':
  user_menu()

