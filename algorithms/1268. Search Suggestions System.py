#sol https://leetcode.com/problems/search-suggestions-system/discuss/439312/python-Time%3A-O(mnlog(n))-99.9-Space%3A-O(1)-100.0-squeeze-clean-full-comment
#https://happygirlzt.com/code/1268.html
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        # After sort, product list will follow alphabetic order
        products.sort()
        
        # Use two iter to hold the target words between
        start, end, ret = 0, len(products)-1, []
        for n_th, c in enumerate(searchWord):
            # Check between start and end to prevent unusable move
            # Check lenth of current "product string" to prevent "search word" longer than "product string"
            while start <= end and (products[start][n_th] < c if len(products[start])>n_th else True):
                start += 1
            while start <= end and (products[end][n_th] > c if len(products[end])>n_th else True):
                end -= 1
                
            # Append at most three element array
            ret.append(products[start:start+3] if end > start+1 else products[start:end+1])
        return ret

#sol https://github.com/daniel22c/codinginterviewquestions/new/master/algorithms
#Only check whether the current character of the searchWord is at the same index in a product.
#Only search products that have previously been considered.
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        self.possible_products = sorted(products)
        res = []
        for i, c in enumerate(searchWord):
            res.append(self.find_possible_products(c, i))
        return res
    
    def find_possible_products(self, c, idx):
        new_possible_products = []
        for product in self.possible_products:
            if idx < len(product) and product[idx] == c:
                new_possible_products.append(product)
        self.possible_products = new_possible_products
        return self.possible_products[:3]

#brute force
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ret = []
        for i in range(1,len(searchWord)+1):
            arr = []
            for product in products:
                idx=-1
                try:
                    idx = product.index(searchWord[:i])
                except:
                    pass
                if idx==0:
                    arr.append(product)
            if arr:
                arr.sort()
                ret.append(arr[:3])
            else:
                ret.append([])
        return ret
        
