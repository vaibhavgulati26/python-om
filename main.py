
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
import os
import asyncio
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fix for Windows asyncio event loop issue
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

app = FastAPI(title="Simple FastAPI HTTP Server", version="1.0.0")

@app.get("/hello")
def hello():
    """Simple hello world endpoint"""
    return {"message": "Hello World"}

@app.get("/name", response_class=HTMLResponse)
def name_form():
    """Display HTML form for name and adjectives"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Name Form</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f5f5f5;
            }
            .container {
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #333;
                text-align: center;
                margin-bottom: 30px;
            }
            .form-group {
                margin-bottom: 20px;
            }
            label {
                display: block;
                margin-bottom: 5px;
                font-weight: bold;
                color: #555;
            }
            input[type="text"] {
                width: 100%;
                padding: 12px;
                border: 2px solid #ddd;
                border-radius: 5px;
                font-size: 16px;
                box-sizing: border-box;
            }
            input[type="text"]:focus {
                border-color: #4CAF50;
                outline: none;
            }
            button {
                background-color: #4CAF50;
                color: white;
                padding: 12px 24px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
                width: 100%;
                margin-top: 10px;
            }
            button:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Tell us about yourself!</h1>
            <form method="post" action="/name">
                <div class="form-group">
                    <label for="name">Your Name:</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="adjective1">First Adjective:</label>
                    <input type="text" id="adjective1" name="adjective1" required>
                </div>
                <div class="form-group">
                    <label for="adjective2">Second Adjective:</label>
                    <input type="text" id="adjective2" name="adjective2" required>
                </div>
                <button type="submit">Submit</button>
            </form>
        </div>
    </body>
    </html>
    """
    return html_content

@app.post("/name", response_class=HTMLResponse)
def process_name(name: str = Form(...), adjective1: str = Form(...), adjective2: str = Form(...)):
    """Process the name form submission"""
    message = f"{name} is {adjective1} and {adjective2}!"
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Result</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f5f5f5;
            }}
            .container {{
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                text-align: center;
            }}
            h1 {{
                color: #4CAF50;
                margin-bottom: 20px;
            }}
            .result {{
                font-size: 24px;
                color: #333;
                margin: 30px 0;
                padding: 20px;
                background-color: #f0f8ff;
                border-radius: 5px;
                border-left: 4px solid #4CAF50;
            }}
            .back-link {{
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background-color: #4CAF50;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }}
            .back-link:hover {{
                background-color: #45a049;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Here's what we know about you:</h1>
            <div class="result">{message}</div>
            <a href="/name" class="back-link">Try Again</a>
        </div>
    </body>
    </html>
    """
    return html_content

@app.get("/convert", response_class=HTMLResponse)
def convert_form():
    """Display HTML form for decimal to binary conversion"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Decimal to Binary Converter</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f5f5f5;
            }
            .container {
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #333;
                text-align: center;
                margin-bottom: 30px;
            }
            .form-group {
                margin-bottom: 20px;
            }
            label {
                display: block;
                margin-bottom: 5px;
                font-weight: bold;
                color: #555;
            }
            input[type="number"] {
                width: 100%;
                padding: 12px;
                border: 2px solid #ddd;
                border-radius: 5px;
                font-size: 16px;
                box-sizing: border-box;
            }
            input[type="number"]:focus {
                border-color: #2196F3;
                outline: none;
            }
            button {
                background-color: #2196F3;
                color: white;
                padding: 12px 24px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
                width: 100%;
                margin-top: 10px;
            }
            button:hover {
                background-color: #1976D2;
            }
            .info {
                background-color: #e3f2fd;
                padding: 15px;
                border-radius: 5px;
                margin-top: 20px;
                color: #1565c0;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Decimal to Binary Converter</h1>
            <form method="post" action="/convert">
                <div class="form-group">
                    <label for="decimal">Enter a Decimal Number:</label>
                    <input type="number" id="decimal" name="decimal" min="0" required>
                </div>
                <button type="submit">Convert to Binary</button>
            </form>
            <div class="info">
                Enter any positive decimal number and we'll convert it to binary!
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

@app.post("/convert", response_class=HTMLResponse)
def process_convert(decimal: int = Form(...)):
    """Process the decimal to binary conversion"""
    if decimal < 0:
        error_message = "Please enter a non-negative number."
        binary_result = "Error"
    else:
        binary_result = bin(decimal)[2:]  # Remove '0b' prefix
        error_message = None
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Conversion Result</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f5f5f5;
            }}
            .container {{
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                text-align: center;
            }}
            h1 {{
                color: #2196F3;
                margin-bottom: 20px;
            }}
            .result {{
                font-size: 24px;
                color: #333;
                margin: 30px 0;
                padding: 20px;
                background-color: #f0f8ff;
                border-radius: 5px;
                border-left: 4px solid #2196F3;
            }}
            .error {{
                font-size: 18px;
                color: #f44336;
                margin: 30px 0;
                padding: 20px;
                background-color: #ffebee;
                border-radius: 5px;
                border-left: 4px solid #f44336;
            }}
            .back-link {{
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background-color: #2196F3;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }}
            .back-link:hover {{
                background-color: #1976D2;
            }}
            .binary {{
                font-family: 'Courier New', monospace;
                font-weight: bold;
                color: #1976D2;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Conversion Result</h1>
            {"<div class='error'>" + error_message + "</div>" if error_message else f"<div class='result'>Binary of {decimal} is <span class='binary'>{binary_result}</span></div>"}
            <a href="/convert" class="back-link">Convert Another Number</a>
        </div>
    </body>
    </html>
    """
    return html_content

@app.get("/")
def root():
    """Root endpoint with navigation"""
    return {
        "message": "Welcome to Simple FastAPI HTTP Server",
        "available_routes": {
            "/hello": "Simple hello world message",
            "/name": "Interactive name and adjectives form",
            "/convert": "Decimal to binary converter"
        }
    }

if __name__ == "__main__":
    import uvicorn
    
    # Set Windows Proactor Event Loop Policy to fix Python 3.12 + Windows compatibility
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    
    port = int(os.getenv("PORT", 8000))
    debug = os.getenv("DEBUG", "False").lower() == "true"
    
    uvicorn.run("main:app", host="127.0.0.1", port=port, reload=debug)


