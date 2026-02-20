"""
Interface to the HST catalog of the LMC field.

Author:
    S. Tony Sohn
"""

from importlib.resources import files
from astropy.table import Table

def hst_catalog(decimal_year_of_observation=2017.38):
    """
    Return astropy table containing the HST catalog at the specified date.

    Parameters
    ----------
    decimal_year_of_observation : real
        Decimal year of the catalog to be returned. Reference year is 2017.38.

    Returns
    -------
    : astropy.table.Table
        Catalog in astropy table format
    """
    # Read directly from shipped package data (Astropy handles .gz)
    catalog_path = files("jwcf.data") / "lmc_calibration_field_hst_2017p38_jwstmags.fits.gz"
    t = Table.read(catalog_path)

    # Propagate proper motions
    decimal_year_ref = 2017.38
    if decimal_year_of_observation != decimal_year_ref:
        dT = decimal_year_of_observation - decimal_year_ref
        t['ra_deg'] = t['ra_deg'] + dT * t['pmra'] * 0.001 / 3600.
        t['dec_deg'] = t['dec_deg'] + dT * t['pmdec'] * 0.001 / 3600.
        t['x'] = t['x'] - dT * t['pmra'] * 0.02
        t['y'] = t['y'] + dT * t['pmdec'] * 0.02

    return t
