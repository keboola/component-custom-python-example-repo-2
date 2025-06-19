import os
import pathlib
import sys

import httpx
from keboola.component import CommonInterface

# for local development: add path for absolute imports to start at the project root level
sys.path.append(os.path.join(pathlib.Path(__file__).parent.parent))


from src import config


def get_request(url) -> httpx.Response:
    try:
        response = httpx.get(url)
        response.raise_for_status()
        return response
    except httpx.HTTPError as e:
        print(f"Error fetching data from {url}: {e}")
        return None


def main():
    cfg = config.Config()

    if resp := get_request(cfg.endpoint):
        print(resp.request.url, resp.status_code)

    ci = CommonInterface()
    # access user parameters
    print(ci.configuration.parameters)
    print(ci.data_folder_path)


main()
