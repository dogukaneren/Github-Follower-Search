import requests
import sys
import renkler

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
            print(f"{renkler.kirmizi}Failed to fetch followers for {username}. Status code: {response.status_code}{renkler.sifirla}")
            return None

    return followers

#Random color list
color_list = [renkler.kirmizi,renkler.turuncu,renkler.sari,renkler.lacivert,renkler.pembe,renkler.mor,renkler.mavi,renkler.turkuaz]

def list_followers(username):
    followers = get_all_user_followers(username)

    if followers:
        print(f"{renkler.yesil}Followers of {username}:")
        for follower in followers:
            print(renkler.rastgeleRenkler(*color_list))
            print(f"- {follower['login']}")

        print(f"\n{renkler.yesil}Total followers: {len(followers)}")

    print(renkler.sifirla)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{renkler.kirmizi}Usage: {sys.argv[0]} <username>{renkler.sifirla}")
        sys.exit(1)

    username = sys.argv[1]
    list_followers(username)
