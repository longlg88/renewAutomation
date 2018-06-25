create table smgr_inventory_cpu(
    date_long_agent number(20),
    date_long_server number(20),
    agent_id number(20),
    id number(20),
    vender varchar2(128),
    model varchar2(256),
    clock varchar2(128),
    total_socket number(10),
    core_per_socket number(10),
    total_cores number(10),
    architecture varchar2(64)
)
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2
STORAGE (
    MAXEXTENTS UNLIMITED
)
LOGGING
NOPARALLEL;

create index smgr_inevntory_cpu_index_date_long_server on smgr_inventory_cpu(date_long_server desc)
LOGGING
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2;
create index smgr_inventory_cpu_index_agent_id on smgr_inventory_cpu(agent_id)
LOGGING
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2;

create table smgr_inventory_memory(
    date_long_agent number(20),
    date_long_server number(20),
    agent_id number(20),
    id number(20),
    vender varchar2(128),
    model varchar2(256),
    capacity number(10)
)
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2
STORAGE (
    MAXEXTENTS UNLIMITED
)
LOGGING
NOPARALLEL;
  
create index smgr_inventory_memory_index_date_long_server on smgr_inventory_memory(date_long_server desc)
LOGGING
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2;
create index smgr_inventory_memory_index_agent_id on smgr_inventory_memory(agent_id)
LOGGING
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2;

create table smgr_inventory_disk(
    date_long_agent number(20),
    date_long_server number(20),
    agent_id number(20),
    id number(20),
    vender varchar2(128),
    model varchar2(256),
    capacity number(10)
)
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2
STORAGE (
    MAXEXTENTS UNLIMITED
)
LOGGING
NOPARALLEL;

create index smgr_inventory_disk_index_date_long_server on smgr_inventory_disk(date_long_server desc)
LOGGING
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2;
create index smgr_inventory_disk_index_agent_id on smgr_inventory_disk(agent_id)
LOGGING
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2;

create table smgr_inventory_nic(
    date_long_agent number(20),
    date_long_server number(20),
    agent_id number(20),
    id number(20),
    vender varchar2(128),
    model varchar2(256)
)
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2
STORAGE (
    MAXEXTENTS UNLIMITED
)
LOGGING
NOPARALLEL;

create index smgr_inventory_nic_date_long_server on smgr_inventory_nic(date_long_server desc)
LOGGING
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2;
create index smgr_inventory_nic_agent_id on smgr_inventory_nic(agent_id)
LOGGING
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2;

create table smgr_inventory_graphics(
    date_long_agent number(20),
    date_long_server number(20),
    agent_id number(20),
    id number(20),
    vender varchar2(128),
    model varchar2(256),
    architecture varchar2(64),
    memory_type varchar2(64),
    memory_size number(10)
)
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2
STORAGE (
    MAXEXTENTS UNLIMITED
)
LOGGING
NOPARALLEL;
 
create index smgr_inventory_graphics_date_long_server on smgr_inventory_graphics(date_long_server desc)
LOGGING
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2;
create index smgr_inventory_graphics_agent_id on smgr_inventory_graphics(agent_id)
LOGGING
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2;

create table smgr_inventory_monitor(
    date_long_agent number(20),
    date_long_server number(20),
    agent_id number(20),
    id number(20),
    vender varchar2(128),
    model varchar2(256)
)
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2
STORAGE (
    MAXEXTENTS UNLIMITED
)
LOGGING
NOPARALLEL;

create index smgr_inventory_monitor_date_long_server on smgr_inventory_monitor(date_long_server desc)
LOGGING
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2;
create index smgr_inventory_monitor_agent_id     on smgr_inventory_monitor(agent_id)
LOGGING
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2;

create table smgr_inventory_os(
    date_long_agent number(20),
    date_long_server number(20),
    agent_id number(20),
    vender varchar2(128),
    architecture varchar2(64),
    version varchar2(128)
)
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2
STORAGE (
    MAXEXTENTS UNLIMITED
)
LOGGING
NOPARALLEL;

create index smgr_inventory_os_date_long_server on smgr_inventory_os(date_long_server desc)
LOGGING
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2;
create index smgr_inevntory_os_agent_id on smgr_inventory_os(agent_id)
LOGGING
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2;

create table smgr_inventory_software(
    date_long_agent number(20),
    date_long_server number(20),
    agent_id number(20),
    copyright varchar2 (128),
    path varchar2(1024),
    version varchar2(256),
    software_size number(10),
    last_modi_date number(20),
    language varchar2(64)
)
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2
STORAGE (
    MAXEXTENTS UNLIMITED
)
LOGGING
NOPARALLEL;

create index smgr_inventory_software_date_long_server on smgr_inventory_software(date_long_server desc)
LOGGING
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2;
create index smgr_inventory_software_agent_id on smgr_inventory_software(agent_id)
LOGGING
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2;

create table smgr_measure(
    date_long_agent number(20),
    date_long_server number(20),
    agent_id number(20),
    instance_id number(20),
    type varchar2(32),
    id number(20),
    value number(20)
)
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2
STORAGE (
    MAXEXTENTS UNLIMITED
)
LOGGING
NOPARALLEL;

create index smgr_measure_index_date_long_server on smgr_measure(date_long_server desc)
LOGGING
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2;
create index smgr_measure_index_agent_id on smgr_measure(agent_id)
LOGGING
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2;
create index smgr_measure_index_instance_id on smgr_measure(instance_id)
LOGGING
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2;
create index smgr_measure_index_type on smgr_measure(type)
LOGGING
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2;
create index smgr_measure_index_id on smgr_measure(id)
LOGGING
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2;

