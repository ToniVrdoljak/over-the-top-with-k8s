import os
import subprocess

color_off = "\033[0m"
b_green = "\033[1;32m"
b_red = "\033[0;31m"


DOCKER_USERNAME = os.environ["DOCKER_USERNAME"]
SHA = os.environ["SHA"]

def build_image(service):
    print(f"{b_green} Building docker image for {service} service... {color_off}")

    subprocess.run(f"docker build -t {DOCKER_USERNAME}/over-the-top-with-k8s-{service} -t {DOCKER_USERNAME}/over-the-top-with-k8s-{service}:{SHA} ./{service}",
                   shell=True,
                   check=True)

    print(f"{b_green} Finished building docker image for {service} service {color_off}\n")

if __name__ == '__main__':
    build_image("client")
    build_image("worker")
    build_image("server")
