create table employee (id number(10),name varchar(20),age number(3),city varchar(20),gender varchar(12),contact number(10), primary key(id));

create table money (id number(10),description varchar(140),dte date,amount number(20), emp_id number(10) references employee(id) on delete cascade, primary key(id));

create table site (id number(10),address varchar(20),work_type varchar(20),primary key(id));

create table attendance (id number(10),dte date,description varchar(140),remark varchar(20), emp_id number(10) references employee(id) on delete cascade,  site_id number(10) references site(id) on delete cascade,primary key(id));

create table emp_site (emp_id number(10) references employee(id) on delete cascade,  site_id number(10) references site(id) on delete cascade);

create table supervisor (id number(10),name varchar(20),contact number(10), site_id number(10) references site(id) on delete cascade);

create user ritika identified by ritika;
grant all privilege to ritika;

create table ritika.emphm (id number(10),name varchar(20),age number(3),city varchar(20),gender varchar(12),contact number(10), primary key(id));

create table sandeep.empha (id number(10),name varchar(20),age number(3),city varchar(20),gender varchar(12),contact number(10), primary key(id));

commit;

create or replace trigger emp_rand
after insert on employee
for each row
begin
IF(:NEW.city='mumbai') THEN
INSERT INTO ritika.emphm
VALUES(:NEW.ID,
:NEW.NAME,
:NEW.AGE,
:NEW.CITY,
:NEW.GENDER,
:NEW.CONTACT);
ELSE
INSERT INTO sandeep.empha
VALUES(:NEW.ID,
:NEW.NAME,
:NEW.AGE,
:NEW.CITY,
:NEW.GENDER,
:NEW.CONTACT);
END IF;
end;
/

insert into employee values(1,'binoy',20,'mumbai','male',9922129496)





    select * from employee;
ALTER TABLE employee
  ADD password varchar(20);
  
  desc employee;
  delete from employee where id=1;
  
  select * from employee;
  
  desc supervisor;
  
  ALTER TABLE supervisor 
  ADD password varchar(20);
  
  select * from supervisor;
  
  desc employee;
  
  truncate table ritika.emphm;
    truncate table sandeep.empha;
  insert into employee values(1,'binoy',20,'mumbai','male',9922129395,'binoy');
  delete from employee where id=3;
    delete from employee where id=4;
   delete from employee where id=5;
    delete from employee where id=2
   

    
  insert into employee values(2,'sandeep',20,'chennai','male',9922129395,'sandeep');
  insert into employee values(3,'ritika',20,'chembur','male',9922129395,'ritika');
  insert into employee values(4,'sandep',20,'chennai','male',9922129395,'sandep');
  insert into employee values(5,'ritka',20,'chembur','male',9922129395,'ritka');
  
  select * from employee;
  select * from sandeep.empha;
  select * from ritika.emphm;
  
  
  commit;
select * from employee;
select * from ritika.emphm;
select * from sandeep.empha;


