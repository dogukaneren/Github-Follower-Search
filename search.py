import requests
import sys

def get_all_user_followers(username):
    followers_url = f"https://api.github.com/users/{username}/followers"
    followers = []

    while followers_url:
        response = requests.get(followers_url)
        
        if response.status_code == 200:
            current_followers = response.json()
            followers.extend(current_followers)

            followers_url = response.links.get('next', {}).get('url')
        else:
            print(f"Failed to fetch followers for {username}. Status code: {response.status_code}")
            return None

    return followers

def list_followers(username):
    followers = get_all_user_followers(username)

    if followers:
        print(f"Followers of {username}:")
        for follower in followers:
            print(f"- {follower['login']}")

        print(f"\nTotal Followers: {len(followers)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <github_username>")
        sys.exit(1)

    username = sys.argv[1]
    list_followers(username)
