from src.my_requests import MyRequests


class TestCreateUsers:
    body = {
        "first_name": "Trofim",
        "last_name": "Trofim",
        "company_id": 1,
    }


    def test_create_user(self):
        print(self.body.get('first_name'))
        resource = MyRequests.post(url="/users/", data=self.body)
        print(resource.json())
        print(resource.json()['first_name'] == self.body.get('first_name'), "first name was not created")
        print(resource.json()['last_name'] == self.body.get('last_name'), "last name was not created")



    def test_get_datus_code_201(self):
        resource = MyRequests.post(url="/users/", data=self.body)
        assert resource.status_code == 201, f" Status code not 201, status code is {resource.status_code}"
