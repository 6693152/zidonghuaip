import requests
from bs4 import BeautifulSoup

# 定义一个函数来获取IP地址
def get_ips_from_url(url):
    try:
        # 发送HTTP请求获取网页内容
        response = requests.get(url)
        # 检查请求是否成功
        response.raise_for_status()
        
        # 使用BeautifulSoup解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 根据不同的URL结构提取IP地址
        if 'cloudflare' in url:
            # CloudFlare的结构
            ips = soup.find_all('td', class_='ip')
        elif 'ip.164746.xyz' in url:
            # 164746.xyz的结构
            ips = soup.find_all('td', class_='ip')
        else:
            # 默认结构
            ips = soup.find_all('td', class_='ip')
        
        # 提取IP地址
        return [ip.get_text(strip=True) for ip in ips]
    except requests.RequestException as e:
        print(f"请求错误: {e}")
        return []

# 定义URL列表
urls = [
    'https://monitor.gacjie.cn/page/cloudflare/ipv4.html',
    'https://ip.164746.xyz',
    # 'https://cfno1.pages.dev/pure'  # 注意：此URL内容获取失败，已注释掉
]

# 打开文件准备写入
with open('ip.txt', 'w') as file:
    for url in urls:
        # 获取当前URL的IP地址列表
        ips = get_ips_from_url(url)
        # 遍历IP地址列表，写入文件
        for ip in ips:
            file.write(ip + '\n')

print('IP地址已保存到ip.txt文件中。')
