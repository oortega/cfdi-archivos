# -*- coding: utf-8 -*-
import pprint
import datetime 
import json
import os
from cfdi.cfdi import SATcfdi, CfdiStamp
from cfdi.finkok import PACFinkok
import tempfile
import lxml.etree as ET

PATH = os.path.abspath(os.path.dirname(__file__))
CERT_NUM = '20001000000300022815'
key_path = os.path.join("cfdi/certificados","cert_test.key")
cert_path = os.path.join("cfdi/certificados","cert_test.cer")
pem_path = os.path.join("cfdi/certificados","cert_test2.pem")
path_xlst = os.path.join("cfdi/xslt","cadena_3.3_1.2.xslt")
 
#Generamos un Dic
with open('cfdi_minimo.json') as f:
    datos = json.load(f)
#Generamos XML
cfdi = SATcfdi(datos)
cfdi_xml =  cfdi.get_xml()

#Sellamos la Factura
xml_instace = CfdiStamp(cfdi_xml, key_path, cert_path, pem_path, CERT_NUM)
xml_sellado = xml_instace.add_sello()

# res_file = open('sellado.xml', 'w')
# res_file.write(xml_sellado)
# res_file.close()
# print "--------------------"

# with open('sellado.xml') as f:
#     datos = f.read()

#Timbrar la factura

timbrar = PACFinkok()
result = timbrar.cfdi_stamp(xml_sellado)

if result:
    print result['xml']
else:
    print "timbrar.error"
