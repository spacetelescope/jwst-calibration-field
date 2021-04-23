"""Interface to the HST catalog of the LMC field.

Author:
-------
    Tony Sohn

"""
import os
import gzip
import shutil
from astropy.table import Table
from .utils import download_file

local_dir = os.path.dirname(os.path.abspath(__file__))

hst_catalog_name = 'lmc_calibration_field_hst_2017p38_jwstmags'
hst_catalog_url  = 'https://stsci.box.com/shared/static/hgj3gv2ktehkenpbxktbalyp57ocicxe'

def hst_catalog(decimal_year_of_observation=2017.38):
    """Return astropy table containing the HST catalog at the specified data.

    Parameters
    ----------
    decimal_year_of_observation : real
        Decimal year of the catalog to be returned. Reference year is 2017.38.

    Returns
    -------
     : astropy.table.Table
        Catalog in astropy table format
    
    """
    
    catalog_dir = os.path.join(local_dir, 'catalogs')
    hst_catalog_fits = '{}.fits'.format(hst_catalog_name)
    hst_catalog_fits_gz = '{}.fits.gz'.format(hst_catalog_name)
    full_path_fits = os.path.join(catalog_dir,hst_catalog_fits)
    full_path_fits_gz = os.path.join(catalog_dir,hst_catalog_fits_gz)

    # If subdirectory doesn't exist, create it, download the catalog file, and uncompress.
        
    if os.path.isdir(catalog_dir) is False:
        os.makedirs(catalog_dir)

    if os.path.isfile(full_path_fits) is False:
        if os.path.isfile(full_path_fits_gz) is False:
            download_file(hst_catalog_url, hst_catalog_fits_gz, catalog_dir)
        with gzip.open(full_path_fits_gz, 'rb') as f_in:
            with open(full_path_fits, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    t = Table.read(full_path_fits)
    
    # Decimal year of the reference catalog. Currently, the 2020 version is set at 2017.38 positions.
    decimal_year_ref = 2017.38

    if decimal_year_of_observation != 2017.38:
        dT = decimal_year_of_observation - decimal_year_ref

        t['ra_deg']  = t['ra_deg']  + dT*t['pmra']*0.001/3600.
        t['dec_deg'] = t['dec_deg'] + dT*t['pmdec']*0.001/3600.

        t['x'] = t['x'] - dT*t['pmra']*0.02
        t['y'] = t['y'] + dT*t['pmdec']*0.02
    
    return t
