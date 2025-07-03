import requests

base_url = "https://ru.yougile.com"
token = ""


def test_create_project_positive():
    project = {
        "title": "Услуги"
    }
    myheaders = {
        "Authorization": f"Bearer {token}"
    }
    resp = requests.post(base_url+'/api-v2/projects', json=project, headers=myheaders)
    assert resp.status_code == 201


def test_create_project_nigative():
    project = {
        "title": ""
    }
    myheaders = {
        "Authorization": f"Bearer {token}"
    }
    resp = requests.post(base_url+'/api-v2/projects', json=project, headers=myheaders)
    assert resp.status_code == 400


def test_get_project_id_positive():
    project = {
        "title": "Услуги"
    }
    myheaders = {
        "Authorization": f"Bearer {token}"
    }
    result = requests.post(base_url+'/api-v2/projects', json=project, headers=myheaders)
    new_id = result.json().get("id")

    get_project_id = requests.get(base_url+"/api-v2/projects/" + str(new_id), headers=myheaders)
    assert get_project_id.status_code == 200


def test_get_project_id_negative():
    negative_id = "123456789"
    project = {
        "title": "Услуги"
    }
    myheaders = {
        "Authorization": f"Bearer {token}"
    }
    requests.post(base_url+'/api-v2/projects', json=project, headers=myheaders)

    get_project_id = requests.get(base_url+'/api-v2/projects/' + str(negative_id), headers=myheaders)
    assert get_project_id.status_code == 404


def test_put_project_positive():
    old_project = {
        "title": "Услуги"
    }
    myheaders = {
        "Authorization": f"Bearer {token}"
    }
    result = requests.post(base_url+'/api-v2/projects', json=old_project, headers=myheaders)
    new_id = result.json().get("id")

    new_project = {
        "title": "НовыеУслуги"
    }
    put_project = requests.get(base_url+"/api-v2/projects/" + str(new_id), json=new_project, headers=myheaders)
    assert put_project.status_code == 200


def test_put_project_negative():
    negative_id = "123456789"
    old_project = {
        "title": "Услуги"
    }
    myheaders = {
        "Authorization": f"Bearer {token}"
    }
    requests.post(base_url+'/api-v2/projects', json=old_project, headers=myheaders)

    new_project = {
        "title": "НовыеУслуги"
    }
    put_project = requests.get(base_url+"/api-v2/projects/" + str(negative_id), json=new_project, headers=myheaders)
    assert put_project.status_code == 404
