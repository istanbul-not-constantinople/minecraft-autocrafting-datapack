#builtin:null
execute unless data block ~ ~1 ~ {Items:[{Slot:5b}]} run function ac:autocraft/recipes/polished_blackstone/polished_blackstone/null
#minecraft:polished_blackstone
execute if data block ~ ~1 ~ {Items:[{Slot:5b,id:"minecraft:polished_blackstone"}]} run function ac:autocraft/recipes/polished_blackstone/polished_blackstone/polished_blackstone
