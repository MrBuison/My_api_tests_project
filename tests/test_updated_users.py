from src.my_requests import MyRequests


class TestUpdatedUsers:
    body = {
        "first_name": "Antonina",
        "last_name": "Antonina",
        "company_id": 1,
    }


    def test_updated_user(self):
        resource = MyRequests.put(url="/users/30500", data=self.body)
        print(resource.json())
        assert resource.json()['first_name'] != "Trofim", "First name was not updated"
        assert resource.json()['last_name'] != "Trofim", "First name was not updated"
        assert resource.status_code == 200, f" Status code not 200, status code is {resource.status_code}"







