from fastapi import FastAPI
import httpx

expressions_dict = {
    200: "Access is allowed - OK.",
    301: "Permanent Redirect - OK",
    302: "Temporary Redirect - OK",
    400: "Isn't working",
    401: "Isn't working",
    403: "Isn't working",
    404: "Not Found, Isn't working",
    500: "Isn't working"
}

app = FastAPI()


@app.post("/check_website")
async def check_website(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return {"status_code": response.status_code}


@app.get('/')
def home():
    return ("hello")
