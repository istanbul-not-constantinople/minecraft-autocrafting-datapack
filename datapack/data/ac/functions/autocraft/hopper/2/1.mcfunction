data modify block ~ ~ ~ Items[{Slot:2b}].id set from block ~ ~1 ~ Items[{Slot:4b}].id
data modify block ~ ~ ~ Items[{Slot:2b}].tag set from block ~ ~1 ~ Items[{Slot:4b}].tag
execute store result score @s ac.slot_count run data get block ~ ~1 ~ Items[{Slot:4b}].Count
scoreboard players remove @s ac.slot_count 1
execute store result block ~ ~1 ~ Items[{Slot:4b}].Count byte 1 run scoreboard players get @s ac.slot_count
tag @s add ac.hopper