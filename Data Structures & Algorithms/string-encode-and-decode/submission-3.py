class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ''
        for x in strs:
            length = len(x)
            encodedString += str(length) + '#' + x
        return encodedString
    def decode(self, s: str) -> List[str]:
        i = 0
        decodedString = ''
        res = []
        while i < len(s):
            j = s.find('#', i)
            wordLength = int(s[i : j])
            decodedString = s[j+1 : j + 1 + wordLength]
            i = j + 1 + wordLength
            res.append(decodedString)
        return res
