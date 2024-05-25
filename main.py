
import json
import requests
from app.controller.ControllerEmpresa.ControllerEmpresa import ControllerEmpresa
from app.controller.ControllerItemsFormaPago.ControllerItemsFormaPago import ControllerItemsFormaPago
from app.controller.ControllerItemsPedido.ControllerItemsPedido import ControllerItemsPedido
from app.controller.ControllerVenta.ControllerVenta import ControllerVenta

controllerEmpresa = ControllerEmpresa()
empresas = json.loads(controllerEmpresa.controller("1"))

response = []
for empresa in empresas:
    empresaNombre = empresa['empresa']
    usuario = empresa['usuario']
    password = empresa['password']
    tnsapitoken = empresa['tnsapitoken']
    codsucursal = empresa['codsucursal']
    
    controllerItemsPedido = ControllerVenta()
    ventas = json.loads(controllerItemsPedido.controller(empresa['id_empresa']))
    sells = []

    for venta in ventas:
        sell = {}
        sell['codPrefijo'] = venta['codPrefijo']
        sell['fecha'] = venta['fecha']
        sell['codTercero'] = venta['codTercero']
        sell['codVendedor'] = venta['codVendedor']
        sell['codDespachar'] = venta['codDespachar']
        sell['codFormaPago'] = venta['codFormaPago']
        sell['codBanco'] = venta['codBanco']
        sell['fechaVence'] = venta['fechaVence']
        sell['plazoDias'] = venta['plazoDias']
        sell['observacion'] = venta['observacion']
        sell['itemsPedido'] = []
        sell['itemsFormaPago'] = []
        controllerItemsPedido = ControllerItemsPedido()
        sell['itemsPedido'] = json.loads(controllerItemsPedido.controller(venta['id_venta']))
        print(venta['id_venta'])
        print(sell)    

        controllerItemsPedido = ControllerItemsFormaPago()
        sell['itemsFormaPago'] = json.loads(controllerItemsPedido.controller(venta['id_venta']))
        
        url = "https://api.tns.co/api/Ventas/Crear?"
        url+="empresa="+empresaNombre
        url+="&usuario="+usuario
        url+="&password="+password
        url+="&tnsapitoken="+tnsapitoken
        url+="&codsucursal="+codsucursal

        r = requests.post(url, json=sell)
        #print(r.status_code)
        response.append(r.json())
        sells.append(sell)

controllerEmpresa.writeFile("./data/respuestasTNS.json",json.dumps(response,indent=4))
print(json.dumps(sells,indent=4))
