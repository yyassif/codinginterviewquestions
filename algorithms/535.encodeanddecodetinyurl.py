# using #2 approach from leetcode sol https://leetcode.com/articles/encode-and-decode-tinyurl/
import sys
class Codec:
    def __init__(self):
        self.charSet = ""
        for i in range(0, 10):
            self.charSet+=str(i)
        for i in range(65, 65+26):
            self.charSet+=str(chr(i))
        for i in range(97, 97+26):
            self.charSet+=str(chr(i))
        # print(self.charSet)
        self.map = {}
        self.counter=sys.maxsize
        print(self.charSet, len(self.charSet))
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        def get_encode():
            string=""
            cnt=self.counter
            while cnt>0:
                cnt-=1
                string+=str(self.charSet[cnt%62])
                print(cnt, string)
                cnt //=62
            return string
        encoded = get_encode()
        print("enc:",encoded)
        self.map[encoded] = longUrl
        self.counter-=1
        return encoded
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl=="" or shortUrl==None:
            return "http://tinyurl.com/"
        shortUrl = shortUrl.replace("http://tinyurl.com/","")
        long_url = ""
        if shortUrl in self.map:
            long_url = self.map[shortUrl]
        return long_url
