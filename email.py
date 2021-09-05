email = input("Cual es tu correo: ").strip()

usuario = email[:email.index("@")]

dominio= email[email.index("@")+1:]

output = "Tu usuario'{}' Nombre de dominio'{}'".format(usuario,dominio)

print(output)