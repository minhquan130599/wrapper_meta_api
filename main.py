import requests
import json
import time
import uuid
from api_meta import get_cookies_and_access_token
from parse import parse_json


headers = {
    'accept': '*/*',
    'accept-language': 'vi',
    'origin': 'https://www.meta.ai',
    'priority': 'u=1, i',
    'referer': 'https://www.meta.ai/',
    'sec-ch-ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',

}

session = requests.Session()
externalConversationId = str(uuid.uuid4())
threadSessionId = str(uuid.uuid4())
access_token, cookies = get_cookies_and_access_token(session)

cookies_ = {
    'datr': cookies['datr'],
    'abra_csrf': cookies['abra_csrf'],
    '_js_datr': cookies["_js_datr"]
    #'wd': '1872x954',
}
while True:
    user_input = input("\nBạn: ")
      
    if user_input.lower() == 'exit':
        print("Tạm biệt!")
        break
    params = {
        'locale': 'user',
    }
    files = {
        'av': (None, '0'),
        'access_token': (None, access_token),
        '__user': (None, '0'),
        '__a': (None, '1'),
        '__req': (None, 's'),
        '__hs': (None, '20193.HYP:kadabra_pkg.2.1...0'),
        'dpr': (None, '1'),
        '__ccg': (None, 'EXCELLENT'),
        '__rev': (None, '1021874544'),
        '__s': (None, 'xf5h1u:85pmg6:wwmzob'),
        '__hsi': (None, '7493451552352053286'),
        '__dyn': (None, '7xeUmwlEnwn8K6EjBAg5S1Dxu13w8CewSwAyUco2qwJw4BwUx609vCwjE1EE2Cw8G1Dz81s8hwGwQw9m1YwBgao6C0Mo2swlo5qfK0EUjwGzE2ZwNwmE2eUlwhE2Lwg81soGdw46wbS1LwTwNxK0-E6O1fxC1nw4xxW2W2C1rwea0Go7a'),
         '__comet_req': (None, '72'),
        'lsd': (None, cookies['lsd']),
        'jazoest': (None, '2898'),
        '__spin_r': (None, '1021874544'),
        '__spin_b': (None, 'trunk'),
        '__spin_t': (None, '1744705148'),
        '__jssesw': (None, '1'),
        '__crn': (None, 'comet.kadabra.KadabraPromptRoute'),
        'fb_api_caller_class': (None, 'RelayModern'),
        'fb_api_req_friendly_name': (None, 'useKadabraSendMessageMutation'),
        'variables': (None, '{"message":{"sensitive_string_value":"'+user_input+'"},"externalConversationId":"'+externalConversationId+'","offlineThreadingId":"'+str(int(time.time() * 1000))+'","threadSessionId":"'+threadSessionId+'","suggestedPromptIndex":null,"promptPrefix":null,"entrypoint":"KADABRA__HOME__UNIFIED_INPUT_BAR","attachments":[],"attachmentsV2":[],"activeMediaSets":[],"activeCardVersions":[],"activeArtifactVersion":null,"userUploadEditModeInput":null,"reelComposeInput":null,"qplJoinId":"f668613cc9dfa5c15","sourceRemixPostId":null,"gkKadabraArtifactsEnabled":false,"gkPlannerOrReasoningEnabled":false,"selectedModel":"BASIC_OPTION","conversationMode":null,"conversationStarterId":null,"promptType":null,"artifactRewriteOptions":null,"__relay_internal__pv__AbraArtifactsEnabledrelayprovider":false,"__relay_internal__pv__KadabraMemoryEnabledrelayprovider":false,"__relay_internal__pv__AbraPlannerEnabledrelayprovider":false,"__relay_internal__pv__AbraWidgetsEnabledrelayprovider":false,"__relay_internal__pv__KadabraEmailCalendarIntegrationrelayprovider":false,"__relay_internal__pv__AbraBugNubrelayprovider":false,"__relay_internal__pv__AbraRedteamingrelayprovider":false,"__relay_internal__pv__AbraDebugDevOnlyrelayprovider":false,"__relay_internal__pv__AbraSearchInlineReferencesEnabledrelayprovider":true,"__relay_internal__pv__AbraComposedTextWidgetsrelayprovider":true,"__relay_internal__pv__AbraSearchReferencesHovercardEnabledrelayprovider":true,"__relay_internal__pv__AbraThreadsEnabledrelayprovider":false,"__relay_internal__pv__WebPixelRatiorelayprovider":1,"__relay_internal__pv__AbraArtifactDragImagineFromConversationrelayprovider":false,"__relay_internal__pv__AbraQPDocUploadNuxTriggerNamerelayprovider":"meta_dot_ai_abra_web_doc_upload_nux_tour","__relay_internal__pv__kadabra_show_open_editor_buttonrelayprovider":false,"__relay_internal__pv__AbraSurfaceNuxIDrelayprovider":"12177","__relay_internal__pv__KadabraArtifactsEnabledrelayprovider":false,"__relay_internal__pv__KadabraConversationRenamingrelayprovider":true,"__relay_internal__pv__AbraIsLoggedOutrelayprovider":true,"__relay_internal__pv__KadabraArtifactsRewriteV2relayprovider":false,"__relay_internal__pv__AbraArtifactEditorDebugModerelayprovider":false,"__relay_internal__pv__AbraArtifactEditorSaveEnabledrelayprovider":false,"__relay_internal__pv__AbraArtifactEditorDownloadHTMLEnabledrelayprovider":false,"__relay_internal__pv__AbraArtifactsRenamingEnabledrelayprovider":false}'),
        'server_timestamps': (None, 'true'),
        'doc_id': (None, '9480453975374168'),
    }

    response = requests.post('https://graph.meta.ai/graphql', params=params, cookies=cookies_, headers=headers, files=files, stream=True)
    if response.status_code == 200:
        for line in response.iter_lines():
            if line:  # Đảm bảo dòng không rỗng
                # Xử lý dữ liệu (thường là JSON)
                data = json.loads(line.decode('utf-8'))
                snippet = parse_json(data)
                if not snippet:
                    continue
                print("\033c", end="")  # Xóa màn hình (trong terminal)
                print(snippet)
    else:
        print(f"Error status code: {response.status_code}")
        print(f"Error response: {response.text}")
        break
    time.sleep(1)