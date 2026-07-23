# GitHub Non-Follower Cleaner

A Python command-line application that uses the GitHub REST API to identify users you follow who do not follow you back, and optionally unfollow them.

> **⚠️ Warning:** Unfollowing users is a permanent action. Review the list carefully before confirming.

---

## Features

- 🔑 Authenticate using a GitHub Personal Access Token
- 👥 Retrieve all followers and following users
- 📄 Automatically handle GitHub API pagination
- 🔍 Compare followers and following lists
- 📋 Display users who don't follow you back
- ❌ Automatically unfollow selected users
- 🛡 Confirmation prompt before performing any unfollow action

---

## Technologies

- Python 3
- Requests
- Python Dotenv
- GitHub REST API


## Configuration

Create a `.env` file in the project root.

```env
GITHUB_TOKEN=your_personal_access_token
```

Your GitHub Personal Access Token must have the following permission:

- **user:follow**

---

## Usage

Run the application:

```bash
python main.py
```

Example output:

```text
Fetching GitHub data...

Followers          : 152
Following          : 189
Not following back : 37

- user1
- user2
- user3
- user4

Type 'YES' to unfollow everyone listed:
```

If you type:

```text
YES
```

The application will send an unfollow request for each user in the list.

---

## How It Works

1. Loads your GitHub Personal Access Token.
2. Retrieves every account you follow.
3. Retrieves every account following you.
4. Compares both lists.
5. Displays users who don't follow you back.
6. Requests confirmation.
7. Unfollows each selected user.

---

## GitHub API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/user/followers` | Retrieve your followers |
| GET | `/user/following` | Retrieve users you follow |
| DELETE | `/user/following/{username}` | Unfollow a user |

---

## Requirements

- Python 3.10+
- GitHub Personal Access Token
- Internet connection

---

## Disclaimer

This project interacts directly with your GitHub account using the official GitHub REST API.

Always review the list of users before confirming the unfollow operation. The author is not responsible for accidental or unintended changes to your GitHub account.
