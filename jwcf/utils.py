"""Useful functions.

Author:
-------
    Johannes Sahlmann

References
----------
    Some code was taken from https://github.com/spacetelescope/mirage


"""

import os
import requests

def download_file(url, file_name, output_directory='./'):
    """Download into the current working directory the
    file from Box given the direct URL
    Parameters
    ----------
    url : str
        URL to the file to be downloaded
    Returns
    -------
    download_filename : str
        Name of the downloaded file
    """
    download_filename = os.path.join(output_directory, file_name)
    if not os.path.isfile(download_filename):
        print('Downloading: {}'.format(file_name))
        with requests.get(url, stream=True) as response:
            if response.status_code != 200:
                raise RuntimeError("Wrong URL - {}".format(url))
            with open(download_filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=2048):
                    if chunk:
                        f.write(chunk)
    return download_filename

