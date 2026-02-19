import requests


BASE_URL = "https://ru.yougile.com/api-v2"
#перед тем как запустить автотесты вам необходимо авторизоваться на странице yougile.ru и получить токен
TOKEN = "Введите Ваш токен-ключ"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}


def test_create_project_positive():
    request = requests.post(f'{BASE_URL}/projects',
            json={"title": "New_project"},
            headers=HEADERS
                             )
    assert request.status_code == 201
    assert "id" in request.json()


def test_create_project_negative():
    request = requests.post(f'{BASE_URL}/projects',
            json={},
            headers=HEADERS
                             )
    assert request.status_code == 400


def test_update_project_positive():
    request = requests.post(f'{BASE_URL}/projects',
            json={"title": "New_project"},
            headers=HEADERS
                             )

    assert request.status_code == 201
    assert "id" in request.json()

    project_id = request.json()["id"]

    request = requests.put(f'{BASE_URL}/projects/{project_id}',
            json={"title": "Old_project"},
            headers=HEADERS
                            )
    assert request.status_code == 200
    assert "id" in request.json()


def test_update_project_negative():
    request = requests.put(f'{BASE_URL}/projects/{id}',
            json={"title": "Old_project"},
            headers=HEADERS
                            )
    assert request.status_code == 404


def test_get_project_positive():
    request = requests.post(f'{BASE_URL}/projects',
            json={"title": "New_project"},
            headers=HEADERS
                             )

    assert request.status_code == 201
    assert "id" in request.json()

    project_id = request.json()["id"]

    request = requests.get(f'{BASE_URL}/projects/{project_id}',
                           headers=HEADERS
                           )

    assert request.status_code == 200
    assert "id" in request.json()


def test_get_project_negative():
    request = requests.get(f'{BASE_URL}/projects/{id}',
                           headers=HEADERS
                           )

    assert request.status_code == 404
    assert "id" not in request.json()

