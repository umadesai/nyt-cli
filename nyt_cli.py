"""
Python command-line interface with click and the New York Times API.
"""
import os
import click
import requests

api_key = os.getenv("API_KEY")


def top_stories(section, api_key, count):
    url = f'https://api.nytimes.com/svc/topstories/v2/{section}.json'

    query_params = {
        'apikey': api_key
    }

    response = requests.get(url, params=query_params)
    stories = []
    for i in range(0, count if count <= 10 else 10):
        stories.append((response.json()['results'][i]['title'],
                        response.json()['results'][i]['byline'],
                        response.json()['results'][i]['url']))
    return stories


@click.command()
@click.argument('section')
@click.option(
    '--api-key', '-a',
    envvar="API_KEY",
    help='your API key for the New York Times API',
)
@click.option(
    '--count', default=1,
    help='top __ stories (limit 10)',
)
def main(section, api_key, count):
    """
    A news tool that shows you the top NYT stories in the SECTION of
    your choice. Allowed SECTION values are: home, opinion, world,
    national, politics, upshot, nyregion, business, technology, science,
    health, sports, arts, and books.

    You need a valid API key from the New York Times for the tool to work.
    You can sign up for a free account at https://developer.nytimes.com/signup.
    """
    stories = top_stories(section, api_key, count)
    if len(stories) == 1:
        headline, byline, url = stories[0]
        click.echo(f"The top story in {section} right now: \
        \n{headline} {byline.title()}.")
        click.echo(f"Read more at {url}")
    else:
        click.echo(f"The top {len(stories)} stories in {section} right now: \
        \n")
        for story in stories:
            headline, byline, url = story
            click.echo(f"{headline} {byline.title()}.")
            click.echo(f"Read more at {url}\n")


if __name__ == "__main__":
    main()
