# Representing State

## What are state diagrams?

State diagrams, also known as state machine diagrams or state charts, are a type of behavioral diagram used in software and systems engineering to represent the states of an object or an interaction and the transitions between these states. They are part of the Unified Modeling Language (UML) and are particularly useful for modeling the behavior of reactive systems, where the system responds to external or internal events.

Here are the key components of a state diagram:

1. **States**: These represent the various conditions or situations an object can be in during its lifecycle. States are usually depicted as rounded rectangles.

2. **Transitions**: These are the arrows that connect states, representing the change from one state to another in response to events. Transitions can include conditions that must be met for the transition to occur.

3. **Events**: These trigger transitions. An event can be an action performed by the user, a message received from another object, or an internal event within the system.

4. **Initial State**: Represented by a filled black circle, it indicates the starting point of the state machine.

5. **Final State**: Represented by a circle with a dot inside, it indicates the end of the state machine's lifecycle.

6. **Actions**: These are activities that occur in response to an event, often linked with transitions or states. Actions can include entry actions (executed when entering a state), exit actions (executed when exiting a state), and activities (ongoing actions while in a state).

### Example of a State Diagram

Imagine a simple state diagram for a turnstile, a gate that allows one person to pass at a time. The states could include:

- **Locked**: The turnstile is locked, and no one can pass through.
- **Unlocked**: The turnstile is unlocked, and one person can pass through.

Transitions between these states could be:

- **Coin Inserted**: When a coin is inserted, the turnstile moves from the Locked state to the Unlocked state.
- **Person Passed**: When a person passes through, the turnstile moves from the Unlocked state back to the Locked state.

Here's a simple textual representation:

1. Initial State: Locked
2. Locked -> (Coin Inserted) -> Unlocked
3. Unlocked -> (Person Passed) -> Locked

### Uses of State Diagrams

State diagrams are used in various fields such as:

- **Software Engineering**: To model the behavior of classes and objects in object-oriented design.
- **Systems Engineering**: To represent the states and transitions of systems and subsystems.
- **Workflow Design**: To illustrate the flow of activities in business processes.
- **User Interface Design**: To map out the states of user interfaces and their responses to user inputs.

By providing a clear visual representation of the states and transitions, state diagrams help in understanding, designing, and documenting the dynamic behavior of systems.

## Is there any standard to represent them in textual representation?

Yes, there are several standardized notations and textual representations for state diagrams, which help ensure clarity and consistency. One common approach is using Statechart XML (SCXML), a standardized markup language recommended by the World Wide Web Consortium (W3C). However, simpler textual notations are also widely used in various documentation and discussions.

### Simplified Textual Notation

A simplified textual notation might use the following structure:

1. **States**: Listed with a label.
2. **Transitions**: Indicated by arrows (->) between states, with events and conditions specified.

Here’s an example of a simple textual representation for a turnstile:

```
State Diagram: Turnstile

States:
  - Locked
  - Unlocked

Transitions:
  - Locked -> Unlocked [Coin Inserted]
  - Unlocked -> Locked [Person Passed]

Initial State: Locked
Final State: None (cyclic process)
```

### SCXML (State Chart XML)

SCXML provides a more formalized way to define state machines. It uses XML to specify states, transitions, events, and actions. Here’s an example of how the turnstile state machine might look in SCXML:

```xml
<scxml initial="locked" version="1.0"
       xmlns="http://www.w3.org/2005/07/scxml">

  <state id="locked">
    <transition event="coinInserted" target="unlocked"/>
  </state>

  <state id="unlocked">
    <transition event="personPassed" target="locked"/>
  </state>

</scxml>
```

### Other Textual Representations

Various other tools and methodologies use their own notations. For instance, in the context of programming, state machines might be defined in comments or configuration files using custom textual formats.

### Example in Pseudo-Code

Here’s another way to represent a state machine in pseudo-code:

```plaintext
state_machine Turnstile {
  state Locked {
    on coinInserted -> Unlocked
  }
  
  state Unlocked {
    on personPassed -> Locked
  }
  
  initial Locked
}
```

