import collections
class Sol:
    def find_differrence(self,s,t):
        c=collections.Counter(s)
        idx=0
        for char in t:
            if c[char]==0:
                return idx
            else:
                idx+=1
if __name__ == '__main__':
    p1=Sol()
    print(p1.find_differrence('abcd','abecd'))
