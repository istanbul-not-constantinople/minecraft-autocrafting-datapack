execute if data block ~ ~1 ~ Items[{Slot:1b}] run summon item ~ ~1 ~ {Item:{id:"minecraft:dirt",Count:1b},Tags:["ac.gui_save"]}
execute if data block ~ ~1 ~ Items[{Slot:1b}] run data modify entity @e[tag=ac.gui_save,limit=1] Item set from block ~ ~1 ~ Items[{Slot:1b}]
tag @e[tag=ac.gui_save] remove ac.gui_save
data modify block ~ ~1 ~ Items append value {Slot:1b,id:"minecraft:white_stained_glass_pane",Count:1b,tag:{ac_gui:1b,CustomModelData:10b,display:{Name:'{"text":""}'}}}
function #ac:api/gui/draw/1