### Example Using UML's textual syntax

The Unified Modeling Language (UML) also has a textual syntax for state machines, though it’s less commonly used than the graphical representation:

```plaintext
statechart Turnstile {
  state Locked {
    on entry: do / lockTurnstile()
    transition CoinInserted -> Unlocked
  }
  
  state Unlocked {
    on entry: do / unlockTurnstile()
    transition PersonPassed -> Locked
  }

  initial Locked
}
```

These textual representations provide different levels of detail and formality, making them suitable for various contexts, from simple documentation to formal specifications.

## If i want to communicate to a LLM a state diagram which is the best way to do it in the prompt

When communicating a state diagram to a Large Language Model (LLM) in a prompt, clarity and structure are essential. The best approach is to use a standardized and structured textual format that the LLM can easily parse and understand. Here’s a recommended approach:

1. **Define the States Clearly**: List all the states with unique identifiers.
2. **Specify the Initial State**: Clearly state which state is the initial one.
3. **Describe the Transitions**: Detail each transition, specifying the event that triggers it and the source and target states.
4. **Use a Consistent and Clear Format**: Ensure that the format is consistent throughout to avoid confusion.

### Example of a Structured Prompt

Here is an example prompt that describes a state diagram for a turnstile:

```plaintext
State Diagram: Turnstile

Initial State:
  - Locked

States:
  1. Locked
  2. Unlocked

Transitions:
  - Locked -> Unlocked [Event: Coin Inserted]
  - Unlocked -> Locked [Event: Person Passed]

Description:
1. The initial state of the turnstile is Locked.
2. In the Locked state, when the event 'Coin Inserted' occurs, the turnstile transitions to the Unlocked state.
3. In the Unlocked state, when the event 'Person Passed' occurs, the turnstile transitions back to the Locked state.
```

### Example with SCXML Format

Using the SCXML format can also be effective for its structure and standardization:

```plaintext
<scxml initial="locked" version="1.0"
       xmlns="http://www.w3.org/2005/07/scxml">

  <state id="locked">
    <transition event="coinInserted" target="unlocked"/>
  </state>

  <state id="unlocked">
    <transition event="personPassed" target="locked"/>
  </state>

</scxml>
```

### Example in Pseudo-Code

A simpler pseudo-code format can also work well:

```plaintext
State Machine: Turnstile

Initial State: Locked

States:
  - Locked
  - Unlocked

Transitions:
  - Locked -> Unlocked [Event: Coin Inserted]
  - Unlocked -> Locked [Event: Person Passed]
```

### General Tips

- **Be Explicit**: Clearly define all elements of the state machine, including states, transitions, and events.
- **Use Clear Labels**: Ensure that states and events are labeled in a way that minimizes ambiguity.
- **Structure Information**: Use bullet points, indentation, or other formatting tools to clearly delineate different parts of the state machine.

By using a clear, structured, and consistent format, you can effectively communicate the details of a state diagram to a Large Language Model.

## How do i tell LLM which API to call in which state?

Communicating the state of a system to a client, including an LLM, through a REST API can be effectively done by structuring your API responses to include state information. Here’s a step-by-step approach to achieve this:

### 1. **Define the API Endpoints**

Create endpoints that will allow the client to query the current state and trigger state transitions. For example, you might have endpoints like `/state`, `/transition`, and specific endpoints for actions like `/insert-coin` or `/pass-person`.

### 2. **Include State Information in Responses**

Ensure that your API responses include clear information about the current state, available actions, and any relevant metadata. Use standard HTTP response codes and JSON to structure the responses.

### 3. **Designing the API Endpoints**

#### **Get Current State**

An endpoint to get the current state of the system.

```http
GET /api/turnstile/state
```

**Response:**
```json
{
  "state": "locked",
  "available_actions": ["insert_coin"],
  "metadata": {
    "turnstileId": 123,
    "location": "Main Entrance"
  }
}
```

#### **Transition State Based on an Action**

