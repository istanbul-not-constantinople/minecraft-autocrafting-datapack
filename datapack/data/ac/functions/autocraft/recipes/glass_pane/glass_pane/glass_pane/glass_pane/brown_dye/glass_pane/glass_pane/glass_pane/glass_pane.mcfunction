data modify block ~ ~1 ~ Items[{Slot:0b}] set value {Slot:0b,id:"minecraft:brown_stained_glass_pane",Count:8b}
tag @s add ac.offering
data modify entity @s ArmorItems[1].tag.ac_last set from block ~ ~1 ~ Items
