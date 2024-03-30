import requests, json
from dotenv import dotenv_values
from time_report import get_report_data

config = dotenv_values("../../.env")


pixela_graph_id = "lp1"

url_pixela_users = "https://pixe.la/v1/users"
url_pixela_graphs = f"{url_pixela_users}/{config["PIXELA_USER"]}/graphs"
url_pixela_graph = f"{url_pixela_graphs}/{pixela_graph_id}"
url_pixela_pixels = f"{url_pixela_graph}/pixels"

headers = {
    "X-USER-TOKEN": config["PIXELA_TKN"],
}


def create_user():  # https://docs.pixe.la/entry/post-user
    user_params = {
        "token": config["PIXELA_TKN"],
        "username": config["PIXELA_USER"],
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    r = requests.post(url=url_pixela_users, json=user_params)
    print(r.text)


def pin_graph():  # https://docs.pixe.la/entry/put-profile
    url = f"https://pixe.la/@{config["PIXELA_USER"]}"
    user_params = {
        "pinnedGraphID": pixela_graph_id
    }
    r = requests.put(url=url, json=user_params, headers=headers)
    print(r.text)


def create_graph():  # https://docs.pixe.la/entry/post-graph
    graph_params = {
        "id": pixela_graph_id,
        "name": "Learning Python",
        "unit": "h",
        "type": "float",
        "color": "shibafu",
        "timezone": "EET"
    }
    r = requests.post(url=url_pixela_graph, json=graph_params, headers=headers)
    print(r.text)


def post_pixel():  # https://docs.pixe.la/entry/post-pixel
    pixel_params = {
        "date": f"{"2024"}{"03"}{"06"}",
        "quantity": "2.01",
        "optionalData": json.dumps({
            "Start Time (%H:%M:%S)": "12:30:00",
            "Duration (%H:%M:%S)": "02:00:43",
        })
    }
    r = requests.post(url=url_pixela_graph, json=pixel_params, headers=headers)
    print(r.text)


def put_pixel():  # https://docs.pixe.la/entry/put-pixel
    pixel = f"{"2024"}{"03"}{"06"}"
    pixel_params = {
        "quantity": "2.01",
        "optionalData": json.dumps({
            "Start Time (%H:%M:%S)": "12:30:00",
            "Duration (%H:%M:%S)": "02:00:43",
        })
    }
    url_put_pixel = f"{url_pixela_graph}/{pixel}"
    r = requests.put(url_put_pixel, json=pixel_params, headers=headers)
    print(r.text)


def delete_pixel():  # https://docs.pixe.la/entry/delete-pixel
    pixel = f"{"2024"}{"03"}{"06"}"
    url_delete_pixel = f"{url_pixela_graph}/{pixel}"
    r = requests.delete(url_delete_pixel, headers=headers)
    print(r.text)


def get_graph_pixels():
    response = requests.get(url_pixela_pixels, headers=headers)
    print(response.text)
    graph_pixels_data = response.json()["pixels"]
    for pixel_data in graph_pixels_data:
        url_pixela_pixel_get = f"{url_pixela_graph}/{pixel_data}"
        response = requests.get(url_pixela_pixel_get, headers=headers)
        print(response.text)


def save_data_to_pixela(count=-1):
    data = get_report_data()
    for key in data:
        print(f"posting: {key}:{data[key]}")
        pixel_params = {
            "date": key,
            "quantity": str(data[key]["quantity"]),
            "optionalData": data[key]["optionalData"],
        }

        success = False
        while not success:
            r = requests.post(url=url_pixela_graph, json=pixel_params,
                              headers=headers)
            print(r.text)
            response_data = r.json()
            success = response_data['isSuccess']
        count -= 1
        if count == 0:
            return


get_graph_pixels()
