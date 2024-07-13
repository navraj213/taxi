from datetime import datetime, timedelta
import requests
import threading

#DriverObject = [ Authorization, Medallion, Email ]
# Have to update Authorization every week or so (currently manually)
Jogi = ['eyJhbGciOiJSUzI1NiIsImtpZCI6Ilg1ZVhrNHh5b2pORnVtMWtsMll0djhkbE5QNC1jNTdkTzZRR1RWQndhTmsiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiI2NzI1NWRlMC1kY2EwLTRmZmUtYWIzMy1kZTMwY2M5NWM2ZjgiLCJpc3MiOiJodHRwczovL3BhbnluamIyYzExMC5iMmNsb2dpbi5jb20vN2E2NzJmYTUtNTEwMC00ZWI3LWFiZDMtM2I4NTkxNWEyNDM1L3YyLjAvIiwiZXhwIjoxNzIwODM3MjkyLCJuYmYiOjE3MjA4MzM2OTIsIm9pZCI6IjcyYmIzNzIwLTEwZjktNGJiNS04NDVmLTE0ZDc2NWRkYTJkYyIsInN1YiI6IjcyYmIzNzIwLTEwZjktNGJiNS04NDVmLTE0ZDc2NWRkYTJkYyIsIm5hbWUiOiJqb2dpIiwiZ2l2ZW5fbmFtZSI6IkRldmluZGVyIiwiZXh0ZW5zaW9uX1BBQVZBVFhEVlFBY2NvdW50VmFsaWRhdGlvbiI6dHJ1ZSwiZXh0ZW5zaW9uX1BBUmVnaXN0ZXJlZEFwcGxpY2F0aW9uIjoiVFhELVZRIiwiZXh0ZW5zaW9uX1BBU3BvbnNvckRlcGFydG1lbnQiOiJBVkEiLCJmYW1pbHlfbmFtZSI6IlNpbmdoIiwiZXh0ZW5zaW9uX1Bob25lTnVtYmVyIjoiOTE3OTU3NjE4OSIsImVtYWlscyI6WyJkYW5ueWo4MTIzQGdtYWlsLmNvbSJdLCJ0ZnAiOiJCMkNfMV9QQU5ZTkotVFhEVlEtU2lnblVwU2lnbk9uUGFzc3dvcmRSZXNldF9Vc2VyRmxvdyIsIm5vbmNlIjoiZGVmYXVsdE5vbmNlIiwic2NwIjoidXNlcl9tb2RlIiwiYXpwIjoiMjkxZjg1Y2MtOTU0Ni00NGQzLWJmMDctMWQzZTBlMTQ0OWRlIiwidmVyIjoiMS4wIiwiaWF0IjoxNzIwODMzNjkyfQ.l04r6xbd9W06i6e7AN_ji6E-f2BWRtRj72gF-pTRA-HATfpEetKPONAROa19hkIkUy2yq08Tz1yvjv_zcWekWGfdrJaNFa0N51vfDkNadH7zN4GxtBGLTRUP8uDdYMqpBFIvpmKESGMS0k_hD_sm2yrgipwlXE8BMYU3uzt3TP-n_d4Y8VtyQjw1Q6xGpTsI7EceixXnP1Efdn4NPcbFxMC8PouqNuSHPBTv1g494HA0Vao6Yiek00DvC5bZtMOGidWc82iusLL8TewGEDdw9jFdzFo_sQeJWBb7p142-jef-iVNrKwJ1EuoI9l6SkZzSmdwF7zD1R2Np-cKfTg7lw', "6D24", "dannyj8123@gmail.com"]

