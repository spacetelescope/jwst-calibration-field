"""Interface to the HAWK-I catalog of the LMC field.

Author:
-------
    Johannes Sahlmann

References
----------
    Some code was taken from https://github.com/spacetelescope/mirage


"""

import os
import requests
import tarfile

from astropy.table import Table

local_dir = os.path.dirname(os.path.abspath(__file__))



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




hawki_catalog_jwstmags_catalog_name = 'lmc_calibration_field_hawki_gaiadr2_jwstmags'
hawki_catalog_jwstmags_url = ('https://stsci.box.com/shared/static/0yjynlqe5kfzxr6o0b3wlji7hgwv3m75.gz', '{}.tar.gz'.format(hawki_catalog_jwstmags_catalog_name))



def hawki_catalog(include_jwstmags=True):
    """Return astropy table containing the HAWK-I catalog."""

    catalog_dir = os.path.join(local_dir, 'catalogs')

    if include_jwstmags:
        hawki_catalog_jwstmags_file = os.path.join(catalog_dir, '{}.fits'.format(hawki_catalog_jwstmags_catalog_name))

        if os.path.isfile(hawki_catalog_jwstmags_file) is False:
            if os.path.isdir(catalog_dir) is False:
                os.makedirs(catalog_dir)
            file_url = hawki_catalog_jwstmags_url[0]
            filename = hawki_catalog_jwstmags_url[1]
            local_file = os.path.join(catalog_dir, filename)
            if os.path.isfile(local_file) is False:
                download_file(file_url, filename, catalog_dir)
            if 'tar.gz' in local_file:
                print('Unzipping/extracting {}'.format(filename))
                file_object = tarfile.open(name=local_file, mode='r:gz')
                file_object.extractall(path=catalog_dir)
            return Table.read(hawki_catalog_jwstmags_file)
        else:
            return Table.read(hawki_catalog_jwstmags_file)

