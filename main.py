from pysimplesoap.server import SoapDispatcher, SOAPHandler
from BaseHTTPServer import HTTPServer


class Calculator(object):
    def add(self, a,b):
        sum = a+b
        return sum

    def subtract(self, a,b):
        diff = a-b
        return diff

    def multiply(self, a,b):
        product = a*b
        return product

    def divide(self, a,b):
        if b != 0:
            quote = a/b
            return quote
        else:
            return "cannot divide by zero"



dispatcher = SoapDispatcher(
    'my_dispatcher',
    location="http://localhost:8008/",
    action='http://localhost:8008/', # SOAPAction
    namespace="http://example.com/sample.wsdl", prefix="ns0",
    trace=True,
    ns=True)

dispatcher.register_function('sum', Calculator().add, returns={'Result': int}, args={'a': int, 'b': int})
dispatcher.register_function('difference', Calculator().subtract, returns={'Result': int}, args={'a': int, 'b': int})
dispatcher.register_function('product', Calculator().multiply, returns={'Result': int}, args={'a': int, 'b': int})
dispatcher.register_function('quote', Calculator().divide, returns={'Result': int}, args={'a': int, 'b': int})

httpd = HTTPServer(("", 8008), SOAPHandler)
httpd.dispatcher = dispatcher
httpd.serve_forever()