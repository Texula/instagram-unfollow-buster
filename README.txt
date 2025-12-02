    _            __        __               __
   (_)___  _____/ /_____ _/ /_  __  _______/ /____  _____
  / / __ \/ ___/ __/ __ `/ __ \/ / / / ___/ __/ _ \/ ___/
 / / / / (__  ) /_/ /_/ / /_/ / /_/ (__  ) /_/  __/ /
/_/_/ /_/____/\__/\__,_/_.___/\__,_/____/\__/\___/_/
v1.0
by Texula

FOR HELP:
    ❯ python3 instabuster.py -help

INSTRUCTIONS:
1.Go to "Meta Accounts Center"
2.Go to "Your information and permissions"
3.Go to "Export your information"

4.Select "Create export" -> "Export to device"
    -> "Customise information"
        -> SELECT ONLY "Connections" -> "Followers and Following"
    -> "Date range"
        -> SELECT "All time" (unless you need a specific time period)
    -> "Format" !VERY IMPORTANT!
        -> SELECT "JSON"
    -> "Media Quality"
        -> SELECT "Medium quality"
        (I have no idea how this influences the result but I always use "Medium quality")
    -> "Start export"

Shortly, you will recieve an email when your export is ready.

5.Download the .zip file with your information and unzip the archive.

6.Locate the .json files
    > ./connections/followers_and_following/followers_1.json
    > ./connections/followers_and_following/following.json
    (yours may differ but you should be able to figure out which is which)

7.Move the script instabuster.py in the same folder as the following and followers file.

8. Run the script, remember to supply the followers.json and following.json
if they're not the default values.

    For help, you can always type
    ❯ python3 instabuster.py -help
    usage: instabuster.py [-h] [--following FOLLOWING] [--followers FOLLOWERS]

    Bust the users that don't follow you back on instagram.

    options:
        -h, --help              show this help message and exit
        --following FOLLOWING
                                Path to the file containing people you follow
                                (default: following.json)
        --followers FOLLOWERS
                                Path to the file containing your followers
                                (default: followers_1.json)

9. Enjoy <3