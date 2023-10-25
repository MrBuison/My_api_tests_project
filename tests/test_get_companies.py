import requests
import pytest
from data.urls import base_url
from data.data_files import StatusCompanies
from src.my_requests import MyRequests

status_list = StatusCompanies.status_list


class TestStatusCompanies:
    status_list = StatusCompanies.status_list
    request = MyRequests()

    @pytest.mark.parametrize("status", status_list)
    def test_get_status_companies(self, status):
        response = self.request.get(f'/companies/?status={status}&limit=3&offset=0')
        # print()
        # pprint(response.json())
        assert response.status_code == 200, f'Status code is not 200, status code is  {response.status_code}'


    @pytest.mark.parametrize("status", status_list)
    def test_get_active_companies(self, status):
        response = self.request.get(url=f'/?status={status}&limit=3&offset=0')
        items_list = response.json()["data"]
        for item in range(len(items_list)):
            assert items_list[item]["company_status"] == status
        print(items_list)
        # print(response.json()["data"][0]['company_status'])

#
#
#
# def test_get_closed_companies():
#     response = requests.get(f'''{base_url}/?status=CLOSED&limit=3&offset=0''')
#     print()
#     pprint(response.json())
#     # pprint(response.status_code)
#     assert response.status_code == 201, 'Status code is not 200, status code is  {response.status_code}'
#     # pprint(response.request.url)
#     # pprint(response.request.headers)
#
#
#
# def test_get_bankrupt_companies():
#     response = requests.get(f'''{base_url}/?status=BANKRUPT&limit=3&offset=0''')
#     print()
#     pprint(response.json())
