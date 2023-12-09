import requests
import json

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
        'referer': 'https://www.bilibili.com/video/BV1ie411C7Hz/?spm_id_from=333.934.0.0&vd_source=0c2a631b6a3f941a8ddf7fdcad920f42'
    }


def get_response():

    target_url = "https://api.bilibili.com/x/player/wbi/playurl?avid=236982191&bvid=BV1ie411C7Hz&cid=1359176039&qn=0&fnver=0&fnval=4048&fourk=1&gaia_source=&from_client=BROWSER&session=5a9f7a688c72ed6b8b2534b82785f9e3&web_location=1315873&w_rid=d4763de559d65eb3b3bbdb232c21df2f&wts=1702109407"
    res = requests.get(target_url, headers=headers)

    return res


def get_content(res):

    data_json = json.loads(res.text)

    video_url = data_json['data']['dash']['video'][0]['baseUrl']
    audio_url = data_json['data']['dash']['audio'][0]['baseUrl']

    video_content = requests.get(url=video_url, headers=headers).content
    audio_content = requests.get(url=audio_url, headers=headers).content

    with open('video.mp4', 'wb') as file:
        file.write(video_content)
    with open('audio.mp3', 'wb') as file:
        file.write(audio_content)


if __name__ == '__main__':
    res = get_response()
    get_content(res)