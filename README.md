# Sr.SoftwareEngineerInterviewPrep

# 
<details>
  <summary>common interview system design questions:</summary>
  
  


```
What is the architecture of the system?
The architecture of the system is typically designed to balance performance, scalability, and security requirements. It may include multiple layers of caching, load balancing, and failover mechanisms to ensure that requests are distributed evenly across multiple servers and that data is stored and retrieved efficiently.

How are requests handled?
Requests are typically handled by the system's request handler, which listens for incoming requests and dispatches them to the appropriate server or service. The request handler may also handle load balancing and failover mechanisms to ensure that requests are distributed evenly across multiple servers.

How are requests distributed across multiple servers?
Requests are typically distributed across multiple servers using a load balancing mechanism, which distributes incoming requests evenly across all available servers. The load balancer may also monitor the health of each server and route requests to healthy servers only.

How are requests stored and retrieved?
Requests are typically stored and retrieved from a database or cache using a key-value store or a cache provider. The key-value store or cache provider may use a distributed cache to store and retrieve data efficiently across multiple servers.

How is data stored and retrieved?
Data is typically stored and retrieved from a database or cache using a key-value store or a cache provider. The key-value store or cache provider may use a distributed cache to store and retrieve data efficiently across multiple servers.

How is security implemented?
Security is typically implemented using a combination of authentication, authorization, and encryption mechanisms. The system may use SSL/TLS to encrypt data in transit, and may also use encryption at rest to protect sensitive data. The system may also use rate limiting and other security mechanisms to prevent attacks and ensure that the system is secure.

How is load balancing implemented?
Load balancing is typically implemented using a load balancer or a reverse proxy. The load balancer or reverse proxy may distribute incoming requests evenly across all available servers, and may also monitor the health of each server and route requests to healthy servers only.

How is fault tolerance implemented?
Fault tolerance is typically implemented using redundancy and failover mechanisms. The system may use multiple servers to ensure that requests are distributed evenly across all available servers, and may also use failover mechanisms to switch to a backup server if a server fails.

How is scalability implemented?
Scalability is typically implemented using a combination of horizontal and vertical scaling techniques. The system may use a scaling strategy that adds or removes servers based on demand, or it may use a scaling strategy that adjusts the resources allocated to each server based on demand.

How is performance optimized?
Performance optimization is typically implemented using a combination of caching, compression, and other techniques. The system may use caching to store frequently accessed data in memory, and may also use compression to reduce the size of data that is transmitted over the network.

How is monitoring and logging implemented?
Monitoring and logging are typically implemented using a monitoring system and logging framework. The monitoring system may monitor the health of each server, the performance of each server, and the overall performance of the system, and may generate alerts or notifications if any of these metrics exceed a certain threshold. The logging framework may log all requests and responses, as well as other relevant information, to help diagnose and troubleshoot issues.

How is documentation and support provided?
Documentation and support are typically provided through a user manual, a help desk, and a knowledge base. The user manual may provide detailed instructions on how to use the system, including how to navigate the user interface, how to perform common tasks, and how to report issues. The help desk may provide support for users who encounter issues with the system, and may also provide training on how to use the system effectively. The knowledge base may provide detailed information on how the system is designed, how it works, and how to troubleshoot issues.

How is the system designed for scalability and performance?
The system is designed for scalability and performance by using a combination of caching, load balancing, and other techniques. The system may use a caching provider to store frequently accessed data in memory, and may also use a load balancer to distribute incoming requests evenly across all available servers. The system may also use a scaling strategy that adds or removes servers based on demand, or it may use a scaling strategy that adjusts the resources allocated to each server based on demand.

How is the system designed for security and reliability?
The system is designed for security and reliability by using a combination of authentication, authorization, and encryption mechanisms. The system may use SSL/TLS to encrypt data in transit, and may also use encryption at rest to protect sensitive data. The system may also use rate limiting and other security mechanisms to prevent attacks and ensure that the system is secure. The system may also use redundancy and failover mechanisms to ensure that the system is resilient to failures.

How is the system designed for maintainability and evolution?
The system is designed for maintainability and evolution by using a modular architecture that allows for easy customization and extension. The system may use a microservices architecture to break the system into smaller, independent services that can be developed, tested, and deployed independently. The system may also use a version control system to track changes to the code and documentation, and may use automated testing


Frugal Streaming: 
Frugal Streaming is a technique used to approximate the results of a query over a data stream, while using minimal memory. It is often used in scenarios where the data stream is too large to fit into memory, but approximate results are acceptable. One example of Frugal Streaming is the Count-Min Sketch algorithm, which uses a fixed-size array of counters to estimate the frequency of items in a data stream. Each item is hashed to a set of counters, and the minimum count in that set is incremented. The estimate for the frequency of an item is the minimum count across all sets. 
 
Geohash / S2 Geometry: 
Geohash and S2 Geometry are two related techniques used to represent and index geographic locations on a two-dimensional surface, such as a map. Geohash is a hierarchical spatial data structure that uses a string of characters to represent a location. Each character in the string represents a subdivision of the space, with longer strings representing smaller subdivisions. S2 Geometry is a library for manipulating geometric shapes on the surface of a sphere, such as the Earth. It uses a hierarchical grid system to partition the surface of the sphere into cells of varying sizes. Both Geohash and S2 Geometry are useful for indexing and querying large datasets of geographic locations. 
 
Leaky bucket / Token bucket: 
Leaky bucket and Token bucket are two algorithms used for traffic shaping and rate limiting in computer networks. The Leaky bucket algorithm regulates the rate at which data is transmitted by imposing a constant rate of data removal from a buffer. Any data that arrives in excess of the rate is discarded. The Token bucket algorithm regulates the rate at which data is transmitted by issuing tokens at a fixed rate. Each token allows a fixed amount of data to be transmitted. If there are no tokens available, data transmission is blocked. 
 
Loosy Counting: 
Loosy Counting is a technique used to estimate the frequency of items in a data stream, while using minimal memory. It is similar to Frugal Streaming, but allows for a small amount of error in the estimates. One example of Loosy Counting is the HyperLogLog algorithm, which uses a fixed-size array of registers to estimate the number of distinct items in a data stream. Each item is hashed to a register, and the maximum number of leading zeros in the binary representation of the register values is used to estimate the number of distinct items. 
 
Operational transformation: 
Operational Transformation is a technique used to synchronize the state of a shared document or data structure across multiple clients in a distributed system. It is often used in collaborative editing applications, such as Google Docs. Operational Transformation works by transforming the operations performed by each client into a common form that can be applied in any order without affecting the final state of the document. This allows each client to see the changes made by other clients in real-time, while ensuring that the final state of the document is consistent across all clients. 
 
Quadtree / Rtree: 
Quadtree and Rtree are two related spatial data structures used for indexing and querying two-dimensional data, such as points, lines, and polygons. Quadtree is a hierarchical data structure that recursively subdivides a two-dimensional space into four quadrants, with each quadrant represented by a node in the tree. Rtree is a similar data structure that uses a hierarchical tree of rectangles to represent the data. Both Quadtree and Rtree are useful for spatial indexing and querying in applications such as geographic information systems and computer graphics. 
 
Ray casting: 
Ray casting is a technique used to render three-dimensional scenes in computer graphics. It works by tracing rays from the viewer's eye through each pixel in the image plane and into the scene. The rays are tested for intersections with objects in the scene, and the color of the pixel is determined based on the properties of the closest object. Ray casting is a computationally intensive process, but can produce high-quality images with realistic lighting and shading effects. 
 
Reverse index: 
Reverse index, also known as an inverted index, is a data structure used to index and search text documents. It works by creating an index of all the words in the documents, along with a list of the documents that contain each word. This allows for efficient searching of documents based on the words they contain. Reverse index is used in many applications, such as search engines and document management systems. 
 
Rsync algorithm: 
Rsync is a file synchronization algorithm used to efficiently transfer files between two systems over a network. It works by comparing the contents of the files on both systems and transferring only the differences between them. This can greatly reduce the amount of data that needs to be transferred, especially for large files or files that have only small changes. Rsync is commonly used for backups and for transferring large files over the internet. 
 
Trie algorithm: 
A Trie, also known as a prefix tree, is a tree-like data structure used to store and retrieve strings efficiently. Each node in the tree represents a prefix of one or more strings, and the edges represent the characters that can follow the prefix. Tries are useful for applications such as autocomplete and spell checking, where fast string lookups are required.


```
</details>


# 


#  

<details>
  <summary> java interview questions:</summary>
  
  

```
Number ways to create object in java?

Using new keyword
Using new instance
Using clone() method
Using deserialization
Using newInstance() method of Constructor class 

Using new keyword: 
 
The  new  keyword is used to create a new instance of a class. It allocates memory for the object and initializes its fields with their default values. Here's an example:
MyClass obj = new MyClass();
This creates a new instance of the  MyClass  class and assigns it to the  obj  variable. 
 
Using new instance: 
 
The  newInstance()  method of the  Class  class is used to create a new instance of a class at runtime. It is similar to using the  new  keyword, but allows you to create an instance of a class whose name is not known until runtime. Here's an example:
Class<?> cls = Class.forName("MyClass");
MyClass obj = (MyClass) cls.newInstance();
This creates a new instance of the  MyClass  class using the  newInstance()  method of the  Class  class. 
 
Using clone() method: 
 
The  clone()  method is used to create a copy of an object. It creates a new instance of the same class as the original object and copies the values of all fields from the original object to the new object. Here's an example:
MyClass obj1 = new MyClass();
MyClass obj2 = obj1.clone();
This creates a new instance of the  MyClass  class using the  clone()  method and assigns it to the  obj2  variable. 
 
Using deserialization: 
 
Deserialization is the process of converting a serialized object back into an object in memory. It is typically used to transfer objects between different systems or to store objects in a database. Here's an example:
ObjectInputStream in = new ObjectInputStream(new FileInputStream("data.bin"));
MyClass obj = (MyClass) in.readObject();
This reads a serialized object from a file called  data.bin  and deserializes it into a new instance of the  MyClass  class. 
 
Using newInstance() method of Constructor class: 
 
The  newInstance()  method of the  Constructor  class is used to create a new instance of a class using a constructor at runtime. It is similar to using the  new  keyword, but allows you to create an instance of a class whose constructor is not known until runtime. Here's an example:
Constructor<MyClass> constructor = MyClass.class.getConstructor(String.class, int.class);
MyClass obj = constructor.newInstance("hello", 123);
This creates a new instance of the  MyClass  class using the  newInstance()  method of the  Constructor  class and passing arguments to the constructor.

what is use of reflections in java?
Reflection is a mechanism in Java that allows you to inspect, manipulate, and create objects at runtime. Reflection allows you to get information about classes, methods, fields, and other objects at runtime, without having to know the class or object at compile time.

Reflection is useful in a variety of situations, such as:

Dynamically loading classes at runtime
Creating objects based on user input or configuration files
Implementing frameworks that can work with any class, without having to know the class at compile time
Debugging and testing frameworks that need to work with any class
Creating proxies for objects that intercept method calls and perform additional actions
Reflection can also be used to bypass access control restrictions, which can be useful in certain situations. However, it is important to use reflection judiciously and only when necessary, as it can make your code more complex and harder to maintain.

Here are some common use cases for reflection in Java:

Dynamically loading classes at runtime:
 Class<?> clazz = Class.forName("com.example.MyClass");
Object obj = clazz.newInstance();
In this example, we use the  Class.forName() method to load the 
MyClass class at runtime. We then use the newInstance() 
 method to create a new instance of the class.

Creating objects based on user input or configuration files:
 String className = "com.example.MyClass";
Class<?> clazz = Class.forName(className);
Constructor<?> constructor = clazz.getConstructor(String.class);
Object obj = constructor.newInstance("John");
In this example, we use the Class.forName()  method to load the 
MyClass  class at runtime. We then use the  getConstructor()
 method to get the constructor that takes a  String  argument. We then use the  newInstance()
 method to create a new instance of the class and pass in the argument "John".

Implementing frameworks that can work with any class, without having to know the class at compile time:
 Class<?> clazz = Class.forName(className);
Object obj = clazz.newInstance();
Method method = clazz.getMethod("myMethod", String.class);
method.invoke(obj, "John");
In this example, we use the  Class.forName()  method to load the class at runtime. We then use the  newInstance()  method to create a new instance of the class. We then use the 
getMethod()  method to get the  myMethod  method of the class that takes a  String  argument. We then use the  invoke()  method to call the method and pass in the argument "John".

Debugging and testing frameworks that need to work with any class:
 Class<?> clazz = Class.forName(className);
Object obj = clazz.newInstance();
Field field = clazz.getField("myField");
field.set(obj, "John");
In this example, we use the  Class.forName()  method to load the class at runtime. We then use the newInstance()  method to create a new instance of the class. We then use the 
getField()  method to get the myField  field of the class. We then use the  set()  method to set the value of the field to "John".


HashMap is a class in Java that implements the Map interface, which allows you to store key-value pairs. HashMap is a hash table, which means that it uses a hash function to map keys to indices in an array. When you add a key-value pair to a HashMap, the key is hashed to determine the index in the array where the value should be stored. If there is already a value stored at that index, the new value is added to the end of a linked list at that index.

Here's how HashMap works internally:

The HashMap class implements the Map interface, which means that it has methods for adding, removing, and accessing key-value pairs.

When you create a new HashMap, it is initialized with a default capacity of 16. The capacity is the number of indices in the hash table.

When you add a key-value pair to a HashMap, the key is hashed to determine the index in the array where the value should be stored. The hash function used by HashMap is a simple modulo operation, which means that the index is calculated as 
hash(key) % capacity
.

If there is already a value stored at that index, the new value is added to the end of a linked list at that index. This allows multiple values to be stored at the same index.

When you access a value in a HashMap, the key is hashed to determine the index in the array where the value is stored. If there is more than one value stored at that index, you need to iterate through the linked list to find the value you are looking for.

When you remove a key-value pair from a HashMap, the key is hashed to determine the index in the array where the value is stored. If there is more than one value stored at that index, you need to iterate through the linked list to find the value you want to remove. Once you find the value, you remove it from the linked list and update the size of the HashMap.

HashMap is not synchronized, which means that it can be accessed by multiple threads simultaneously without causing data corruption. If you need to synchronize access to a HashMap, you can use a synchronized wrapper class such as 
Collections.synchronizedMap()
.

Overall, HashMap is a useful data structure for storing key-value pairs in Java, especially when you need to access values quickly based on the key. However, it is important to choose the right type of HashMap (e.g. LinkedHashMap, TreeMap, etc.) based on your specific use case, as some types of HashMaps are better suited for certain types of operations.

how to make custom immutable class in java?
To create a custom immutable class in Java, you can follow these steps:

Create a public class with a private constructor and public static factory methods to create instances of the class.
Make all fields final and private.
Override the equals  and  hashCode  methods to compare instances based on their fields.
Implement the  toString  method to provide a human-readable string representation of the instance.
Here's an example implementation:

public final class Point {
    private final int x;
    private final int y;

    private Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public static Point of(int x, int y) {
        return new Point(x, y);
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass()!= o.getClass()) return false;
        Point point = (Point) o;
        return x == point.x &&
                y == point.y;
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }

    @Override
    public String toString() {
        return "Point{" +
                "x=" + x +
                ", y=" + y +
                '}';
    }
}

import java.util.Arrays;

public class Main {
    public static int upper_bound(int[] A, int t) {
        int l = 0, r = A.length - 1;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (A[mid] <= t) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return l;
    }

    public static void main(String[] args) {
        int[] A = {1, 2, 3, 4, 5};
        int t = 3;
        int res = upper_bound(A, t);
        System.out.println(res); // Output: 3
    }
}

import java.util.Arrays;

public class Main {
    public static int upper_bound(int[] A, int t) {
        int l = 0, r = A.length - 1;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (A[mid] <= t) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return l;
    }

    public static void main(String[] args) {
        int[] A = {1, 2, 3, 4, 5};
        int t = 3;
        int res = upper_bound(A, t);
        System.out.println(res); // Output: 3
    }
}

```
</details>


