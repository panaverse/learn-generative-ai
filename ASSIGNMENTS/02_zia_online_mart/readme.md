# Project Assignment: Online Imtiaz Mart API Using Event-Driven Microservices Architecture

## Project Overview

This project aims to develop an online mart API using an event-driven microservices architecture. The API will leverage various technologies such as FastAPI, Docker, Dapr, DevContainers, Docker Compose, PostgreSQL, Kafka, Protocol Buffers (Protobuf), and Kong for API gateway management. It will use Azure Container Apps (ACA) for deployment, and GitHub Actions for CI/CD. The goal is to create a scalable, maintainable, and efficient system that handles high volumes of transactions and data in a distributed manner.

Additionally, Test-Driven Development (TDD) and Behavior-Driven Development (BDD) practices will be incorporated to ensure high code quality and alignment with business requirements.


## Objectives

- **Develop a scalable and efficient API** for an online mart using microservices.
- **Implement an event-driven architecture** to handle asynchronous communication between services.
- **Utilize modern technologies** such as FastAPI for API development, Docker for containerization, and Kafka for event streaming.
- **Ensure smooth development and deployment** using DevContainers and Docker Compose.
- **Manage and route API requests** through Kong API Gateway.
- **Use Protocol Buffers (Protobuf)** for efficient data serialization.
- **Persist data** using PostgreSQL.
- **Incorporate TDD and BDD** to enhance code quality and ensure the application meets business requirements.

## Technologies

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **Docker**: For containerizing the microservices, ensuring consistency across different environments.
- **Dapr**: Dapr stands for distributed application runtime. It is a self-hosted, open-source project that offers extra functionality to cloud-native applications through APIs, called building blocks, that simplify microservice connectivity. 
- **DevContainers**: To provide a consistent development environment.
- **Docker Compose**: For orchestrating multi-container Docker applications.
- **PostgreSQL**: A powerful, open-source relational database system.
- **SQLModel**: For interacting with the PostgreSQL database using Python.
- **Kafka**: A distributed event streaming platform for building real-time data pipelines and streaming applications.
- **Protocol Buffers (Protobuf)**: A method developed by Google for serializing structured data, similar to XML or JSON but smaller, faster, and simpler.
- **Kong**: An open-source API Gateway and Microservices Management Layer.
- **Github Actions**: For CI/CD pipeline.
- **Pytest**: For unit testing and TDD.
- **Behave**: For BDD.
- **Azure Container Apps**: For Cloud Deployment
- **Github Actions**: For CI/CD

## Architecture

### Microservices

1. **User Service**: Manages user authentication, registration, and profiles.
2. **Product Service**: Manages product catalog, including CRUD operations for products.
3. **Order Service**: Handles order creation, updating, and tracking.
4. **Inventory Service**: Manages stock levels and inventory updates.
5. **Notification Service**: Sends notifications (email, SMS) to users about order statuses and other updates.
6. **Payment Service**: Processes payments and manages transaction records.

Note: We will use Pay Fast for Local Payment System. https://gopayfast.com/ And Stripe for international payments.

### Event-Driven Communication

- **Kafka**: Acts as the event bus, facilitating communication between microservices. Each service can produce and consume messages (events) such as user registration, order placement, and inventory updates.
- **Protobuf**: Used for defining the structure of messages exchanged between services, ensuring efficient and compact serialization.

### Data Storage

- **PostgreSQL**: Each microservice with data persistence needs will have its own PostgreSQL database instance, following the database-per-service pattern.

### API Gateway

- **Kong**: Manages API request routing, authentication, rate limiting, and other cross-cutting concerns.

## Development Environment

- **DevContainers**: Provide consistent development environments using VSCode DevContainers, ensuring that all team members work in identical environments.
- **Docker Compose**: Orchestrates the various microservices and dependencies (PostgreSQL, Kafka, etc.) during development and testing.

## Development Methodologies

**Test-Driven Development (TDD)**:

TDD involves writing tests before writing the actual code. This ensures that the code meets the required functionality and helps prevent bugs. In this project, Pytest will be used for unit testing.

**Behavior-Driven Development (BDD)**:

BDD extends TDD by writing test cases in a natural language that non-programmers can read. This ensures that the software development process aligns closely with business requirements. In this project, Behave will be used for BDD.

As mentioned above, Behavior-driven development is an extension of Test-driven development (TDD) that emphasizes collaboration among project stakeholders. Behave operates on the principle of scenarios, which are written in a natural language that non-programmers can understand. These scenarios describe how a feature should work from the end user’s perspective.

**Behave** is a BDD framework for Python that follows the principles of writing tests in a human-readable format. It uses Gherkin language to describe software behaviors without detailing how that functionality is implemented.

