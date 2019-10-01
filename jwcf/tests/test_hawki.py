#!/usr/bin/env python
"""Tests for the jwcf hawki module.

Authors
-------
    Johannes Sahlmann

"""

# import numpy as np
import pytest

from ..hawki import hawki_catalog

def test_hawki(verbose=False):
    """Test the access to the catalog."""

    catalog = hawki_catalog()

    assert len(catalog) > 1e5
