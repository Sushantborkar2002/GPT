import time
from datetime import datetime
from github import Github
import os


ACCESS_TOKEN = open("token.txt", "r").read()
g = Github(ACCESS_TOKEN)
print(g.get_user())

end_time = time.time()
start_time = end_time - 86400
for _ in range(5):
    start_time_str = datetime.utcfromtimestamp(start_time).strftime('%Y-%m-%d')
    end_time_str = datetime.utcfromtimestamp(end_time).strftime('%Y-%m-%d')
    query = f"opencv  language:python created:{start_time_str}..{end_time_str}"
    #print(query)
    result = g.search_repositories(query)
    print(result.totalCount)

    for repository in result:
        print(f"{repository.clone_url}")
        print(f"{repository.tags_url}")
        os.system (f"git clone {repository.clone_url} repos/{repository.owner.login}/{repository.name}")
    start_time -= 86400
    end_time -= 86400
    break





