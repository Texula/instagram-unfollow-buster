import json
import os
import argparse


### supply the files downloaded from Meta Account Center
def parse_arguments():
    parser = argparse.ArgumentParser(description="Bust the users that don't follow you back on instagram.")

    # the following.json file
    parser.add_argument(
        '--following',
        default='following.json',
        help='Path to the file containing people you follow (default: following.json)'
    )

    # the followers.json file
    parser.add_argument(
        '--followers',
        default='followers_1.json',
        help='Path to the file containing your followers (default: followers_1.json)'
    )

    return parser.parse_args()


def load_json_file(filename):
    """Loads JSON data from a file with error handling."""
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        return None

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Error: Could not parse '{filename}'. Check if it's valid JSON.")
        return None


# ==========================================
# 3. LOGIC TO EXTRACT USERNAMES
# ==========================================

def get_users_i_follow(json_data):
    """Extracts users from following.json"""
    users = set()
    relationships = json_data.get('relationships_following', [])

    for item in relationships:
        # In following.json, the username is simply the 'title'
        users.add(item['title'])
    return users


def get_users_following_me(json_data):
    """Extracts users from followers.json"""
    users = set()

    # Handle both list and dictionary structures
    if isinstance(json_data, dict):
        data_list = json_data.get('relationships_followers', [])
    else:
        data_list = json_data

    for item in data_list:
        try:
            # In followers files, username is deep inside string_list_data -> value
            user_val = item['string_list_data'][0]['value']
            users.add(user_val)
        except (KeyError, IndexError, TypeError):
            continue
    return users


### main execution of the script
if __name__ == "__main__":
    args = parse_arguments()

    print(f"--- Configuration ---")
    print(f"Following file: {args.following}")
    print(f"Followers file: {args.followers}")
    print(f"---------------------")

    # Load files
    following_data = load_json_file(args.following)
    followers_data = load_json_file(args.followers)

    if following_data and followers_data:
        print("Processing data...")

        # Extract the sets
        my_following = get_users_i_follow(following_data)
        my_followers = get_users_following_me(followers_data)

        # Calculate the difference
        not_following_back = my_following - my_followers

        # Output results
        print(f"\nTotal Following: {len(my_following)}")
        print(f"Total Followers: {len(my_followers)}")
        print(f"Not Following Back: {len(not_following_back)}")
        print("-" * 30)
        print("LIST OF PEOPLE NOT FOLLOWING BACK:")
        print("-" * 30)

        for user in sorted(not_following_back):
            print(user)
    else:
        print("\nProcess stopped due to missing or invalid files.")

### enjoy <3