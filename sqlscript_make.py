def sqlscript_make(sqlscriptfile, commid, name, created, ends, length, reason):
    queryInsert = f"INSERT INTO `sa_bans` (`player_steamid`, `player_name`, `player_ip`, `admin_steamid`, `admin_name`, `reason`, `duration`, `ends`, `created`) \nVALUES ('{commid}', '{name}', 'NULL', 'Console', 'Console', '{reason}', {length}, timestamp('{ends}'), timestamp('{created}'));\n"

    with open(sqlscriptfile, "a") as file:
        file.write(queryInsert)
