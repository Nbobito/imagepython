import re

def compress(str):
    stripped = re.sub('\s{2,}', ' ', re.sub('\n', ' ', str))
    array = stripped.split(' ')
    
    out = ""
    for i in array:
        if i == "ffffff":
            out += "00"
        elif i == "000000":
            out += "01"
        elif i == "ff0000":
            out += "10"
        elif i == "0000ff":
            out += "11"
    return out

def decompress(str):
    array = re.findall('.{1,2}', str)
    out = ""
    for i in array:
        if i == "00":
            out += "ffffff"
        elif i == "01":
            out += "000000"
        elif i == "10":
            out += "ff0000"
        elif i == "11":
            out += "0000ff"
    return out
    
compressed = compress(image)
decompressed = decompress(compressed)

print(decompressed)
