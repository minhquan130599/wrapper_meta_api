import requests
import uuid
import json
import urllib
def extract_value(text: str, start_str: str, end_str: str) -> str:
    try:
        start = text.index(start_str) + len(start_str)
        end = text.index(end_str, start)
        return text[start:end]
    except ValueError:
        return ""
def get_cookies(session: requests.Session, externalConversationId: str):
    try:
        headers = {
            'accept': '*/*',
            'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
            'origin': 'https://www.meta.ai',
            'priority': 'u=1, i',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
            'sec-ch-ua-full-version-list': '"Microsoft Edge";v="135.0.3179.73", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.85"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"19.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
            'x-asbd-id': '359341',
            'x-fb-lsd': '4PlqDt0mob7o1CNa0eC8P2',
        }
        
        response = session.get(f"https://www.meta.ai/", headers=headers)
        cookies = {
            "_js_datr": extract_value(response.text, '_js_datr":{"value":"', '",'),
            "datr": extract_value(response.text, 'datr":{"value":"', '",'),
            "lsd": extract_value(response.text, '"LSD",[],{"token":"', '"}'),
            "fb_dtsg": extract_value(response.text, 'DTSGInitData",[],{"token":"', '"'),
            "abra_csrf": extract_value(response.text, 'abra_csrf":{"value":"', '",')
        }
        print(cookies)
        headers['cookie'] = f'_js_datr={cookies["_js_datr"]}; abra_csrf={cookies["abra_csrf"]}; datr={cookies["datr"]};'
        response = session.get(f"https://www.meta.ai/prompt/{externalConversationId}", headers=headers)
        cookies = {
            "_js_datr": extract_value(response.text, '_js_datr":{"value":"', '",'),
            "datr": extract_value(response.text, 'datr":{"value":"', '",'),
            "lsd": extract_value(response.text, '"LSD",[],{"token":"', '"}'),
            "fb_dtsg": extract_value(response.text, 'DTSGInitData",[],{"token":"', '"'),
            "abra_csrf": extract_value(response.text, 'abra_csrf":{"value":"', '",')
        }
        print(cookies)
        with open("response.txt", "w", encoding="utf-8") as f:
            f.write(str(response.text))

    except Exception as e:
        print(e)
        
def get_cookies_and_access_token(session: requests.Session):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        'sec-ch-ua-platform': "\"Windows\"",
        'sec-ch-ua': "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
        'sec-ch-ua-mobile': "?0",
        'origin': "https://www.meta.ai",
        'sec-fetch-site': "same-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://www.meta.ai/",
        'accept-language': "vi-VN,vi;q=0.9",
        'priority': "u=1, i",
    }


    response = session.get('https://meta.ai', headers=headers)
    cookies = {
            "_js_datr": extract_value(response.text, '_js_datr":{"value":"', '",'),
            "datr": extract_value(response.text, 'datr":{"value":"', '",'),
            "lsd": extract_value(response.text, '"LSD",[],{"token":"', '"}'),
            "fb_dtsg": extract_value(response.text, 'DTSGInitData",[],{"token":"', '"'),
            "abra_csrf": extract_value(response.text, 'abra_csrf":{"value":"', '",')
        }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.meta.ai',
        'priority': 'u=1, i',
        'referer': 'https://www.meta.ai/',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-full-version-list': '"Microsoft Edge";v="135.0.3179.73", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.85"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"19.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
        'cookie': f'datr={cookies["datr"]}; wd=1912x954; abra_csrf={cookies["abra_csrf"]}',
    }

    data = {

        'lsd': cookies['lsd'],
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'useKadabraAcceptTOSForTempUserMutation',
        'variables': '{"dob":"2005-01-01","__relay_internal__pv__AbraQPDocUploadNuxTriggerNamerelayprovider":"meta_dot_ai_abra_web_doc_upload_nux_tour","__relay_internal__pv__kadabra_show_open_editor_buttonrelayprovider":false,"__relay_internal__pv__AbraSurfaceNuxIDrelayprovider":"12177"}',
        'server_timestamps': 'true',
        'doc_id': '24330743546514627',
    }

    response = session.post('https://www.meta.ai/api/graphql/', headers=headers, data=data)
    
    
    auth_json = json.loads(response.text)
    access_token = auth_json["data"]["xab_abra_accept_terms_of_service"]["new_temp_user_auth"]["access_token"]
    return access_token, cookies
    
    
  