An endpoint to perform an action that may result in a state transition.

```http
POST /api/turnstile/insert-coin
```

**Response:**
```json
{
  "state": "unlocked",
  "message": "Coin inserted successfully, turnstile is now unlocked.",
  "available_actions": ["pass_person"],
  "metadata": {
    "turnstileId": 123,
    "location": "Main Entrance"
  }
}
```

### 4. **Using Hypermedia (HATEOAS)**

HATEOAS (Hypermedia as the Engine of Application State) can be used to provide links to available actions directly in the API responses, guiding the client on the next possible actions.

#### **Example of HATEOAS in Response**

```json
{
  "state": "locked",
  "links": {
    "self": { "href": "/api/turnstile/state" },
    "insert_coin": { "href": "/api/turnstile/insert-coin" }
  },
  "metadata": {
    "turnstileId": 123,
    "location": "Main Entrance"
  }
}
```

### 5. **Documenting the API**

Provide clear documentation for the API endpoints, including the state transitions and the expected request and response formats. This documentation can be part of your API specification (e.g., using OpenAPI/Swagger).

### Example OpenAPI Specification

```yaml
openapi: 3.0.0
info:
  title: Turnstile API
  version: 1.0.0

paths:
  /api/turnstile/state:
    get:
      summary: Get current state of the turnstile
      responses:
        '200':
          description: Current state
          content:
            application/json:
              schema:
                type: object
                properties:
                  state:
                    type: string
                  available_actions:
                    type: array
                    items:
                      type: string
                  metadata:
                    type: object
                    properties:
                      turnstileId:
                        type: integer
                      location:
                        type: string

  /api/turnstile/insert-coin:
    post:
      summary: Insert coin to unlock the turnstile
      responses:
        '200':
          description: State after inserting coin
          content:
            application/json:
              schema:
                type: object
                properties:
                  state:
                    type: string
                  message:
                    type: string
                  available_actions:
                    type: array
                    items:
                      type: string
                  metadata:
                    type: object
                    properties:
                      turnstileId:
                        type: integer
                      location:
                        type: string
```

### General Tips

- **Consistent State Representation**: Ensure that the state is consistently represented in all responses.
- **Clear Actions**: Clearly define available actions in each state and how to trigger them.
- **Use HTTP Status Codes**: Use appropriate HTTP status codes to indicate success, failure, and other relevant states.

By structuring your API responses to include clear state information and available actions, you can effectively communicate the state of the system to a client, including an LLM.

## Representing Sub States to a LLM

Representing substates (or nested states) to an LLM requires a clear and structured format to ensure the hierarchy and relationships between states and substates are well-understood. Here's a step-by-step approach to achieve this:

### 1. **Define Main States and Substates**

Clearly distinguish between main states and substates. Use indentation or hierarchical notation to represent the relationship between them.

### 2. **Include Entry and Exit Actions**

Specify any actions that should be taken when entering or exiting a state or substate.

### 3. **Use a Structured Format**

Ensure that the format is clear and consistent. Use lists, indentation, and labeling to differentiate between different levels of states.

### Example: Structured Prompt with Substates

#### Textual Representation

```plaintext
State Diagram: Order Processing

Initial State:
  - OrderPlaced

States:
  1. OrderPlaced
     - Entry Action: Call API to confirm order placement
       Endpoint: POST /api/order/confirm
       Parameters: { "orderId": 123 }

  2. OrderProcessing
     - Substates:
       a. PaymentProcessing
          - Entry Action: Call API to process payment
            Endpoint: POST /api/payment/process
            Parameters: { "orderId": 123 }
       b. Packaging
          - Entry Action: Call API to package order
            Endpoint: POST /api/order/package
            Parameters: { "orderId": 123 }
       c. Shipping
          - Entry Action: Call API to ship order
            Endpoint: POST /api/order/ship
            Parameters: { "orderId": 123 }

  3. OrderCompleted
     - Entry Action: Call API to complete order
       Endpoint: POST /api/order/complete
       Parameters: { "orderId": 123 }

Transitions:
  - OrderPlaced -> OrderProcessing [Event: Order Confirmed]
  - OrderProcessing.PaymentProcessing -> OrderProcessing.Packaging [Event: Payment Success]
  - OrderProcessing.Packaging -> OrderProcessing.Shipping [Event: Package Ready]
  - OrderProcessing.Shipping -> OrderCompleted [Event: Order Shipped]
```

