class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for x in strs:
            length = str(len(x))
            encodedString += (length + "#" + x)
        return encodedString

    def decode(self, s: str) -> List[str]:
        i = 0
        temp = ""
        string = ""
        decoded = []
        while i < len(s):
            if s[i] != "#":
                temp += s[i]
                i += 1
            else:
                y = i + 1
                num = int(temp)
                while y <= num + i:
                    string += s[y]
                    y += 1
                decoded.append(string)
                i = y
                temp = ""
                string = ""
        return decoded
