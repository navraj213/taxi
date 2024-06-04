from datetime import datetime, timedelta
import requests
import threading

#DriverObject = [ Authorization, Medallion, Email ]
Jogi = ['eyJhbGciOiJSUzI1NiIsImtpZCI6Ilg1ZVhrNHh5b2pORnVtMWtsMll0djhkbE5QNC1jNTdkTzZRR1RWQndhTmsiLCJ0eXAiOiJKV1QifQ.eyJvaWQiOiI3MmJiMzcyMC0xMGY5LTRiYjUtODQ1Zi0xNGQ3NjVkZGEyZGMiLCJzdWIiOiI3MmJiMzcyMC0xMGY5LTRiYjUtODQ1Zi0xNGQ3NjVkZGEyZGMiLCJuYW1lIjoiam9naSIsImdpdmVuX25hbWUiOiJEZXZpbmRlciIsImV4dGVuc2lvbl9QQUFWQVRYRFZRQWNjb3VudFZhbGlkYXRpb24iOnRydWUsImV4dGVuc2lvbl9QQVJlZ2lzdGVyZWRBcHBsaWNhdGlvbiI6IlRYRC1WUSIsImV4dGVuc2lvbl9QQVNwb25zb3JEZXBhcnRtZW50IjoiQVZBIiwiZmFtaWx5X25hbWUiOiJTaW5naCIsImV4dGVuc2lvbl9QaG9uZU51bWJlciI6IjkxNzk1NzYxODkiLCJlbWFpbHMiOlsiZGFubnlqODEyM0BnbWFpbC5jb20iXSwidGZwIjoiQjJDXzFfUEFOWU5KLVRYRFZRLVNpZ25VcFNpZ25PblBhc3N3b3JkUmVzZXRfVXNlckZsb3ciLCJub25jZSI6ImRlZmF1bHROb25jZSIsInNjcCI6InVzZXJfbW9kZSIsImF6cCI6IjI5MWY4NWNjLTk1NDYtNDRkMy1iZjA3LTFkM2UwZTE0NDlkZSIsInZlciI6IjEuMCIsImlhdCI6MTcxNjA1ODg5MiwiYXVkIjoiNjcyNTVkZTAtZGNhMC00ZmZlLWFiMzMtZGUzMGNjOTVjNmY4IiwiZXhwIjoxNzE2MDYyNDkyLCJpc3MiOiJodHRwczovL3BhbnluamIyYzExMC5iMmNsb2dpbi5jb20vN2E2NzJmYTUtNTEwMC00ZWI3LWFiZDMtM2I4NTkxNWEyNDM1L3YyLjAvIiwibmJmIjoxNzE2MDU4ODkyfQ.bjnz838m02c5etxuiOC0S_3f-m2zR1wRB6UgSl_qfdmcksDnOAQ-lCd71CxyBSKa_pG5HwllholiNkBllSfh-ReSVntT1AnedOeAKgyBkdw832B496I_wzkw-MdJguYqlznN38RidwuMWsRZHjdM5UYbh2rMy0Z6B4CHDodV75WLh0LqWRVx88GXpscxD1CWqFsKtqlvGOqqKOBv8f2Sf3lC5i1fHiO44yw2YvAFCWzafceiGr0ONKvwjeY-0KtcAojqUQOVLJ3PpCB_cL0QIBk4vYE-f8KbW_lS5-jKLu2ZEOlOrjw8xlo5P6wudrrIcrkrtFhM7gF2FbmInSLuCA', "6D24", "dannyj8123@gmail.com"]