# 



# 

<details>
  <summary>ACID properties </summary>
  
  
```
ACID stands for Atomicity, Consistency, Isolation, and Durability. These are the four properties that guarantee the reliability and consistency of database transactions. Here's a brief explanation of each property:

Atomicity: Atomicity ensures that a transaction is treated as a single, indivisible unit of work. This means that either all the operations in the transaction are completed successfully or none of them are completed at all.

Consistency: Consistency ensures that a transaction brings the database from one valid state to another. This means that all the data written to the database is valid according to the defined rules and constraints.

Isolation: Isolation ensures that a transaction does not interfere with other transactions. This means that the changes made by one transaction are isolated from the changes made by other transactions.

Durability: Durability ensures that once a transaction is committed, its changes are permanent and will survive any subsequent failures. This means that the changes made by a transaction are stored in a persistent storage medium, such as a hard disk.

By ensuring that a transaction satisfies the ACID properties, database transactions can provide a high level of reliability and consistency. This helps to ensure that the data stored in the database is accurate and up-to-date, and that transactions are processed in a consistent and reliable manner.
````
</details>


# 


# 
<details>
  <summary>spring boot framework</summary>
  
  

```
In Spring Framework, there are two ways to inject dependencies into a class: constructor autowiring and setter autowiring. Here are some guidelines on when to use each approach:

Constructor autowiring: Constructor autowiring is a form of constructor injection, where the dependencies are passed to the class through its constructor. This approach is useful when you want to ensure that all the required dependencies are available when the object is created. Constructor autowiring is also useful when you want to use different dependencies for different instances of the same class.

Setter autowiring: Setter autowiring is a form of setter injection, where the dependencies are passed to the class through setter methods. This approach is useful when you want to inject optional dependencies or when you want to change the dependencies at runtime. Setter autowiring is also useful when you want to use the same dependencies for multiple instances of the same class.

Here are some situations where you might want to use constructor autowiring:

When you want to ensure that all the required dependencies are available when the object is created.
When you want to use different dependencies for different instances of the same class.
When you want to use a default constructor and only provide optional dependencies through setter methods.
Here are some situations where you might want to use setter autowiring:

When you want to inject optional dependencies or when you want to change the dependencies at runtime.
When you want to use the same dependencies for multiple instances of the same class.
When you want to provide a default implementation for the dependencies and only override them when necessary.
In general, constructor autowiring is recommended when you want to ensure that all the required dependencies are available when the object is created, and setter autowiring is recommended when you want to inject optional dependencies or when you want to change the dependencies at runtime. However, there may be situations where you need to use both approaches together, depending on your specific requirements.



In Spring Framework, @Component, @Service, @Controller, and @Repository are all annotations used to define different types of components in a Spring application
 Here are some of the key differences between these annotations:Purpose: The @Component annotation is a generic annotation that can be used to define any type of Spring-managed component
 The @Service, @Controller, and @Repository annotations are specializations of the @Component annotation that are used to define specific types of components
Semantics: The @Service annotation is used to define a service layer component that performs business logic
 The @Controller annotation is used to define a controller component that handles HTTP requests and responses
 The @Repository annotation is used to define a repository component that provides data access services
Exception translation: The @Repository annotation provides additional functionality for exception translation, which is the process of translating database-specific exceptions into Spring's DataAccessException hierarchy
 This functionality is not provided by the @Service or @Controller annotations
Auto-detection: Spring provides auto-detection for @Service, @Controller, and @Repository components, which means that Spring will automatically detect and create instances of these components based on their annotations
 The @Component annotation requires manual registration, which means that you need to explicitly define each component in your application
Overall, the @Service, @Controller, and @Repository annotations are used to define specific types of components in a Spring application, while the @Component annotation is a generic annotation that can be used to define any type of component
 The @Repository annotation provides additional functionality for exception translation, while the @Service and @Controller annotations do not
  


In software development, I often hear the terms "Inversion of Control" (IoC) and "Dependency Injection" (DI) used interchangeably, but they are actually related concepts.

IoC is a design pattern that suggests that the control of object creation and dependencies should be inverted. Instead of creating objects directly within a class, the class should receive the objects it depends on as parameters, and it should be responsible for creating and managing those objects. This approach can help to improve the modularity, testability, and maintainability of the code.

DI, on the other hand, is a design pattern that suggests that dependencies should be injected into a class instead of creating them directly. This means that the class should not create its own dependencies, but should receive them from an external source, such as a dependency injection framework. This approach can help to reduce coupling between classes and improve the flexibility and scalability of the system.

In summary, IoC is a design pattern that suggests inverting the control of object creation and dependencies, while DI is a design pattern that suggests injecting dependencies into a class instead of creating them directly. Both approaches can help to improve the modularity, testability, and maintainability of the code, and can help to reduce coupling between classes and improve the flexibility and scalability of the system.

What is the purpose of the Spring Boot Application YAML Properties?
The Spring Boot Application YAML Properties are a type of configuration file that uses YAML syntax to specify key-value pairs. They provide a more structured and readable way of configuring a Spring Boot application than the traditional application.properties file. YAML is a human-readable data serialization language that is often used for configuration files, as it is easier to read and write than XML.

What is the purpose of the Spring Boot Application Environment?
The Spring Boot Application Environment is a container for all the configuration properties that are used by a Spring Boot application. It provides a range of methods and APIs for accessing and manipulating the configuration properties, as well as for retrieving information about the application environment. The Application Environment is typically accessed using the Environment interface, which is provided by the Spring Boot framework.

What is the purpose of the Spring Boot Application Events?
The Spring Boot Application Events are a mechanism for notifying Spring Boot applications about significant events that occur during the application's lifecycle. Spring Boot provides a range of built-in events, such as ContextStartedEvent, ContextStoppedEvent, and ContextClosedEvent, that can be used to trigger actions based on these events. Applications can also define their own custom events and trigger actions based on these events using the ApplicationEventPublisher interface.

What is the purpose of the Spring Boot Application Exception Handling?
The Spring Boot Application Exception Handling is a mechanism for handling exceptions that occur during the execution of a Spring Boot application. Spring Boot provides a range of built-in exception handlers, such as DefaultHandlerExceptionResolver and WhitelabelErrorPage, that can be used to handle exceptions in a generic way. Applications can also define their own exception handlers to handle specific exceptions.

What is the purpose of the Spring Boot Application Testing?
The Spring Boot Application Testing is a mechanism for testing a Spring Boot application. Spring Boot provides a range of built-in testing frameworks, such as JUnit and Mockito, that can be used to write unit tests and integration tests for a Spring Boot application. Applications can also define their own custom testing frameworks to test specific functionality.

What is the purpose of the Spring Boot Application Security?
The Spring Boot Application Security is a mechanism for securing a Spring Boot application. Spring Boot provides a range of built-in security features, such as authentication and authorization, that can be used to secure a Spring Boot application. Applications can also define their own custom security configurations to meet specific security requirements.

What is the purpose of the Spring Boot Application Logging?
The Spring Boot Application Logging is a mechanism for logging messages from a Spring Boot application. Spring Boot provides a range of built-in logging frameworks, such as Logback and Log4j2, that can be used to log messages in a structured way. Applications can also define their own custom logging configurations to meet specific logging requirements.

What is Spring Boot?
Spring Boot is a framework that simplifies the process of building and deploying web applications in Java. It provides a set of pre-configured components and conventions that make it easy to get started with Spring-based applications.

What are the advantages of using Spring Boot?
Some advantages of using Spring Boot include:

It simplifies the process of building and deploying web applications in Java.
It provides a set of pre-configured components and conventions that make it easy to get started with Spring-based applications.
It reduces the amount of boilerplate code required to set up a Spring application.
It provides a range of features for building microservices, such as service discovery, load balancing, and circuit breaking.
It supports a range of programming languages, including Java, Kotlin, and Groovy.
What is the difference between Spring and Spring Boot?
Spring is a framework for building Java applications, while Spring Boot is a framework for building and deploying web applications in Java. Spring Boot builds on top of Spring and provides a set of pre-configured components and conventions that make it easy to get started with Spring-based applications.

What is the purpose of the @Autowired annotation in Spring Boot?
The @Autowired annotation is used to inject dependencies into a Spring-managed component. When a component is annotated with @Autowired, Spring will automatically find the appropriate bean and inject it into the component.

What is the purpose of the @RestController annotation in Spring Boot?
The @RestController annotation is used to create a RESTful web service in Spring Boot. When a class is annotated with @RestController, Spring will automatically configure it to handle HTTP requests and responses.

What is the purpose of the @RequestMapping annotation in Spring Boot?
The @RequestMapping annotation is used to map HTTP requests to methods in a Spring-managed component. When a method is annotated with @RequestMapping, Spring will automatically map HTTP requests that match the specified URL pattern to that method.

What is the purpose of the @Transactional annotation in Spring Boot?
The @Transactional annotation is used to mark a method as transactional. When a method is marked as transactional, Spring will automatically manage the transaction for that method, ensuring that it is committed or rolled back as appropriate.

What is the purpose of the application.properties file in Spring Boot?
The application.properties file is used to configure a Spring Boot application. It contains key-value pairs that specify various configuration options, such as the port number to use, the database connection details, and the logging level.

What is the purpose of the Spring Boot Actuator?
The Spring Boot Actuator is a set of tools and APIs that provide insight into the running Spring Boot application. It provides a range of features, such as health checks, metrics, and tracing, that can be used to monitor and manage the application.

What is the purpose of the Spring Boot DevTools?
The Spring Boot DevTools is a set of tools that provide fast and efficient development time features for Spring Boot applications. It provides features such as automatic restarts, live reload, and remote debugging.

What is the purpose of the Spring Boot Starter POM?
The Spring Boot Starter POM is a set of dependencies that can be used to quickly add common Spring Boot functionality to a project. It provides a range of dependencies, such as Spring Web, Spring Data, and Spring Security, that can be easily added to a project.

What is the purpose of the Spring Boot Auto-configuration?
The Spring Boot Auto-configuration is a feature that automatically configures a Spring Boot application based on the dependencies that are included in the project. It provides a range of default configurations that can be used to quickly set up a Spring application without having to manually configure it.

What is the purpose of the Spring Boot Application Properties?
The Spring Boot Application Properties are key-value pairs that can be used to configure a Spring Boot application. They provide a range of configuration options, such as the port number to use, the database connection details, and the logging level.

What is the purpose of the Spring Boot Application YAML Properties?
The Spring Boot Application YAML Properties are a type of configuration file that uses YAML syntax to specify key-value pairs. They provide a more structured and readable way of configuring a Spring Boot application than the traditional application.properties file.

What is the purpose of the Spring Boot Application Environment?
The Spring Boot Application Environment is a container for all the configuration properties that are used by a Spring Boot application. It provides a range of methods and APIs for accessing and manipulating the
```
</details>


# 


# 
<details>
  <summary>microservices </summary>
  
  

```
HATEOAS stands for Hypermedia as the Engine of Application State. It is a design principle for building scalable and interoperable web services that follows the principles of Representational State Transfer (REST).

HATEOAS allows web services to provide a self-documenting interface, where the client can discover the available resources and their relationships by following links in the response. This makes it easier for clients to interact with the service and understand its capabilities, and it allows the service to evolve over time without breaking clients.

In a RESTful web service, HATEOAS is achieved by using HTTP headers to provide links between resources. For example, a response from a web service might include a header that contains a link to a related resource, such as a next page of results. The client can then follow this link to retrieve the next page of results, without having to know the URL or any other details about the service or its resources.

HATEOAS is particularly important in microservices architecture, where services are designed to be loosely coupled and independently deployable. By using HATEOAS, services can provide a self-documenting interface that allows clients to discover the available resources and their relationships, without having to know the exact URLs or endpoints of each service. This makes it easier to build complex applications that are composed of multiple microservices.

Overall, HATEOAS is an important design principle for building scalable and interoperable web services that follow the principles of REST. It allows clients to discover the available resources and their relationships, making it easier for them to interact with the service and understand its capabilities.


SOAP stands for Simple Object Access Protocol. It is a protocol used for exchanging structured information in the implementation of web services. It is a platform-independent, lightweight, and simple protocol that uses XML to encode data and HTTP to transport it.

SOAP messages consist of a header, a body, and an envelope. The header contains metadata about the message, such as the encoding, the version of the protocol, and the security credentials. The body contains the actual data being exchanged, such as function calls or responses. The envelope is a container that wraps the header and body and provides additional information about the message, such as the target service and the action to be performed.

SOAP was developed as a replacement for the earlier Web Services Description Language (WSDL) and Simple Object Access Protocol (SOAP) specifications. It is now widely used in web service development and is supported by many programming languages and frameworks.

Some of the key features of SOAP include:

Platform-independent: SOAP messages can be exchanged between different platforms and programming languages, making it a flexible and portable protocol.
Lightweight: SOAP messages are relatively lightweight compared to other protocols, such as REST, which can reduce latency and improve performance.
Simple: SOAP is a simple protocol that uses XML to encode data and HTTP to transport it, making it easy to understand and use.
Secure: SOAP supports security features such as SSL/TLS and WS-Security, which can help protect sensitive data and prevent unauthorized access.
Scalable: SOAP is designed to be scalable, allowing services to be added or removed from the system without affecting other services.
Overall, SOAP is a powerful and flexible protocol that is widely used in web service development.



RESTful web services are a type of web service that use a simple, lightweight, and stateless protocol to exchange data between applications. They are designed to be scalable, reliable, and secure, and are widely used in modern web applications. Here are some of the key features of RESTful web services:

Stateless: RESTful web services are stateless, which means that each request from a client to a server must contain all the necessary information to complete the request, and the server does not store any information about previous requests.

Resource-based: RESTful web services use a resource-based architecture, where each resource is identified by a unique URI. This makes it easy to identify and access specific data or functionality in the service.

Representational state transfer (REST): RESTful web services use a set of principles known as REST, which are guidelines for designing web services. These principles include:

Client-server architecture: The client and server are separate entities that communicate with each other through requests and responses.
Statelessness: Each request from the client must contain all the necessary information to complete the request, and the server does not store any information about previous requests.
Cacheability: Responses from the server can be cached by the client to improve performance and reduce the load on the server.
Uniform interface: The interface between the client and server should be uniform and standardized, so that different clients can interact with the service in a consistent manner.
Layered system: The system should be layered, with each layer adding a specific functionality to the service.
Code on demand (optional): The server can provide code to the client in response to a request, which can improve performance and reduce the load on the server.
HTTP methods: RESTful web services use a set of HTTP methods, such as GET, POST, PUT, and DELETE, to perform different operations on the resources. These methods are used to create, retrieve, update, and delete resources on the server.

Authentication and authorization: RESTful web services can use various authentication and authorization mechanisms, such as OAuth, JWT, and SAML, to ensure that only authorized users can access the service and its resources.

Versioning: RESTful web services can use different versions of the API to support different versions of the client application. This can help ensure backward compatibility and reduce the risk of breaking changes.

