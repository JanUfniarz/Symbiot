import requests
from bs4 import BeautifulSoup, Tag, ResultSet

from requests import Response


def get_stack_overflow_thread(thread_url):
    def f_next(post) -> Tag:
        return post.find_next('div', class_='js-vote-count')

    response: Response = requests.get(thread_url)

    if response.status_code != 200:
        raise Exception(f"ERROR:\n\tstatus_code: {response.status_code}")

    soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')

    # Znajdowanie liczby głosów dla głównego wątku
    vote_element: Tag = soup.find('div', class_='js-vote-count')
    vote_count: str = vote_element['data-value'] \
        if vote_element and 'data-value' in vote_element.attrs else 'N/A'

    # Znajdowanie tytułu wątku dla nazwy pliku
    thread_title_element: Tag = soup.find('a', class_='question-hyperlink')
    thread_title: str = thread_title_element.text.strip() \
        if thread_title_element else 'stack_overflow_thread'

    # Znajdowanie elementów zawierających treść wątku
    post_elements: ResultSet = soup.find_all('div', class_='js-post-body')

    elements: list[str] = [
        f"<@element>{content + answer_vote_element}</@element>"
        for content, answer_vote_element in zip(
            [f"<@content>{str(post)}</@content>" for post in post_elements],
            [f"<@answer-vote-element>{f_next(post)}</@answer-vote-element>"
             for post in post_elements if f_next(post) and 'data-value' in f_next(post).attrs])]

    return f"""
           <@THREAD>
             <@meta>
                <@thread-title>{thread_title}</@thread-title>
                <@vote-count-for-the-thread>{vote_count}</@vote-count-for-the-thread>
             </@meta>
             <@elements>{"".join(elements)}</@elements>
           </@THREAD>
           """


if __name__ == "__main__":
    url: str = "https://stackoverflow.com/questions/42841271/web-scraping-with-python-and-beautiful-soup"
    thread: str = get_stack_overflow_thread(url)
    print(thread)
