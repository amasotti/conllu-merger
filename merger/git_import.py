import os
import requests
from urllib.parse import unquote
from typing import Optional

GITHUB_API_BASE_URL = "https://api.github.com/repos"
def make_github_api_url(github_url: str) -> Optional[str]:
    """Create GitHub API URL from a given GitHub repository URL.

    Parameters:
        github_url (str): The GitHub URL to the folder.

    Returns:
        str: The corresponding GitHub API URL, or None if the URL is invalid.
    """
    try:
        # Decode URL-encoded characters
        github_url = unquote(github_url)

        # Remove the base GitHub URL and split the remaining path
        path_parts = github_url.replace("https://github.com/", "").split("/")

        # Extract repo owner, repo name, and branch/subfolder
        repo_owner = path_parts[0]
        repo_name = path_parts[1]
        branch_or_folder = "/".join(path_parts[3:])

        # Create the GitHub API URL
        api_url = f"{GITHUB_API_BASE_URL}/{repo_owner}/{repo_name}/contents/{branch_or_folder}"
        print(f"Querying GitHub at URL: {api_url}")
        return api_url
    except IndexError:
        print("Invalid GitHub URL.")
        return None


def fetch_github_directory(api_url: str) -> Optional[list]:
    """Fetch the directory content from GitHub.

    Parameters:
        api_url (str): The GitHub API URL to the folder.

    Returns:
        list: A list of items in the directory, or None if the fetch fails.
    """
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from GitHub. Status code: {response.status_code}")
        return None


def download_file(file_url: str, dest_path: str) -> None:
    """Download a single file.

    Parameters:
        file_url (str): The URL of the file to download.
        dest_path (str): The local path to save the file.
    """
    response = requests.get(file_url)
    if response.status_code == 200:
        with open(dest_path, 'wb') as f:
            f.write(response.content)
    else:
        print(f"Failed to download {dest_path}. Status code: {response.status_code}")


def download_from_github(github_url: str, dest_folder: str) -> None:
    """Download all files from a GitHub folder to a local directory.

    Parameters:
        github_url (str): The GitHub URL to the folder.
        dest_folder (str): The local folder to save the files.
    """
    api_url = make_github_api_url(github_url)
    if api_url is None:
        print("Invalid GitHub URL.")
        return

    directory_content = fetch_github_directory(api_url)
    if directory_content is None:
        return

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for item in directory_content:
        if item['type'] == 'file':
            file_url = item['download_url']
            file_name = os.path.join(dest_folder, item['name'])
            download_file(file_url, file_name)