Hypermedia: RESTful web services use hypermedia as a mechanism for representing and navigating between resources. This allows clients to dynamically discover the available resources and their relationships, which can improve the usability and accessibility of the service.

Overall, RESTful web services are a powerful and flexible architecture that is widely used in modern web applications. They provide a simple, lightweight, and stateless protocol for exchanging data between applications, and they follow a set of principles known as REST to ensure that the interface between the client and server is uniform and standardized.

What is a microservice architecture?
A microservice architecture is an approach to building software systems that combines multiple small, independent services that communicate with each other through APIs. Each service is designed to perform a specific business function and can be developed, deployed, and scaled independently of the other services.

What are the benefits of using a microservice architecture?
Microservice architecture provides several benefits, including:

Scalability: Microservices can be developed, deployed, and scaled independently of each other, which makes it easier to handle large and complex applications.
Flexibility: Microservices can be developed using different programming languages, frameworks, and tools, which makes it easier to choose the best technology for each service.
Resilience: Microservices can be designed to be resilient to failures, which makes it easier to ensure that the application remains available and functional even in the event of hardware or software failures.
Agility: Microservices can be developed and deployed quickly and independently of each other, which makes it easier to iterate on features and fix bugs.
What are the drawbacks of using a microservice architecture?
Microservice architecture also has several drawbacks, including:

Complexity: Microservices can be complex to design, deploy, and manage, which can lead to increased development and maintenance costs.
Inter-service communication: Microservices need to communicate with each other through APIs, which can add complexity to the system and increase latency.
Data management: Microservices need to manage their own data storage and synchronization, which can add complexity to the system.
Security: Microservices need to be designed with security in mind, which can add complexity to the system and require additional security measures.
What are the advantages of using containerization technologies like Docker for microservices?
Docker provides several advantages for microservices architecture, including:

Portability: Docker containers can be easily deployed and moved between environments, which makes it easier to manage and scale the application.
Isolation: Docker containers provide a high level of isolation between services, which makes it easier to ensure that each service is running in a secure and stable environment.
Scalability: Docker containers can be easily scaled up or down based on demand, which makes it easier to handle large and complex applications.
Efficiency: Docker containers are lightweight and efficient, which makes it easier to run multiple services on a single machine.
What is a service mesh?
A service mesh is a dedicated infrastructure layer that provides features for microservices architecture, such as service discovery, load balancing, and encryption. It is designed to make it easier to manage and secure microservices, and to provide features such as observability, traffic management, and policy enforcement.

What are the benefits of using a service mesh?
Service mesh provides several benefits for microservices architecture, including:

Simplified management: Service mesh provides a centralized layer for managing microservices, which makes it easier to manage and monitor the application.
Security: Service mesh provides features such as encryption, authentication, and authorization, which makes it easier to ensure that microservices are secure and protected from external threats.
Observability: Service mesh provides features such as monitoring, logging, and tracing, which makes it easier to monitor and troubleshoot the application.
Traffic management: Service mesh provides features such as load balancing, circuit breaking, and rate limiting, which makes it easier to manage the traffic to microservices and ensure that the application remains available and responsive.
What are the drawbacks of using a service mesh?
Service mesh also has several drawbacks, including:

Complexity: Service mesh can be complex to design, deploy, and manage, which can lead to increased development and maintenance costs.
Performance overhead: Service mesh can introduce a small performance overhead, which can impact the performance of microservices.
Vendor lock-in: Service mesh is typically vendor-specific, which can limit its adoption by other vendors and make it more difficult to integrate with existing systems.
What is an API gateway?
An API gateway is a server that sits between the client and the microservices and routes requests to the appropriate microservice. It is designed to simplify the communication between microservices and to provide features such as authentication, rate limiting, and caching.

What are the benefits of using an API gateway?
API gateway provides several benefits for microservices architecture, including:

Simplified communication: API gateway simplifies the communication between microservices by providing a single entry point for client requests.
Authentication and authorization: API gateway provides features such as authentication 

```
</details>


# 


# 
<details>
  <summary>SOLID PRINCIPALS AND DESIGN PATTERNS</summary>
  
  

```

The Dependency Inversion Principle (DIP) helps eliminate undesirable dependencies by inverting the direction of dependencies and relying on abstractions.

The DIP suggests that high-level modules should not depend on low-level modules. Instead, both should depend on abstractions. This means that the high-level modules should not be dependent on the specific implementation details of the low-level modules, but should instead depend on abstractions that define the contracts for interacting with those modules.

By doing this, developers can create code that is more modular, flexible, and maintainable, as changes to the low-level modules do not affect the high-level modules, and vice versa. This can help to eliminate undesirable dependencies between modules, as the high-level modules do not depend on the specific implementation details of the low-level modules, but instead depend on abstractions that define the contracts for interacting with those modules.

For example, consider the following code that has undesirable dependencies between modules:

public class Car {
    private Engine engine;

    public Car(Engine engine) {
        this.engine = engine;
    }

    public void start() {
        engine.start();
    }

    public void stop() {
        engine.stop();
    }
}

public class Engine {
    public void start() {
        // implementation
    }

    public void stop() {
        // implementation
    }
}
In this code, the Car class has a direct dependency on the Engine class, which violates the DIP
 By inverting the direction of dependencies and relying on an abstraction, the Car class can depend on an interface that defines the contracts for interacting with the Engine class, without directly depending on the Engine class

public interface EngineInterface {
    public void start();
    public void stop();
}

public class DieselEngine implements EngineInterface {
    public void start() {
        // implementation
    }

    public void stop() {
        // implementation
    }
}

public class ElectricEngine implements EngineInterface {
    public void start() {
        // implementation
    }

    public void stop() {
        // implementation
    }
}

public class Car {
    private EngineInterface engine;

    public Car(EngineInterface engine) {
        this.engine = engine;
    }

    public void start() {
        engine.start();
    }

    public void stop() {
        engine.stop();
    }
}


In this refactored code, the Engine class is replaced with an interface, which allows the Car class to depend on an abstraction that defines the contracts for interacting with the engine
 This decouples the Car class from the specific implementation of the engine, which promotes flexibility in the code

Overall, the Dependency Inversion Principle helps eliminate undesirable dependencies by inverting the direction of dependencies and relying on abstractions, which promotes loose coupling between modules and promotes the creation of flexible and maintainable code.

Coupling principles in code organization are guidelines that focus on the degree to which the elements of a module or class are related to each other and how they are related. These principles are designed to promote a clear and modular architecture for the code, which makes it easier to understand, test, and maintain.

Here are some common coupling principles in code organization:

The High Cohesion Principle (HCP): This principle suggests that a class should have only one responsibility, and that it should encapsulate its own behavior and data.

The Low Coupling Principle (LCP): This principle suggests that modules should be loosely coupled, meaning that changes to one module should not require changes to other modules.

The Dependency Inversion Principle (DIP): This principle suggests that high-level modules should not depend on low-level modules. Instead, both should depend on abstractions.

The Interface Segregation Principle (ISP): This principle suggests that clients should not be forced to depend on interfaces they do not use. Instead, clients should depend on abstractions that are large enough to encompass the behavior they need.

The Common Closure Principle (CCP): This principle suggests that classes should be closed for modification, meaning that they should not allow behavior to be added to them without modifying them.

Overall, coupling principles in code organization are designed to promote a clear and modular architecture for the code, which makes it easier to understand, test, and maintain. By following these principles, developers can create code that is more flexible, maintainable, and extensible, while minimizing the number of client-specific interfaces that the code has.

Cohesion principles in code organization are guidelines that focus on the degree to which the elements of a module or class are related to each other and how they are related. These principles are designed to promote a clear and modular architecture for the code, which makes it easier to understand, test, and maintain.

Here are some common cohesion principles in code organization:

The Single Responsibility Principle (SRP): This principle suggests that a class should have only one reason to change, and that it should encapsulate its own behavior and data.

The Open-Closed Principle (OCP): This principle suggests that a class should be open for extension but closed for modification. This means that you should be able to add new functionality to a class without modifying its existing code.

The Liskov Substitution Principle (LSP): This principle suggests that a subclass should be able to replace its superclass without affecting the correctness of the program.

The Interface Segregation Principle (ISP): This principle suggests that clients should not be forced to depend on interfaces they do not use. Instead, clients should depend on abstractions that are large enough to encompass the behavior they need.

The Dependency Inversion Principle (DIP): This principle suggests that high-level modules should not depend on low-level modules. Instead, both should depend on abstractions.

Overall, cohesion principles in code organization are designed to promote a clear and modular architecture for the code, which makes it easier to understand, test, and maintain. By following these principles, developers can create code that is more flexible, maintainable, and extensible, while minimizing the number of client-specific interfaces that the code has.

Violations of the Law of Demeter (LoD) can have several impacts on code maintainability, including:

Improving code modularity and encapsulation: By following the LoD, developers can create code that is more modular, flexible, and maintainable. This makes it easier to modify or extend the code without affecting other parts of the system.

Simplifying debugging and error handling: By minimizing the number of client-specific interfaces that a class has, developers can create code that is more modular and easier to understand. This makes it easier to debug and handle errors in the code, as it is easier to identify the source of the problem.

Introducing tight coupling: By violating the LoD, developers can create code that is more difficult to modify and maintain. This can lead to tight coupling between modules, which can make it harder to modify or extend the code without affecting other parts of the system.

Ensuring consistent naming conventions across the codebase: By following the LoD, developers can ensure that the naming conventions used throughout the codebase are consistent and easy to understand. This makes it easier to collaborate with other developers and to maintain the code over time.

Overall, violations of the LoD can have a significant impact on code maintainability, as they can lead to improved code modularity, encapsulation, and maintainability, but they can also introduce tight coupling and inconsistent naming conventions. It is important to weigh the pros and cons carefully, and to follow the LoD only when it is necessary to create clear and modular architecture for the code.

The Law of Demeter (LoD) is a design principle that suggests that a class should only communicate with its immediate dependencies, and should avoid communicating with other classes. This helps to create a clear and modular architecture for the code, which makes it easier to understand, test, and maintain.

Here are some pros and cons of applying the LoD:

Pros:

Improved maintainability: By following the LoD, developers can create code that is more modular, flexible, and maintainable. This makes it easier to modify or extend the code without affecting other parts of the system.
Reduced coupling: By minimizing the number of client-specific interfaces that a class has, developers can create code that is more modular and easier to understand. This makes it easier to modify or extend the code without affecting other parts of the system.
Cons:

Potentially increased number of method calls: By following the LoD, developers can create code that is more modular and easier to understand, but it can also potentially increase the number of method calls in the code. This can lead to slower performance and increased memory usage.
Overall, the LoD is a useful design principle that can help to create clear and modular architecture for the code, which makes it easier to understand, test, and maintain. However, it is important to weigh the pros and cons carefully, and to consider the potential impact on performance and memory usage before applying the LoD to the code.
The primary goal of applying the Law of Demeter (LoD) is to minimize the knowledge and dependencies between objects.

The LoD suggests that a class should only interact with its immediate dependencies, and should avoid interacting with indirect dependencies. This means that a class should not have methods that return objects that are not of the same type as the class itself, and should not have methods that take objects as parameters that are not of the same type as the class itself.

The LoD is related to the Dependency Inversion Principle (DIP), which suggests that high-level modules should not depend on low-level modules directly, but instead should depend on abstractions that define the contracts for interacting with the low-level modules. This allows for the abstraction of the low-level modules from the high-level modules, which can make it easier to swap out or replace low-level modules without affecting the high-level modules.

By following the LoD, developers can create code that is more modular, flexible, and maintainable, and that is easier to understand and modify. This can help to reduce the coupling between modules and improve the reusability and flexibility of the code over time.

Overall, the primary goal of applying the LoD is to create code that is more modular, flexible, and maintainable, and that is easier to understand and modify. By following the LoD, developers can create code that is easier to understand, test, and maintain over time, and that can be easily modified or extended without affecting other parts of the system.

A subclass changes the return type of a method to a subtype of the return type in the superclass is an example of covariance.

Covariance is a concept in object-oriented programming that refers to the ability of a subclass to have a more specific return type than the superclass. In other words, a subclass can have a more specific type of object than the superclass, and the subclass can still be used in a way that is consistent with the superclass.

In the context of method return types, covariance refers to the ability of a subclass to have a more specific type of object than the superclass. For example, consider the following code:
class Animal {
    public void makeSound() {
        System.out.println("Animal is making a sound");
    }
}

class Dog extends Animal {
    public void makeSound() {
        System.out.println("Dog is barking");
    }
}


In this code, the Dog class is a subclass of the Animal class, and the Dog class overrides the makeSound() method to provide a more specific implementation
 The Dog class is still able to return an object of type Animal from the makeSound() method, even though it has overridden the method in the Animal class
This is an example of covariance, as the Dog class is able to provide a more specific implementation of the makeSound() method than the Animal class
 This allows the Dog class to be used in a way that is consistent with the Animal class, and can help to avoid unnecessary type casting and type checking


Overall, covariance is a useful feature of object-oriented programming that allows subclasses to have more specific types of objects than their superclasses, while still maintaining the ability to be used in a way that is consistent with the superclass.

A subclass alters the post-conditions of a method from the superclass is not a violation of the Liskov Substitution Principle.

The Liskov Substitution Principle (LSP) is a design principle that was introduced by Barbara Liskov in her book "The Liskov Substitution Principle: A Proven Guide for Object-Oriented Design" (1987). The principle states that if S is a subtype of T, then objects of type T may be replaced with objects of type S without affecting the correctness of the program.

In the context of object-oriented programming, this means that a subclass should be able to replace an object of the superclass with an object of the subclass without affecting the correctness of the program. This is because the subclass may have overridden some of the methods of the superclass, and any overridden methods may have different post-conditions.

Altering the post-conditions of a method from the superclass is not a violation of the Liskov Substitution Principle, as long as the subclass is still able to meet the requirements of the LSP. In other words, the subclass may have overridden the method and provided a different implementation, but it must still meet the requirements of the LSP by providing a valid implementation of the method that is consistent with the superclass.

Overall, the Liskov Substitution Principle is a useful design principle that helps to ensure that subtypes of a superclass are able to replace objects of the superclass without affecting the correctness of the program.

Violations of the Interface Segregation Principle (ISP) can have a negative impact on software development in several ways.

Firstly, violations of the ISP can lead to tight coupling between objects, which can make it difficult to modify or replace individual components of the system without affecting other components. This can make it difficult to maintain and extend the system over time, as it can be difficult to isolate and test individual components.

Secondly, violations of the ISP can result in increased dependencies between objects, which can make it more difficult to understand and maintain the system over time. This can make it more difficult to modify or replace individual components of the system without affecting other components, as it can be difficult to determine the impact of changes on the system as a whole.

Thirdly, violations of the ISP can promote loose coupling and modular design, which can make it easier to modify or replace individual components of the system without affecting other components. This can make it easier to maintain and extend the system over time, as it can be easier to isolate and test individual components.

Overall, violations of the ISP can have a negative impact on software development by making it more difficult to maintain and extend the system, and by promoting tight coupling and increased dependencies between objects. It is important to carefully design and implement interfaces that follow the ISP, to ensure that objects are loosely coupled and that the system is modular and maintainable over time.

A drawback of the Anemic Domain Model is "Objects become bloated with both data and behavior."

