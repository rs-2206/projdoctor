create database DMS;
use DMS;
create table patient(
Email varchar(100),
Firstname varchar(100),
Lastname varchar(100),
Password varchar(100),
cpassword varchar(100),
DOB varchar(50),
Gender varchar(100),
Bloodgroup varchar(100),
mobilenumber varchar(100),
Address varchar(50),
Address1 varchar(100),
State varchar(100),
Pincode bigint,
City varchar(100),
primary key(Email)
);
select * from patient;
create table Receptionist(
Email varchar(100),
HospitalName varchar(100),
Password varchar(100),
primary key(Email)
);
select * from Receptionist;
create table Doctor(
Email varchar(100),
Hid varchar(100),
Name varchar(100),
Specialisation varchar(100),
RegistrationNo bigint,
Experience bigint,
TotalRating int,
Languageknown varchar(100),
foreign key(Hid)references Receptionist(Email),
primary key(Email)
);
select * from Doctor;
create table slots(
Hid varchar(100),
Did varchar(100),
Date date,
AvailableSlots int,
foreign key(Hid)references Receptionist(Email),
foreign key(Did)references Doctor(Email),
primary key(Did,Hid,Date)
);
select* from slots;
create table Appointments(
id varchar(100),
Hid varchar(100),
Did varchar(100),
Reason varchar(1000),
Date date,
Status varchar(100),
foreign key(id)references Patient(Email),
foreign key(Hid)references Receptionist(Email),
foreign key(Did)references Doctor(Email),
primary key(id,Hid,Did,Date)
);
select * from Appointments;
create table FavouriteDoctors(
id varchar(100),
Did varchar(100),
foreign key(id)references Patient(Email),
foreign key(Did)references Doctor(Email),
primary key(id,Did)
);
select * from FavouriteDoctors;
create  table insurance(
Pid varchar(100),
InsuranceNumber int,
HolderName varchar(100),
insuranceExpiryDate date,
Benefitscontact bigint,
primary key(InsuranceNumber),
foreign key(Pid) references Patient(Email)
);
select * from insurance;
INSERT INTO 
Receptionist(Email, HospitalName, Password)
 VALUES
 ('sunshine@gmail.com', 'Sunshine Hospitals','sun@123'),
 ('apollo@gmail.com', 'Apollo Hospitals', 'apollo@123'),
 ('niims@gmail.com', 'Niims Hospitals', 'niims@123'),
 ('kims@gmail.com','Kims Hospitals', 'kims@123'),
 ('yashoda@gmail.com','Yashoda Hospitals', 'yashoda@123'),
 ('care@gmail.com', 'Care Hospitals', 'care@123'),
 ('gandhi@gmail.com','Gandhi Hospitals','gandhi@123'),
 ('rainbow@gmail.com','Rainbow Hospitals', 'rainbow@123');
 
 INSERT INTO 
 Doctor(Email, Hid, Name, Specialisation, RegistrationNO, Experience, TotalRating, Languageknown)
 VALUES
 ('ravi@gmail.com' ,'apollo@gmail.com' , 'Ravi kumar' , 'GeneralMedicine' ,156784,5, 0, 'Telugu-Hindi-English'),