**Key Features of Behave**

- **Gherkin Language**: Enables the definition of application behavior in natural language, which stakeholders can easily understand.
- **Scenario Outline**: Facilitates data-driven tests, allowing the same scenario to be run multiple times with different data sets.
- **Hooks**: Offers setup and teardown operations for scenarios or features, improving test management.

## Implementation Plan

### Phase 1: Setup and Initial Development

1. **Setup Development Environment**
   - Configure DevContainers with necessary dependencies and tools.
   - Create Docker Compose file for orchestrating services and dependencies.

2.  **Develop Microservices with TDD**

	- Implement the User Service, Product Service, Order Service, Payment Service, and Notification Service using FastAPI and SQLModel.
	- Write unit tests using Pytest before writing the actual code.
	- Containerize each microservice using Docker.

3. **Setup Kafka and Protobuf**
   - Configure Kafka for event streaming.
   - Define Protobuf schemas for messages exchanged between services.

4. **Write BDD Scenarios**
    - Define user stories and acceptance criteria.
	- Write BDD scenarios in Gherkin language using Behave.
	- Implement step definitions to automate the BDD scenarios.

5. **Testing**
    - Ensure all unit tests and BDD scenarios pass.
	- Use Docker Compose to run the entire application locally for integration testing.



### Phase 2: Expand Functionality

1. **Develop Additional Microservices**
   - Inventory Service: Manage stock levels and inventory updates.
   - Notification Service: Send notifications about order statuses and other events.
   - Payment Service: Process payments and manage transactions.

2. **Integrate Event-Driven Communication**
   - Ensure all services can produce and consume relevant Kafka messages.
   - Use Protobuf for message serialization.

### Phase 3: Implement API Gateway and Finalize

1. **Setup Kong API Gateway**
   - Configure Kong for routing, authentication, and rate limiting.
   - Create routes for each microservice.

2. **Testing and Quality Assurance**
   - Write unit, integration, and end-to-end tests for all services.
   - Perform load testing to ensure scalability and performance.

3. **Deployment**

Azure Container Apps (Using Dapr and Keda)

https://azure.microsoft.com/en-us/products/container-apps

Get started with the free tier: The first 180,000 vCPU per second, 360,000 GiB/s, and 2 million requests each month are free.

Watch: https://www.youtube.com/watch?v=0HwQfsa03K8

Deploy: https://learn.microsoft.com/en-us/azure/container-apps/code-to-cloud-options

Azure Container Registry

https://azure.microsoft.com/en-us/products/container-registry/

Deploy to Azure Container Apps with GitHub Actions

https://learn.microsoft.com/en-us/azure/container-apps/github-actions


### Phase 4: Monitoring and Continues Delivery (Optional)

1. **Implement Monitoring and Logging**
   - Set up monitoring tools (e.g., Prometheus, Grafana) to track service health and performance.
   - Implement centralized logging for troubleshooting and analysis.

2. **Continuous Delivery with GitHub Actions (Options)**
   - Use Github Actions to continuesly deliver code for deployment to the the cloud. 
   Using GitHub Actions in your Online Mart API project can greatly enhance your development workflow by automating building, testing, and deployment processes. This not only saves time but also ensures consistency and reliability in your deployment pipeline. Below is a comprehensive conclusion to the setup:

- **Consistency and Reliability**
   - Automated workflows ensure that every code change is consistently built, tested, and deployed, reducing the risk of human error.

- **Early Error Detection**
   - Running tests on every push helps detect issues early in the development process, making it easier to fix bugs before they reach production.

- **Scalability**
   - Automated workflows can handle multiple microservices and scale with your project. As your application grows, you can easily add more workflows for additional services.

- **Efficiency**
   - Automating the build and deployment process reduces the time developers spend on manual tasks, allowing them to focus on writing code and developing features.

- **Integration with Other Tools**
   - GitHub Actions integrates well with other tools and services, such as container registries.Do


## Points to Note

1. Use Dapr for interservices and Kafka messaging.
2. Use SQLModel to communicate with Postgres Database.
3. Docker Compose up should also create Dapr sidecar for each microservice.
4. Use Azure Container Apps (ACA) to deploy on each git commit using Github Actions.
5. When deploying to ACA we should run all tests and only deploy if all the tests have passed.

## Conclusion

This project aims to create a robust, scalable, and efficient online mart API using an event-driven microservices architecture. By leveraging modern technologies such as FastAPI, Docker, Kafka, Protobuf, and Kong, we ensure a high-performance and maintainable system capable of handling large-scale operations. The development will follow a phased approach, ensuring thorough testing, quality assurance, and continuous improvement.

