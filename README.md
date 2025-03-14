##  簡介
ShortURL 是一個簡單的短網址服務，提供 API 來縮短和管理網址。

### 方法一: 透過 Docker Hub 拉取 Image
您可以直接從 Docker Hub 下載並運行本服務：

```
docker pull jimmyhsun/shorturl:latest
```
之後Run Image
```
docker run -d -p 8000:8000 --name short-url-container jimmyhsun/shorturl:latest
```
### 方法二: 一鍵啟動，git clone後直接建立
可以在專案資料夾下啟動Docker

```
docker compose up -d
```

### 查看Swagger文件
請輸入網址
```
http://127.0.0.1:8000/api/docs
```
可在Swagger文件下直接運行POST    
速率限制同個IP下，每分鐘五次