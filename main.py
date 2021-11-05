from cpf_cnpj import Documento
from validate_docbr import CNPJ

cpf = Documento.documento('15316264754')
cnpj = Documento.documento('35379838000112')
print("CPF:", cpf)
print("CNPJ:", cnpj)