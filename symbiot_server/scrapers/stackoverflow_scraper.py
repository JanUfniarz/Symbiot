import requests
from bs4 import BeautifulSoup, Tag

from requests import Response


def get_stack_overflow_thread(thread_url) -> dict:
    def f_next(post) -> str:
        res = post.find_next('div', class_='js-vote-count')
        return str(res) if res and 'data-value' in res.attrs else ""

    response: Response = requests.get(thread_url)
    if response.status_code != 200:
        raise Exception(f"HTTP ERROR:\n\tstatus_code: {response.status_code}")

    soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')

    # Znajdowanie liczby głosów dla głównego wątku
    vote_element: Tag = soup.find('div', class_='js-vote-count')

    # Znajdowanie tytułu wątku dla nazwy pliku
    thread_title_element: Tag = soup.find('a', class_='question-hyperlink')

    return dict(
        meta=dict(
            thread_title=thread_title_element.text.strip() if thread_title_element else 'stack_overflow_thread',
            vote_count=vote_element['data-value'] if vote_element and 'data-value' in vote_element.attrs else 'N/A'),
        elements=[dict(
            content=str(post),
            answer_vote_element=f_next(post))
                for post in soup.find_all('div', class_='js-post-body')])


if __name__ == "__main__":
    url: str = "https://stackoverflow.com/questions/42841271/web-scraping-with-python-and-beautiful-soup"
    thread: dict = get_stack_overflow_thread(url)
    print(thread)
