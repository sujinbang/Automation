
# -- AES256 암호화 --
# 서버 파라미터 값 암복호화
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import urllib.parse
import base64

# AES256 키와 IV 준비
key = b''  # 256비트 키
iv = b''  # 128비트 IV
ciphertext = b''  # 암호화된 토큰

# URL 디코딩
ciphertext_url_decoded = urllib.parse.unquote(ciphertext.decode())

# Base64 디코딩
ciphertext_decoded = base64.b64decode(ciphertext_url_decoded)

# 복호화
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = unpad(cipher.decrypt(ciphertext_decoded), AES.block_size)

print(plaintext.decode('utf-8'))

