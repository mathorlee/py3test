建表
CREATE EXTERNAL TABLE 库名.库名_输入表名(
  字段1 字段类型 comment 中文注释,
  字段2 字段类型  comment 中文注释)
PARTITIONED BY (。  
  分区键1 string,
  分区键2 string)
STORED AS 文件格式
LOCATION
  'hdfs://cootek/data/external/库名/库名_输入表名'

create table kv_table
(key String comment 'this is key', value String comment 'this is value')
comment 'key value table'
row format delimited fields terminated by 'val_' lines terminated by '\n';

load data local inpath '../hive/examples/files/kv1.txt' OVERWRITE INTO TABLE kv_table;

create table employee2
(employee_id INT comment '编号', employee_name String comment 'name of employee')
comment '员工table'
row format delimited fields terminated by '|' lines terminated by '\n';

load data local inpath '../hive/examples/files/employee.dat' OVERWRITE INTO TABLE employee;