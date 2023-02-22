#%%
import requests

response = requests.post("http://localhost:8080/users", json={
    "username": "other",
    "email": "potato@hello.com",
    "password": "p0t4t0"
})

print(response.text)
# %%
