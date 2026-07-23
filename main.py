import os

import requests
from dotenv import load_dotenv

# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")
API_URL = "https://api.github.com"
PER_PAGE = 100

session = requests.Session()
session.headers.update(
    {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
    }
)


# -----------------------------------------------------------------------------
# GitHub API
# -----------------------------------------------------------------------------

def get_github_users(endpoint: str) -> set[str]:
    """
    Retrieve every GitHub user from the specified endpoint.

    Args:
        endpoint: API endpoint (e.g. "/user/followers")

    Returns:
        A set containing GitHub usernames.
    """

    users: set[str] = set()
    page = 1

    while True:
        response = session.get(
            f"{API_URL}{endpoint}",
            params={
                "per_page": PER_PAGE,
                "page": page,
            },
        )

        response.raise_for_status()

        data = response.json()

        if not data:
            break

        users.update(user["login"] for user in data)

        page += 1

    return users


def unfollow_user(username: str) -> bool:
    """
    Unfollow a GitHub user.

    Returns:
        True if successful.
    """

    response = session.delete(f"{API_URL}/user/following/{username}")

    return response.status_code == 204


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

def main() -> None:
    print("Fetching GitHub data...\n")

    followers = get_github_users("/user/followers")
    following = get_github_users("/user/following")

    non_followers = sorted(following - followers)

    print(f"Followers          : {len(followers)}")
    print(f"Following          : {len(following)}")
    print(f"Not following back : {len(non_followers)}\n")

    if not non_followers:
        print("Everyone follows you back")
        return

    for username in non_followers:
        print(f"- {username}")

    confirm = input(
        "\nType 'YES' to unfollow everyone listed: "
    )

    if confirm != "YES":
        print("\nOperation cancelled.")
        return

    print()

    for username in non_followers:
        if unfollow_user(username):
            print(f"✓ Unfollowed {username}")
        else:
            print(f"✗ Failed to unfollow {username}")


if __name__ == "__main__":
    main()