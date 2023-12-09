# Web-Crawler---Videos-in-Bilibili


Steps
1. Load the page at a low speed and look for the files that contain the required information.
2. Find 'user-agent' and 'Referer' in the message header, and "params" and "encSecKey" in the form data.
3. Use requests.get() to crawl the file.
4. Extract the links to the video resources contained in the file.
5. Crawl the link and extract the video and audio resources.

中文
1. 低网速加载网页，寻找包含所需内容的文件。
2. 找到消息头中的'user-agent'和'Referer'，和表单数据中的"params"，"encSecKey"。
3. 使用requests.get()爬取文件。
4. 将文件中包含的视频资源链接提取出来。
5. 爬取该链接，并提取视频和音频资源。
