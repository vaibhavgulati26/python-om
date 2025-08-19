# Simple FastAPI HTTP Server

A demonstration FastAPI application with three interactive routes showcasing different web development concepts.

## Features

- **`/hello`** - Simple "Hello World" endpoint
- **`/name`** - Interactive form for name and adjectives with personalized response  
- **`/convert`** - Decimal to binary conversion tool
- **Environment variable management** using dotenv
- **Clean HTML forms** with responsive styling

## Setup and Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --reload --port=8000
```

3. Open your browser and navigate to:
- http://localhost:8000 - Main navigation
- http://localhost:8000/hello - Hello World
- http://localhost:8000/name - Name form  
- http://localhost:8000/convert - Binary converter

## Project Structure

- `main.py` - Main FastAPI application with all routes
- `.env` - Environment variables (PORT, DEBUG)  
- `requirements.txt` - Python dependencies
- `README.md` - Project documentation

## Environment Variables

The application uses the following environment variables from `.env`:

- `PORT` - Server port (default: 8000)
- `DEBUG` - Enable debug/reload mode (default: True)

## Example Usage

### Name Form (`/name`)
Input:
- Name: Vaibhav
- Adjective 1: smart  
- Adjective 2: hardworking

Output: "Vaibhav is smart and hardworking!"

### Binary Converter (`/convert`)
Input: 10
Output: "Binary of 10 is 1010"

## Deployment

This project is ready for deployment to platforms like Heroku, Railway, or any cloud provider that supports Python applications.