Kulwinder = ['eyJhbGciOiJSUzI1NiIsImtpZCI6Ilg1ZVhrNHh5b2pORnVtMWtsMll0djhkbE5QNC1jNTdkTzZRR1RWQndhTmsiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiI2NzI1NWRlMC1kY2EwLTRmZmUtYWIzMy1kZTMwY2M5NWM2ZjgiLCJpc3MiOiJodHRwczovL3BhbnluamIyYzExMC5iMmNsb2dpbi5jb20vN2E2NzJmYTUtNTEwMC00ZWI3LWFiZDMtM2I4NTkxNWEyNDM1L3YyLjAvIiwiZXhwIjoxNzE4ODQzMDAxLCJuYmYiOjE3MTg4Mzk0MDEsIm9pZCI6ImU2MTcyZjJiLWQzNDMtNGQ1OS1iNmVhLTM4M2ZiNGE2N2FjNyIsInN1YiI6ImU2MTcyZjJiLWQzNDMtNGQ1OS1iNmVhLTM4M2ZiNGE2N2FjNyIsIm5hbWUiOiJLVUxXSU5ERVIgIFNJTkdIIiwiZ2l2ZW5fbmFtZSI6IktVTFdJTkRFUiIsImV4dGVuc2lvbl9QQUFWQVRYRFZRQWNjb3VudFZhbGlkYXRpb24iOnRydWUsImV4dGVuc2lvbl9QQVJlZ2lzdGVyZWRBcHBsaWNhdGlvbiI6IlRYRC1WUSIsImV4dGVuc2lvbl9QQVNwb25zb3JEZXBhcnRtZW50IjoiQVZBIiwiZmFtaWx5X25hbWUiOiJTSU5HSCIsImV4dGVuc2lvbl9QaG9uZU51bWJlciI6IjM0Ny0zMjMtNDIzOSAiLCJlbWFpbHMiOlsiUHVuamFiaWJveXowMUBhb2wuY29tIl0sInRmcCI6IkIyQ18xX1BBTllOSi1UWERWUS1TaWduVXBTaWduT25QYXNzd29yZFJlc2V0X1VzZXJGbG93Iiwibm9uY2UiOiJkZWZhdWx0Tm9uY2UiLCJzY3AiOiJ1c2VyX21vZGUiLCJhenAiOiIyOTFmODVjYy05NTQ2LTQ0ZDMtYmYwNy0xZDNlMGUxNDQ5ZGUiLCJ2ZXIiOiIxLjAiLCJpYXQiOjE3MTg4Mzk0MDF9.T0k4IXciNGVs_qgdkhiAMvjnmID5XcKSiqJobR1swNvBNF2hJs6PtQB_jYF9Mal3Ju5WGVKYyWLMVFXmQlkzjLTPJsawxSnXC_bHOPMDs0dZqJwjUfQVeOAthFj0sDVHlc0vQUPrqnUhY2kjCLXbaCaSae7QGoo93mRru0Q4oCGom8XvlRw9-0gbsRYp_akzg_BGSjg2dbzfK_mVk4tQLDzUSgVa3j0uTz7SFcD3Di56exoaX9wCnLhkHsGh4MruJ1r9q8r1L-7npJ7Q9Y-RZN8k1vgMS8-tXY4XHWNnvNWPRy6aObTOY1eHOWa7I585y_iG1Bb_2M1o8QsaLWNtsw', "1T65", "Punjabiboyz01@aol.com"]

Mirza = ['eyJhbGciOiJSUzI1NiIsImtpZCI6Ilg1ZVhrNHh5b2pORnVtMWtsMll0djhkbE5QNC1jNTdkTzZRR1RWQndhTmsiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiI2NzI1NWRlMC1kY2EwLTRmZmUtYWIzMy1kZTMwY2M5NWM2ZjgiLCJpc3MiOiJodHRwczovL3BhbnluamIyYzExMC5iMmNsb2dpbi5jb20vN2E2NzJmYTUtNTEwMC00ZWI3LWFiZDMtM2I4NTkxNWEyNDM1L3YyLjAvIiwiZXhwIjoxNzE4ODQzMTQ1LCJuYmYiOjE3MTg4Mzk1NDUsIm9pZCI6IjNjMDQ5NDk4LWRlODQtNDIyNi1iYTJlLTUwMjg4ZjBkNzY2MiIsInN1YiI6IjNjMDQ5NDk4LWRlODQtNDIyNi1iYTJlLTUwMjg4ZjBkNzY2MiIsIm5hbWUiOiJNSVJaQSAgQkFJRyIsImdpdmVuX25hbWUiOiJNSVJaQSIsImV4dGVuc2lvbl9QQUFWQVRYRFZRQWNjb3VudFZhbGlkYXRpb24iOnRydWUsImV4dGVuc2lvbl9QQVJlZ2lzdGVyZWRBcHBsaWNhdGlvbiI6IlRYRC1WUSIsImV4dGVuc2lvbl9QQVNwb25zb3JEZXBhcnRtZW50IjoiQVZBIiwiZmFtaWx5X25hbWUiOiJCQUlHIiwiZXh0ZW5zaW9uX1Bob25lTnVtYmVyIjoiNjQ2LTcxOS0wNDgwIiwiZW1haWxzIjpbIm1pcnphNzIzQHlhaG9vLmNvbSJdLCJ0ZnAiOiJCMkNfMV9QQU5ZTkotVFhEVlEtU2lnblVwU2lnbk9uUGFzc3dvcmRSZXNldF9Vc2VyRmxvdyIsIm5vbmNlIjoiZGVmYXVsdE5vbmNlIiwic2NwIjoidXNlcl9tb2RlIiwiYXpwIjoiMjkxZjg1Y2MtOTU0Ni00NGQzLWJmMDctMWQzZTBlMTQ0OWRlIiwidmVyIjoiMS4wIiwiaWF0IjoxNzE4ODM5NTQ1fQ.VIcW-svLNz6Um0luR4SN_d-V2XPVTbaM_3TdTrmChJvucZpWVwtTPkvpLpmlisiOLgdCmqolWNq76rCj3q-HYM1iVUhuHL0HGklOTG2_mym1MneO_5g7FCqq54iAhbNA6Y_O2zIkTF1MzegbwLkn0eK2-lTiuNk6oix3SYtsrNQ-V0uvBC8iuTO0oif4Q2n23jHvJQ-vYJ9Wd9lT_XroGI82R8hwUDABAHiEc7y4ClhGx2HL3PoFdiOgFkfsZhBAUieVBaRRICkufUxyOU6JrGjKyYhletoxeA0HmUKf0Z1W7FUdBEGbk5U2Q9_2dRz-KXasjqdqTNOJqZOva2NvkQ', "6P23", "Mirza723@yahoo.com"]

