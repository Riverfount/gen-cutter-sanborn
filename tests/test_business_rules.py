import httpx
from pytest_httpx import HTTPXMock

from api.business_rules.cutter_table import gen_cutter_table


def test_gen_cutter_table_works_ok(httpx_mock: HTTPXMock):
    httpx_mock.add_response(
        text='<b>A</b><pre><b>    111     Aa\n    112     Aabb</b></pre>'
    )

    with httpx.Client():
        response = gen_cutter_table()
        assert response['a'] == [('111', 'Aa'.lower()), ('112', 'Aabb'.lower())]
