#minecraft:stick
execute if data block ~ ~1 ~ {Items:[{Slot:5b,id:"minecraft:stick"}]} run function ac:autocraft/recipes/stick/null/stick
#builtin:null
execute unless data block ~ ~1 ~ {Items:[{Slot:5b}]} run function ac:autocraft/recipes/stick/null/null
