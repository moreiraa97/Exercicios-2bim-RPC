from xmlrpc.server import SimpleXMLRPCServer


def somaisoma(i, a):
  return i + a


def sobtraisub(i, a):
  return i - a


def multiplicaismult(i, a):
  return i * a


def divideisdiv(i, a):
  if (i == 0 or a == 0):
    return 0
  else:
    return i / a


server = SimpleXMLRPCServer(("0.0.0.0", 8000))
server.register_function(somaisoma, "somaisoma")
server.register_function(sobtraisub, "sobtraisub")
server.register_function(multiplicaismult, "multiplicaismult")
server.register_function(divideisdiv, "divideisdiv")

print("Servidor ligado")
server.serve_forever()