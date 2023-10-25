from src.my_requests import MyRequests


class TestDeleteUser:


    def test_delete_user(self):
        resource = MyRequests.delete(url="/users/30526")
        print(resource.text)
        assert resource.status_code == 202, f" Status code not 202, status code is {resource.status_code}"

    def test_delete_user_has_text_null(self):
        resource = MyRequests.delete(url="/users/30538")
        print(resource.text)
        assert resource.text == "null", "Wrong text"


    def test_delete_deleted_user_has_status_cod_404(self):
        resource = MyRequests.delete(url="/users/30526")
        assert resource.status_code == 404, f" Status code not 404, status code is {resource.status_code}"


    def test_delete_deleted_user_has_text(self):
        resource = MyRequests.delete(url="/users/30526")
        assert resource.json()['details']['reason'] == "User with requested id: 30500 is absent", "Wrong text"
