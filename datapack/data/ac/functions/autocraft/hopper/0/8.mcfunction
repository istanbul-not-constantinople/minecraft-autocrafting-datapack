data modify block ~ ~ ~ Items[{Slot:0b}].id set from block ~ ~1 ~ Items[{Slot:23b}].id
data modify block ~ ~ ~ Items[{Slot:0b}].tag set from block ~ ~1 ~ Items[{Slot:23b}].tag
execute store result score @s ac.slot_count run data get block ~ ~1 ~ Items[{Slot:23b}].Count
scoreboard players remove @s ac.slot_count 1
execute store result block ~ ~1 ~ Items[{Slot:23b}].Count byte 1 run scoreboard players get @s ac.slot_count
tag @s add ac.hopper