#builtin:null
execute unless data block ~ ~1 ~ {Items:[{Slot:12b}]} run function ac:autocraft/recipes/warped_planks/null/null/null
#minecraft:warped_planks
execute if data block ~ ~1 ~ {Items:[{Slot:12b,id:"minecraft:warped_planks"}]} run function ac:autocraft/recipes/warped_planks/null/null/warped_planks