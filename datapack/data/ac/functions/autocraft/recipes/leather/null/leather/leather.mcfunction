#builtin:null
execute unless data block ~ ~1 ~ {Items:[{Slot:13b}]} run function ac:autocraft/recipes/leather/null/leather/leather/null
#minecraft:leather
execute if data block ~ ~1 ~ {Items:[{Slot:13b,id:"minecraft:leather"}]} run function ac:autocraft/recipes/leather/null/leather/leather/leather