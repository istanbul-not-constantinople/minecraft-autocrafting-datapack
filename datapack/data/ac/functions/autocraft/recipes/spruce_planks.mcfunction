#builtin:null
execute unless data block ~ ~1 ~ {Items:[{Slot:4b}]} run function ac:autocraft/recipes/spruce_planks/null
#minecraft:spruce_planks
execute if data block ~ ~1 ~ {Items:[{Slot:4b,id:"minecraft:spruce_planks"}]} run function ac:autocraft/recipes/spruce_planks/spruce_planks
#minecraft:stick
execute if data block ~ ~1 ~ {Items:[{Slot:4b,id:"minecraft:stick"}]} run function ac:autocraft/recipes/spruce_planks/stick
