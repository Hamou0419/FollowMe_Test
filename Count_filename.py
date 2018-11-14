from collections import Counter

def count(urls):
    filenames = []
    for url in urls:
        filenames.append(url.split('/')[-1])
    return (Counter(filenames))

urls = [
"http://www.baidu.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"https://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg"
]

print(count(urls))