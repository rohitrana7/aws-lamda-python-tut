# AWS Lambda - "Run code without thinking about servers"
### Why Lambda?
- <b>Note</b> that the usage of the term Lambda here is not related to anonymous functions in Python, which are also known as lambda functions.
- In a traditional cloud usage model, you provision servers, deploy code to the server, and manage resource usage and scaling, along with other traditional server activities.
- While this is still the right way to handle a lot of scenarios, sometimes you just need to run a bit of code to handle some kind of event. For example, let’s say you have an application that allows users to upload a photo for a profile image. The application stores these images in Amazon S3. Now, say you want to resize the image to a max resolution. You could most definitely handle this task using the traditional model, but since this code runs based on an event (the file upload), Amazon S3 can fire an event and trigger the execution of code to handle the image resize.
- Where does this piece of code live, if we aren’t deploying a server? Well, that’s where AWS Lambda comes into play.
- AWS Lambda is the glue that binds many AWS services together, including S3, API Gateway, and DynamoDB. Alexa Skill Kits and Alexa Home also have events that can trigger Lambda functions!
- Lambda, you only pay for the compute time that you consume - there is no charge when your code is not running. With Lambda, you can run code for virtually any type of application or backend service, all with zero administration
- Amazon also handles all the resource scaling and load balancing! So AWS Lambda could be a good choice
- While creating a Lambda,  Lambda will automatically create a basic execution role so the Lambda function can access CloudWatch for logs.

  ### Creating Lambda
  - This view shows two tabs: Configuration and Monitoring (viewing activity and CloudWatch logs)
  - This diagram view is a handy visual representation of which triggers are utilizing this function, as well as the resources that the function has access to
  - triggers can be added by clicking on the trigger in the left column
  - Multiple triggers can be added for e.g. API Gateway, Alexa
  - a layer essentially allows you to add additional dependencies or frameworks for your function to use. A layer is a ZIP archive that contains libraries, a custom runtime, or other dependencies. With layers, you can use libraries in your function without needing to include them in your deployment package.
  - With layers, you can use libraries in your function without needing to include them in your deployment package.
  - 
