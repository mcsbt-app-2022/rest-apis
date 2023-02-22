#%%

import requests

users = requests.get("http://localhost:8080/users").json()

for user in users:
    print(user["email"])


# %%