Custom = ['eyJhbGciOiJSUzI1NiIsImtpZCI6Ilg1ZVhrNHh5b2pORnVtMWtsMll0djhkbE5QNC1jNTdkTzZRR1RWQndhTmsiLCJ0eXAiOiJKV1QifQ.eyJvaWQiOiJhMzU5MjVlYy1lMmU2LTQzYzQtYWIwNi1lYTExZGFmNTJiMWEiLCJzdWIiOiJhMzU5MjVlYy1lMmU2LTQzYzQtYWIwNi1lYTExZGFmNTJiMWEiLCJuYW1lIjoiREhBUkFNUEFMIFNJTkdIIiwiZ2l2ZW5fbmFtZSI6IkRIQVJBTVBBTCIsImV4dGVuc2lvbl9QQUFWQVRYRFZRQWNjb3VudFZhbGlkYXRpb24iOnRydWUsImV4dGVuc2lvbl9QQVJlZ2lzdGVyZWRBcHBsaWNhdGlvbiI6IlRYRC1WUSIsImV4dGVuc2lvbl9QQVNwb25zb3JEZXBhcnRtZW50IjoiQVZBIiwiZmFtaWx5X25hbWUiOiJTSU5HSCIsImV4dGVuc2lvbl9QaG9uZU51bWJlciI6Iig5MTcpIDk1Ny02MTg3IiwiZW1haWxzIjpbIlhwcHJlZXR4QGFvbC5jb20iXSwidGZwIjoiQjJDXzFfUEFOWU5KLVRYRFZRLVNpZ25VcFNpZ25PblBhc3N3b3JkUmVzZXRfVXNlckZsb3ciLCJub25jZSI6ImRlZmF1bHROb25jZSIsInNjcCI6InVzZXJfbW9kZSIsImF6cCI6IjI5MWY4NWNjLTk1NDYtNDRkMy1iZjA3LTFkM2UwZTE0NDlkZSIsInZlciI6IjEuMCIsImlhdCI6MTcxNjE3MTM2NCwiYXVkIjoiNjcyNTVkZTAtZGNhMC00ZmZlLWFiMzMtZGUzMGNjOTVjNmY4IiwiZXhwIjoxNzE2MTc0OTY0LCJpc3MiOiJodHRwczovL3BhbnluamIyYzExMC5iMmNsb2dpbi5jb20vN2E2NzJmYTUtNTEwMC00ZWI3LWFiZDMtM2I4NTkxNWEyNDM1L3YyLjAvIiwibmJmIjoxNzE2MTcxMzY0fQ.T47JH9gPneGVA14yDMZ0YgrvGVNUKkLQlZMOyrCMuu6ko3obBfHflg3CxHFDuqewFLRCW1k9dQPCdgeEbxR_IfxkTPR-RpNWw_a9n3JnVeYFpMUc-4hCl53VHQjo80cSBj_KzoItny7f7zUrTNZ2Q3v0OsB0FRFMthsRfZYuZsmPM9wanuwvQ9AM8tKjmV2by4kGI57_ajM8V7fOXIbDZeKotXUQG4FgFIU8G6q2wz3Pt9I1pmYAPfQU_Jfa-tpQ-y4pDUC7PxGsWZbszVenwSqwUAXtSG28Z4hpIH39jU0QTdU7bisO4nQEuPUFIUpeF78VEijSNvXe0nYsawDPrg', "8F83", "xppreetx@aol.com"]