#OLDKulwinder = ['eyJhbGciOiJSUzI1NiIsImtpZCI6Ilg1ZVhrNHh5b2pORnVtMWtsMll0djhkbE5QNC1jNTdkTzZRR1RWQndhTmsiLCJ0eXAiOiJKV1QifQ.eyJvaWQiOiJlNjE3MmYyYi1kMzQzLTRkNTktYjZlYS0zODNmYjRhNjdhYzciLCJzdWIiOiJlNjE3MmYyYi1kMzQzLTRkNTktYjZlYS0zODNmYjRhNjdhYzciLCJuYW1lIjoiS1VMV0lOREVSICBTSU5HSCIsImdpdmVuX25hbWUiOiJLVUxXSU5ERVIiLCJleHRlbnNpb25fUEFBVkFUWERWUUFjY291bnRWYWxpZGF0aW9uIjp0cnVlLCJleHRlbnNpb25fUEFSZWdpc3RlcmVkQXBwbGljYXRpb24iOiJUWEQtVlEiLCJleHRlbnNpb25fUEFTcG9uc29yRGVwYXJ0bWVudCI6IkFWQSIsImZhbWlseV9uYW1lIjoiU0lOR0giLCJleHRlbnNpb25fUGhvbmVOdW1iZXIiOiIzNDctMzIzLTQyMzkgIiwiZW1haWxzIjpbIlB1bmphYmlib3l6MDFAYW9sLmNvbSJdLCJ0ZnAiOiJCMkNfMV9QQU5ZTkotVFhEVlEtU2lnblVwU2lnbk9uUGFzc3dvcmRSZXNldF9Vc2VyRmxvdyIsIm5vbmNlIjoiZGVmYXVsdE5vbmNlIiwic2NwIjoidXNlcl9tb2RlIiwiYXpwIjoiMjkxZjg1Y2MtOTU0Ni00NGQzLWJmMDctMWQzZTBlMTQ0OWRlIiwidmVyIjoiMS4wIiwiaWF0IjoxNzE2MDkwNDY0LCJhdWQiOiI2NzI1NWRlMC1kY2EwLTRmZmUtYWIzMy1kZTMwY2M5NWM2ZjgiLCJleHAiOjE3MTYwOTQwNjQsImlzcyI6Imh0dHBzOi8vcGFueW5qYjJjMTEwLmIyY2xvZ2luLmNvbS83YTY3MmZhNS01MTAwLTRlYjctYWJkMy0zYjg1OTE1YTI0MzUvdjIuMC8iLCJuYmYiOjE3MTYwOTA0NjR9.DYIvQPLVVI0HFi5CqptGZfKtgpx4uOkBSE3Gcd3ce-u0JtVqkktbfaAOQbSQtf4oMn0NDZpdLzx_ADOyelvZQ3dukuT-sGadU7oNUryFgJ7Rwjod09JdCPFPyCdj9dq-QxhLDiIRlbTag4k6Fxl497sQpSqfuLF0E5MWc4Nnt087FzU4jmALhukOUkTHvJq36vZDfNFIJHhPjfDsVcTSPTme677HDgTOif5STCr9t_0nw7l3RWtvgBcWueAMlnMouQDc6OXxNTvpxXn0X1e7X88veI_ufG70sSf3BcmB6zlCdtAhdwbXKm4tptIfdjmez_Oe-S_X11v32JV_GA-i9g', "1T65", "punjabiboyz01@aol.com"]
Kulwinder = ['eyJhbGciOiJSUzI1NiIsImtpZCI6Ilg1ZVhrNHh5b2pORnVtMWtsMll0djhkbE5QNC1jNTdkTzZRR1RWQndhTmsiLCJ0eXAiOiJKV1QifQ.eyJvaWQiOiJlNjE3MmYyYi1kMzQzLTRkNTktYjZlYS0zODNmYjRhNjdhYzciLCJzdWIiOiJlNjE3MmYyYi1kMzQzLTRkNTktYjZlYS0zODNmYjRhNjdhYzciLCJuYW1lIjoiS1VMV0lOREVSICBTSU5HSCIsImdpdmVuX25hbWUiOiJLVUxXSU5ERVIiLCJleHRlbnNpb25fUEFBVkFUWERWUUFjY291bnRWYWxpZGF0aW9uIjp0cnVlLCJleHRlbnNpb25fUEFSZWdpc3RlcmVkQXBwbGljYXRpb24iOiJUWEQtVlEiLCJleHRlbnNpb25fUEFTcG9uc29yRGVwYXJ0bWVudCI6IkFWQSIsImZhbWlseV9uYW1lIjoiU0lOR0giLCJleHRlbnNpb25fUGhvbmVOdW1iZXIiOiIzNDctMzIzLTQyMzkgIiwiZW1haWxzIjpbIlB1bmphYmlib3l6MDFAYW9sLmNvbSJdLCJ0ZnAiOiJCMkNfMV9QQU5ZTkotVFhEVlEtU2lnblVwU2lnbk9uUGFzc3dvcmRSZXNldF9Vc2VyRmxvdyIsIm5vbmNlIjoiZGVmYXVsdE5vbmNlIiwic2NwIjoidXNlcl9tb2RlIiwiYXpwIjoiMjkxZjg1Y2MtOTU0Ni00NGQzLWJmMDctMWQzZTBlMTQ0OWRlIiwidmVyIjoiMS4wIiwiaWF0IjoxNzE2NjIwMDk3LCJhdWQiOiI2NzI1NWRlMC1kY2EwLTRmZmUtYWIzMy1kZTMwY2M5NWM2ZjgiLCJleHAiOjE3MTY2MjM2OTcsImlzcyI6Imh0dHBzOi8vcGFueW5qYjJjMTEwLmIyY2xvZ2luLmNvbS83YTY3MmZhNS01MTAwLTRlYjctYWJkMy0zYjg1OTE1YTI0MzUvdjIuMC8iLCJuYmYiOjE3MTY2MjAwOTd9.Ae4sBRrCx6P7wEabAQij26CKUEk3bGr8tgRFg8Q13yFkBVqzzEq91KUqaxFIsJe_8ZsvQ_Y_2mvBDeeRYdnrs5iC1WDenHdG6BvoLmdz8t8MGaqBKFySMBuQnSAn1vgsCPnJIfSAGcLkU1cKInf7upqbQoS5uguO8ceZr4atlLCH6apoy7q9EBMVX2IRU2OmoeXR3XBu7lSbpvnqKUooVytrD0WsT-4dW7LLLoQ8xDB5lwK_9XDbw30ir9iVkref9YFTL8VkL82h1lGoxzaCTunuV7tyKwyTqUXvMSlAeUIn-vqaFQ2NfAkqwlVOrsadf4EHJnui8PxwzCpw4EEbHg', "1T65", "Punjabiboyz01@aol.com"]

