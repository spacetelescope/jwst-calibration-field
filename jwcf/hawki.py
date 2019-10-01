"""Interface to the HAWK-I catalog of the LMC field.

Author:
-------
    Johannes Sahlmann


"""

import os
import tarfile

from astropy.table import Table

from .utils import download_file

local_dir = os.path.dirname(os.path.abspath(__file__))

hawki_catalog_jwstmags_catalog_name = 'lmc_calibration_field_hawki_gaiadr2_jwstmags'
hawki_catalog_jwstmags_url = ('https://stsci.box.com/shared/static/'
                              '0yjynlqe5kfzxr6o0b3wlji7hgwv3m75.gz',
                              '{}.tar.gz'.format(hawki_catalog_jwstmags_catalog_name))

def hawki_catalog(include_jwstmags=True):
    """Return astropy table containing the HAWK-I catalog.

    Parameters
    ----------
    include_jwstmags : bool
        Whether to include the version of the catalog with JWST magnitudes.

    Returns
    -------
     : astropy.table.Table
        Catalog in table format

    """
    catalog_dir = os.path.join(local_dir, 'catalogs')

    if include_jwstmags:
        hawki_catalog_jwstmags_file = os.path.join(catalog_dir, '{}.fits'.format(
            hawki_catalog_jwstmags_catalog_name))

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
    else:
        raise NotImplementedError