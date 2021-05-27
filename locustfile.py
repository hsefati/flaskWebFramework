import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def hello_world(self):
        self.client.get("/")
        self.client.get("/")

    @task(3)
    def predict_items(self):
        for item_id in range(10):
            payload = { "CHAS":{"0":0},
                        "RM":{"0":6.575},
                        "TAX":{"0":296.0},
                        "PTRATIO":{"0":15.3},
                        "B":{"0":396.9},
                        "LSTAT":{"0":4.98}
                      }
            
            r = self.client.post("/predict", json=payload)
            time.sleep(1)

    def on_start(self):
        print("This is locust without login")