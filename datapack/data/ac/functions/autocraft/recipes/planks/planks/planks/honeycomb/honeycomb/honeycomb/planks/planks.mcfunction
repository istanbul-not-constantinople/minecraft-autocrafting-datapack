#minecraft:planks
data modify entity @s ArmorItems[0] set value {id:"minecraft:jigsaw",Count:1b}
data modify entity @s ArmorItems[0].id set from block ~ ~1 ~ Items[{Slot:23b}].id
execute if predicate ac:tags/minecraft/planks run function ac:autocraft/recipes/planks/planks/planks/honeycomb/honeycomb/honeycomb/planks/planks/planks