('srinu@gmail.com' ,'niims@gmail.com' , 'Srinivas rao' , 'GeneralMedicine' ,'234678','6', '0', ' Telugu-Hindi-English'),
('venu@gmail.com' ,'kims@gmail.com' , 'Venu' , 'CovidConsultation' ,'473893', '7', '0',' Telugu-Hindi-English') ,
('ramu@gmail.com' ,'yashoda@gmail.com' , 'Ramesh' , 'CovidConsultation' , '344577','5', '0','  Telugu-Hindi-English') ,
('selva@gmail.com' ,'sunshine@gmail.com' , 'Selva' , 'Dermatology' , '749273','6', '0','Telugu-Tamil-English') ,
('kar@gmail.com' ,'rainbow@gmail.com' , 'Karthi' , 'Dermatology' ,'384969','7', '0', ' Telugu-Hindi-English') ,
('arv@gmail.com' ,'care@gmail.com' , 'Arvind singh' , 'Gastroenterology ','234778' ,'5', '0', 'Hindi-English'),
('raju@gmail.com' ,'gandhi@gmail.com' , 'Rajendra' , 'Gastroenterology ' , '345698','6', '0','Telugu-English-Hindi') ,
('prashanth@gmail.com' ,'apollo@gmail.com' , 'Prashanth kumar' , 'Nutrition','633834' ,'7', '0', 'Telugu-Hindi-English') ,
('pav@gmail.com' ,'niims@gmail.com' , 'Pavan reddy' , 'Nutrition' ,'573643','5', '0', ' Telugu-Hindi-English') ,
('sri@gmail.com' ,'kims@gmail.com' , 'Suchetha Sri' , 'Psychiatry' ,'735635','6', '0', 'Hindi-English') ,
('rakesh@gmail.com' ,'yashoda@gmail.com' , 'Rakesh sharma' , 'Psychiatry' ,'745636','7', '0', 'Telugu-Hindi-English') ,
('shru@gmail.com' ,'sunshine@gmail.com' , 'Shruthi' , 'Gynecology' ,'826381','5', '0', 'Telugu-Hindi-English') ,
('sej6@gmail.com' ,'rainbow@gmail.com' , 'Sejal' , 'Gynecology' ,'937353','6', '0', 'Malayalam-Hindi-English') ,
('bala@gmail.com' ,'care@gmail.com' , 'Bala Kumar' , 'ConsultantPhysician' ,'537357','7', '0', 'Telugu-Hindi-English') ,
('ram@gmail.com' ,'gandhi@gmail.com' , 'Ramesh rao' , 'ConsultantPhysician' ,'439373', '5', '0','Telugu-Hindi-English') ,
('neha@gmail.com' ,'apollo@gmail.com' , 'Neha' , 'Pediatrics' ,'986543','6', '0', 'Hindi-English') ,
('ak@gmail.com' ,'niims@gmail.com' , 'Aarya' , 'Pediatrics' ,'754245','7', '0', 'Tamil-English-Hindi') ,
('rk3@gmail.com' ,'kims@gmail.com' , 'Ram' , 'ENT' ,'865336','5', '0', ' Telugu-Hindi-English') ,
('shyam@gmail.com' ,'yashoda@gmail.com' , 'Shyam Kumar' , 'ENT' ,'237865','6', '0', 'Hindi-English') ,
('ajju@gmail.com' ,'sunshine@gmail.com' , 'Arjun' , 'Orthopedics' ,'986543','7', '0', 'Hindi-English') ,
('kuttan@gmail.com' ,'rainbow@gmail.com' , 'Kuttan' , 'Orthopedics' ,'679436','5', '0', 'Malayalam-English') ,
('srija@gmail.com' ,'care@gmail.com' , 'Srija reddy' , 'Cardiology' ,'347786','6', '0', 'Telugu-Hindi-English') ,
('akshay@gmail.com' ,'gandhi@gmail.com' , 'Akshay kumar' , 'Cardiology' ,'986532','7', '0', 'Telugu-Hindi-English') ,
('sushma@gmail.com' ,'apollo@gmail.com','Sushma chowdhary','Diabetology','134678','5', '0','Telugu-Hindi-English') ,
('abhi@gmail.com' ,'niims@gmail.com','Abhiram','Diabetology','976446','6', '0','Telugu-Hindi-English') ,
('rishi@gmail.com' ,'kims@gmail.com','Rishitha','Neurology','467922','7', '0','Telugu-Hindi-English') ,
('sanju@gmail.com' ,'yashoda@gmail.com','Sanjana','Neurology','797535','5', '0','Telugu-Hindi-English') ,
('deepthi@gmail.com' ,'sunshine@gmail.com','Thanmai deepthi','Pulmonology','536653','6', '0','Telugu-Hindi-English') ,
('richa@gmail.com' ,'rainbow@gmail.com','Richa reddy','Pulmonology','643538','7', '0','Telugu-Hindi-English') ,
('vijju@gmail.com' ,'care@gmail.com','Vijay','Nephrology','537383','5', '0','Telugu-Hindi-English') ,
('kuppi@gmail.com' ,'gandhi@gmail.com','Sai Krupakar','Nephrology','635363','6', '0','Telugu-Hindi-English') ,
('krishna@gmail.com' ,'apollo@gmail.com','Ravi Krishna','Endocrinology','863563','7', '0','Telugu-Hindi-English') ,
('jay@gmail.com' ,'niims@gmail.com','Jayanth','Endocrinology','636709','5', '0','Telugu-Hindi-English') ,
('unni@gmail.com' ,'kims@gmail.com','Unnathi Sharma','Radiology','903763','6', '0','Telugu-Hindi-English') ,
('mala@gmail.com' ,'yashoda@gmail.com','Malavika Reddy','Radiology','836365','7', '0','Telugu-Hindi-English') ,
('teju@gmail.com' ,'sunshine@gmail.com','Tejaswi','Psychology','774743','5', '0','Telugu-Hindi-English') ,
('shiva@gmail.com' ,'rainbow@gmail.com','Shiva Charan','Psychology','865424','6', '0','Telugu-Hindi-English') ,
('shafi@gmail.com' ,'care@gmail.com','Shafeeq','Urology','753249','7', '0','Telugu-Hindi-English') ,
('varshith@gmail.com' ,'gandhi@gmail.com','Sai varshith','Urology','643467','5', '0','Telugu-Hindi-English');

