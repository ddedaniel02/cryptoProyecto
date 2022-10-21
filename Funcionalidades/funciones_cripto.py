
from cryptography.hazmat.primitives import hashes


class FuncionesCripto:

    def hashing(self, valor:str):
        valor_bits = valor.encode()
        digest = hashes.Hash(hashes.SHA384())
        digest.update(valor_bits)
        valor_hash = tuple(digest.finalize())
        return valor_hash

    def cifrado(self, valor:str):
