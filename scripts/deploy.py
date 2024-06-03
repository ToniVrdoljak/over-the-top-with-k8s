import os
import subprocess

color_off = "\033[0m"
b_green = "\033[1;32m"
b_red = "\033[0;31m"

DOCKER_USERNAME = os.environ["DOCKER_USERNAME"]
SHA = os.environ["SHA"]

def applyNewestImage(service):
    print(f"{b_green} Applying newest image to {service}-deployment... {color_off}")
    subprocess.run(f"kubectl set image deployments/{service}-deployment {service}={DOCKER_USERNAME}/over-the-top-with-k8s-{service}:{SHA}", shell=True, check=True)
    print(f"{b_green} Succesfully applied newest image to {service}-deployment {color_off}\n")

if __name__ == '__main__':
    print(f"{b_green} Applying k8s configs... {color_off}")
    subprocess.run("kubectl apply -R -f k8s/configs", shell=True, check=True)
    print(f"{b_green} k8s configs successfully applied {color_off}\n")

    applyNewestImage("client")
    applyNewestImage("worker")
    applyNewestImage("server")
