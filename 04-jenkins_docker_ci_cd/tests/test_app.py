from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")
    print(response)

    assert response.status_code == 200
    assert b"Hello from Jenkins + Docker CI/CD!" in response.data


def test_health():
    client = app.test_client()

    response = client.get("/health")
    print(response)

    assert response.status_code == 200
    assert response.json["status"] == "Healthy"
