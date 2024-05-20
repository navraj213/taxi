import requests

url = 'https://gtmsapi.panynj.gov/txd-prod-mobile/v1/api/virtualQueues/register'

headers = {
    'Host': 'gtmsapi.panynj.gov',
    'User-Agent': 'PANYNJ%20Virtual%20Taxi%20Dispatch/3 CFNetwork/1410.0.3 Darwin/22.6.0',
    'Connection': 'keep-alive',
    'SessionHashCode': '90FF29AF630B8EDCE855AE0F82A5AF456DB6FA',
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization': 'eyJhbGciOiJSUzI1NiIsImtpZCI6Ilg1ZVhrNHh5b2pORnVtMWtsMll0djhkbE5QNC1jNTdkTzZRR1RWQndhTmsiLCJ0eXAiOiJKV1QifQ.eyJvaWQiOiJhMzU5MjVlYy1lMmU2LTQzYzQtYWIwNi1lYTExZGFmNTJiMWEiLCJzdWIiOiJhMzU5MjVlYy1lMmU2LTQzYzQtYWIwNi1lYTExZGFmNTJiMWEiLCJuYW1lIjoiREhBUkFNUEFMIFNJTkdIIiwiZ2l2ZW5fbmFtZSI6IkRIQVJBTVBBTCIsImV4dGVuc2lvbl9QQUFWQVRYRFZRQWNjb3VudFZhbGlkYXRpb24iOnRydWUsImV4dGVuc2lvbl9QQVJlZ2lzdGVyZWRBcHBsaWNhdGlvbiI6IlRYRC1WUSIsImV4dGVuc2lvbl9QQVNwb25zb3JEZXBhcnRtZW50IjoiQVZBIiwiZmFtaWx5X25hbWUiOiJTSU5HSCIsImV4dGVuc2lvbl9QaG9uZU51bWJlciI6Iig5MTcpIDk1Ny02MTg3IiwiZW1haWxzIjpbIlhwcHJlZXR4QGFvbC5jb20iXSwidGZwIjoiQjJDXzFfUEFOWU5KLVRYRFZRLVNpZ25VcFNpZ25PblBhc3N3b3JkUmVzZXRfVXNlckZsb3ciLCJub25jZSI6ImRlZmF1bHROb25jZSIsInNjcCI6InVzZXJfbW9kZSIsImF6cCI6IjI5MWY4NWNjLTk1NDYtNDRkMy1iZjA3LTFkM2UwZTE0NDlkZSIsInZlciI6IjEuMCIsImlhdCI6MTcxNjA1NDkyNSwiYXVkIjoiNjcyNTVkZTAtZGNhMC00ZmZlLWFiMzMtZGUzMGNjOTVjNmY4IiwiZXhwIjoxNzE2MDU4NTI1LCJpc3MiOiJodHRwczovL3BhbnluamIyYzExMC5iMmNsb2dpbi5jb20vN2E2NzJmYTUtNTEwMC00ZWI3LWFiZDMtM2I4NTkxNWEyNDM1L3YyLjAvIiwibmJmIjoxNzE2MDU0OTI1fQ.ZHNJt_O99fmfebFirzdBXqFYqqncgZ98wgLqttbJw2QRbcmS4vHz8IwBL2X4K7Wdvk7ECcLpmy0BP3-Hocj77yimPpFaZYyntIB4OohlpkWIwxx8FR1LCaurPefR5aQQUBwI-YIS2Z0QKgx6G7YO29Ep-kakHq4xiQJyNQfmpSpOlt7o2IeZStkpktLnjuIJF-NxmdA9sNW2_tlPRyt097LxnFXcvfjpOpb264uhKyJ_VoAEJ20UvvMiiGXPOCLfklUuCJMMp-20pOygYnXUPf56rMgPYHfqTeWEuE-YxvjksUkmYkLLIVX1NnnLT6u-_cKjP4DocaIwkDUU2e8FVw',
    'Ocp-Apim-Subscription-Key': 'c622816b255045bc85f7e68dbc33c00e',
    'Content-Type': 'application/json-patch+json'
}

data = {
    "airportAreaCode": "J_H"
}


response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