INSERT INTO 
 slots(Hid, Did, Date, AvailableSlots)
 VALUES
 ('apollo@gmail.com','ravi@gmail.com', "2022:10:14", 15);
 
 INSERT INTO 
 slots(Hid, Did, Date, AvailableSlots)
 VALUES
 ('niims@gmail.com','srinu@gmail.com',"2022:05:14",10),
 ('kims@gmail.com','venu@gmail.com',"2022:04:14",12),
 ('yashoda@gmail.com','ramu@gmail.com',"2022:05:03",8),
 ('sunshine@gmail.com','selva@gmail.com',"2022:04:14",6),
 ('rainbow@gmail.com','kar@gmail.com',"2022:05:01",11),
 ('care@gmail.com','arv@gmail.com',"2022:04:14",14),
 ('gandhi@gmail.com','raju@gmail.com',"2022:05:07",12),
 ('apollo@gmail.com','prashanth@gmail.com',"2022:04:14",16),
 ('niims@gmail.com','pav@gmail.com',"2022:05:06",18),
 ('kims@gmail.com','sri@gmail.com',"2022:04:14",15),
 ('yashoda@gmail.com','rakesh@gmail.com',"2022:05:02",14),
 ('sunshine@gmail.com','shru@gmail.com',"2022:04:12",13),
 ('rainbow@gmail.com','sej6@gmail.com',"2022:05:04",16),
 ('care@gmail.com','bala@gmail.com',"2022:04:16",17);
INSERT INTO 
slots(Hid, Did, Date, AvailableSlots)
VALUES
('gandhi@gmail.com','ram@gmail.com',"2022:05:10",19),
('apollo@gmail.com','neha@gmail.com',"2022:04:15",18),
('niims@gmail.com','ak@gmail.com',"2022:05:08",6),
('kims@gmail.com','rk3@gmail.com',"2022:04:15",11),
('yashoda@gmail.com','shyam@gmail.com',"2022:05:07",14),
('sunshine@gmail.com','ajju@gmail.com',"2022:04:19",15),
('rainbow@gmail.com','kuttan@gmail.com',"2022:05:04",17),
('care@gmail.com','srija@gmail.com',"2022:04:14",18);
 INSERT INTO 
 slots(Hid, Did, Date, AvailableSlots)
 VALUES
('gandhi@gmail.com','akshay@gmail.com',"2022:05:05",19),
('apollo@gmail.com','sushma@gmail.com',"2022:04:16",9),
('niims@gmail.com','abhi@gmail.com',"2022:05:08",13),
('kims@gmail.com','rishi@gmail.com',"2022:04:17",15),
('yashoda@gmail.com','sanju@gmail.com',"2022:05:09",12),
('sunshine@gmail.com','deepthi@gmail.com',"2022:04:12",11),
('rainbow@gmail.com','richa@gmail.com',"2022:05:10",8);
 INSERT INTO 
 slots(Hid, Did, Date, AvailableSlots)
 VALUES
('care@gmail.com','vijju@gmail.com',"2022:04:17",7),
('gandhi@gmail.com','kuppi@gmail.com',"2022:05:06",10),
('apollo@gmail.com','krishna@gmail.com',"2022:04:15",13),
('niims@gmail.com','jay@gmail.com',"2022:05:04",12),
('kims@gmail.com','unni@gmail.com',"2022:04:18",15),
('yashoda@gmail.com','mala@gmail.com',"2022:05:05",17);
 INSERT INTO 
 slots(Hid, Did, Date, AvailableSlots)
 VALUES
('sunshine@gmail.com','teju@gmail.com',"2022:04:13",18),
('rainbow@gmail.com','shiva@gmail.com',"2022:05:03",19),
('care@gmail.com','shafi@gmail.com',"2022:04:15",14),
('gandhi@gmail.com','varshith@gmail.com',"2022:05:03",12);
 INSERT INTO 
 slots(Hid, Did, Date, AvailableSlots)
 VALUES
 ('yashoda@gmail.com','sanju@gmail.com',"2022:05:10",13);
 
  INSERT INTO 
 slots(Hid, Did, Date, AvailableSlots)
 VALUES
 ('sunshine@gmail.com','deepthi@gmail.com',"2022:04:13",11);
 
 INSERT INTO 
 slots(Hid, Did, Date, AvailableSlots)
 VALUES
 ('apollo@gmail.com','ravi@gmail.com', "2022:10:15", 15);
 
 DELETE FROM Appointments WHERE id = 'xxx@gmail.com' and Hid = 'apollo@gmail.com' and Did = 'ravi@gmail.com' and Date = "2022:10:15";