class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        # encoded_string = ""
        # for s in strs:
        #     encoded_string += s.replace("/", "//") + "/:"
        # return encoded_string

        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "/:" + s
        return encoded_string

    def decode(self, str):
        # print(str)
        # decoded_strings = []
        # current_string = ""

        # i = 0
        # while i < len(str):
        #     if str[i] == "/":
        #         if str[i + 1] == "/":
        #             i += 1
        #         elif str[i + 1] == ":":
        #             i = i + 1
        #             decoded_strings.append(current_string)
        #             current_string = ""
        #     else:
        #         current_string += str[i]
        #     i += 1
        # if current_string:
        #     decoded_strings.append(current_string)
        # return decoded_strings
        decoded_strings = []
        current_string = ""

        i = 0
        while i < len(str):
            delimiter = str.find("/:", i)
            length = int(str[i:delimiter])
            current_string = str[delimiter + 2 : delimiter + 2 + length]
            decoded_strings.append(current_string)
            i = delimiter + 2 + length
        return decoded_strings


codec = Codec()
strs = ["Hello", "World"]
print(codec.decode(codec.encode(strs)))
