
# FastAPI Application with Docker

This is a FastAPI project that provides APIs for URL processing, PDF processing, and a chat service. The project is containerized using Docker.

## Project Structure

```
/Fast_apis_development
│
├── /app
│   ├── /routes
│   │   ├── __init__.py
│   │   ├── chat.py        # Chat-related endpoint logic
│   │   ├── pdf_processing.py  # PDF processing logic
│   │   ├── url_processing.py  # URL processing logic
│   │
│   ├── /services
│   │   ├── __init__.py
│   │   ├── chat_service.py   # Chat-related services (business logic)
│   │   ├── pdf_service.py    # PDF handling logic (e.g., store PDF, extract data)
│   │   ├── url_service.py    # URL handling logic (e.g., fetch data from URL)
│   │
│   ├── /utils
│   │   ├── __init__.py
│   │   ├── storage_utils     # Module for storing data (PDFs, URLs, etc.)
│   │   └── web_url_utils     # Helper module for web urls
        ├── pdf_utils     # Helper Module for PDFs
│   │   └── chat_utils     # Helper module for chat_api
│   │  
├── main.py            # FastAPI app and routing│
├── Dockerfile
├── requirements.txt        # Project dependencies (FastAPI, PyPDF2, etc.)
└── README.md               # Project documentation
```

## Requirements

- **Docker**: Ensure Docker is installed and running on your system.
  - [Install Docker](https://docs.docker.com/get-docker/)
- **Python 3.12**: (Only if you run the project without Docker)

## How to Run the Application

### 1. Clone the Repository

```bash
git clone https://github.com/Ansh9728/hygwell.git
cd Fast_apis_development
```

### 2. Docker Setup

#### Step 1: Build the Docker Image

Run the following command to build the Docker image:

```bash
docker build -t myfastapiapp .
```

This will create a Docker image tagged as `myfastapiapp`.

#### Step 2: Run the Docker Container

Once the image is built, you can run the container by executing:

```bash
docker run -d -p 8000:8000 --name fastapi_container myfastapiapp
```

- `-d`: Runs the container in detached mode (in the background).
- `-p 8000:8000`: Maps port 8000 of your local machine to port 8000 of the container.
- `--name fastapi_container`: Names the running container as `fastapi_container`.

#### Step 3: Access the Application

Once the container is running, you can access the FastAPI app at:

- **API Base URL**: `http://localhost:8000`
- **API Documentation** (Swagger UI): `http://localhost:8000/docs`

### 3. Testing and Development

For development purposes, you can directly run the FastAPI app without Docker:

#### Install Dependencies (Optional for Local Development)

First, create a Python virtual environment and install the dependencies from `requirements.txt`:

```bash
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Run the FastAPI Application Locally

You can start the FastAPI server locally using Uvicorn:

```bash
run python main.py
```

The app will be accessible at `http://127.0.0.1:8000/` locally.

### 4. Docker Container Management

#### Stop the Container

To stop the running Docker container:

```bash
docker stop fastapi_container
```

#### Restart the Container

To restart a stopped Docker container:

```bash
docker start fastapi_container
```

#### Remove the Container

To remove the Docker container after stopping it:

```bash
docker rm fastapi_container
```


## Built With

- [FastAPI](https://fastapi.tiangolo.com/) - FastAPI framework for building APIs.
- [Docker](https://www.docker.com/) - Containerization platform for running and deploying apps.

---

This `README.md` file provides all necessary steps to run the FastAPI application using Docker, 
