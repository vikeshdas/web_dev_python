# web_dev_python

This is a web application  developed using the django framework.Data based is used mysql. I have explained all the routes . <br>
**Client**<br>
    Our application operates on a subscription-based model, which means clients pay a periodic fee to access its features and services. One of the key features of our application is the ability for clients to create and manage multiple user accounts under a single subscription. This flexibility allows organizations and teams to efficiently use our application and tailor it to their specific needs.Below seciton explain about API to  create new client <br>
    **API:** Create new Client
    <br>
    **URL:** timba/client
    <br>
    **HTTP Method:** PUT
    <br>
    **Request Parameters:** {"name", "address", "contact", "email"}
    <br>

**User**<br>
    get() : get information of a user by user_id.<br>
    put(): create user .insert information of user in databases.<br>
    patch() :update user information by user_ id.<br>
    delete() : delete user from the database by user_id.<br>
**Users**<br>
    get(): fetch information of all users of a client by client_id.<br>
**Role**<br>
    create a new role.<br>
**Log**<br>
    put() : insert information of a log in database.<br>
    get() : get information from a log.<br>
**Logs**<br>
    get(): get all logs of a particular consignment by consignment_id.<br>
    Consignment<br>
    put(): create a consignment .insert information of a consignment of a client .it store client_id because each consignment belongs to a <br>client. It also stores user_id by which user this consignment is created.<br>
    get(): get information of a consignment by consignment_id.<br>
**Consignments**<br>
    get() : get all consignments of a particular client by client_id.<br>

**django**
I used the VIEW class of django which provides features to create  a view including request ,response handling and error handling.
<br>Sql database is used to store the data.<br>
<br>ORM feature is used to design the database schema.Defined a model Django models are Python classes that represent database tables. Each model class corresponds to a table, and the class attributes define the table's fields.<br>
<br>
**Tool**
<br>
<br>
**Docker:** I have used two services: backend_service and mysql_service. backend_serivce containerize my web application and mysl_service containerize mysql database.<br>
<br>
**Gunicorn:**
 I have used gunicorn in this project to handle multiple HTTP request at a same time.Gunicorn's worker process model is a way to handle multiple requests concurrently. Each worker process can handle multiple requests at a time.all of the worker processes are created before the application starts, and they remain running until the application is stopped.When a request comes in, Gunicorn assigns it to a worker process, The worker process then handles the request and returns the response. Once the request is complete, the worker process is ready to handle another request.Gunicorn can handle multiple requests concurrently because it uses a non-blocking I/O model. This means that the worker process does not wait for a request to complete before it starts handling the next request. Instead, the worker process will handle multiple requests at the same time, switching between them as needed.if a worker process gets down a new process will be created and all the old HTTP request will be sift to new process.<br>
<br>Database Design : https://drive.google.com/file/d/1C748XCKq61HWiMTg0Swm8zz6H1GpzmDU/view?usp=drive_link<br>
<br>Class Diagram : https://drive.google.com/file/d/1xEZBJOGFLpyMvgoNKuaxNEFExaMRx494/view?usp=drive_link<br>

