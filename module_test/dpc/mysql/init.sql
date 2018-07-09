use `test` ;
create table `account`(
	`acctid` int(11) default null comment '账户id',
    `money` int(11) default null comment '余额'
)Engine =InnoDB default charset =utf8;