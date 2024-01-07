import sys
from steamid_to_commid import steamid_to_commid
from file_load import oldFileLoader
from get_vars import get_vars


def main():
    # Take in only argument for source bans.json file from sourcebans
    oldBans = oldFileLoader(sys.argv[1])
    # Loop across old file and grab values for insertion into new file
    for ban in oldBans:
        # Grab username for description reference, old style steamid, and current group for permissionss
        name, authid, length, reason = get_vars(ban)
        # Convert to steamdid64 for future proofing
        commid = steamid_to_commid(authid)


if __name__ == "__main__":
    main()