The Anemic Domain Model is a design pattern that was introduced by Eric Evans in his book "Domain-Driven Design: Tackling Complexity in the Heart of Software" (2003). The model is based on the idea that domain objects should have a small set of responsibilities and should be focused on the core attributes and behaviors of the object.

One of the main advantages of the Anemic Domain Model is that it encourages encapsulation and reduces coupling between objects. By focusing on the core attributes and behaviors of an object, the model helps to create a clear and focused domain model that is easy to understand and maintain.

However, the Anemic Domain Model can also have drawbacks. One of the main drawbacks of the Anemic Domain Model is that it can lead to objects becoming bloated with both data and behavior. This can make it difficult to understand and maintain the object, as it can become difficult to distinguish between the object's data and behavior.

In addition, the Anemic Domain Model can also lead to objects becoming too tightly coupled to each other, which can make it difficult to modify the object's behavior without affecting other parts of the program.

Overall, while the Anemic Domain Model can be a useful design pattern in some cases, it can also have drawbacks such as bloated objects and tightly coupled objects. It is important to carefully consider the trade-offs and use the model in a way that is appropriate for the specific domain and problem being solved.

An object that exposes its internal state through a public getter method violates the Tell, Don't Ask Principle.

The Tell, Don't Ask Principle suggests that objects should tell other objects what to do, rather than asking other objects for their state. However, if an object exposes its internal state through a public getter method, it is allowing other objects to access the object's internal state directly, which violates the principle.

In other words, the public getter method is violating the Tell, Don't Ask Principle because it allows other objects to access the object's internal state directly, rather than allowing them to tell the object what to do. This can make it difficult to modify the object's behavior without affecting other parts of the program, and can make the object more difficult to understand and maintain.

To avoid violating the Tell, Don't Ask Principle, it is generally recommended to use methods or functions to allow other objects to perform a specific task, rather than allowing them to access the object's internal state directly. This can help to ensure that the object's behavior is encapsulated and can be easily modified without affecting other parts of the program.

Overall, while it is possible to expose internal state through public getter methods, it is generally considered bad practice and can lead to problems such as violations of the principle of encapsulation and the difficulty of modifying the object's behavior.

The Tell, Don't Ask Principle is a design principle that encourages objects to expose behavior instead of state.

The Tell, Don't Ask Principle is a design principle that was introduced by Uncle Bob Martin (also known as Robert C. Martin) in the book "Agile Software Development, Principles, Patterns, and Practices" (2002). The principle states that objects should tell other objects what to do, rather than asking other objects for their state.

In other words, the Tell, Don't Ask Principle suggests that objects should provide methods or functions that allow other objects to perform a specific task, rather than allowing other objects to access the object's internal state directly. This helps to ensure that the object's behavior is encapsulated and can be easily modified without affecting other parts of the program.

The Tell, Don't Ask Principle is an important principle in object-oriented programming, as it helps to create more modular, flexible, and maintainable code. By following the Tell, Don't Ask Principle, you can create code that is easier to understand, test, and modify, and that can be easily extended and adapted to new requirements.

Overall, the Tell, Don't Ask Principle is a useful design principle that encourages objects to expose behavior instead of state, which can help to create more modular, flexible, and maintainable code.

The disadvantage of data exposure is "It violates the principle of encapsulation."

Data exposure is a concept in object-oriented programming that refers to the practice of exposing the internal data of an object to other parts of the program. This can make it difficult to maintain the integrity and consistency of the object's data, as it can be difficult to ensure that the data is used correctly and in a consistent manner.

In object-oriented programming, it is generally considered good practice to encapsulate the data of an object and to provide methods or functions that allow other parts of the program to access and manipulate the data. This helps to ensure that the object's data is used correctly and in a consistent manner, and that the object's behavior is encapsulated and can be easily modified without affecting other parts of the program.

While data exposure can be useful in some cases, it can also lead to problems such as violations of the principle of encapsulation and the difficulty of maintaining the integrity and consistency of the object's data. Therefore, it is generally recommended to use data hiding and encapsulation to ensure that objects are used correctly and in a consistent manner.

The Shotgun Surgery anti-pattern is "Modifying the implementation of a method in multiple classes."

Shotgun Surgery is an anti-pattern in software development that occurs when a change is made to a method or module in multiple places without considering the consequences of the change. This can lead to significant and unexpected issues, such as bugs, performance problems, and maintenance problems.

In the case of modifying the implementation of a method in multiple classes, the Shotgun Surgery anti-pattern occurs when a change is made to the implementation of a method in one class, but the change is not propagated to all the other classes that depend on the method. This can lead to inconsistencies and unexpected behavior in the system, as different parts of the system may behave differently depending on the specific implementation of the method.

To avoid the Shotgun Surgery anti-pattern, it is important to carefully consider the consequences of any changes to the implementation of a method, and to ensure that those changes are propagated to all the relevant classes and modules. This can be achieved through the use of design patterns and other software design principles, such as the Single Responsibility Principle and the Open-Closed Principle.

The benefit of avoiding over-design is "It makes code more modular and extensible."

Over-design is the practice of designing a system that is too complex and difficult to modify or extend. This can lead to code that is difficult to understand, maintain, and update over time.

By avoiding over-design, you can create code that is modular and extensible. This means that the code is designed to be easily divided into smaller, more focused modules that can be easily modified or extended without affecting the rest of the system. This makes it easier to add new features or fix bugs, as you can simply modify the relevant module without affecting the rest of the system.

Overall, avoiding over-design can help to create code that is more maintainable, scalable, and flexible, which is essential for long-term success and sustainability.

The difference between cohesion and coupling is "Cohesion refers to how closely related the responsibilities of a module are, while coupling refers to how much a module depends on other modules."

Cohesion is a measure of how closely related the responsibilities of a module are. It is a measure of how well the responsibilities of a module are grouped together and how well they are related to each other. A high cohesion score indicates that the responsibilities of a module are well-grouped and related to each other, while a low cohesion score indicates that the responsibilities of a module are spread out and unrelated to each other.

Coupling, on the other hand, is a measure of how much a module depends on other modules. It is a measure of how interdependent the modules are and how tightly coupled they are to each other. A high coupling score indicates that the modules are highly interdependent and tightly coupled, while a low coupling score indicates that the modules are loosely coupled and less interdependent.

In summary, cohesion is a measure of how closely related the responsibilities of a module are, while coupling is a measure of how much a module depends on other modules. Cohesion is a good measure to optimize in software design, as it helps to ensure that modules have a clear and well-defined responsibility.

Domain Driven Design based Microservices development?
Domain-driven design (DDD) is an approach to software development that emphasizes the importance of understanding the business domain in which the software operates. DDD focuses on the development of domain models that describe the core concepts and behaviors of the business domain, and they are used to guide the design of the software.

Microservices architecture is a software architecture style that involves breaking down a single application into smaller, independent services that communicate with each other through APIs. Each service is designed to perform a specific business function and can be developed, deployed, and scaled independently of the other services.

Domain-driven design can be applied to microservices architecture in several ways. One approach is to use bounded contexts to identify the core domain concepts and boundaries within which the microservices are designed. Each microservice can be designed to operate within its own bounded context, and they can communicate with each other through APIs.

Another approach is to use domain models to represent the core domain concepts and behaviors within each microservice. The domain models can be used to guide the design of the microservice, and they can be validated against the business requirements to ensure that they are accurate and complete.

Domain-driven design can also be applied to the design of the data model within each microservice. The data model can be designed to reflect the domain models, and it can be optimized for performance and scalability.

Overall, domain-driven design can be a powerful tool for microservices development, as it helps to ensure that the microservices are aligned with the business domain and that they are designed to meet the needs of the business.
```
</details>


# 


# 
<details>
  <summary>Cloud  releated questions</summary>
  
  


```
What is cloud computing and how does it work?
Cloud computing is a model of computing in which resources are provided on-demand with pay-as-you-go pricing. It involves delivering computing services over the internet, such as storage, processing power, and software, without direct management by the user. Cloud providers offer a range of services, including virtual machines, storage, databases, and networking, that can be accessed through a web interface or a command-line interface.

What are the different types of cloud providers and how do they differ?
There are several different types of cloud providers, including public, private, and hybrid clouds. Public clouds, such as Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform, are owned and operated by large corporations and organizations, and are designed to be scalable, reliable, and secure. Private clouds, such as OpenStack and VMware vSphere, are operated by smaller organizations or individuals, and are designed to be more secure and flexible. Hybrid clouds, which combine public and private clouds, are designed to provide a balance between the benefits of public and private clouds.

What is the difference between IaaS, PaaS, and SaaS?
IaaS (Infrastructure as a Service) provides a virtualized infrastructure layer, allowing users to create and manage virtual machines, storage, and networking resources. PaaS (Platform as a Service) provides a platform for developers to build and deploy applications, without needing to manage the underlying infrastructure. SaaS (Software as a Service) provides access to software applications over the internet, without needing to install or maintain the software on their own devices.

What is a cloud-native application and how does it differ from traditional applications?
A cloud-native application is designed to take advantage of the features and benefits of cloud computing, such as scalability, reliability, and automatic scaling. It is built using cloud-native technologies, such as containers, microservices, and serverless architecture. Cloud-native applications are designed to be resilient to failures, secure, and observable, and are typically built using a combination of programming languages, frameworks, and tools. Traditional applications, on the other hand, are typically built using monolithic architecture, and are typically designed to be single-tenant and run on a single server.

What is a containerization technology and how does it work?
A containerization technology is a way of packaging and deploying applications in a way that is isolated from the underlying operating system and hardware. Containers are lightweight, portable, and self-contained, and can be run on any machine that supports Docker. Containers are designed to be portable, meaning that they can be moved between environments without requiring any changes to the underlying software or hardware.

What is a serverless architecture and how does it work?
A serverless architecture is a cloud computing model where the cloud provider manages the infrastructure and automatically provisions and scales resources as needed. In a serverless architecture, developers write code in the form of functions or microservices, and the cloud provider automatically provisions the resources needed to run those functions. The cloud provider also automatically scales the resources up or down based on the amount of traffic or workload.

What is a microservices architecture and how does it differ from a monolithic architecture?
A microservices architecture is a software architecture style where an application is built as a collection of small, independent services that communicate with each other through APIs. Each service is designed to perform a specific task, and can be developed, tested, and deployed independently of the other services. Microservices architecture is designed to be scalable, resilient, and secure, and is often used in modern software development. Monolithic architecture, on the other hand, is a traditional software architecture style where an entire application is built as a single unit.

What is a load balancer and how does it work?
A load balancer is a device that distributes network traffic across multiple servers to improve performance and reliability. It is typically used to distribute incoming traffic to multiple servers that are running the same application, so that if one server becomes overloaded or fails, the load balancer can automatically distribute the traffic to other servers. Load balancers can be configured to use different algorithms, such as round-robin, least connections, or weighted round-robin, to distribute traffic in a more efficient way.

What is a database and how does it work?
A database is a structured collection of data that is stored and managed in a database management system. It is used to store and retrieve data for applications, such as web applications, mobile applications, and enterprise applications. Databases can be used to store a wide range of data, including text, images, audio, and video.

What is a caching layer and how does it work? 
A caching layer is a component of a software system that stores frequently accessed data in memory or on disk, in order to improve performance and reduce the number of requests to the underlying data source. When a user requests data, the caching layer first checks if the data is already in the cache. If it is, the data is returned immediately without querying the underlying data source. If the data is not in the cache, the caching layer retrieves it from the data source, stores it in the cache, and returns it to the user. This reduces the response time and the load on the data source. Examples of caching layers include Redis, Memcached, and Varnish. 
 
What is a message queue and how does it work? 
A message queue is a component of a software system that allows different parts of the system to communicate asynchronously by sending and receiving messages. When a sender sends a message to a message queue, the message is stored in the queue until a receiver retrieves it. The receiver can retrieve messages from the queue in the order they were added, or based on other criteria such as message priority or content. This decouples the sender and receiver, allowing them to operate independently and asynchronously. Message queues are used in a variety of scenarios, such as task scheduling, event processing, and distributed systems. Examples of message queue systems include RabbitMQ, Apache Kafka, and Amazon SQS. 
 
What is a workflow automation tool and how does it work? 
A workflow automation tool is a software system that automates and streamlines business processes by defining, executing, and managing workflows. Workflows are sequences of tasks or activities that need to be performed in a specific order, often involving multiple people or systems. Workflow automation tools allow users to define workflows graphically or through code, and then execute them automatically based on predefined triggers or events. Workflows can include tasks such as approvals, notifications, data processing, and integrations with other systems. Workflow automation tools can improve efficiency, reduce errors, and increase visibility into business processes. Examples of workflow automation tools include Zapier, Microsoft Power Automate, and Nintex. 
 
What is a monitoring tool and how does it work? 
A monitoring tool is a software system that monitors the performance, availability, and health of a software system, network, or infrastructure. Monitoring tools collect data such as CPU usage, memory usage, network traffic, and application logs, and then analyze and visualize this data to provide insights into the system's behavior and identify potential issues. Monitoring tools can also generate alerts or notifications when certain thresholds or conditions are met, allowing operators to take corrective action before issues become critical. Monitoring tools are used in a variety of scenarios, such as IT operations, DevOps, and security. Examples of monitoring tools include Nagios, Zabbix, and Prometheus. 
 
What is a backup and restore strategy and how does it work? 
A backup and restore strategy is a plan for creating and storing copies of data or systems in order to recover them in the event of a data loss or system failure. Backup and restore strategies typically involve creating regular backups of data or systems, storing them in a secure location, and then restoring them when needed. Backups can be created using a variety of methods, such as full backups, incremental backups, or differential backups. The backup and restore strategy should also specify how often backups are created, how long they are retained, and how they are tested for reliability and recoverability. Backup and restore strategies are critical for ensuring business continuity and minimizing the impact of data loss or system failures. Examples of backup and restore tools or services include Amazon S3, Google Cloud Storage, and Veeam Backup & Replication. 
 
What is a disaster recovery strategy and how does it work? 
A disaster recovery strategy is a plan for recovering a software system, network, or infrastructure in the event of a major disaster or disruption, such as a natural disaster, cyber attack, or hardware failure. Disaster recovery strategies typically involve creating redundant systems or infrastructure in a different location, and then implementing processes and procedures for recovering data and systems in the event of a disaster. Disaster recovery strategies may also involve creating backup and restore plans, testing disaster recovery procedures, and training personnel on disaster recovery procedures. Disaster recovery strategies are critical for ensuring business continuity and minimizing the impact of major disruptions. Examples of disaster recovery tools or services include AWS Disaster Recovery, Microsoft Azure Site Recovery, and Zerto.

Cloud Ops is a set of practices and tools that are used to manage and monitor cloud-based infrastructure and applications. The following are some of the key components of Cloud Ops:

Observability: Observability refers to the ability to monitor and analyze the behavior of cloud-based infrastructure and applications. This includes monitoring the performance, availability, and security of the infrastructure and applications, as well as collecting and analyzing data to identify trends and patterns.

Serviceability: Serviceability refers to the ability to provide customers with the ability to diagnose and resolve issues with cloud-based infrastructure and applications. This includes providing monitoring and alerting tools, as well as providing tools for troubleshooting and debugging.

Resiliency: Resiliency refers to the ability of cloud-based infrastructure and applications to recover from failures and continue to function properly. This includes designing the infrastructure and applications to be resilient to failures, such as using redundancy and failover mechanisms, and testing the resiliency of the infrastructure and applications.

Scalability: Scalability refers to the ability of cloud-based infrastructure and applications to handle increased traffic and workload. This includes designing the infrastructure and applications to be scalable, such as using auto-scaling mechanisms, and testing the scalability of the infrastructure and applications.

