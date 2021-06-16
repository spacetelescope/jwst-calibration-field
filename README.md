[![Build Status](https://travis-ci.org/spacetelescope/jwst-calibration-field.svg?branch=master)](https://travis-ci.org/spacetelescope/jwst-calibration-field)
[![Documentation Status](https://readthedocs.org/projects/jwst-calibration-field/badge/?version=latest)](https://jwst-calibration-field.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/jwcf.svg)](https://badge.fury.io/py/jwcf)
[![PyPI - License](https://img.shields.io/pypi/l/Django.svg)](https://github.com/spacetelescope/jwcf/blob/master/LICENSE.md)

# jwcf  -  JWST calibration field catalogs

Python interface to the HAWK-I and HST-based JWST calibration field catalogs. Both of these catalogs have RA, Dec positions as well as estimated magnitudes for most JWST instruments+filters.

### Example usage
Access HAWK-I based catalog:        
````
    from jwcf import hawki 
    catalog = hawki.hawki_catalog() 
````    

Access HST based catalog:
````
    from jwcf import hst
    catalog = hst.hst_catalog(decimal_year_of_observation=2022.50)
````
`decimal_year_of_observation` above provides the RA, Dec locations at the desired epoch. These locations are projected based on accurate HST proper motions derived using dual-epoch data obtained in 2006.39 and 2017.38. If `decimal_year_of_observation` is not provided, the output catalog will default to 2017.38 positions.

The resulting `catalog` above is an astropy table (class). Available columns can be accessed by `catalog.colnames`. To extract a specific column: e.g., `catalog['ra_deg']` as a table column or `catalog['ra_deg'].data` as a (masked) array.


### Documentation


Sahlmann, J., 2019, Astrometric catalog for JWST focal plane geometric calibration, Technical Report JWST-STScI-006828 STScI 

Sahlmann, J., 2017, Astrometric accuracy of the JWST calibration field astrometric catalog examined with the first Gaia data release, Technical Report JWST-STScI-005492, STScI


### Contributing
Please open a new issue or new pull request for bugs, feedback, or new features you would like to see. If there is an issue you would like to work on, please leave a comment and we will be happy to assist. New contributions and contributors are very welcome!   
 

### References



