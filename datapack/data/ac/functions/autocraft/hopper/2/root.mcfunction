execute if block ~ ~1 ~ barrel{Items:[{Slot:3b}]} run function ac:autocraft/hopper/2/0
execute unless entity @s[tag=ac.hopper] if block ~ ~1 ~ barrel{Items:[{Slot:4b}]} run function ac:autocraft/hopper/2/1
execute unless entity @s[tag=ac.hopper] if block ~ ~1 ~ barrel{Items:[{Slot:5b}]} run function ac:autocraft/hopper/2/2
execute unless entity @s[tag=ac.hopper] if block ~ ~1 ~ barrel{Items:[{Slot:12b}]} run function ac:autocraft/hopper/2/3
execute unless entity @s[tag=ac.hopper] if block ~ ~1 ~ barrel{Items:[{Slot:13b}]} run function ac:autocraft/hopper/2/4
execute unless entity @s[tag=ac.hopper] if block ~ ~1 ~ barrel{Items:[{Slot:14b}]} run function ac:autocraft/hopper/2/5
execute unless entity @s[tag=ac.hopper] if block ~ ~1 ~ barrel{Items:[{Slot:21b}]} run function ac:autocraft/hopper/2/6
execute unless entity @s[tag=ac.hopper] if block ~ ~1 ~ barrel{Items:[{Slot:22b}]} run function ac:autocraft/hopper/2/7
execute unless entity @s[tag=ac.hopper] if block ~ ~1 ~ barrel{Items:[{Slot:23b}]} run function ac:autocraft/hopper/2/8
execute unless entity @s[tag=ac.hopper] run data remove block ~ ~ ~ Items[{Slot:2b}]
tag @s[tag=ac.hopper] remove ac.hopper