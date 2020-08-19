import base64

key = input(("Please input the Base64 Key: "))

#key = "REY1NExqZVJ2OEVGMGo0OHRvSW5FMVFYM01KZi1pSlhld0VobnFSWXBVc0cwRDFSOlk3VkJDZ2JZeXpWWjFWOHZ6M29GWE9sWkVUS2dvaUVRc245R1U1V1ppaU4xNFl4ZA=="

encode_key = key.encode('ascii')
m_bytes = base64.standard_b64decode(encode_key)
decode_key = m_bytes.decode('ascii')

#print(decode_key)

decode_key = decode_key.split(':')

#print(decode_key)

vendor_key = decode_key.pop(0)

user_key = decode_key.pop(0)

print('Vendor Key = {}'.format(vendor_key),
      'User Key = {}' .format(user_key))