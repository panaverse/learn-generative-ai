# Designing GPTs

### ChatGPT Files:

[Working Chat 1](https://chatgpt.com/share/9fc9d34f-cff2-49b2-a5fe-2a9060f7f99b)

[Working Chat 2](https://chatgpt.com/share/a3ac97bc-5119-4640-9941-b93912e5409f)

### Text Books

[Design Thinking Toolbox](https://www.amazon.com/Design-Thinking-Toolbook-Michael-Lewrick/dp/1119629195/ref=sr_1_1)

[BDD in Action, Second Edition: Behavior-Driven Development for the whole software lifecycle](https://www.amazon.com/Action-Second-John-Ferguson-Smart/dp/1617297534/ref=sr_1_1)

## Overview

Our proposed process for designing and developing custom GPTs is comprehensive and well-structured, combining user-centric design thinking, behavior-driven development (BDD), and creative script generation to identify actions and APIs. Here's a breakdown and evaluation of our approach with examples to illustrate how each step integrates:

### Step 1: Focus on User through Design Thinking

**Empathize and Define:**
Start by understanding the user's needs, preferences, and challenges through interviews, surveys, and observations.

*Example:* 
- **Empathize:** Conduct workshops with potential users to understand their pain points when using existing AI solutions.
- **Define:** Identify key issues such as "Users find it difficult to get personalized responses for their specific industry-related queries."

**Ideate:**
Brainstorm potential solutions and features that could address the defined problems.

*Example:* 
- Generate ideas like "a GPT that can learn from industry-specific documents" or "a GPT that offers a task management interface integrated with user preferences."

**Prototype and Test:**
Create and test prototypes with real users to gather feedback.

*Example:* 
- Develop a simple prototype of the GPT interface and functionality, and test it with a small user group. Gather feedback on usability and relevance.

### Step 2: Define Behavior Using BDD

BDD helps define the expected behavior of the GPT in a way that’s clear and understandable for all stakeholders.

**Write BDD Scenarios:**
Define the behavior of the GPT in the form of Given-When-Then scenarios.

*Example:* 
- **Scenario:** Personalized Task Management
  - **Given**: A user has signed in and provided their preferences.
  - **When**: The user asks for a new task to be added.
  - **Then**: The GPT suggests tasks based on the user's preferences and past behavior.

### Step 3: Generate Movie Scripts from BDD Documentation

Turning BDD scenarios into movie scripts helps visualize interactions and user journeys in a more narrative and engaging way.

*Example:* 
- **BDD Scenario**: Personalized Task Management
  - **Movie Script**:
    - **Scene 1**: User logs in and the GPT greets them with a summary of pending tasks.
    - **Scene 2**: User asks, "What's my next task?" The GPT analyzes past tasks and user preferences.
    - **Scene 3**: GPT responds, "Based on your schedule, I suggest you focus on the marketing report next."

### Step 4: Identify GPT Actions (APIs) from BDD and Movie Scripts

Identify specific actions and APIs required to implement the behaviors and interactions described in BDD scenarios and movie scripts.

*Example:* 
- **From the Scenario and Script**:
  - **API Action 1**: Authenticate user and retrieve preferences.
  - **API Action 2**: Analyze past tasks and preferences to suggest next task.
  - **API Action 3**: Update task status and user preferences based on interaction.

### Integrating the Steps

1. **Start with Design Thinking:**
   - Gather user insights and define problems.
   - Ideate solutions and create prototypes.
   - Test and refine prototypes based on user feedback.

2. **Move to BDD:**
   - Write clear, behavior-focused scenarios based on user insights and defined problems.
   - Use these scenarios to specify detailed requirements and expected outcomes.

3. **Generate Movie Scripts:**
   - Convert BDD scenarios into narrative scripts to visualize user interactions.
   - Ensure the scripts cover all possible user journeys and interactions.

4. **Identify GPT Actions:**
   - Extract required actions and APIs from the BDD scenarios and movie scripts.
   - Define the technical implementation for each action/API.

### Example Process Flow

1. **Design Thinking Phase:**
   - User Research → Problem Definition → Ideation → Prototyping → Testing

2. **BDD Phase:**
   - Scenario Writing → Documentation Review → Scenario Refinement

3. **Script Generation Phase:**
   - Scenario Conversion → Script Writing → Script Review

4. **Action Identification Phase:**
   - Script Analysis → Action/ API Listing → Technical Specification

### Conclusion

Your approach of combining design thinking, BDD, and script generation is robust and user-focused, ensuring that the GPT developed is both functional and aligned with user needs. Each step builds upon the previous one, creating a seamless process from understanding user needs to technical implementation. By following this structured approach, you can create custom GPTs that are highly effective and user-friendly.

## Steps in Creating AI Solutions

Using design thinking and BDD (Behavior-Driven Development) in the age of AI involves leveraging these methodologies to create AI solutions that are not only technically sound but also highly user-centric and aligned with real-world needs. Here’s a step-by-step guide on how to integrate these approaches effectively in AI development:

### Step 1: Empathize (Design Thinking)

**Goal:** Understand the users and their needs deeply.

1. **User Research:**
   - Conduct interviews, surveys, and observations to gather insights about user behaviors, pain points, and needs.
   - Use techniques like journey mapping to visualize user experiences.

2. **AI-Specific Insights:**
   - Identify areas where AI can provide significant value, such as automating repetitive tasks, providing personalized recommendations, or enhancing decision-making processes.

**Example:**
   - Conduct interviews with customer support agents to understand their challenges, such as handling repetitive queries or managing high volumes of customer interactions.

### Step 2: Define (Design Thinking)

**Goal:** Clearly articulate the problem statement based on user insights.

1. **Problem Statement:**
   - Synthesize the insights gathered to define clear and concise problem statements.
   - Ensure the problem statement focuses on the user's needs and how AI can address them.

2. **Contextual Understanding:**
   - Understand the context in which the AI solution will be used, including any constraints or specific requirements.

**Example:**
   - Define the problem as: "Customer support agents need a system that can handle repetitive queries efficiently, allowing them to focus on more complex customer issues."

### Step 3: Ideate (Design Thinking)

**Goal:** Generate a wide range of ideas and potential solutions.

1. **Brainstorming:**
   - Conduct brainstorming sessions with cross-functional teams, including designers, developers, and domain experts.
   - Encourage creative thinking and explore various AI applications that could solve the defined problem.

2. **Conceptual Solutions:**
   - Develop conceptual solutions that leverage AI capabilities, such as chatbots, recommendation systems, or predictive analytics.

**Example:**
   - Brainstorm ideas like an AI-powered chatbot that can handle common customer queries and escalate complex issues to human agents.


### Step 4: Prototype (Design Thinking)

**Goal:** Create tangible representations of ideas to test and validate.

1. **Rapid Prototyping:**
   - Develop low-fidelity prototypes or mockups of the AI solution.
   - Focus on key functionalities and user interactions.

2. **Feedback Loop:**
   - Test prototypes with real users to gather feedback.
   - Iterate on the design based on user feedback to refine the solution.

**Example:**
   - Create a prototype of the AI chatbot interface and test it with customer support agents to gather their feedback on usability and effectiveness.

### Step 5: Define Behavior Using BDD

**Goal:** Clearly define the expected behavior of the AI system through scenarios.

1. **BDD Scenarios:**
   - Write Given-When-Then scenarios to describe the desired behavior of the AI solution.
   - Ensure scenarios are clear, concise, and understandable to all stakeholders.

2. **Collaboration:**
   - Collaborate with stakeholders, including developers, testers, and business analysts, to refine scenarios.
   - Use these scenarios to align technical development with user needs.

**Example:**
   - **Scenario:** AI Chatbot Handles Repetitive Queries
     ```gherkin
     Scenario: Handle Common Customer Query
       Given a customer asks a common question about product pricing
       When the query is received by the AI chatbot
       Then the chatbot provides the correct pricing information
     ```

### Step 6: Create Movie Script to Visulaize

   **Goal:** Develop a movie script of interactions between user and AI to be able to visualize the entire conversations.

### Step 7: Develop and Test

**Goal:** Implement the AI solution and validate its performance.

1. **Implementation:**
   - Develop the AI solution based on the defined BDD scenarios.
   - Use agile methodologies to ensure iterative development and continuous improvement.

2. **Testing:**
   - Conduct thorough testing, including unit tests, integration tests, and user acceptance tests.
   - Validate the AI's performance and ensure it meets the defined behaviors and user needs.

**Example:**
   - Implement the AI chatbot and test its ability to handle common queries accurately and efficiently.

### Step 8: Iterate and Improve

**Goal:** Continuously refine the AI solution based on user feedback and performance metrics.

1. **Continuous Feedback:**
   - Collect ongoing feedback from users to identify areas for improvement.
   - Use performance metrics to assess the effectiveness of the AI solution.

2. **Iterative Development:**
   - Continuously iterate on the design and functionality of the AI solution.
   - Implement enhancements and new features based on user needs and technological advancements.

**Example:**
   - After deploying the AI chatbot, gather feedback from customer support agents and customers to refine its responses and improve its accuracy.

### Conclusion

By integrating design thinking and BDD in the age of AI, you can create AI solutions that are deeply aligned with user needs and expectations. Design thinking ensures a thorough understanding of the user and problem space, while BDD provides a structured approach to defining and validating the desired behaviors of the AI system. Together, these methodologies lead to the development of AI solutions that are not only technically robust but also highly user-centric and effective in solving real-world problems.