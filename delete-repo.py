import requests

# Replace with your GitHub username and access token
username = 'your_username'
access_token = 'your_access_token'

# Function to delete a GitHub repository
def delete_repository(repo_name):
    url = f'https://api.github.com/repos/{username}/{repo_name}'
    headers = {'Authorization': f'token {access_token}'}

    try:
        response = requests.delete(url, headers=headers)

        if response.status_code == 204:
            print(f"Repository {repo_name} deleted successfully.")
        elif response.status_code == 404:
            print(f"Repository {repo_name} not found.")
        else:
            print(f"Failed to delete repository {repo_name}. Status code: {response.status_code}")
            print(f"Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# List of repositories to be deleted
repositories_to_delete = ['', '', '']  # Add your repository names here

print("The following repositories are scheduled for deletion:")
for repo in repositories_to_delete:
    print(repo)

confirmation = input("Do you want to proceed with deletion? (yes/no): ")

if confirmation.lower() == "yes":
    for repo in repositories_to_delete:
        print(f"Deleting {repo}...")
        delete_repository(repo)
else:
    print("Deletion aborted. No repositories were deleted.")
