from chirpsdk import ChirpConnect, CallbackSet

chirp=ChirpConnect()
chirp.start(send=True,receive=True)

identifier='50 * 51'
payload = bytearray([ord(ch) for ch in identifier])
chirp.send(payload,blocking=True)
print(payload)


