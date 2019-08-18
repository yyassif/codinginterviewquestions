class Codec:
    map = {}
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        #check if the longUrl already exists
        try:
            self.map[longUrl]
            return self.map[longUrl]
        except:
            self.map[longUrl] = "http://tinyurl.com/"+self.generate_random_string_length6()
        return self.map[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        for k,v in self.map.items():
            if(shortUrl==v):
                return k
        return None
    def generate_random_string_length6(self):
        #generate character array A to Z , a to z, 0 to 9
        char_arr = []
        # char_arr =list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
                 
        string =""
        for i in range(ord('0'), ord('9') + 1): #0 to 9, 10 of them
            char_arr.extend(chr(i))
        for i in range(ord('A'), ord('Z') + 1): #A to Z : 26 of them
            char_arr.extend(chr(i))
        for i in range(ord('a'), ord('z') + 1): #a to z 26 of them
            char_arr.extend(chr(i))
        #randomly generate string of length 6
        while(True):
            for i in range(6):
                index = random.randint(0,61) #randomly generate 1 in 62 probability
                string+= char_arr[index]
            isDuplicate=False
            for k,v in self.map.items():
                if v==string:
                    isDuplicate=True
                    break
            if isDuplicate==False:
                break
        return string

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
