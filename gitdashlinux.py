# Import the necessary modules
from github import Github
from datetime import datetime, timedelta
from ascii_graph import Pyasciigraph
from collections.abc import Iterable

class GitHubContributionsDashboard:
    def __init__(self, github_token, github_username):
        self.github_token = github_token
        self.github_username = github_username
        self.github = Github(self.github_token)
        self.user = self.github.get_user(self.github_username)

    def fetch_contributions_data(self):
        # Get the user's public events, which include contributions
        events = self.user.get_public_events()
        
        # Process contributions data
        data = {}
        for event in events:
            date = event.created_at.replace(tzinfo=None)
            date_str = date.strftime('%Y-%m-%d')
            
            # Increment contributions count for the date
            data[date_str] = data.get(date_str, 0) + 1
        
        sorted_data = sorted(data.items(), key=lambda x: datetime.strptime(x[0], '%Y-%m-%d'))
        return sorted_data

    def display_contributions_graph(self, data):
        graph = Pyasciigraph()
        for line in graph.graph('GitHub Contributions', data):
            print(line)

    def run(self):
        dates_counts = self.fetch_contributions_data()
        self.display_contributions_graph(dates_counts)


# Replace with your GitHub API token and username
github_token = "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"
github_username = "nafiul93"

dashboard = GitHubContributionsDashboard(github_token, github_username)
dashboard.run()
