#builtin:null
execute unless data block ~ ~1 ~ {Items:[{Slot:12b}]} run function ac:autocraft/recipes/dark_oak_planks/null/null/null
#minecraft:dark_oak_planks
execute if data block ~ ~1 ~ {Items:[{Slot:12b,id:"minecraft:dark_oak_planks"}]} run function ac:autocraft/recipes/dark_oak_planks/null/null/dark_oak_planks
