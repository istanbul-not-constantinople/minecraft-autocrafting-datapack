#minecraft:wooden_slabs
data modify entity @s ArmorItems[0] set value {id:"minecraft:jigsaw",Count:1b}
data modify entity @s ArmorItems[0].id set from block ~ ~1 ~ Items[{Slot:23b}].id
execute if predicate ac:tags/minecraft/wooden_slabs run function ac:autocraft/recipes/wooden_slabs/null/wooden_slabs/wooden_slabs/null/wooden_slabs/wooden_slabs/wooden_slabs/wooden_slabs
