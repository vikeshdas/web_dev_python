# web_dev_python

This is a web application  developed using the django framework.Data based is used mysql. I have explained all the API designed . <br>
Client<br>
    put(): create a new client.<br>
User<br>
    get() : get information of a user by user_id.<br>
    put(): create user .insert information of user in databases.<br>
    patch() :update user information by user_ id.<br>
    delete() : delete user from the database by user_id.<br>
Users<br>
    get(): fetch information of all users of a client by client_id.<br>
Role<br>
    create a new role.<br>
Log<br>
    put() : insert information of a log in database.<br>
    get() : get information from a log.<br>
Logs<br>
    get(): get all logs of a particular consignment by consignment_id.<br>
    Consignment<br>
    put(): create a consignment .insert information of a consignment of a client .it store client_id because each consignment belongs to a <br>client. It also stores user_id by which user this consignment is created.<br>
    get(): get information of a consignment by consignment_id.<br>
    Consignments<br>
    get() : get all consignments of a particular client by client_id.<br>

Feature of django used
I used the VIEW class of django which provides features to create  a view including request ,response handling and error handling.
<br>Sql database is used to store the data.<br>
<br>ORM feature is used to design the database schema.Defined a model Django models are Python classes that represent database tables. Each model class corresponds to a table, and the class attributes define the table's fields.<br>
<br>Tool<br>
<br>Docker: I have used two services: backend_service and mysql_service. backend_serivce containerize my web application and mysl_service containerize mysql database.<br>
<br>Gunicorn: gunicorn is a python web server which handle concurrent request.it creates process for each worker and each process handle concurrent request.<br>
<br>Database Design : https://drive.google.com/file/d/1C748XCKq61HWiMTg0Swm8zz6H1GpzmDU/view?usp=drive_link<br>
<br>Class Diagram : https://drive.google.com/file/d/1xEZBJOGFLpyMvgoNKuaxNEFExaMRx494/view?usp=drive_link<br>

