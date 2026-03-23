import os

from hatchet_sdk import Hatchet

from agimage_domain import SERVICE_NAME
from agimage_worker.tasks.utils import task_image_gen

HATCHET_CLIENT_TOKEN = os.getenv("HATCHET_CLIENT_TOKEN")
HATCHET_CLIENT_HOST_PORT = os.getenv("HATCHET_CLIENT_HOST_PORT")

hatchet = Hatchet()


if __name__ == "__main__":
    worker = hatchet.worker(f"{SERVICE_NAME}-worker", workflows=[task_image_gen])
    worker.start()
