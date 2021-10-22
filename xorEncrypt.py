class xorEncrypt():
    
    def cipher(data, key):
        result = ""
        if len(data) > len(key):
            buff = len(data) % len(key)
        # sets key to appropriate length
        for i in range(buff + 1):
            key += key
        # set key to the same length as data
        key = key[:-(len(key)-len(data))]

        for i in range(len(data)):
            result = result + str(int(data[i]) ^ int(key[i]))
        return result
