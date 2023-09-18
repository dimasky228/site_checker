import requests
import httpx

server_input_name = input(' ')
server_get_response = httpx.get(server_input_name)
if server_get_response.status_code == 200:
    print("Access is allowed - OK.")
elif server_get_response.status_code == 301:
    print("Permanent Redirect - OK")
elif server_get_response.status_code == 302:
    print("Temporary Redirect - OK")
elif server_get_response.status_code == 400:
    print("Isn't working")
elif server_get_response.status_code == 401:
    print("Isn't working")
elif server_get_response.status_code == 403:
    print("Isn't working")
elif server_get_response.status_code == 404:
    print("Not Found, Isn't working")
elif server_get_response.status_code == 500:
    print("Isn't working")



