# sbbanstocsharp-simpleadmin
Takes a sourcebans bans.json export and converts it to a sql script to run on a CS2 CounterStrikeSharp server to add bans for CS2-SimpleAdmin

Note it will also remove a variety of characters like single or double quotes for ease of importing, as well as scrub for SQL commands

# usage

Ensure you have python3.x installed

Run from a command line interface, `python3 main.py oldbans.json`, with oldadmins.json being your sourcebans exported bans file.
