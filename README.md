# web_dev_python

This is a web application developed using the Django framework. I have used the MySQL database. I have explained all the routes. To handle requests concurrently I have used the Gunicorn server. <br><br>

**Client**<br>
Our application operates on a subscription-based model, which means clients pay a periodic fee to access its features and services. One of the key features of our application is the ability for clients to create and manage multiple user accounts under a single subscription. This flexibility allows organizations and teams to efficiently use our application. The below section explains all Routes for the user
<br>
**Create new Client**
<br>
**URL:** timba/client
<br>
**HTTP Method:** put()
<br>
**Request Parameters:** {"name", "address", "contact", "email"}
<br>
**Response :** {"Client created Successfully"}
<br><br>

    
**User**<br>
The below route help our client to manage their user, like seeing a list of user, adding new user, updating existing user, and deleting a user.<br>
**Description:** Get information of a user by user_id.
<br>
**URL:** timba/user
<br>
**HTTP Method:** get()
<br>
**Request Parameters:** {user_id}
<br>
**Response :** {"Client created Successfully"}
<br>
put(): create user. insert information of user in databases.<br>
patch() :update user information by user_ id.<br>
delete() : delete user from the database by user_id.<br><br>

    
**Users**<br>Bellow rote help our client to fetch information of their all users<br>
**URL:** timbba/usres<br>
**HTTP Method:** get()<br>
**Request Parameters:** {clilent_id}<br>
**Response :** list of user information in JSON form.<br>

<br><br>
    
**Role: Each user will have one or more then  role in our application. For example a user can access an application using mobile only, another user can access using the web only and someone will have access to both. Some features in the mobile app are not available in the web app and vice versa.**  <br>   
**Bellow route helps our client to Create a new role.**<br>
**URL:** timbba/role<br>
**HTTP Method:** put()<br>
**Request Parameters:** {rolename}<br>
**Response:** Simple message in jsonform if successfully created or Error.<br><br>

**Log: Each consignment will have a list of logs. We can fetch or put one log at a time in the database of a particular consignment.**<br>
**Bellow route helps our client to insert and fetch the log of a consignment**<br>
**URL:** timbba/log<br>
**HTTP Method:**<br>
put(): insert information of a log in database<br>
Request Parameters: {length,breadth,height,consignment_id,client_id}<br>
get() : get information of a log.<br>
Request Parameters: {consignment_id,client_id}<br>
<br><br>
    
**Logs:  To fetch information of all logs of consignment**<br>
**URL:** timbba/logs<br>
**HTTP Methods:**<br>
    get(): get all logs of a particular consignment by consignment_id.<br>
    Request Parameters: {consignment_id,client_id}<br>
    Response : information of a consignment with all logs information in json form<br><br>
    
**Consignment: Insert information of new consignment, fetch information of existing consignment **<br>
**URL:** timbba/consignment<br>
**HTTP Methods:**<br>
put(): create a consignment .insert information of a consignment of a client .it store client_id because each consignment belongs to a client. It also stores user_id by which this consignment is created.<br>
Request Parameters: {user_id,client_id,name,type}<br>
Response : Json response with text message either success or error<br><br>
get(): get information of a consignment by consignment_id.
Request Parameters: {user_id,client_id,name,type}<br>
Response :   "consignment": {"id": 1,"name": "cons11","type": "0","client_id": 2,"created_by": 2,"updated_by": 2,"created_at": "2023-10-07T12:15:14.713Z","updated_at": "2023-10-07T12:15:14.714Z"}
<br>
<br><br><br>
    
**Consignments  **<br>
**URL:** timbba/consignment<br>
**HTTP Methods:**<br>
get() :get all consignments of a particular client by client_id <br>
Request Parameters: {client_id}<br>
Response :   "consignments": [{"id": 1,"name": "cons11","type": "0","client_id": 2,"created_by": 2,"updated_by": 2,"created_at": "2023-10-07T12:15:14.713Z","updated_at": "2023-10-07T12:15:14.714Z"}]
<br><br>

**django**
I used the VIEW class of django which provides features to create a view including request ,response handling and error handling.
<br>Sql database is used to store the data.<br>
<br>ORM feature is used to design the database schema. Defined a model Django models are Python classes that represent database tables. Each model class corresponds to a table, and the class attributes define the table's fields.<br>
<br>
**Tool**
<br>
<br>
**Docker:** I have used two services: backend_service and mysql_service. backend_serivce containerizes my web application and mysl_service containerizes MySQL database.<br>
<br>
**Gunicorn:**
 I have used Gunicorn in this project to handle multiple HTTP request at a same time.Gunicorn's worker process model is a way to handle multiple requests concurrently. Each worker process can handle multiple requests at a time.all of the worker processes are created before the application starts, and they remain running until the application is stopped.When a request comes in, Gunicorn assigns it to a worker process, The worker process then handles the request and returns the response. Once the request is complete, the worker process is ready to handle another request.Gunicorn can handle multiple requests concurrently because it uses a non-blocking I/O model. This means that the worker process does not wait for a request to complete before it starts handling the next request. Instead, the worker process will handle multiple requests at the same time, switching between them as needed.if a worker process gets down a new process will be created and all the old HTTP request will be sift to new process.<br>
<br>Database Design : https://drive.google.com/file/d/1C748XCKq61HWiMTg0Swm8zz6H1GpzmDU/view?usp=drive_link<br>
<br>Class Diagram : https://drive.google.com/file/d/1xEZBJOGFLpyMvgoNKuaxNEFExaMRx494/view?usp=drive_link<br>

