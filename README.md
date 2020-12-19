# What is job_api
I am building job_api as a quick and dirty job tracking web app so I can have access to the information about any jobs I've applied to at any time.
There are some great tools out there already like huntr, 
but I felt like this was a good application to learn some technologies 
I've been interested in but haven't had a chance to use (also, I don't have to pay except my time). Please keep in mind, this project is still very much a work in process.
<br>
The stack I'm using was recently coined as the ["FARM" stack](https://developer.mongodb.com/how-to/FARM-Stack-FastAPI-React-MongoDB) by [Aaron Basset](https://twitter.com/aaronbassett). 
As an Iowa native, I obviously approve of this naming convention.

## FastAPI
FastAPI was created by [tianglo](https://github.com/tiangolo), who also created the fantastic tool
 [click](https://github.com/tiangolo/click). Both tools are built off of Pydantic, which provides 
 data validation by using nothing more than standard Python type annotations. There is also this neat 
 ability to use Pydantic "BaseModel" to build complete, nested structures, which can then be validated 
 as a JSON body in the post. On top of all that, a super useful /doc page that allows you to test your API
 and the package is async compatible. 

 ## MongoDB
 I have used SQL databased (SQLite, SQLServer, Postgres) for everything up to this point. It has always been a cofort 
 thing, but the web speaks in JSON, and the "BSON" format aligns much better with this format. Beyond scalability (which 
 I don't expect to need), you also gain a lot flexibility. I am using a free, MongoAtlas deployment of MongoDB because my 
 current PC is not capable of running a local instance. 
 ## React
 Now that I have some Javascript under my belt, my 2nd pass through the React tutorial makes a lot more sense than it did 
 before. I can definately understand the benifit of building and reusing components, and I'm really excited to start building
 my first React front-end. 