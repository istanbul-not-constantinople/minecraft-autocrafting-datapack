#minecraft:planks
data modify entity @s ArmorItems[0] set value {id:"minecraft:jigsaw",Count:1b}
data modify entity @s ArmorItems[0].id set from block ~ ~1 ~ Items[{Slot:13b}].id
execute if predicate ac:tags/minecraft/planks run function ac:autocraft/recipes/red_wool/red_wool/red_wool/planks/planks
