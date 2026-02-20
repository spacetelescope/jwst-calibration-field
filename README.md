[![Build Status](https://travis-ci.org/spacetelescope/jwst-calibration-field.svg?branch=master)](https://travis-ci.org/spacetelescope/jwst-calibration-field)

# jwcf  -  JWST calibration field catalogs

Python interface to the HAWK-I and HST-based JWST calibration field catalogs. Both catalogs provide RA, Dec positions as well as estimated magnitudes for most JWST instruments + filters. Catalogs are bundled with the package as compressed FITS files (Astropy reads `.fits.gz` transparently).

## Installation

```bash
pip install jwst-calibration-field
```

Or edtiable install:

```bash
git lfs install # This is required for the large catalog files to be downloaded along with the package
git clone https://github.com/spacetelescope/jwst-calibration-field
cd just-calibration-field
pip install -e .
```
Requires Python ≥ 3.8, `numpy`, `astropy`

## Example usage
HAWK-I catalog:
```python
from jwcf import hawki_catalog

catalog = hawki_catalog()
print(catalog.colnames)
```    

HST catalog:
```python
from jwcf import hst_catalog

# Default: 2017.38 epoch
catalog = hst_catalog()

# Any epoch (proper motions propagated from 2017.38 reference)
catalog = hst_catalog(decimal_year_of_observation=2026.0)
```
The result is an `astropy.table.Table`. Access columns via `catalog['ra_deg']` (column) or `catalog['radeg'].data` (array).

## Catalog details
- **HAWK-I**: LMC calibration field calibrated to Gaia DR2 reference
- **HST**: Dual-epoch (2006.39 + 2017.38) proper motions; positions propagated to any epoch. Gaia DR2 reference.

## References

Anderson, J., Fall, M., and the Astrometry Working Group, The JWST Calibration Field: Absolute Astrometry and Proper Motions with GAIA and a Second HST Epoch, Technical Report JWST-STScI-007716, STScI

Sahlmann, J., 2019, Astrometric catalog for JWST focal plane geometric calibration, Technical Report JWST-STScI-006828 STScI 

Sahlmann, J., 2017, Astrometric accuracy of the JWST calibration field astrometric catalog examined with the first Gaia data release, Technical Report JWST-STScI-005492, STScI


## Contributing
Open issues or PRs for bugs, feedback, or features. New contributors welcome!
 
## Licenses
BSD-3-Clause
