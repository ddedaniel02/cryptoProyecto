
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

from cryptography.hazmat.primitives.asymmetric import rsa


# INTRODUCIR CONTRASEÑA DE ADMINISTRADOR PARA EL CIFRADO DE LA CLAVE PRIVADA
password_admin = input('Introduce la contraseña de administrador por favor: ')
password_bytes = password_admin.encode('utf-8')
# GENERAR NUEVA CLAVE PRIVADA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=4096,
    backend=default_backend()
)

# SERIALIZAR Y GUARDAR LA CLAVE PRIVADA
with open("res/private_key.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(password_bytes)
    ))
# GENERAR NUEVA CLAVE PUBLICA CON PRIVADA
public_key = private_key.public_key()

# SERIALIZAR Y GUARDAR LA CLAVE PUBLICA
with open("res/public_key.pem", "wb") as f:
    f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
))


