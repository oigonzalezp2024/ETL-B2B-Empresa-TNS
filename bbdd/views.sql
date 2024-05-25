
CREATE OR REPLACE VIEW administracion.view_venta AS
SELECT id_venta,
codPrefijo,
numero,
fecha,
codTercero,
codVendedor,
codDespachar,
codFormaPago,
codBanco,
fechaVence,
plazoDias,
observacion,
empresa_id 
FROM administracion.venta;

CREATE OR REPLACE VIEW administracion.view_empresa AS
SELECT
id_empresa,
empresa,
usuario,
passw,
tnsapitoken,
codsucursal
FROM administracion.empresa;

CREATE OR REPLACE VIEW administracion.view_itemspedido AS
SELECT
id_itemspedido,
codMat,
codBodega,
codTalla,
codColor,
cantidad,
tipoUnidad,
descuento,
centrosCostos,
porcIva,
valor,
impConsumo,
observacion,
venta_id
FROM administracion.itemspedido;

CREATE OR REPLACE VIEW administracion.view_itemsdescuentos AS
SELECT 
id_itemsdescuentos,
codconcepto,
valordto,
baseretd,
porcretd,
porivad,
centrocostos,
codarea,
venta_id
FROM administracion.itemsdescuentos;

CREATE OR REPLACE VIEW administracion.view_itemsformapago AS
SELECT
id_itemsformapago,
codFormaPago,
plazoDias,
fechaVencimiento,
valor,
venta_id 
FROM administracion.itemsformapago;
