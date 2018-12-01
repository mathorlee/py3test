
select reportfield.flow_id,
      reportfield.dp_id,
      mtdp.mt_id,
      reportfield.field_name,
      reportfield.last_value,
      reportfield.report_value,
      reportfield.audit_value,
      reportfield.audit_status,
      case reportfield.auditor_id
           when 1                 then '前置检测 AI'
           when 2                 then '锁定 AI'
           when 3                 then '侵权 AI'
           when 4                 then '报错源 AI'
           when 5                 then '地图 AI'
           when 6                 then '垃圾 AI'
           when 7                 then '保护 AI'
           when 8                 then '报错机审 AI'
           when 9                 then '诚信审核 AI'
           when 10                then '类目分发 AI'
           when 11                then '外卖机审 AI'
           when 12                then '分发 AI'
           when 13                then '父子关系 AI'
           when 13                then '主流程更新审核'
           else auditor_type
           end as auditor,
      reportfield.audit_comment,
      reportfield.ext_info,
      reportfield.create_time,
      reportfield.update_time,
      reportextinfo.client_type,
      dpshop.category0_name,
      dpshop.shop_name,
      dpshop.city_name
 from (
       select *
         from origindb_ss.dp_poibusiness__poi_reportfield
        where dt='20181115'
          and audit_status <> 'STATUS_LOCKED'
          and (auditor_type!='System' or auditor_id!=1 and auditor_id!=10)
          and create_time>='2018-11-09 00:00:00'
          and create_time<'2018-11-16 00:00:00'
      ) reportfield
inner join (
       select *
         from origindb_ss.dp_poibusiness__poi_reportextinfo
        where dt='20181115'
      ) reportextinfo
   on reportextinfo.flow_id=reportfield.flow_id
inner join mart_poi.dp_mt_poi mtdp
   on mtdp.dt='20181115'
  and mtdp.dp_shop_id=reportfield.dp_id
 left join (
       select *
         from mart_poimining.dpdm_dppoi_dp_shop
        where province_id <=31
          and hp_cal_dt = '2018-11-15'
      ) dpshop
   on dpshop.shop_id=mtdp.dp_
