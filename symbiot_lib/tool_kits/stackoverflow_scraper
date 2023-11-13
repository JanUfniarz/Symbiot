import os
import requests
from bs4 import BeautifulSoup

def get_stack_overflow_thread(thread_url):
    # Send an HTTP request to fetch the page content
    response = requests.get(thread_url)

    # Check if the request was successful (response code 200)
    if response.status_code == 200:
        # Create a Beautiful Soup object and parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate the element containing the vote count for the main thread
        vote_element = soup.find('div', class_='js-vote-count')
        vote_count = vote_element['data-value'] if vote_element and 'data-value' in vote_element.attrs else 'N/A'

        # Try to get the thread title for the file name
        thread_title_element = soup.find('a', class_='question-hyperlink')
        thread_title = thread_title_element.text.strip() if thread_title_element else 'stack_overflow_thread'

        # Create a folder if it doesn't exist
        folder_path = 'stack_overflow_threads'
        os.makedirs(folder_path, exist_ok=True)

        # Save the thread content along with the vote count to a text file
        file_path = os.path.join(folder_path, f'{thread_title}.txt')
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"Vote count for the thread: {vote_count}\n\n")

            # Locate elements containing the thread content
            post_elements = soup.find_all('div', class_='js-post-body')
            for post in post_elements:
                file.write(str(post) + '\n\n')  # Save full posts, not just text

                # Locate the vote count for answers
                answer_vote_element = post.find_next('div', class_='js-vote-count')
                answer_vote_count = answer_vote_element['data-value'] if answer_vote_element and 'data-value' in answer_vote_element.attrs else 'N/A'
                if answer_vote_count != 'N/A':
                    file.write(f"Vote count for the answer: {answer_vote_count}\n\n")

        print(f"Successfully saved the thread content to the file: {file_path}")

        # Print the saved content
        with open(file_path, 'r', encoding='utf-8') as file:
            saved_content = file.read()
            print(f"\nSaved thread content:\n\n{saved_content}")
    else:
        print(f"Failed to fetch the page. Response code: {response.status_code}")

# Provide the URL of the Stack Overflow thread
thread_url = 'https://stackoverflow.com/questions/42841271/web-scraping-with-python-and-beautiful-soup'
get_stack_overflow_thread(thread_url)
