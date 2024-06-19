import os
import subprocess

color_off = "\033[0m"
b_green = "\033[1;32m"
b_red = "\033[0;31m"


DOCKER_USERNAME = os.environ["DOCKER_USERNAME"]
DOCKER_ACCESS_TOKEN = os.environ["DOCKER_ACCESS_TOKEN"]
SHA = os.environ["SHA"]

def push_image_with_tag_latest_to_repo(service):
    print(f"{b_green} Pushing {service} docker image with tag latest to repo... {color_off}")
    subprocess.run(f"docker push {DOCKER_USERNAME}/over-the-top-with-k8s-{service}", shell=True, check=True)
    print(f"{b_green} Successfuly pushed {service} image with tag latest {color_off}\n")

def push_image_with_sha_tag_to_repo(service):
    print(f"{b_green} Pushing {service} docker image with SHA tag to repo... {color_off}")
    subprocess.run(f"docker push {DOCKER_USERNAME}/over-the-top-with-k8s-{service}:{SHA}", shell=True, check=True)
    print(f"{b_green} Successfuly pushed {service} image with SHA tag {color_off}\n")

if __name__ == '__main__':
    print(f"{b_green} Logging into DockerHub... {color_off}")
    subprocess.run(f"""docker login --username {DOCKER_USERNAME} --password {DOCKER_ACCESS_TOKEN}""", shell=True, check=True)

    # we push tag latest so that it can be used for local deployments
    push_image_with_tag_latest_to_repo("client")
    push_image_with_tag_latest_to_repo("worker")
    push_image_with_tag_latest_to_repo("server")

    push_image_with_sha_tag_to_repo("client")
    push_image_with_sha_tag_to_repo("worker")
    push_image_with_sha_tag_to_repo("server")
