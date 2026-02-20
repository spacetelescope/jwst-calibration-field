"""
Interface to the HAWK-I catalog of the LMC field.

Author:
    S. Tony Sohn
"""

from importlib.resources import files
from astropy.table import Table

def hawki_catalog(include_jwstmags=True):
    """
    Return astropy table containing the HAWK-I catalog.

    Parameters
    ----------
    include_jwstmags : bool
        Whether to include the version of the catalog with JWST magnitudes.

    Returns
    -------
    : astropy.table.Table
        Catalog in table format
    """
    if not include_jwstmags:
        raise NotImplementedError("Only JWST magnitudes version supported.")

    # Read directly from shipped package data (Astropy handles .gz)
    catalog_path = files("jwcf.data") / "lmc_calibration_field_hawki_gaiadr2_jwstmags.fits.gz"
    return Table.read(catalog_path)
