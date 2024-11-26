import requests
import json

# 发送HTTP请求并获取JSON数据
url = 'https://inews-api.tvb.com/news/checkout/live/hd/ott_I-NEWS_h264?profile=safari'
headers = {
    'CLIENT-IP': '127.0.0.1',
    'X-FORWARDED-FOR': '127.0.0.1'
}

response = requests.get(url, headers=headers, verify=False)

# 检查请求是否成功
if response.status_code == 200:
    data = response.json()

    # 提取播放 URL
    hd_url = data.get('content', {}).get('url', {}).get('hd')

    if hd_url:
        # 生成M3U文件内容
        m3u_content = f"""#EXTM3U url-tvg="https://assets.livednow.com/epg.xml"
#EXTINF:-1 tvg-id="無綫新聞台" tvg-logo="https://assets.livednow.com/logo/無線新聞台.png" group-title="新聞財經",無線新聞台
{hd_url}
"""
       
        
        # 将内容写入 playlist.m3u 文件
        with open('playlist.m3u', 'w', encoding='utf-8') as file:
            file.write(m3u_content)
        print("M3U playlist file generated successfully.")
    else:
        print("HD URL not found in the response.")
else:
    print(f"Failed to fetch data, status code: {response.status_code}")
