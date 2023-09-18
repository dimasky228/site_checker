from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import Form
import httpx

app = FastAPI()


def check_server(server_input_name: str) -> str:
    server_get_response = httpx.get(server_input_name)
    status_code = server_get_response.status_code
    if status_code == 200:
        return "Access is allowed - OK."
    elif status_code == 301:
        return "Permanent Redirect - OK"
    elif status_code == 302:
        return "Temporary Redirect - OK"
    elif status_code == 400:
        return "Isn't working"
    elif status_code == 401:
        return "Isn't working"
    elif status_code == 403:
        return "Isn't working"
    elif status_code == 404:
        return "Not Found, Isn't working"
    elif status_code == 500:
        return "Isn't working"
    else:
        return "Unknown status code"


@app.get("/", response_class=HTMLResponse)
def home():
    return """
        <html>
            <head>
                <title>Server Checker</title>
            </head>
            <body>
                <form method="post" action="/check">
                    <input type="text" name="server_input_name" placeholder="Enter server name">
                    <button type="submit">Check</button>
                </form>
            </body>
        </html>
    """


@app.post("/check")
def check(server_input_name: str = Form(...)):
    server_status = check_server(server_input_name)
    return {
        "Server": server_input_name,
        "Status": server_status
    }