Mirza = ['eyJhbGciOiJSUzI1NiIsImtpZCI6Ilg1ZVhrNHh5b2pORnVtMWtsMll0djhkbE5QNC1jNTdkTzZRR1RWQndhTmsiLCJ0eXAiOiJKV1QifQ.eyJvaWQiOiIzYzA0OTQ5OC1kZTg0LTQyMjYtYmEyZS01MDI4OGYwZDc2NjIiLCJzdWIiOiIzYzA0OTQ5OC1kZTg0LTQyMjYtYmEyZS01MDI4OGYwZDc2NjIiLCJuYW1lIjoiTUlSWkEgIEJBSUciLCJnaXZlbl9uYW1lIjoiTUlSWkEiLCJleHRlbnNpb25fUEFBVkFUWERWUUFjY291bnRWYWxpZGF0aW9uIjp0cnVlLCJleHRlbnNpb25fUEFSZWdpc3RlcmVkQXBwbGljYXRpb24iOiJUWEQtVlEiLCJleHRlbnNpb25fUEFTcG9uc29yRGVwYXJ0bWVudCI6IkFWQSIsImZhbWlseV9uYW1lIjoiQkFJRyIsImV4dGVuc2lvbl9QaG9uZU51bWJlciI6IjY0Ni03MTktMDQ4MCIsImVtYWlscyI6WyJtaXJ6YTcyM0B5YWhvby5jb20iXSwidGZwIjoiQjJDXzFfUEFOWU5KLVRYRFZRLVNpZ25VcFNpZ25PblBhc3N3b3JkUmVzZXRfVXNlckZsb3ciLCJub25jZSI6ImRlZmF1bHROb25jZSIsInNjcCI6InVzZXJfbW9kZSIsImF6cCI6IjI5MWY4NWNjLTk1NDYtNDRkMy1iZjA3LTFkM2UwZTE0NDlkZSIsInZlciI6IjEuMCIsImlhdCI6MTcxNzQ4MDIzMywiYXVkIjoiNjcyNTVkZTAtZGNhMC00ZmZlLWFiMzMtZGUzMGNjOTVjNmY4IiwiZXhwIjoxNzE3NDgzODMzLCJpc3MiOiJodHRwczovL3BhbnluamIyYzExMC5iMmNsb2dpbi5jb20vN2E2NzJmYTUtNTEwMC00ZWI3LWFiZDMtM2I4NTkxNWEyNDM1L3YyLjAvIiwibmJmIjoxNzE3NDgwMjMzfQ.qYqsd_ZLCgnp0rwNDbBlrYmRDpl8yfWBOsJS2uemXwZwK-YL-VpqQfC2qjUCTIs4Cbmd616hIqhnpT16LgHmp0opOzwKCZxhbdUOXmPfhci2_w0_SDR0eWzILxlJUnRwsPVH5dfm5xp_wTgX0gFz8ZT7iqNiDIIRP_t3q9avjep65vVrRs9i7PkP8qSkj0DYaMFZV_8C9OWpBjjDlKGrlZFKsd93ZzKbo97NBMybFI7qGe7tMjXdes329HP_I0y0W8cbvU3l-yfA-UU2kszLHlVBAn8Rd6vSPeimZDc2y6-YCm9EOBtYaGQC3HpxVhger7baUKaukiRM_l2puRVuzg', "mirza723@yahoo.com", "6P23"]

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
