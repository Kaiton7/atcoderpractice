## 逆元を求める処理を記す
## mとaが互いに素であれば良い
## 
import unittest

def modinv(a:int, m:int):
    b,u,v = m,1,0
    
    while b:
        t=  a//b
        a -= t*b
        a,b = b,a
        u-= t*v
        u,v = v,u

    u%= m
    if u<0:
        u+=m
    return u

def test():
    MOD = 1000000007

    a = 29875326655643
    b = 9237523
    a %= MOD

    print(a * modinv(b, MOD) % MOD,"== 123456789")

class TestM(unittest.TestCase):
    """test class of tashizan.py
    """

    def test_modinv(self):
        MOD = 1000000007

        a = 29875326655643
        b = 9237523
        a %= MOD

        self.assertEqual(a * modinv(b, MOD) % MOD,341069608)



if __name__ == "__main__":
    unittest.main()

