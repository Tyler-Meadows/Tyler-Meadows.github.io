!alias HitDice embed
<drac2>
ch = character()
ARGS = '%*%'
classes = {"Sorcerer": "D6 Hit Dice" ,
               "Wizard": "D6 Hit Dice",
               "Warlock": "D6 Hit Dice",
               "Bard": "D8 Hit Dice",
               "Cleric": "D8 Hit Dice",
               "Druid": "D8 Hit Dice",
               "Monk": "D8 Hit Dice",
               "Rogue": "D8 Hit Dice",
               "Fighter": "D10 Hit Dice",
               "Ranger": "D10 Hit Dice",
               "Paladin": "D10 Hit Dice",
               "Artificer": "D10 Hit Dice",
               "Barbarian": "D12 Hit Dice"}

Dice_Types = ["D6 Hit Dice","D8 Hit Dice","D10 Hit Dice","D12 Hit Dice"]
Dice_alias = {"d6": "D6 Hit Dice",
              "d8": "D8 Hit Dice",
              "d10": "D10 Hit Dice",
              "d12": "D12 Hit Dice"}

if "Set" == ARGS:
    for dice in Dice_Types:
        if ch.cc_exists(dice):
            ch.delete_cc(dice)
    for (cls, level) in ch.levels:
        dice = classes[cls]
        if ch.cc_exists(dice):
            ch.edit_cc(dice,0,ch.get_cc_max(dice)+level,"long","square",None,None,dice,None)
        else:
            ch.create_cc(dice,0,level,"long","square",None,None,dice,None)
    out = None
elif ARGS == None:
    None
else:
    dice_class = Dice_alias[ARGS[1:]]
    if ch.cc_exists(dice_class):    
        ch.mod_cc(dice_class,-int(ARGS[0]),strict=True)
        out = f"You rolled ARGS and got ${roll(ARGS)}"
    else:
        out = "No such hit dice"

# Set up output
</drac2>
-title "Hit Dice"
-desc "{{out}}"
-f 