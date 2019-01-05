"""
Python command-line interface with click and the New York Times API.
"""
import os
import click
import requests

api_key = os.getenv("API_KEY")


def top_story(section, api_key):
    url = f'https://api.nytimes.com/svc/topstories/v2/{section}.json'

    query_params = {
        'apikey': api_key
    }

    response = requests.get(url, params=query_params)
    return (response.json()['results'][0]['title'],
            response.json()['results'][0]['byline'],
            response.json()['results'][0]['url'])


@click.command()
@click.argument('section')
@click.option(
    '--api-key', '-a',
    envvar="API_KEY",
    help='your API key for the New York Times API',
)
def main(section, api_key):
    """
    A news tool that shows you the top NYT story in the SECTION of
    your choice. Allowed SECTION values are: home, opinion, world,
    national, politics, upshot, nyregion, business, technology, science,
    health, sports, arts, and books.

    You need a valid API key from the New York Times for the tool to work.
    You can sign up for a free account at https://developer.nytimes.com/signup.
    """
    story, byline, url = top_story(section, api_key)
    print(f"The top story in {section} right now: \n{story} {byline.title()}.")
    print(f"Read more at {url}")


if __name__ == "__main__":
    main()
