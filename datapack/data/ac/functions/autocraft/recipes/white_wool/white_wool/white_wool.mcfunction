#minecraft:white_wool
execute if data block ~ ~1 ~ {Items:[{Slot:12b,id:"minecraft:white_wool"}]} run function ac:autocraft/recipes/white_wool/white_wool/white_wool/white_wool
#minecraft:planks
data modify entity @s ArmorItems[0] set value {id:"minecraft:jigsaw",Count:1b}
data modify entity @s ArmorItems[0].id set from block ~ ~1 ~ Items[{Slot:12b}].id
execute if predicate ac:tags/minecraft/planks run function ac:autocraft/recipes/white_wool/white_wool/white_wool/planks
