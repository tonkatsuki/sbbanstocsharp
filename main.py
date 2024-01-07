import sys
from datetime import datetime
from steamid_to_commid import steamid_to_commid
from file_load import oldFileLoader
from get_vars import get_vars
from sqlscript_make import sqlscript_make


def main():
    # Make sql file and use the right database
    sqlscriptfile = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-newbans.sql")
    usedatabase = "USE simpleadmin;\n"
    with open(sqlscriptfile, "a") as file:
        file.write(usedatabase)

    # Take in only argument for source bans.json file from sourcebans
    oldBans = oldFileLoader(sys.argv[1])
    # Loop across old file and grab values for insertion into new file
    for ban in oldBans:
        # Grab username for description reference, old style steamid, and current group for permissionss
        authid, name, created, ends, length, reason = get_vars(ban)
        # Convert to steamdid64 for future proofing
        commid = steamid_to_commid(authid)
        sqlscript_make(sqlscriptfile, commid, name, created, ends, length, reason)


if __name__ == "__main__":
    main()
