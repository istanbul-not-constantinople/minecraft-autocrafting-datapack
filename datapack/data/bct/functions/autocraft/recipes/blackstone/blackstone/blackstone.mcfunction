#builtin:null
execute unless data block ~ ~1 ~ {Items:[{Slot:12b}]} run function bct:autocraft/recipes/blackstone/blackstone/blackstone/null
#minecraft:blackstone
execute if data block ~ ~1 ~ {Items:[{Slot:12b,id:"minecraft:blackstone"}]} run function bct:autocraft/recipes/blackstone/blackstone/blackstone/blackstone