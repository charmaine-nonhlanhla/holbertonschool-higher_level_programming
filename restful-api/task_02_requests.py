import requests
import csv

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    print("Status Code:", response.status_code)
    
    if response.status_code == 200:
        posts = response.json()
        
        fieldnames = ['id', 'title', 'body']  # Include only 'id', 'title', and 'body'
        
        with open("posts.csv", "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts:
                del post['userId']  # Remove 'userId' from the post dictionary
                writer.writerow(post)

