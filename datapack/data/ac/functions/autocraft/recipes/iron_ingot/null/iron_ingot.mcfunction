#builtin:null
execute unless data block ~ ~1 ~ {Items:[{Slot:12b}]} run function ac:autocraft/recipes/iron_ingot/null/iron_ingot/null
#minecraft:iron_ingot
execute if data block ~ ~1 ~ {Items:[{Slot:12b,id:"minecraft:iron_ingot"}]} run function ac:autocraft/recipes/iron_ingot/null/iron_ingot/iron_ingot