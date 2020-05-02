# 1236. Web Crawler
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        #find host
        idx = startUrl[7:].find("/")
        hostname = 'http://' + startUrl[7:idx]
        
        stack=[startUrl]
        result=set([startUrl]) #set is faster
        
        while stack:
            link = stack.pop()
            urls = htmlParser.getUrls(link)
            for url in urls:
                if url.find(hostname)!=-1 and url not in result:
                    stack.append(url)
                    result.add(url)
        return result
