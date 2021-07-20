use mysql:5.7;
select host, user from user;
create user docker identified by '123456';
grant all on docker_mysql.* to docker@'%' identified by '123456' with grant option;
create user socialcontact identified by 'socialcontact123';
grant all on socialcontact.* to socialcontact@'%' identified by 'socialcontact123' with grant option;
flush privileges;