create table smgr_group_info(
    group_id number(20) not null,
    group_alias varchar2(64),
    parent_group_id number(20),
    constraint pk_smgr_group_info_parent_group_id primary key(group_id),
    constraint fk_smgr_group_info_parent_group_id foreign key(parent_group_id) references smgr_group_info(group_id) on delete set null
)
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2
STORAGE (
    MAXEXTENTS UNLIMITED
)
LOGGING
NOPARALLEL;

insert into smgr_group_info values (1, 'ALL', '');  --default value

create table smgr_agent_info(
    agent_id        number(20)      not null,
    group_id        number(20),
    hostname        varchar2(64),
    ip              varchar2(128),
    description     varchar(256),
    security_level  number(1)       default 0,
    policy_name     varchar2(512)   default 'default',
    os_version      varchar2(128),
    node_type       varchar2(128),
    inventory       blob,
    --inventory     varchar2(10240),
    hb_interval     number(20),
    cpu_interval    number(20),
    mac_address     varchar2(50),
    constraint pk_smgr_agent_info primary key (agent_id),
    constraint fk_smgr_agent_info_group_id  foreign key(group_id) references smgr_group_info(group_id)
)
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2
STORAGE (
    MAXEXTENTS UNLIMITED
)
LOGGING
NOPARALLEL;
create table smgr_avg_measure(
    date_long_agent number(20),
    date_long_server number(20),
    agent_id number(20),
    instance_id number(20),
    cpu number(10),
    mem number(10),
    mem_mb number(20),
    disk number(10),
    disk_mb number(20),
    net_in number(20),
    net_out number(20),
    
    constraint fk_smgr_avg_measure  foreign key(agent_id) references smgr_agent_info(agent_id) on delete cascade
)
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2
STORAGE (
    MAXEXTENTS UNLIMITED
)
LOGGING
NOPARALLEL;


create index smgr_avg_measure_index_date_long_server on smgr_avg_measure(date_long_server desc)
LOGGING
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2;
create index  smgr_avg_measure_index_agent_id on smgr_avg_measure(agent_id)
LOGGING
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2;
create index  smgr_avg_measure_index_instance_id on smgr_avg_measure(instance_id)
LOGGING
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2;

create table smgr_request_info(
    request_id number(20) not null,
    request_name varchar2(128),
    category varchar2(32),
    target_node number(20),
    host_name varchar2(32),
    commander varchar2(32),
    commander_ip varchar2(128),
    date_long number(20) not null,
    target_ip varchar2(128),
    security_level varchar2(8),
    result varchar2(16),
    constraint pk_smgr_request_info_request_id primary key (request_id, date_long)
)
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2
STORAGE (
    MAXEXTENTS UNLIMITED
)
LOGGING
NOPARALLEL;


create index smgr_request_info_date_long on smgr_request_info(date_long desc)
LOGGING
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2;

create table smgr_instance_group_info(
    instance_id number(20) not null,
    group_id number(20) not null,
    tenant_id number(20),
    project_id number(20),
    instance_type number(10),
    constraint pk_container_group_info primary key (instance_id)
)
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2
STORAGE (
    MAXEXTENTS UNLIMITED
)
LOGGING
NOPARALLEL;


create table smgr_policy_list(
    policy_id       number(20)  not null,
    policy_name     varchar2(512)   not null,
    policy_category varchar2(20),
    policy_creator  varchar2(128),
    policy_create_time  date,
    policy_deploy_time  date,
    policy_update_time  date,
    policy_blob         blob,
    policy_result   varchar2(20),
    
    constraint pk_smgr_policy_list primary key (policy_id)
)
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2
STORAGE (
    MAXEXTENTS UNLIMITED
)
LOGGING
NOPARALLEL;

create table smgr_policy_agent_map_info (
    policy_id   number(20)  not null,
    agent_id    number(20) not null,
    policy_category varchar2(20) not null,
    
    constraint unique_smgr_policy_agent_map_info unique (policy_id, agent_id),
    constraint fk_smgr_policy_agent_map_info1  foreign key(policy_id) references smgr_policy_list(policy_id) on delete cascade,
    constraint fk_smgr_policy_agent_map_info2  foreign key(agent_id) references smgr_agent_info(agent_id) on delete cascade
)
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2
STORAGE (
    MAXEXTENTS UNLIMITED
)
LOGGING
NOPARALLEL;

create sequence smgr_policy_list_seq
start with 1
increment by 1
maxvalue 9999999999;
create sequence smgr_agent_group_seq
start with 1
increment by 1
maxvalue 9999999999;

create table smgr_rule_meta(
    rule_id         number(20) not null,
    time_window     number(10) not null,
    min_count       number(10) not null,
    cooldown        number(10),
    event_message   varchar2(1024),
    is_activate     varchar2(1),
    event_type      varchar2(128),
    oid             varchar2(128),
    policy_id       number(20),
    policy_name     varchar2(512),
    event_level     number(1),
    constraint pk_rule_meta primary key (rule_id)
    
)
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2
STORAGE (
    MAXEXTENTS UNLIMITED
)
LOGGING
NOPARALLEL;

create table smgr_rule_detail(
    rule_id number(20) not null,
    key varchar2(128) not null,
    value varchar2(128)  not null,
    constraint  fk_rule_meta_detail foreign key (rule_id) references smgr_rule_meta(rule_id) on delete cascade
)
TABLESPACE "SYSMGR"
PCTFREE 10
INITRANS 2
STORAGE (
    MAXEXTENTS UNLIMITED
)
LOGGING
NOPARALLEL; 

commit;
exit
