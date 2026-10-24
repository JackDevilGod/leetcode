class Solution:
    def __init__(self) -> None:
        self.storage: dict[str, int] = {}
    
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        index: int = 0
       
        while True:
            slice: list[str] = list(s[index: index + k]) 

            if self.hash(slice, power, modulo) == hashValue:
                return "".join(slice)

            index += 1

    def hash(self, s: list[str], p: int, m: int) -> int:
        return sum([(ord(c) - 96)* (p**n) for (n, c) in enumerate(s)]) % m


if __name__ == "__main__":
    print(Solution().subStrHash("fbxzaad", 31, 100, 3, 32))
