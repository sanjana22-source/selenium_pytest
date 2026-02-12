

from utilities.api_utility import APIClient


class UserService:

    def __init__(self, base_url, default_headers=None):
        self.client = APIClient(base_url, default_headers)

    def get_users(self, page=1):
        return self.client.get("/users", params={"page": page})

    def get_single_user(self, user_id):
        return self.client.get(f"/users/{user_id}")

    def create_user(self, payload):
        return self.client.post("/users", json=payload)

    def update_user(self, user_id, payload):
        return self.client.put(f"/users/{user_id}", json=payload)

    def delete_user(self, user_id):
        return self.client.delete(f"/users/{user_id}")

    def login(self, payload):
        return self.client.post("/login", json=payload)