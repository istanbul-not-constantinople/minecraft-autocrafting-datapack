#minecraft:stick
execute if data block ~ ~1 ~ {Items:[{Slot:4b,id:"minecraft:stick"}]} run function ac:autocraft/recipes/null/stick
#minecraft:blaze_rod
execute if data block ~ ~1 ~ {Items:[{Slot:4b,id:"minecraft:blaze_rod"}]} run function ac:autocraft/recipes/null/blaze_rod
#minecraft:gold_ingot
execute if data block ~ ~1 ~ {Items:[{Slot:4b,id:"minecraft:gold_ingot"}]} run function ac:autocraft/recipes/null/gold_ingot
#minecraft:redstone_torch
execute if data block ~ ~1 ~ {Items:[{Slot:4b,id:"minecraft:redstone_torch"}]} run function ac:autocraft/recipes/null/redstone_torch
#minecraft:iron_ingot
execute if data block ~ ~1 ~ {Items:[{Slot:4b,id:"minecraft:iron_ingot"}]} run function ac:autocraft/recipes/null/iron_ingot
#minecraft:book
execute if data block ~ ~1 ~ {Items:[{Slot:4b,id:"minecraft:book"}]} run function ac:autocraft/recipes/null/book
#builtin:null
execute unless data block ~ ~1 ~ {Items:[{Slot:4b}]} run function ac:autocraft/recipes/null/null
#minecraft:redstone
execute if data block ~ ~1 ~ {Items:[{Slot:4b,id:"minecraft:redstone"}]} run function ac:autocraft/recipes/null/redstone
#minecraft:logs
data modify entity @s ArmorItems[0] set value {id:"minecraft:jigsaw",Count:1b}
data modify entity @s ArmorItems[0].id set from block ~ ~1 ~ Items[{Slot:4b}].id
execute if predicate ac:tags/minecraft/logs run function ac:autocraft/recipes/null/logs
#minecraft:glowstone_dust
execute if data block ~ ~1 ~ {Items:[{Slot:4b,id:"minecraft:glowstone_dust"}]} run function ac:autocraft/recipes/null/glowstone_dust
