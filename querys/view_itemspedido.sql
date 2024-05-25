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
FROM view_itemspedido
WHERE venta_id = xxxx;