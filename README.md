# Doctor Management System
### Team Members
 1) Kayala Raana Pramodh
 2) Koneti Anuhya
 3) Kothuru Sharvani
 4) Maddaka Yashwanth
 5) Nelavalli Sri Nikhitha
 
  ### Description 
The Doctor management system allows patients to enquire about availability of doctors based on their schedule ,book and cancel appointments. The goal of this case study is to design and develop a database that stores information about various doctors.. Patients may look for doctors by entering the details. If there are any doctors available, they will be displayed. Following that, patients maygo to cancellation page and then cancel the appointment. 

### Templates
 This folder contains all the html files along with their stylings. In total, there are 37 html files which comprise  of login, register, search doctors, cancel appointments , book appointments,blog posts,contactus,aboutus, add doctors,release slots and favourite doctors pages. 
 
### App.py 
This is the back end for the entire project. This is made using Flask. ER Diagram Contains the Entity Relationship diagram of our database. DMS.mwb Contains the schemas of the database.DMS.sql is the SQL code for the project. The database consists of 6 tables.

### UML
This folder also contains activity diagrams which shows the activities involved in a process of booking appointments,cancelling appointments,adding doctors and releasing slots

### How to use the website 
Create a database with the above sql code, then download all the html files from the Template folder and the app.py file. Then run the python file on the terminal. When you run the program, you will be directed to the homepage, where you may login, register and opt for the need. To register, click the Register button, where you will be asked to provide the required details. After successfully registering, you will be directed to the login page, where you must enter your registered email and password. Then, you may search for doctors. You will search doctors based on the details you input and then book appointment. When you book an appointment, you will be requested to provide the patient information. After successfully booking, an appointment will be generated, which may be downloaded by choosing the "Generate PDF" option.Now,to cancel appointment go to the appointments page and select “cancel appointment” If the Cancellation is successful, the message "Cancelled Successfully" will display.In case of receptionist in order to add doctors to their respective hospitals they have to provide details of doctors. While releasing slots for respective doctors, receptionists provides the details of the number of slots registered on that day.