Fault Containment: Fault containment refers to the ability of cloud-based infrastructure and applications to isolate and contain failures and disruptions. This includes designing the infrastructure and applications to be fault-tolerant, such as using redundancy and failover mechanisms, and testing the fault containment of the infrastructure and applications.

Overall, Cloud Ops is a set of practices and tools that are used to manage and monitor cloud-based infrastructure and applications, and they help ensure that the infrastructure and applications are performing optimally and reliably.

```
</details>


# 


# 
<details>
  <summary>messaging queues questions</summary>
  
  

```
1. What is a message queue and how does it work? 
A message queue is a form of communication between software components or systems that enables asynchronous processing and decouples the sender and receiver of the message. Messages are stored in a queue until they can be processed by the receiver. A message queue typically has a producer, which generates messages, and a consumer, which processes them. Examples of message queue systems include RabbitMQ, Apache Kafka, and Amazon SQS. 
 
2. What are the benefits of using a message queue in a distributed system? 
Using a message queue in a distributed system has several benefits, including decoupling the sender and receiver of the message, enabling asynchronous processing, improving scalability and fault tolerance, and providing a buffer for handling spikes in traffic. Message queues also enable processing of messages in the order they were received, and can be used to implement reliable messaging patterns such as request-reply and publish-subscribe. 
 
3. How do you ensure message ordering in a message queue system? 
Message ordering can be ensured in a message queue system by using a first-in-first-out (FIFO) queue, where messages are processed in the order they were received. Some message queue systems also support message priorities, where higher-priority messages are processed before lower-priority messages. Another approach is to use message sequencing, where messages are assigned a sequence number that can be used to order them. 
 
4. What is the difference between a message queue and a publish-subscribe system? 
A message queue is a one-to-one communication pattern, where a message is sent from one producer to one consumer. A publish-subscribe system is a one-to-many communication pattern, where a message is sent from one producer to multiple consumers. In a publish-subscribe system, consumers subscribe to topics or channels, and receive messages published to those topics. In a message queue system, messages are stored in a queue until they can be processed by a single consumer. 
 
5. How do you handle message failures in a message queue system? 
Message failures can be handled in a message queue system by implementing retry mechanisms, where failed messages are retried a certain number of times before being discarded or sent to a dead-letter queue for further analysis. Monitoring and alerting can also be used to detect and respond to message failures. Some message queue systems also support message acknowledgement, where the receiver acknowledges receipt of the message, and the sender can detect and retry failed messages. 
 
6. What are some common message queue systems and their use cases? 
Some common message queue systems include RabbitMQ, Apache Kafka, Amazon SQS, and Microsoft Azure Service Bus. RabbitMQ is commonly used for general-purpose messaging, while Kafka is often used for high-throughput, real-time data streaming. SQS is a cloud-based message queue service that provides scalability and reliability, while Azure Service Bus is a messaging service that supports both queue-based and publish-subscribe messaging patterns. 
 
7. How do you scale a message queue system to handle high throughput and/or large volumes of messages? 
Message queue systems can be scaled to handle high throughput and large volumes of messages by using techniques such as horizontal scaling, where multiple instances of the message queue are deployed and load-balanced, and vertical scaling, where the resources of the message queue instances are increased. Other techniques include sharding, where messages are partitioned across multiple queues, and batching, where multiple messages are processed in a single operation. 
 
8. What are some best practices for designing and implementing a message queue system? 
Some best practices for designing and implementing a message queue system include using message serialization to ensure compatibility between different systems, using message versioning to handle changes in message formats, and using message compression to reduce network bandwidth. It is also important to consider security and access control, message durability and reliability, and monitoring and alerting. 
 
9. How do you ensure message delivery and prevent message loss in a message queue system? 
Message delivery and prevention of message loss can be ensured in a message queue system by using techniques such as message acknowledgement, where the receiver acknowledges receipt of the message, and message replication, where messages are replicated across multiple nodes for redundancy. Other techniques include message durability, where messages are persisted to disk, and message backup, where messages are backed up to another location. 
 
10. What is the role of message brokers in a message queue system? 
Message brokers are responsible for receiving messages from producers, storing them in a queue, and delivering them to consumers. They are often used to implement message routing and filtering, where messages are selectively delivered to specific consumers based on their content or metadata. Message brokers can also provide features such as message transformation, message aggregation, and message enrichment. Examples of message brokers include RabbitMQ, Apache Kafka, and ActiveMQ.


Kafka: 
1. What is Kafka and how does it work? 
Kafka is a distributed streaming platform that allows for the processing of high-volume, real-time data streams. It works by using a publish-subscribe model, where producers publish messages to topics, and consumers subscribe to those topics to receive the messages. 
 
2. What are the benefits of using Kafka? 
Kafka has several benefits, including high throughput and low latency, fault tolerance and scalability, and support for real-time data processing and analytics. It also provides a distributed architecture that allows for easy scaling and integration with other systems. 
 
3. How does Kafka ensure message ordering? 
Kafka ensures message ordering by using a partitioning mechanism, where messages are assigned to specific partitions based on their key. Messages within a partition are processed in the order they were received, ensuring message ordering. 
 
4. How do you handle message failures in Kafka? 
Message failures in Kafka can be handled by implementing a retry mechanism, where failed messages are retried a certain number of times before being sent to a dead-letter queue. Monitoring and alerting can also be used to detect and respond to message failures. 
 
5. What are some common use cases for Kafka? 
Kafka is commonly used for real-time data processing, stream processing, log aggregation, and messaging. It is also used in microservices architecture and as a data pipeline for big data processing. 
 
RabbitMQ: 
1. What is RabbitMQ and how does it work? 
RabbitMQ is a message broker that allows for the exchange of messages between different systems or components. It works by using a publish-subscribe model, where messages are sent to exchanges, which then route the messages to queues for processing by consumers. 
 
2. What are the benefits of using RabbitMQ? 
RabbitMQ has several benefits, including reliability and durability, scalability and performance, and support for multiple messaging patterns such as request-reply and publish-subscribe. It also provides a flexible and extensible architecture that allows for easy integration with other systems. 
 
3. How does RabbitMQ ensure message ordering? 
RabbitMQ ensures message ordering by using a FIFO (first-in-first-out) queue, where messages are processed in the order they were received. 
 
4. How do you handle message failures in RabbitMQ? 
Message failures in RabbitMQ can be handled by implementing a retry mechanism, where failed messages are retried a certain number of times before being sent to a dead-letter queue. Monitoring and alerting can also be used to detect and respond to message failures. 
 
5. What are some common use cases for RabbitMQ? 
RabbitMQ is commonly used for messaging, task management, and job queues. It is also used in microservices architecture and as a data pipeline for big data processing.

````
</details>


# 


# 

<details>
  <summary>Operating System Basics:</summary>
  
  

```
1. What is an operating system? 
Answer: An operating system (OS) is a software program that manages computer hardware and software resources and provides common services for computer programs. 
 
2. Explain the main functions of an operating system. 
Answer: The main functions of an operating system are process management, memory management, device management, file management, and security management. 
 
3. Describe the difference between a process and a thread. 
Answer: A process is an instance of a program that is being executed, while a thread is a lightweight process that shares the same memory and resources as its parent process. 
 
4. What are the differences between multiprogramming, multitasking, and multiprocessing? 
Answer: Multiprogramming refers to the ability of an operating system to run multiple programs concurrently, while multitasking refers to the ability of an operating system to switch between multiple tasks or processes quickly. Multiprocessing refers to the ability of an operating system to use multiple CPUs or cores to run multiple processes simultaneously. 
 
5. Explain the concept of a context switch. 
Answer: A context switch is the process of saving the current state of a process or thread and restoring the state of another process or thread so that it can continue executing. 
 
6. What are the differences between a monolithic kernel and a microkernel? 
Answer: A monolithic kernel is a single large program that contains all the basic functions of the operating system, while a microkernel is a small kernel that provides only basic functionality and other services are provided by separate processes or modules. 
 
7. Describe the process of process creation and termination. 
Answer: Process creation involves allocating memory and resources for a new process, setting up the initial state of the process, and starting the execution of the process. Process termination involves releasing the memory and resources used by the process and notifying the operating system that the process has ended. 
 
8. What is the difference between preemptive and non-preemptive scheduling? 
Answer: Preemptive scheduling allows the operating system to interrupt a running process and switch to another process, while non-preemptive scheduling does not allow the operating system to interrupt a running process. 
 
9. What are system calls, and how are they different from normal function calls? 
Answer: System calls are functions that provide access to the services provided by the operating system, such as opening and closing files or allocating memory. They are different from normal function calls because they require a switch from user mode to kernel mode. 
 
10. Explain the concept of kernel mode and user mode. 
Answer: Kernel mode is a privileged mode of operation that allows the operating system to access hardware resources and perform privileged operations, while user mode is a non-privileged mode of operation that restricts access to hardware resources and privileged operations. Applications run in user mode, while the operating system runs in kernel mode.
```
</details>


# 


# 

<details>
  <summary>Process Management: </summary>
  
  

````
11. Describe the process of process scheduling. 
Answer: Process scheduling involves selecting the next process to run on a CPU based on a set of criteria, such as priority, time-sharing, and resource availability. The operating system maintains a list of processes in a ready queue, and the scheduler selects a process from this queue to run on the CPU. The process scheduling algorithm determines the order in which processes are selected from the ready queue. 
12. What are the different scheduling algorithms used in operating systems? 
Answer: Some common scheduling algorithms used in operating systems include First-Come, First-Served (FCFS), Shortest Job First (SJF), Priority Scheduling, Round Robin Scheduling, and Multi-Level Queue Scheduling. 
13. Explain the differences between preemptive and non-preemptive scheduling. 
Answer: Preemptive scheduling allows the operating system to interrupt a running process and switch to another process, while non-preemptive scheduling does not allow the operating system to interrupt a running process. Preemptive scheduling is more responsive to changes in the system, but can potentially cause more overhead due to frequent context switches. 
14. What is a context switch, and how does it affect the performance of a system? 
Answer: A context switch is the process of saving the current state of a process or thread and restoring the state of another process or thread so that it can continue executing. Context switches can affect the performance of a system by introducing overhead due to the time required to save and restore process state, and by potentially causing cache misses and other performance issues. 
15. Describe the process of process synchronization using semaphores. 
Answer: Process synchronization using semaphores involves using special variables called semaphores to coordinate access to shared resources between multiple processes or threads. A semaphore can be thought of as a counter that is used to control access to a shared resource. Processes or threads can acquire or release a semaphore to signal that they need access to the shared resource or that they are done using it. 
16. Explain the dining philosophers problem and how it can be solved. 
Answer: The dining philosophers problem is a classic problem in concurrent programming that involves a group of philosophers sitting around a table with a bowl of rice and chopsticks. Each philosopher needs two chopsticks to eat, and there are only five chopsticks available. The problem is to design a solution that allows the philosophers to eat without getting into a deadlock. One solution to the problem is to use a semaphore to control access to the chopsticks and to ensure that only one philosopher can pick up a chopstick at a time. 
17. What is a critical section, and how is it protected in concurrent programming? 
Answer: A critical section is a section of code that accesses shared resources and must be executed atomically to prevent race conditions and other synchronization issues. Critical sections can be protected in concurrent programming using synchronization primitives such as semaphores, mutexes, and monitors to ensure that only one process or thread can access the critical section at a time. 
18. Explain the reader-writer problem and how it can be solved. 
Answer: The reader-writer problem is another classic problem in concurrent programming that involves multiple processes or threads accessing a shared resource, where some processes or threads only read the resource and others also write to it. The problem is to design a solution that allows multiple readers to access the resource simultaneously while ensuring that writers have exclusive access. One solution to the problem is to use a reader-writer lock, which allows multiple readers to acquire the lock simultaneously but requires writers to wait until all readers have released the lock. 
19. Describe the process of process communication using inter-process communication (IPC). 
Answer: Inter-process communication (IPC) involves the exchange of data and messages between different processes running on the same or different computers. IPC can be achieved using various mechanisms such as pipes, sockets, shared memory, and message queues. The processes must agree on a common protocol for communication, and the operating system provides the necessary mechanisms for sending and receiving data between processes. 
20. What are the different IPC mechanisms available in operating systems? 
Answer: Some common IPC mechanisms available in operating systems include pipes, sockets, shared memory, message queues, and signals. Pipes and sockets are used for communication between processes on the same or different computers, while shared memory is used for fast communication between processes running on the same computer. Message queues and signals are used for asynchronous communication between processes.
````
</details>


# 


<details>
  <summary>Memory Management: </summary>

````
21. What is virtual memory, and how does it work? 
Answer: Virtual memory is a technique used by operating systems to provide the illusion of a larger amount of memory than is physically available. It works by using a combination of hardware and software to map virtual memory addresses to physical memory addresses. When a program requests memory, the operating system allocates a virtual address space for the program, which is divided into pages. These pages are then mapped to physical memory as needed, allowing the program to access more memory than is physically available. 
  
22. Explain the concept of paging and its advantages. 
Answer: Paging is a memory management technique used by operating systems to manage virtual memory. It involves dividing memory into fixed-size pages and mapping these pages to physical memory as needed. The advantages of paging include improved memory utilization, as only the pages that are needed by a process are loaded into memory, and improved memory protection, as each process has its own virtual address space that is isolated from other processes. 
  
23. What is a page fault, and how is it handled by the operating system? 
Answer: A page fault occurs when a program attempts to access a page that is not currently in physical memory. When a page fault occurs, the operating system handles it by loading the required page from disk into memory and updating the page table to reflect the new mapping between the virtual page and the physical page. The program is then allowed to continue executing as if the page was always in memory. 
  
24. Describe the process of memory allocation and deallocation. 
Answer: Memory allocation involves reserving a portion of memory for use by a program or process. This can be done using system calls such as malloc() or new() in programming languages like C or C++. Memory deallocation involves freeing up memory that is no longer needed by a program or process. This can be done using system calls such as free() or delete() in programming languages like C or C++. 
  
25. Explain the concepts of thrashing and working set model. 
Answer: Thrashing is a phenomenon that occurs when a system spends more time swapping pages in and out of memory than executing actual processes. This can occur when the working set of a process exceeds the available physical memory, causing the system to spend more time swapping pages than executing processes. The working set model is a technique used to identify the set of pages that a process is currently using, which can be used to optimize memory allocation and reduce thrashing. 
  
26. Describe the different page replacement algorithms, such as LRU, FIFO, and Optimal. 
Answer: Page replacement algorithms are used by operating systems to choose which page to evict from physical memory when a page fault occurs. Some common page replacement algorithms include Least Recently Used (LRU), First-In, First-Out (FIFO), and Optimal. LRU replaces the page that has not been used for the longest time, FIFO replaces the page that was loaded first, and Optimal replaces the page that will not be needed for the longest time in the future. 
  
27. What is the purpose of a page table, and how is it used in virtual memory management? 
Answer: A page table is a data structure used by operating systems to keep track of the mapping between virtual memory addresses and physical memory addresses. Each process has its own page table, which is used to translate virtual memory addresses used by the process into physical memory addresses. The page table is used by the operating system to manage virtual memory and to handle page faults. 
  
28. Explain the concept of demand paging and its advantages. 
Answer: Demand paging is a technique used by operating systems to load pages into physical memory only when they are needed, rather than loading all pages into memory at once. This reduces the amount of memory required by a process and allows more processes to run simultaneously. Demand paging also reduces the time required to load a program into memory, as only the pages that are needed immediately are loaded. 
  
