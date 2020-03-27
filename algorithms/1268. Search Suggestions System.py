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
        
