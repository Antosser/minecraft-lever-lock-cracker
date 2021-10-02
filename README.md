# Minecraft Leaver Safe Lock Cracker
A python programm to bruteforce minectaft leaver locks

## Usage
1. Run main.py (packages will be installed automatically)
2. Enter the delay wetween the clicks in seconds (Recomended: 0.1 for singleplayer, 0.2 - 0.3 for servers)
3. Open Minecraft
4. Look on the first leaver
5. Press Insert
6. Further only use arrows to look around as python cannot capture mouse moves in games
7. Look on the second leaver (using arrows) and press Insert
8. Do 7. for all other leavers
9. Press Alt
10. The programm should have started clicking the leavers
11. Press Insert once to stop

## Probelms
If the programm hasn't started clicking the leavers after step 9., use the following steps to fix it:
- Look at the console output of the programm. If an error has been thrown please make a [New Issue](https://github.com/Antosser/minecraft-leaver-lock-cracker/issues/new)
- Check if the "Raw Input" option is set to false. This setting is under Options/Conrols/Mouse Settings/Raw Input

If the programm started clicking on the wrong points, adjust you sensitivity. The programm simply can't reach one leaver with only one mouse move
