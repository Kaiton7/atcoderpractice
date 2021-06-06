# 二分累乗法


import unittest


def modpow(a,n,mod):
    res = 1
    while n>0:
        if n&1:
            res = res * a %mod
        a = a*a%mod
        n>>=1
    return res

class TestM(unittest.TestCase):
    def test_modpow(self):

        self.assertEqual(modpow(3,45,1000000007), 644897553)
        self.assertEqual(modpow(4,5,1000000007), 4**5)



if __name__ == "__main__":
    unittest.main()

