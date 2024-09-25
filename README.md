# Fetch Rewards Receipt Processor

## Setup and running instructions

1. Prerequisites:

- Clone this repository.
- Install [Docker](https://www.docker.com/) on your machine if do not have it already.

2. Build Docker Image:

- Navigate to the root directory of the repo where the `Dockerfile` and this `README.md` are located.
- Run the following command to build the Docker image:

```
docker build -t <name_of_your_choice> .
```

3. Run Docker Container:

- Now, you can run the following command to start the container:

```
docker run -p 8000:5050 <name_of_your_choice_from_before>
```

4. Accessing the Application:

- You will now be able to access the web application at http://localhost:8000.
- You can now use the defined endpoints from the problem to process receipts and retrieve points: http://localhost:8000/receipts/process for processing receipts and http://localhost:8000/receipts/{id}/points for retrieving points.

5. Stop and Remove Docker Container:

- To stop the running container, first find the container ID with the following command:

```
docker ps
```

- Then stop the container with:

```
docker stop <container-id>
```