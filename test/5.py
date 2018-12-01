
select *.*
 from reportfield join  reportextinfo
   on reportextinfo.flow_id=reportfield.flow_id
join mart_poi.dp_mt_poi mtdp
   on mtdp.dt='20181115' and mtdp.dp_shop_id=reportfield.dp_id
 left join dpshop
   on dpshop.shop_id=mtdp.dp_