29. What is a segmentation fault, and how is it handled by the operating system? 
Answer: A segmentation fault occurs when a program attempts to access memory that it is not allowed to access, such as memory that has not been allocated or memory that is outside the bounds of an array. When a segmentation fault occurs, the operating system handles it by terminating the program and freeing up any resources that were allocated to the program. 
  
30. Describe the process of process swapping. 
Answer: Process swapping is a technique used by operating systems to free up memory by moving inactive processes from physical memory to disk. When a process is swapped out, its memory is written to disk and its page table is updated to reflect the new mapping between virtual memory and physical memory. The process is then removed from physical memory, freeing up space for other processes. When the process is needed again, it is swapped back into memory and its memory is read from disk.
````
</details>


# 



<details>
  <summary> File Systems: </summary>

  

````
31. What is a file system, and what are its components? 
Answer: A file system is a way of organizing and storing files on a computer. It provides a logical structure for files and directories, and manages access to these files. The components of a file system typically include a file allocation table (FAT), a directory structure, and a set of file control blocks (FCBs) or inodes that describe the attributes and location of each file. 
  
32. Explain the different types of file systems, such as FAT, NTFS, and ext4. 
Answer: FAT (File Allocation Table) is a file system used by older versions of Windows and other operating systems. NTFS (New Technology File System) is a file system used by newer versions of Windows, and is designed to be more secure and reliable than FAT. ext4 is a file system used by Linux and other Unix-like operating systems, and is designed to be fast and scalable. Other file systems include HFS+ (used by macOS), exFAT (used for external storage devices), and many others. 
  
33. Describe the process of file allocation and deallocation. 
Answer: File allocation involves reserving space on a storage device for a file. This can be done using system calls such as fopen() or create() in programming languages like C or C++. File deallocation involves freeing up space that is no longer needed by a file. This can be done using system calls such as fclose() or delete() in programming languages like C or C++. 
  
34. What is a file control block (FCB) or an inode, and how is it used in file systems? 
Answer: A file control block (FCB) or an inode is a data structure used by file systems to store information about a file. This includes attributes such as the file's name, size, location, and permissions. The FCB or inode is used by the file system to manage access to the file and to locate the file's data on disk. 
  
35. Explain the concepts of file descriptors and file descriptor tables. 
Answer: A file descriptor is a unique identifier used by an operating system to identify an open file. It is typically an integer value that is returned by a system call such as open() or create() in programming languages like C or C++. A file descriptor table is a data structure used by the operating system to keep track of open files and their associated file descriptors. This table is used by the operating system to manage access to files and to ensure that multiple processes can access the same file without conflicts. 
  
36. What is a file allocation table (FAT), and how does it work? 
Answer: A file allocation table (FAT) is a data structure used by file systems to keep track of the location of files on disk. It is used by file systems such as FAT and exFAT. The FAT consists of a series of entries, each of which corresponds to a cluster on the disk. Each entry in the FAT contains a pointer to the next cluster in the file, allowing the file system to locate the entire file on disk. 
  
37. Describe the differences between sequential, direct, and indexed file allocation methods. 
Answer: Sequential file allocation involves storing files on disk in a contiguous block of space. Direct file allocation involves storing files in a series of non-contiguous blocks, with each block containing a pointer to the next block in the file. Indexed file allocation involves using an index to locate the blocks of a file on disk. Each block of the file contains a pointer to the next block, allowing the file system to locate the entire file on disk. 
  
38. Explain the concept of file buffering and its advantages. 
Answer: File buffering is a technique used by operating systems to improve the performance of file I/O operations. It involves temporarily storing data in memory before writing it to disk or reading it from disk. This can improve performance by reducing the number of disk I/O operations required and by allowing the operating system to optimize the order in which data is written or read from disk. 
  
39. What is a symbolic link, and how does it work in file systems? 
Answer: A symbolic link is a type of file that acts as a pointer to another file or directory. When a program or user accesses the symbolic link, the operating system redirects the request to the target file or directory. This allows multiple symbolic links to point to the same file or directory, and can simplify file organization and management. 
  
40. Describe the process of file permission management in operating systems. 
Answer: File permission management involves controlling access to files and directories on a computer. This is typically done using a set of permissions that specify which users or groups are allowed to read, write, or execute a file or directory. In Unix-like operating systems, permissions are managed using a set of three bits for the owner, group, and others. In Windows, permissions are managed using a set of access control lists (ACLs)
````
</details>

# 

<details>
  <summary> Device Management: </summary>

```
41. What is a device driver, and what is its role in an operating system? 
Answer: A device driver is a software program that allows an operating system to communicate with a hardware device. It acts as an interface between the operating system and the device, translating commands from the operating system into a format that the device can understand. The device driver is responsible for managing the device's resources, such as memory and I/O operations, and for ensuring that the device operates correctly. 
42. Explain the process of device allocation and deallocation. 
Answer: Device allocation involves reserving a hardware device for use by a particular process or application. This can be done using system calls such as open() or create() in programming languages like C or C++. Device deallocation involves releasing the device when it is no longer needed. This can be done using system calls such as close() or delete() in programming languages like C or C++. 
43. What are the different types of device scheduling algorithms used in operating systems? 
Answer: Different types of device scheduling algorithms used in operating systems include First-Come, First-Served (FCFS), Shortest Job First (SJF), Priority Scheduling, Round Robin, and Deadline Scheduling. These algorithms are used to determine the order in which processes are scheduled to use a particular device, based on factors such as the length of time required for the process, the priority of the process, and the deadline for completing the process. 
44. Describe the process of device interrupt handling. 
Answer: Device interrupt handling is the process by which an operating system responds to an interrupt signal from a hardware device. When a device generates an interrupt signal, the operating system suspends the current process and switches to an interrupt handler routine. The interrupt handler routine communicates with the device driver to determine the cause of the interrupt and to take appropriate action, such as reading or writing data to the device. 
45. What is a device control block (DCB), and how is it used in device management? 
Answer: A device control block (DCB) is a data structure used by device drivers to manage access to a hardware device. The DCB contains information about the device, such as its address, status, and configuration settings. The device driver uses the DCB to manage the device's resources and to communicate with the device. 
46. Explain the concept of spooling and its benefits. 
Answer: Spooling is a technique used in operating systems to improve the performance of I/O operations. It involves temporarily storing data in a buffer or queue before sending it to a device. This allows the operating system to optimize the order in which data is sent to the device, reducing the amount of time that the device spends waiting for data. Spooling can improve the performance of printing and other I/O operations, and can also allow multiple processes to share a single device without conflicts. 
47. What is a device register, and how does it relate to device management? 
Answer: A device register is a hardware component used by a device to store data or control signals. It is typically accessed by a device driver to communicate with the device. The device driver uses the device register to read or write data to the device, or to control the device's operations. The device register is an important component of device management, as it allows the device driver to communicate with the device and to manage its resources. 
48. Describe the differences between polling and interrupt-driven I/O. 
Answer: Polling involves repeatedly checking a device to see if it is ready for data transfer. This can be done using a loop in the device driver. Interrupt-driven I/O, on the other hand, involves waiting for an interrupt signal from the device before initiating data transfer. This can reduce the amount of CPU time required by the device driver, as it allows the operating system to suspend the driver until the device is ready for data transfer. Interrupt-driven I/O is generally considered to be more efficient than polling, as it reduces the amount of CPU time required by the device driver. 
49. What is a device queue, and how is it used in device management? 
Answer: A device queue is a data structure used by operating systems to manage access to a hardware device. It contains a list of processes or requests that are waiting to use the device. The device queue is used by the operating system to determine the order in which processes are scheduled to use the device, based on factors such as the length of time required for the process, the priority of the process, and the deadline for completing the process. 
50. Explain the concept of device management. 
Answer: Device management is the process of managing access to hardware devices in an operating system. It involves allocating and deallocating devices, scheduling device access, handling interrupts, and managing device resources such as memory and I/O operations. Device management is an important component of operating system design, as it allows multiple processes to share a single device without conflicts, and ensures that devices are used efficiently and effectively.
```

  
</details>




# 


