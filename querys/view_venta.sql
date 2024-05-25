SELECT
id_venta,
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
FROM view_venta
where empresa_id = xxxx;