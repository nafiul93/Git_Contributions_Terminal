# Import the necessary modules
from github import Github
from datetime import datetime, timedelta
import requests
import sparklines

class GitHubContributionsDashboard:
    def __init__(self, github_token, username):
        self.github_token = github_token
        self.username = username

    def fetch_contributions_data(self):
        # Fetch the user's contributions data using GitHub REST API
        contributions_url = f'https://api.github.com/users/{self.username}/events'
        response = requests.get(contributions_url)
        events_data = response.json()

        # Process contributions data
        dates = []
        counts = []

        for event in events_data:
            if event['type'] == 'PushEvent':
                date = datetime.strptime(event['created_at'], "%Y-%m-%dT%H:%M:%SZ")
                count = len(event['payload']['commits'])
                dates.append(date)
                counts.append(count)

        return dates, counts

    def display_contributions_graph(self, dates, counts):
        sparkline_data = sparklines.sparklines(counts)
        print(f'GitHub Contributions: {sparkline_data}')

    def run(self):
        dates, counts = self.fetch_contributions_data()
        self.display_contributions_graph(dates, counts)


# Replace with your GitHub API token and username
github_token = "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"
github_username = "nafiul93"

dashboard = GitHubContributionsDashboard(github_token, github_username)
dashboard.run()