#### SCXML Format with Substates

```xml
<scxml initial="OrderPlaced" version="1.0"
       xmlns="http://www.w3.org/2005/07/scxml">

  <state id="OrderPlaced">
    <onentry>
      <send event="confirmOrder" target="http://api.example.com/order/confirm" type="http"/>
    </onentry>
    <transition event="orderConfirmed" target="OrderProcessing"/>
  </state>

  <state id="OrderProcessing">
    <state id="PaymentProcessing">
      <onentry>
        <send event="processPayment" target="http://api.example.com/payment/process" type="http"/>
      </onentry>
      <transition event="paymentSuccess" target="Packaging"/>
    </state>

    <state id="Packaging">
      <onentry>
        <send event="packageOrder" target="http://api.example.com/order/package" type="http"/>
      </onentry>
      <transition event="packageReady" target="Shipping"/>
    </state>

    <state id="Shipping">
      <onentry>
        <send event="shipOrder" target="http://api.example.com/order/ship" type="http"/>
      </onentry>
      <transition event="orderShipped" target="OrderCompleted"/>
    </state>
  </state>

  <state id="OrderCompleted">
    <onentry>
      <send event="completeOrder" target="http://api.example.com/order/complete" type="http"/>
    </onentry>
  </state>

</scxml>
```

#### Pseudo-Code with Substates

```plaintext
State Machine: Order Processing

Initial State: OrderPlaced

States:
  - OrderPlaced
    - Entry Action: Call API to confirm order placement
      Endpoint: POST /api/order/confirm
      Parameters: { "orderId": 123 }

  - OrderProcessing
    - Substates:
      - PaymentProcessing
        - Entry Action: Call API to process payment
          Endpoint: POST /api/payment/process
          Parameters: { "orderId": 123 }
      - Packaging
        - Entry Action: Call API to package order
          Endpoint: POST /api/order/package
          Parameters: { "orderId": 123 }
      - Shipping
        - Entry Action: Call API to ship order
          Endpoint: POST /api/order/ship
          Parameters: { "orderId": 123 }

  - OrderCompleted
    - Entry Action: Call API to complete order
      Endpoint: POST /api/order/complete
      Parameters: { "orderId": 123 }

Transitions:
  - OrderPlaced -> OrderProcessing [Event: Order Confirmed]
  - OrderProcessing.PaymentProcessing -> OrderProcessing.Packaging [Event: Payment Success]
  - OrderProcessing.Packaging -> OrderProcessing.Shipping [Event: Package Ready]
  - OrderProcessing.Shipping -> OrderCompleted [Event: Order Shipped]
```

### General Tips

- **Use Clear Labels**: Clearly label each state and substate.
- **Consistent Formatting**: Use indentation or other formatting tools to clearly differentiate between states and substates.
- **Explicit Actions**: Specify any entry or exit actions for each state and substate.
- **Detailed Transitions**: Clearly define the transitions between states, including events that trigger them.

By following these guidelines, you can effectively represent substates to an LLM, ensuring that the hierarchy and relationships between states are clear and understandable.


## Reading Material:

https://apisyouwonthate.com/blog/representing-state-in-rest-and-graphql/

https://techblog.topdesk.com/architecture/difficulties-in-api-design-resource-state/

https://en.wikipedia.org/wiki/State_diagram

https://www.geeksforgeeks.org/unified-modeling-language-uml-state-diagrams/

https://www.visual-paradigm.com/guide/uml-unified-modeling-language/about-state-diagrams/

Sub-States

https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-state-machine-diagram/#:~:text=Substates%20may%20be%20nested%20to,context%20(the%20enclosing%20state).