### 1. [Code Jam](https://codingcompetitions.withgoogle.com/codejam)
- [2022](https://codingcompetitions.withgoogle.com/codejam/archive/2022)
- [2021](https://codingcompetitions.withgoogle.com/codejam/archive/2021)
- [2020](https://codingcompetitions.withgoogle.com/codejam/archive/2020)
- [2019](https://codingcompetitions.withgoogle.com/codejam/archive/2019)
- [2018](https://codingcompetitions.withgoogle.com/codejam/archive/2018)
- [2017](https://codingcompetitions.withgoogle.com/codejam/archive/2017)
- [2016](https://codingcompetitions.withgoogle.com/codejam/archive/2016)
- [2015](https://codingcompetitions.withgoogle.com/codejam/archive/2015)
- [2014](https://codingcompetitions.withgoogle.com/codejam/archive/2014)
- [2013](https://codingcompetitions.withgoogle.com/codejam/archive/2013)
- [2012](https://codingcompetitions.withgoogle.com/codejam/archive/2012)
- [2011](https://codingcompetitions.withgoogle.com/codejam/archive/2011)
- [2010](https://codingcompetitions.withgoogle.com/codejam/archive/2010)
- [2009](https://codingcompetitions.withgoogle.com/codejam/archive/2009)
- [2008](https://codingcompetitions.withgoogle.com/codejam/archive/2008)

### 2. [Hash Code](https://codingcompetitions.withgoogle.com/hashcode)

### 3. [Kick Start](https://codingcompetitions.withgoogle.com/kickstart)
- [2022](https://codingcompetitions.withgoogle.com/kickstart/archive/2022)
- [2021](https://codingcompetitions.withgoogle.com/kickstart/archive/2021)
- [2020](https://codingcompetitions.withgoogle.com/kickstart/archive/2020)
- [2019](https://codingcompetitions.withgoogle.com/kickstart/archive/2019)
- [2018](https://codingcompetitions.withgoogle.com/kickstart/archive/2018)
- [2017](https://codingcompetitions.withgoogle.com/kickstart/archive/2017)
- [2016](https://codingcompetitions.withgoogle.com/kickstart/archive/2016)
- [2015](https://codingcompetitions.withgoogle.com/kickstart/archive/2015)
- [2014](https://codingcompetitions.withgoogle.com/kickstart/archive/2014)
- [2013](https://codingcompetitions.withgoogle.com/kickstart/archive/2013)




### 1. [Facebook Hacker Cup](https://www.facebook.com/codingcompetitions/hacker-cup)
- [2021](https://www.facebook.com/codingcompetitions/hacker-cup/2021)
- [2020](https://www.facebook.com/codingcompetitions/hacker-cup/2020)
- [2019](https://www.facebook.com/codingcompetitions/hacker-cup/2019)
- [2018](https://www.facebook.com/codingcompetitions/hacker-cup/2018)
- [2017](https://www.facebook.com/codingcompetitions/hacker-cup/2017)
- [2016](https://www.facebook.com/codingcompetitions/hacker-cup/2016)
- [2015](https://www.facebook.com/codingcompetitions/hacker-cup/2015)
- [2014](https://www.facebook.com/codingcompetitions/hacker-cup/2014)
- [2013](https://www.facebook.com/codingcompetitions/hacker-cup/2013)
- [2012](https://www.facebook.com/codingcompetitions/hacker-cup/2012)
- [2011](https://www.facebook.com/codingcompetitions/hacker-cup/2011)

### 2. [FB Hack](https://www.facebook.com/codingcompetitions/fb-hack)


### 1. [Problems](https://leetcode.com/problemset/all)

### 2. [Contests](https://leetcode.com/contest)
- Weekly Contests
- Biweekly Contests

### 3. [Study Plan](https://leetcode.com/study-plan)
- Comprehensive Study Plans
    - [LeetCode 75](https://leetcode.com/study-plan/leetcode-75)
    - [Data Structure](https://leetcode.com/study-plan/data-structure)
    - [Algorithm](https://leetcode.com/study-plan/algorithm)
- In-Depth Topics
    - [SQL](https://leetcode.com/study-plan/sql)
    - [Programming Skills](https://leetcode.com/study-plan/programming-skills)
    - [Binary Search](https://leetcode.com/study-plan/binary-search)
    - [Graph Theory](https://leetcode.com/study-plan/graph)
    - [Dynamic Programming](https://leetcode.com/study-plan/dynamic-programming)


### 1. [Practice](https://www.codingninjas.com/codestudio/problems)
- [Interview Problem](https://www.codingninjas.com/codestudio/problems)
- [Problem Lists](https://www.codingninjas.com/codestudio/problem-lists)
    - [Lists by Experts](https://www.codingninjas.com/codestudio/problem-lists)
    - [Company-wise Lists](https://www.codingninjas.com/codestudio/problem-lists)
    - [Topic-wise Lists](https://www.codingninjas.com/codestudio/problem-lists)

### 2. [Contests](https://www.codingninjas.com/codestudio/contests)
- [Beginner Contest](https://www.codingninjas.com/codestudio/contests)
- [Weekend Contest](https://www.codingninjas.com/codestudio/contests)
- [Monthly Contest](https://www.codingninjas.com/codestudio/contests)



### 1. [Practice](https://www.interviewbit.com/practice/)
- [Programming](https://www.interviewbit.com/courses/programming)
- [Puzzle](https://www.interviewbit.com/puzzles)
- [Databases](https://www.interviewbit.com/courses/databases)
- [Scripting](https://www.interviewbit.com/courses/shell)
- [Data Science](https://www.interviewbit.com/courses/data-science-and-machine-learning)

### 2. Resources
- [All Problems](https://www.interviewbit.com/coding-interview-questions)
- [Fast Track Courses](https://www.interviewbit.com/courses/fast-track)
    - [Python](https://www.interviewbit.com/courses/fast-track-python)
    - [Java](https://www.interviewbit.com/courses/fast-track-java)
    - [C++](https://www.interviewbit.com/courses/fast-track-cpp)
    - [JavaScript](https://www.interviewbit.com/courses/fast-track-js)
    - [C#](https://www.interviewbit.com/courses/fast-track-csharp)

### 3. [Contests](https://www.interviewbit.com/contests)
- [CodeDrift](https://www.interviewbit.com/contests)
    - Topic Wise
        - [Arrays](https://www.interviewbit.com/contest/code-drift-arrays)
        - [Maths](https://www.interviewbit.com/contest/code-drift-maths)
        - [Binary Search](https://www.interviewbit.com/contest/code-drift-binary-search)
        - [Strings](https://www.interviewbit.com/contest/code-drift-strings)
        - [Bit Manipulation](https://www.interviewbit.com/contest/code-drift-bit-manipulation)
        - [2 Pointers](https://www.interviewbit.com/contest/code-drift-2-pointers)
        - [Linked List + Stacks & Queues](https://www.interviewbit.com/contest/codedrift--linked-list---stacks---queues-7cbf)
        - [Backtracking](https://www.interviewbit.com/contest/codedrift--backtracking)
        - [Hashing](https://www.interviewbit.com/contest/codedrift---hashing)
        - [Heaps and Segment Tree](https://www.interviewbit.com/contest/codedrift-stack---heap)
        - [Binary Trees and Trie](https://www.interviewbit.com/contest/codedrift-binary-trees-and-trie)
        - [Dynamic Programming and Greedy](https://www.interviewbit.com/contest/code-drift--dynamic-programming-and-greedy)
        - [Graphs](https://www.interviewbit.com/contest/codedrift--graphs)
    - Monthly
        - 2021
            - [August](https://www.interviewbit.com/contest/codedrift-2-0-august)
            - [September](https://www.interviewbit.com/contest/Codedrift%20Sept%202021)
        - 2022
            - [January](https://www.interviewbit.com/contest/CodeDriftJanuary)
            - [February](https://www.interviewbit.com/contest/codedrift-feb)
            - March
                - [1.0](https://www.interviewbit.com/contest/codedrift-march-)
                - [2.0](https://www.interviewbit.com/contest/codedrift-march)
            - April
                - [1.0](https://www.interviewbit.com/contest/codedrift-april-1-0)
                - [2.0](https://www.interviewbit.com/contest/codedrift-april-2-0)
            - May
                - [1.0](https://www.interviewbit.com/contest/codedrift-may-1-0)
                - [2.0](https://www.interviewbit.com/contest/codedrift-may-2-0)
            - June
                - [1.0](https://www.interviewbit.com/contest/codedrift-june-2-0)
                - [2.0](https://www.interviewbit.com/contest/codedrift-june-2-0-95ed)
            - July
                - [1.0](https://www.interviewbit.com/contest/ccodedrift-july-1-0)
                - [2.0](https://www.interviewbit.com/contest/ccodedrift-july-2-0)
            - August
                - [1.0](https://www.interviewbit.com/contest/codedrift-august-1-0)
                - [2.0](https://www.interviewbit.com/contest/codedrift-august-2-0)
            - September
                - [1.0](https://www.interviewbit.com/contest/codedrift-september-1-0)
                - [2.0](https://www.interviewbit.com/contest/codedrift-september-2-0)
            - October
                - [1.0](https://www.interviewbit.com/contest/codedrift-october-1-0)
                - [2.0](https://www.interviewbit.com/contest/codedrift-october-2-0)
            - November
                - [1.0](https://www.interviewbit.com/contest/codedrift-november-1-0)
                - [2.0](https://www.interviewbit.com/contest/codedrift-november-2-0)
            - [December](https://www.interviewbit.com/contest/codedrift-december-2022)



### 1. [Google](https://codingcompetitions.withgoogle.com/)
- [ ] [Code Jam](https://codingcompetitions.withgoogle.com/codejam)
- [ ] [Hash Code](https://codingcompetitions.withgoogle.com/hashcode)
- [ ] [Kick Start](https://codingcompetitions.withgoogle.com/kickstart)

### 2. [Facebook](https://www.facebook.com/codingcompetitions)
- [ ] [Facebook Hackercup](https://www.facebook.com/codingcompetitions/hacker-cup)
- [ ] [FB Hack](https://www.facebook.com/codingcompetitions/fb-hack)

### 3. [LeetCode](https://leetcode.com/explore)
- [ ] [Problems](https://leetcode.com/problemset/all)
- [ ] [Contests](https://leetcode.com/contest)
    - [ ] Weekly Contests
    - [ ] Biweekly Contests
- [ ] [Study Plan](https://leetcode.com/study-plan)
    - [ ] Comprehensive Study Plans
        - [ ] [LeetCode 75](https://leetcode.com/study-plan/leetcode-75)
        - [ ] [Data Structure](https://leetcode.com/study-plan/data-structure)
        - [ ] [Algorithm](https://leetcode.com/study-plan/algorithm)
    - [ ] In-Depth Topics
        - [ ] [SQL](https://leetcode.com/study-plan/sql)
        - [ ] [Programming Skills](https://leetcode.com/study-plan/programming-skills)
        - [ ] [Binary Search](https://leetcode.com/study-plan/binary-search)
        - [ ] [Graph Theory](https://leetcode.com/study-plan/graph)
        - [ ] [Dynamic Programming](https://leetcode.com/study-plan/dynamic-programming)

### 4. [Coding Ninjas](https://www.codingninjas.com/codestudio)
- [ ] [Practice](https://www.codingninjas.com/codestudio/problems)
    - [ ] [Interview Problems](https://www.codingninjas.com/codestudio/problems)
    - [ ] [Problem Lists](https://www.codingninjas.com/codestudio/problem-lists)
        - [ ] [Lists by Experts](https://www.codingninjas.com/codestudio/problem-lists)
        - [ ] [Company-wise Lists](https://www.codingninjas.com/codestudio/problem-lists)
        - [ ] [Topic-wise Lists](https://www.codingninjas.com/codestudio/problem-lists)
- [ ] [Contests](https://www.codingninjas.com/codestudio/contests)
    - [ ] [Beginner Contests](https://www.codingninjas.com/codestudio/contests)
    - [ ] [Weekend Contests](https://www.codingninjas.com/codestudio/contests)
    - [ ] [Monthly Contests](https://www.codingninjas.com/codestudio/contests)

### 5. [GeeksforGeeks](https://practice.geeksforgeeks.org/topic-tags)
- [ ] [Problems](https://practice.geeksforgeeks.org/explore)
    - [ ] [Topics](https://practice.geeksforgeeks.org/explore)
        - [ ] [Data Structures](https://practice.geeksforgeeks.org/topic-tags)
        - [ ] [Algorithms](https://practice.geeksforgeeks.org/topic-tags)
    - [ ] [Companies](https://practice.geeksforgeeks.org/explore)
    - [ ] [Curated Lists](https://practice.geeksforgeeks.org/explore)
        - [ ] [Beginner's DSA Sheet](https://practice.geeksforgeeks.org/explore?page=1&curated[]=8&sortBy=submissions&curated_names[]=Beginner%27s%20DSA%20Sheet)
        - [ ] [SDE Sheet](https://practice.geeksforgeeks.org/explore?page=1&curated[]=1&sortBy=submissions&curated_names[]=SDE%20Sheet)
        - [ ] [Top 50 Array Problems](https://practice.geeksforgeeks.org/explore?page=1&curated[]=2&sortBy=submissions&curated_names[]=Top%2050%20Array%20Problems)
        - [ ] [Top 50 String Problems](https://practice.geeksforgeeks.org/explore?page=1&curated[]=3&sortBy=submissions&curated_names[]=Top%2050%20String%20Problems)
        - [ ] [Top 50 DP Problems](https://practice.geeksforgeeks.org/explore?page=1&curated[]=4&sortBy=submissions&curated_names[]=Top%2050%20DP%20Problems)
        - [ ] [Top 50 Graph Problems](https://practice.geeksforgeeks.org/explore?page=1&curated[]=5&sortBy=submissions&curated_names[]=Top%2050%20Graph%20Problems)
        - [ ] [Top 50 Tree Problems](https://practice.geeksforgeeks.org/explore?page=1&curated[]=6&sortBy=submissions&curated_names[]=Top%2050%20Tree%20Problems)
- [ ] [Contests](https://practice.geeksforgeeks.org/events)
    - [ ] [Series](https://practice.geeksforgeeks.org/events)
        - [ ] [Problem of the Day](https://practice.geeksforgeeks.org/problem-of-the-day)
        - [ ] [Interview Series](https://practice.geeksforgeeks.org/events/rec/interview-series)
        - [ ] [Job a Thon](https://practice.geeksforgeeks.org/events/rec/job-a-thon)
        - [ ] [BiWizard School Contest](https://practice.geeksforgeeks.org/events/rec/step-up-coding-school)

### 6. [InterviewBit](https://www.interviewbit.com/practice)
- [ ] [Practice](https://www.interviewbit.com/practice/)
    - [ ] [Programming](https://www.interviewbit.com/courses/programming)
    - [ ] [Puzzle](https://www.interviewbit.com/puzzles)
    - [ ] [Databases](https://www.interviewbit.com/courses/databases)
    - [ ] [Scripting](https://www.interviewbit.com/courses/shell)
    - [ ] [Data Science](https://www.interviewbit.com/courses/data-science-and-machine-learning)
- [ ] Resources
    - [ ] [All Problems](https://www.interviewbit.com/coding-interview-questions)
    - [ ] [Fast Track Courses](https://www.interviewbit.com/courses/fast-track)
        - [ ] [Python](https://www.interviewbit.com/courses/fast-track-python)
        - [ ] [Java](https://www.interviewbit.com/courses/fast-track-java)
        - [ ] [C++](https://www.interviewbit.com/courses/fast-track-cpp)
        - [ ] [JavaScript](https://www.interviewbit.com/courses/fast-track-js)
        - [ ] [C#](https://www.interviewbit.com/courses/fast-track-csharp)
- [ ] [Contests](https://www.interviewbit.com/contests)
    - [ ] [CodeDrift](https://www.interviewbit.com/contests)
        - [ ] Topic Wise
            - [ ] [Arrays](https://www.interviewbit.com/contest/code-drift-arrays)
            - [ ] [Maths](https://www.interviewbit.com/contest/code-drift-maths)
            - [ ] [Binary Search](https://www.interviewbit.com/contest/code-drift-binary-search)
            - [ ] [Strings](https://www.interviewbit.com/contest/code-drift-strings)
            - [ ] [Bit Manipulation](https://www.interviewbit.com/contest/code-drift-bit-manipulation)
            - [ ] [2 Pointers](https://www.interviewbit.com/contest/code-drift-2-pointers)
            - [ ] [Linked List + Stacks & Queues](https://www.interviewbit.com/contest/codedrift--linked-list---stacks---queues-7cbf)
            - [ ] [Backtracking](https://www.interviewbit.com/contest/codedrift--backtracking)
            - [ ] [Hashing](https://www.interviewbit.com/contest/codedrift---hashing)
            - [ ] [Heaps and Segment Tree](https://www.interviewbit.com/contest/codedrift-stack---heap)
            - [ ] [Binary Trees and Trie](https://www.interviewbit.com/contest/codedrift-binary-trees-and-trie)
            - [ ] [Dynamic Programming and Greedy](https://www.interviewbit.com/contest/code-drift--dynamic-programming-and-greedy)
            - [ ] [Graphs](https://www.interviewbit.com/contest/codedrift--graphs)
        - [ ] Monthly
            - [ ] 2021
                - [ ] [August](https://www.interviewbit.com/contest/codedrift-2-0-august)
                - [ ] [September](https://www.interviewbit.com/contest/Codedrift%20Sept%202021)
            - [ ] 2022
                - [ ] [January](https://www.interviewbit.com/contest/CodeDriftJanuary)
                - [ ] [February](https://www.interviewbit.com/contest/codedrift-feb)
                - [ ] March
                    - [ ] [1.0](https://www.interviewbit.com/contest/codedrift-march-)
                    - [ ] [2.0](https://www.interviewbit.com/contest/codedrift-march)
                - [ ] April
                    - [ ] [1.0](https://www.interviewbit.com/contest/codedrift-april-1-0)
                    - [ ] [2.0](https://www.interviewbit.com/contest/codedrift-april-2-0)
                - [ ] May
                    - [ ] [1.0](https://www.interviewbit.com/contest/codedrift-may-1-0)
                    - [ ] [2.0](https://www.interviewbit.com/contest/codedrift-may-2-0)
                - [ ] June
                    - [ ] [1.0](https://www.interviewbit.com/contest/codedrift-june-2-0)
                    - [ ] [2.0](https://www.interviewbit.com/contest/codedrift-june-2-0-95ed)
                - [ ] July
                    - [ ] [1.0](https://www.interviewbit.com/contest/ccodedrift-july-1-0)
                    - [ ] [2.0](https://www.interviewbit.com/contest/ccodedrift-july-2-0)
                - [ ] August
                    - [ ] [1.0](https://www.interviewbit.com/contest/codedrift-august-1-0)
                    - [ ] [2.0](https://www.interviewbit.com/contest/codedrift-august-2-0)
                - [ ] September
                    - [ ] [1.0](https://www.interviewbit.com/contest/codedrift-september-1-0)
                    - [ ] [2.0](https://www.interviewbit.com/contest/codedrift-september-2-0)
                - [ ] October
                    - [ ] [1.0](https://www.interviewbit.com/contest/codedrift-october-1-0)
                    - [ ] [2.0](https://www.interviewbit.com/contest/codedrift-october-2-0)
                - [ ] November
                    - [ ] [1.0](https://www.interviewbit.com/contest/codedrift-november-1-0)
                    - [ ] [2.0](https://www.interviewbit.com/contest/codedrift-november-2-0)
                - [ ] [December](https://www.interviewbit.com/contest/codedrift-december-2022)


### 7. [PrepBytes](https://mycode.prepbytes.com/)
- [ ] [Competitive Coding](https://mycode.prepbytes.com/competitive-coding/practice)
- [ ] [Interview Coding](https://mycode.prepbytes.com/interview-coding/practice)
- [ ] [Company Coding](https://mycode.prepbytes.com/company-questions)

### 8. [Work@Tech](https://workat.tech/practice)
- [ ] [Data Structures & Algorithms](https://workat.tech/problem-solving/practice)
    - [ ] [Topics](https://workat.tech/problem-solving/practice/topics)
    - [ ] [Companies](https://workat.tech/problem-solving/practice/companies)
    - [ ] [List](https://workat.tech/problem-solving/practice/lists)
- [ ] [Machine Coding](https://workat.tech/machine-coding/practice)

### 9. [CodeSignal](https://app.codesignal.com)
- [ ] [Arcade](https://binarysearch.com/problems?order=id)
    - [ ] [Intro](https://app.codesignal.com/arcade/intro)
    - [ ] [The Core](https://app.codesignal.com/arcade/code-arcade)
    - [ ] [Databases](https://app.codesignal.com/arcade/db)
    - [ ] [Python](https://app.codesignal.com/arcade/python-arcade)
    - [ ] [Graphs](https://app.codesignal.com/arcade/graphs-arcade)
- [ ] [Interview Practice](https://app.codesignal.com/interview-practice)
    - [ ] [Data Structures](https://app.codesignal.com/interview-practice)
    - [ ] [Sorting & Searching](https://app.codesignal.com/interview-practice)
    - [ ] [Dynamic Programming](https://app.codesignal.com/interview-practice)
    - [ ] [Special Topics](https://app.codesignal.com/interview-practice)
    - [ ] [Math](https://app.codesignal.com/interview-practice)
- [ ] [Challenges](https://app.codesignal.com/challenges/page/1)
    - [ ] [Algorithmic](https://app.codesignal.com/challenges/page/1)
        - [ ] Easy
        - [ ] Medium
        - [ ] Hard
    - [ ] [Frontend](https://app.codesignal.com/challenges/page/1)
        - [ ] Easy
        - [ ] Medium
        - [ ] Hard
    - [ ] [Database](https://app.codesignal.com/challenges/page/1)
        - [ ] Easy
        - [ ] Medium
        - [ ] Hard
    - [ ] [DevOps](https://app.codesignal.com/challenges/page/1)
        - [ ] Easy
        - [ ] Medium
        - [ ] Hard
- [ ] [Company Challenges](https://app.codesignal.com/company-challenges)

### 10. [HackerRank](https://www.hackerrank.com/)
- [ ] [Prepare](https://www.hackerrank.com/dashboard)
    - [ ] [Prepare By Topics](https://www.hackerrank.com/dashboard)
        - [ ] [C](https://www.hackerrank.com/domains/c)
        - [ ] [C++](https://www.hackerrank.com/domains/cpp)
        - [ ] [Python](https://www.hackerrank.com/domains/python)
        - [ ] [Java](https://www.hackerrank.com/domains/java)
        - [ ] [SQL](https://www.hackerrank.com/domains/sql)
        - [ ] [Databases](https://www.hackerrank.com/domains/databases)
        - [ ] [Mathematics](https://www.hackerrank.com/domains/mathematics)
        - [ ] Problem Solving
            - [ ] [Data Structures](https://www.hackerrank.com/domains/data-structures)
            - [ ] [Algorithms](https://www.hackerrank.com/domains/algorithms)
    - [ ] [Tutorials](https://www.hackerrank.com/domains/tutorials)
        - [ ] [30 Days of Code](https://www.hackerrank.com/domains/tutorials/30-days-of-code)
        - [ ] [10 Days of Statistics](https://www.hackerrank.com/domains/tutorials/10-days-of-statistics)
        - [ ] [10 Days of JavaScript](https://www.hackerrank.com/domains/tutorials/10-days-of-javascript)
    - [ ] [Preparation Kits](https://www.hackerrank.com/interview/preparation-kits)
        - [ ] [1 Week Preparation Kit](https://www.hackerrank.com/interview/preparation-kits/one-week-preparation-kit/one-week-day-one)
        - [ ] [1 Month Preparation Kit](https://www.hackerrank.com/interview/preparation-kits/one-month-preparation-kit/one-month-week-one/challenges)
        - [ ] [3 Months Preparation Kit](https://www.hackerrank.com/interview/preparation-kits/three-month-preparation-kit/three-month-week-one/challenges)
    - [ ] [Interview Preparation](https://www.hackerrank.com/interview/interview-preparation-kit)
        - [ ] [Warm-up Challenges](https://www.hackerrank.com/interview/interview-preparation-kit/warmup/challenges)
        - [ ] [Miscellaneous](https://www.hackerrank.com/interview/interview-preparation-kit/miscellaneous/challenges)
        - [ ] [Arrays](https://www.hackerrank.com/interview/interview-preparation-kit/arrays/challenges)
        - [ ] [Search](https://www.hackerrank.com/interview/interview-preparation-kit/search/challenges)
        - [ ] [Sorting](https://www.hackerrank.com/interview/interview-preparation-kit/sorting/challenges)
        - [ ] [String Manipulation](https://www.hackerrank.com/interview/interview-preparation-kit/strings/challenges)
        - [ ] [Dictionaries and Hashmaps](https://www.hackerrank.com/interview/interview-preparation-kit/dictionaries-hashmaps/challenges)
        - [ ] [Recursion and Backtracking](https://www.hackerrank.com/interview/interview-preparation-kit/recursion-backtracking/challenges)
        - [ ] [Linked Lists](https://www.hackerrank.com/interview/interview-preparation-kit/linked-lists/challenges)
        - [ ] [Stacks and Queues](https://www.hackerrank.com/interview/interview-preparation-kit/stacks-queues/challenges)
        - [ ] [Dynamic Programming](https://www.hackerrank.com/interview/interview-preparation-kit/dynamic-programming/challenges)
        - [ ] [Greedy Algorithms](https://www.hackerrank.com/interview/interview-preparation-kit/greedy-algorithms/challenges)
        - [ ] [Trees](https://www.hackerrank.com/interview/interview-preparation-kit/trees/challenges)
        - [ ] [Graphs](https://www.hackerrank.com/interview/interview-preparation-kit/graphs/challenges)
- [ ] [Compete](https://www.hackerrank.com/contests)
    - [ ] [ProjectEuler+](https://www.hackerrank.com/contests/projecteuler/challenges)

### 11. [HackerEarth](https://www.hackerearth.com/)
- [ ] [Practice](https://www.hackerearth.com/practice)
    - [ ] [All Problems](https://www.hackerearth.com/practice/problems)
    - [ ] [Basic Programming](https://www.hackerearth.com/practice/basic-programming)
        - [ ] [Input/Output](https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems)
        - [ ] Complexity Analysis
        - [ ] [Implementation](https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems)
        - [ ] [Operators](https://www.hackerearth.com/practice/basic-programming/operators/basics-of-operators/practice-problems)
        - [ ] [Bit Manipulation](https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems)
        - [ ] [Recursion](https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/practice-problems)
    - [ ] [Data Structure](https://www.hackerearth.com/practice/data-structures)
        - [ ] [Arrays](https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems)
        - [ ] [Stacks](https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems)
        - [ ] [Queues](https://www.hackerearth.com/practice/data-structures/queues/basics-of-queues/practice-problems)
        - [ ] [Hash Tables](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems)
        - [ ] [Linked List](https://www.hackerearth.com/practice/data-structures/linked-list/singly-linked-list/practice-problems)
        - [ ] [Trees](https://www.hackerearth.com/practice/data-structures/trees/binary-and-nary-trees/practice-problems)
        - [ ] [Advanced Data Structures](https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/practice-problems)
        - [ ] [Disjoint Data Structures](https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/practice-problems)
    - [ ] [Algorithms](https://www.hackerearth.com/practice/algorithms)
        - [ ] [Searching](https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems)
        - [ ] [Sorting](https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/practice-problems)
        - [ ] [Greedy Algorithms](https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems)
        - [ ] [Graphs](https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems)
        - [ ] [String Algorithms](https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems)
        - [ ] [Dynamic Programming](https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems)
    - [ ] [Math](https://www.hackerearth.com/practice/math)
        - [ ] [Number Theory](https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/practice-problems)
        - [ ] [Combinatorics](https://www.hackerearth.com/practice/math/combinatorics/basics-of-combinatorics/practice-problems)
        - [ ] [Geometry](https://www.hackerearth.com/practice/math/geometry/line-sweep-technique/practice-problems)
    - [ ] [Codemonk](https://www.hackerearth.com/practice/codemonk)
- [ ] [Compete](https://www.hackerearth.com/challenges)

### 12. [CodeChef](https://www.codechef.com/)
- [ ] [Learn](https://www.codechef.com/selflearning)
    - [ ] Rating Based
        - [ ] [Level UP - 0 Star to 1 Star](https://www.codechef.com/selflearning/0to1stars)
        - [ ] [Level UP - 1 Star to 2 Star](https://www.codechef.com/selflearning/1to2stars)
        - [ ] [Level UP - 2 Star to 3 Star](https://www.codechef.com/selflearning/2to3stars)
        - [ ] [Level UP - 3 Star to 4 Star](https://www.codechef.com/selflearning/3to4stars)
    - [ ] Competition
        - [ ] [Past ZCO Problems](https://www.codechef.com/ZCOPRAC)
        - [ ] [Past INOI Problems](https://www.codechef.com/INOIPRAC)
    - [ ] Interview Preparation
        - [ ] [DSA Concepts](https://www.codechef.com/selflearning/interviewprep)
        - [ ] [Company Specific](https://www.codechef.com/selflearning/interviewprep/companies)
    - [ ] Practice Topic
        - [ ] Basic Programming
        - [ ] Arrays
        - [ ] Strings
        - [ ] Math
        - [ ] String
        - [ ] Binary Search
        - [ ] Data Structures
        - [ ] Greedy Algorithms
        - [ ] Dynamic Programming
        - [ ] Graphs
        - [ ] Segment Trees
- [ ] [Practice](https://www.codechef.com/practice)
    - [ ] Difficulty Rating
        - [ ] [0 - 1000: Beginner Level](https://www.codechef.com/practice?end_rating=999&group=all&hints=0&limit=20&page=0&search=&sort_by=difficulty_rating&sort_order=asc&start_rating=0&tags=&topic=&video_editorial=0&wa_enabled=0)
        - [ ] [1000 - 1200: 1* Beginner Level](https://www.codechef.com/practice?end_rating=1199&group=all&hints=0&limit=20&page=0&search=&sort_by=difficulty_rating&sort_order=asc&start_rating=1000&tags=&topic=&video_editorial=0&wa_enabled=0)
        - [ ] [1200 - 1400: 1* Advanced Level](https://www.codechef.com/practice?end_rating=1399&group=all&hints=0&limit=20&page=0&search=&sort_by=difficulty_rating&sort_order=asc&start_rating=1200&tags=&topic=&video_editorial=0&wa_enabled=0)
        - [ ] [1400 - 1500: 2* Beginner Level](https://www.codechef.com/practice?end_rating=1499&group=all&hints=0&limit=20&page=0&search=&sort_by=difficulty_rating&sort_order=asc&start_rating=1400&tags=&topic=&video_editorial=0&wa_enabled=0)
        - [ ] [1500 - 1600: 2* Advanced Level](https://www.codechef.com/practice?end_rating=1599&group=all&hints=0&limit=20&page=0&search=&sort_by=difficulty_rating&sort_order=asc&start_rating=1500&tags=&topic=&video_editorial=0&wa_enabled=0)
        - [ ] [1600 - 1700: 3* Beginner Level](https://www.codechef.com/practice?end_rating=1699&group=all&hints=0&limit=20&page=0&search=&sort_by=difficulty_rating&sort_order=asc&start_rating=1600&tags=&topic=&video_editorial=0&wa_enabled=0)
        - [ ] [1700 - 1800: 3* Advanced Level](https://www.codechef.com/practice?end_rating=1799&group=all&hints=0&limit=20&page=0&search=&sort_by=difficulty_rating&sort_order=asc&start_rating=1700&tags=&topic=&video_editorial=0&wa_enabled=0)
        - [ ] [1800 - 2000: 4* Level](https://www.codechef.com/practice?end_rating=1999&group=all&hints=0&limit=20&page=0&search=&sort_by=difficulty_rating&sort_order=asc&start_rating=1800&tags=&topic=&video_editorial=0&wa_enabled=0)
        - [ ] [2000 - 2200: 5* Level](https://www.codechef.com/practice?end_rating=2199&group=all&hints=0&limit=20&page=0&search=&sort_by=difficulty_rating&sort_order=asc&start_rating=2000&tags=&topic=&video_editorial=0&wa_enabled=0)
        - [ ] [2200 - 2500: 6* Level](https://www.codechef.com/practice?end_rating=2499&group=all&hints=0&limit=20&page=0&search=&sort_by=difficulty_rating&sort_order=asc&start_rating=2200&tags=&topic=&video_editorial=0&wa_enabled=0)
        - [ ] [2500 - 5001: 7* Level](https://www.codechef.com/practice?end_rating=5000&group=all&hints=0&limit=20&page=0&search=&sort_by=difficulty_rating&sort_order=asc&start_rating=2500&tags=&topic=&video_editorial=0&wa_enabled=0)
    - [ ] Topics
        - [ ] [Basic Programming](https://www.codechef.com/practice?end_rating=5000&group=all&hints=0&limit=20&page=0&search=&sort_by=difficulty_rating&sort_order=asc&start_rating=0&tags=&topic=Basic%20Programming&video_editorial=0&wa_enabled=0)
        - [ ] [Arrays](https://www.codechef.com/practice?end_rating=5000&group=all&hints=0&limit=20&page=0&search=&sort_by=difficulty_rating&sort_order=asc&start_rating=0&tags=&topic=Arrays&video_editorial=0&wa_enabled=0)
        - [ ] [Strings](https://www.codechef.com/practice?end_rating=5000&group=all&hints=0&limit=20&page=0&search=&sort_by=difficulty_rating&sort_order=asc&start_rating=0&tags=&topic=Strings&video_editorial=0&wa_enabled=0)
        - [ ] [Math](https://www.codechef.com/practice?end_rating=5000&group=all&hints=0&limit=20&page=0&search=&sort_by=difficulty_rating&sort_order=asc&start_rating=0&tags=&topic=Math&video_editorial=0&wa_enabled=0)
        - [ ] [String](https://www.codechef.com/practice?end_rating=5000&group=all&hints=0&limit=20&page=0&search=&sort_by=difficulty_rating&sort_order=asc&start_rating=0&tags=&topic=Sorting&video_editorial=0&wa_enabled=0)
        - [ ] [Binary Search](https://www.codechef.com/practice?end_rating=5000&group=all&hints=0&limit=20&page=0&search=&sort_by=difficulty_rating&sort_order=asc&start_rating=0&tags=&topic=Binary%20Search&video_editorial=0&wa_enabled=0)
        - [ ] [Data Structures](https://www.codechef.com/practice?end_rating=5000&group=all&hints=0&limit=20&page=0&search=&sort_by=difficulty_rating&sort_order=asc&start_rating=0&tags=&topic=Data%20Structures&video_editorial=0&wa_enabled=0)
        - [ ] [Greedy Algorithms](https://www.codechef.com/practice?end_rating=5000&group=all&hints=0&limit=20&page=0&search=&sort_by=difficulty_rating&sort_order=asc&start_rating=0&tags=&topic=Greedy%20Algorithms&video_editorial=0&wa_enabled=0)
        - [ ] [Dynamic Programming](https://www.codechef.com/practice?end_rating=5000&group=all&hints=0&limit=20&page=0&search=&sort_by=difficulty_rating&sort_order=asc&start_rating=0&tags=&topic=Dynamic%20Programming&video_editorial=0&wa_enabled=0)
        - [ ] [Graphs](https://www.codechef.com/practice?end_rating=5000&group=all&hints=0&limit=20&page=0&search=&sort_by=difficulty_rating&sort_order=asc&start_rating=0&tags=&topic=Graphs&video_editorial=0&wa_enabled=0)
        - [ ] [Segment Trees](https://www.codechef.com/practice?end_rating=5000&group=all&hints=0&limit=20&page=0&search=&sort_by=difficulty_rating&sort_order=asc&start_rating=0&tags=&topic=Segment%20Trees&video_editorial=0&wa_enabled=0)
- [ ] [Compete](https://www.codechef.com/contests/?itm_medium=navmenu&itm_campaign=allcontests_head)
    - [ ] [Long Challenge](https://www.codechef.com/contests/?itm_medium=navmenu&itm_campaign=allcontests#past-contests)
    - [ ] [Cook-off](https://www.codechef.com/contests/?itm_medium=navmenu&itm_campaign=allcontests#past-contests)
    - [ ] [Lunch Time](https://www.codechef.com/contests/?itm_medium=navmenu&itm_campaign=allcontests#past-contests)
    - [ ] [Starters](https://www.codechef.com/contests/?itm_medium=navmenu&itm_campaign=allcontests#past-contests)

### 13. [CodeForces](https://codeforces.com/)
- [ ] [Problem Set](https://codeforces.com/problemset)
- [ ] [Contests](https://codeforces.com/contests)

### 14. [AtCoder](https://atcoder.jp/)
- [ ] [Contest](https://atcoder.jp/contests/)

### 15. [Sphere Online Judge (SPOJ)](https://www.spoj.com/)
- [ ] [Problems](https://www.spoj.com/problems/)
- [ ] [Contests](https://www.spoj.com/contests/)

### 16. [LightOJ](https://lightoj.com)
- [ ] [Problems](https://lightoj.com/problems/category)
- [ ] [Compete](https://lightoj.com/contests)

### 17. [Toph](https://toph.co)
- [ ] [Problems](https://toph.co/problems)
- [ ] [Contests](https://toph.co/contests/all)

### 18. [Australian  Maths Trust (AMT)](https://orac.amt.edu.au/cgi-bin/train/hub.pl)

### 19. [CSES](https://cses.fi/)
- [ ] [CSES Problem Set](https://cses.fi/problemset/)
- [ ] [BOI Contest Collection](https://cses.fi/boi/list/)
- [ ] [CEOI Contest Collection](https://cses.fi/ceoi/list/)



# Happy learning  & please give a star ⭐  
![image](https://assets.leetcode.com/users/images/5cfe8444-30cf-4882-a87c-54ef5f5820c5_1687108029.48085.gif)
