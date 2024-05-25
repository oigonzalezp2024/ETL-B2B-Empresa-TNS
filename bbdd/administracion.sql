CREATE DATABASE IF NOT EXISTS administracion;

CREATE TABLE IF NOT EXISTS administracion.empresa (
  id_empresa int(11) AUTO_INCREMENT PRIMARY KEY,
  empresa varchar(50) DEFAULT NULL,
  usuario varchar(50) DEFAULT NULL,
  passw varchar(50) DEFAULT NULL,
  tnsapitoken varchar(50) DEFAULT NULL,
  codsucursal varchar(50) DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS administracion.itemsdescuentos (
  id_itemsdescuentos int(11) AUTO_INCREMENT PRIMARY KEY,
  codconcepto varchar(50) DEFAULT NULL,
  valordto varchar(50) DEFAULT NULL,
  baseretd varchar(50) DEFAULT NULL,
  porcretd varchar(50) DEFAULT NULL,
  porivad varchar(50) DEFAULT NULL,
  centrocostos varchar(50) DEFAULT NULL,
  codarea varchar(50) DEFAULT NULL,
  venta_id int(11) NOT NULL
);

CREATE TABLE IF NOT EXISTS administracion.itemsformapago (
  id_itemsformapago int(11) AUTO_INCREMENT PRIMARY KEY,
  codFormaPago varchar(50) DEFAULT NULL,
  plazoDias varchar(50) DEFAULT NULL,
  fechaVencimiento varchar(50) DEFAULT NULL,
  valor varchar(50) DEFAULT NULL,
  venta_id int(11) NOT NULL
);

CREATE TABLE IF NOT EXISTS administracion.itemspedido (
  id_itemspedido int(11) AUTO_INCREMENT PRIMARY KEY,
  codMat varchar(50) DEFAULT NULL,
  codBodega varchar(50) DEFAULT NULL,
  codTalla varchar(50) DEFAULT NULL,
  codColor varchar(50) DEFAULT NULL,
  cantidad int(11) DEFAULT NULL,
  tipoUnidad varchar(50) DEFAULT NULL,
  descuento int(11) DEFAULT NULL,
  centrosCostos varchar(50) DEFAULT NULL,
  porcIva int(11) DEFAULT NULL,
  valor int(11) DEFAULT NULL,
  impConsumo int(11) DEFAULT NULL,
  observacion varchar(50) DEFAULT NULL,
  venta_id int(11) NOT NULL
);

CREATE TABLE IF NOT EXISTS administracion.venta (
  id_venta int(11) AUTO_INCREMENT PRIMARY KEY,
  codPrefijo varchar(50) DEFAULT NULL,
  numero varchar(50) DEFAULT NULL,
  fecha varchar(50) DEFAULT NULL,
  codTercero varchar(50) DEFAULT NULL,
  codVendedor varchar(50) DEFAULT NULL,
  codDespachar varchar(50) DEFAULT NULL,
  codFormaPago varchar(50) DEFAULT NULL,
  codBanco varchar(50) DEFAULT NULL,
  fechaVence varchar(50) DEFAULT NULL,
  plazoDias int(11) DEFAULT NULL,
  observacion varchar(50) DEFAULT NULL,
  empresa_id int(11) NOT NULL
);

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