Opp = ['eyJhbGciOiJSUzI1NiIsImtpZCI6Ilg1ZVhrNHh5b2pORnVtMWtsMll0djhkbE5QNC1jNTdkTzZRR1RWQndhTmsiLCJ0eXAiOiJKV1QifQ.eyJvaWQiOiI2ODNkOThmZS04NWY5LTQ3YzktOTAwOS0yNzI2OWNhNmQ2ZjMiLCJzdWIiOiI2ODNkOThmZS04NWY5LTQ3YzktOTAwOS0yNzI2OWNhNmQ2ZjMiLCJuYW1lIjoiREVWSU5ERVIgU0lOR0giLCJnaXZlbl9uYW1lIjoiREVWSU5ERVIiLCJleHRlbnNpb25fUEFBVkFUWERWUUFjY291bnRWYWxpZGF0aW9uIjp0cnVlLCJleHRlbnNpb25fUEFSZWdpc3RlcmVkQXBwbGljYXRpb24iOiJUWEQtVlEiLCJleHRlbnNpb25fUEFTcG9uc29yRGVwYXJ0bWVudCI6IkFWQSIsImZhbWlseV9uYW1lIjoiU0lOR0giLCJleHRlbnNpb25fUGhvbmVOdW1iZXIiOiI5MTcgOTU3IDYxODkiLCJlbWFpbHMiOlsiRGV2aW5kZXI4MTJAeWFob28uY29tIl0sInRmcCI6IkIyQ18xX1BBTllOSi1UWERWUS1TaWduVXBTaWduT25QYXNzd29yZFJlc2V0X1VzZXJGbG93Iiwibm9uY2UiOiJkZWZhdWx0Tm9uY2UiLCJzY3AiOiJ1c2VyX21vZGUiLCJhenAiOiIyOTFmODVjYy05NTQ2LTQ0ZDMtYmYwNy0xZDNlMGUxNDQ5ZGUiLCJ2ZXIiOiIxLjAiLCJpYXQiOjE3MTYxNzM3MDUsImF1ZCI6IjY3MjU1ZGUwLWRjYTAtNGZmZS1hYjMzLWRlMzBjYzk1YzZmOCIsImV4cCI6MTcxNjE3NzMwNSwiaXNzIjoiaHR0cHM6Ly9wYW55bmpiMmMxMTAuYjJjbG9naW4uY29tLzdhNjcyZmE1LTUxMDAtNGViNy1hYmQzLTNiODU5MTVhMjQzNS92Mi4wLyIsIm5iZiI6MTcxNjE3MzcwNX0.cr05sIqrdIGosyqkVvabdN0RXzqVM9_P9SzixSNg1pqogQCyhsEDFMzKW-hNiBIlPTuWRCbc_0AxZ37H3-dgb0aeYidZxTKd6axj_svTNUmK-kBgqUlpdM5uY-N026DZuZN1oFG5B8fFBtSjnlhe_Z9mtxse3PhSzh43cNH9ND-WBQFF6r8TaEFbEnOJHmu54Xlzf8zbFLPyrRCVlsuBXeZm6e4DP_rAuf-7x6eP80KqI4xHHzIMbOPlwYsgBEczJhLMKf_01HYa25EDic9jwczVBN8i1rJwcqMc0HPvnc6cIk7T-X9YHFAQn8aVqEg7hHYKphOiU2ahgPYRseZCrA', "7Y91", "devinder812@yahoo.com"]


Test = ['', '', '']

