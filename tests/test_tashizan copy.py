import pytest
from tashizan import tashizan


class TestTasizan:
    def test_tasizan(self):
        assert tashizan(1, 2) == 3


#tox+ pytest
