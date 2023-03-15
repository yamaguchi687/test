# これがないとNotFoundMethodになる
'''
ImportError while importing test module '/Users/yamaguchi/orcamo-aws/Lambda/WAFLog/tests/test_tashizan.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
../../../.pyenv/versions/3.9.10/lib/python3.9/importlib/__init__.py:127: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
tests/test_tashizan.py:2: in <module>
    from tashizan import tashizan
E   ModuleNotFoundError: No module named 'tashizan'
'''
from tashizan import tashizan