def get_session_hash():
    url = 'https://gtmsapi.panynj.gov/txd-prod-mobile/v1/api/sessions'
    headers = {
        'Host': 'gtmsapi.panynj.gov',
        'User-Agent': 'PANYNJ%20Virtual%20Taxi%20Dispatch/3 CFNetwork/1410.0.3 Darwin/22.6.0',
        'Connection': 'keep-alive',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.9',
        'Authorization': AUTHORIZATION,
        'Ocp-Apim-Subscription-Key': 'c622816b255045bc85f7e68dbc33c00e',
        'Content-Type': 'application/json-patch+json'
    }
    data = {
        "password": "",
        "taxiCompanyId": 13,
        "medallion": MEDALLIONNUM,
        "userName": EMAIL
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        return get_session_hash()
    session_hash = response.json()['sessionHash']
    return session_hash

def put_location():
    url = 'https://gtmsapi.panynj.gov/txd-prod-mobile/v1/api/virtualQueues/status'

    headers = {
        'Host': 'gtmsapi.panynj.gov',
        'User-Agent': 'PANYNJ%20Virtual%20Taxi%20Dispatch/3 CFNetwork/1410.0.3 Darwin/22.6.0',
        'Connection': 'keep-alive',
        'SessionHashCode': SESSION_HASH,
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.9',
        'Authorization': AUTHORIZATION,
        'Ocp-Apim-Subscription-Key': 'c622816b255045bc85f7e68dbc33c00e',
        'Content-Type': 'application/json-patch+json'
    }

    data = {
        "longitude": -73.713507820474277,
        "latitude": 40.737523713240549
    }

    response = requests.put(url, headers=headers, json=data)
    return response.status_code == 200

def register_taxi():
    url = 'https://gtmsapi.panynj.gov/txd-prod-mobile/v1/api/virtualQueues/register'
    headers = {
        'Host': 'gtmsapi.panynj.gov',
        'User-Agent': 'PANYNJ%20Virtual%20Taxi%20Dispatch/3 CFNetwork/1410.0.3 Darwin/22.6.0',
        'Connection': 'keep-alive',
        'SessionHashCode': SESSION_HASH,
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.9',
        'Authorization': AUTHORIZATION,
        'Ocp-Apim-Subscription-Key': 'c622816b255045bc85f7e68dbc33c00e',
        'Content-Type': 'application/json-patch+json'
    }

    data = {
        "airportAreaCode": "J_H"
    }


    def spam_requests():
        def spam_requests():
            while True:
                response = requests.post(url, headers=headers, json=data)
                if response.status_code == 200:
                    return True
                elif datetime.now() >= timeStarted + timedelta(minutes=5):
                    return False
                try:
                    if response.json()[0:4] == 'Wait':
                        return False
                except:
                    continue

        # Create multiple threads to spam requests
        threads = []
        num_threads = 2  # Specify the number of threads you want to create
        for i in range(num_threads):
            t = threading.Thread(target=spam_requests)
            threads.append(t)
            t.start()

        # Wait for all threads to finish
        for t in threads:
            t.join()
    timeStarted = datetime.now()
    return spam_requests()

def check_status():
    url = 'https://gtmsapi.panynj.gov/txd-prod-mobile/v1/api/virtualQueues/register'
    headers = {
        'Host': 'gtmsapi.panynj.gov',
        'User-Agent': 'PANYNJ%20Virtual%20Taxi%20Dispatch/3 CFNetwork/1410.0.3 Darwin/22.6.0',
        'Connection': 'keep-alive',
        'SessionHashCode': SESSION_HASH,
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.9',
        'Authorization': AUTHORIZATION,
        'Ocp-Apim-Subscription-Key': 'c622816b255045bc85f7e68dbc33c00e',
        'Content-Type': 'application/json-patch+json'
    }
    data = {
        "airportAreaCode": "J_H"
    }
    response = requests.post(url, headers=headers, json=data)
    response = response.json()

    try:
        if len(response)>1:
            return response + ". Try again in a few minutes."
        else:
            return "Success! Log into app now."
    except:
        return "Log into app, thank you for using our service!"


AUTHORIZATION = 'Joe mama'
MEDALLIONNUM = Test[1]
EMAIL = Test[2]

def main(currMedallion):
    global AUTHORIZATION, MEDALLIONNUM, EMAIL, SESSION_HASH
    currMedallion = currMedallion.upper()
    if currMedallion.lower() == "sabi" or currMedallion == "1T65":
        AUTHORIZATION = Kulwinder[0]
        MEDALLIONNUM = Kulwinder[1]
        EMAIL = Kulwinder[2]
    elif currMedallion.lower() == "jogi" or currMedallion == "6D24":
        AUTHORIZATION = Jogi[0]
        MEDALLIONNUM = Jogi[1]
        EMAIL = Jogi[2]
    elif currMedallion.lower() == "mirza" or currMedallion == "6P23":
        AUTHORIZATION = Mirza[0]
        MEDALLIONNUM = Mirza[1]
        EMAIL = Mirza[2]
    elif currMedallion.lower() == "custom" or currMedallion == "8F83":
        AUTHORIZATION = Custom[0]
        MEDALLIONNUM = Custom[1]
        EMAIL = Custom[2]
    elif currMedallion.lower() == "opp" or currMedallion == "7Y91":
        AUTHORIZATION = Opp[0]
        MEDALLIONNUM = Opp[1]
        EMAIL = Opp[2]
    else:
        AUTHORIZATION = Test[0]
        MEDALLIONNUM = Test[1]
        EMAIL = Test[2]

    SESSION_HASH = get_session_hash()
    put_location()
    register_taxi()
    return check_status()