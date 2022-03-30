from sql_format import __version__, main

def test_version():
    assert __version__ == '0.0.1'

test_formated_sql_expected = """SELECT 1
FROM dual"""
def test_formated_sql():
    result = main.api_call('select 1 from dual')
    assert result == test_formated_sql_expected
