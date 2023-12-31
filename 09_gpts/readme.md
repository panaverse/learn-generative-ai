# OpenAI GPTs

GPTs are a new feature from OpenAI that allows subscription users to create their own ChatGPT versions. GPTs can use custom data to offer capabilities like image generation, web browsing, and data analysis. 


[Introducing GPTs](https://openai.com/blog/introducing-gpts)

[Watch Video](https://www.youtube.com/watch?v=pq34V_V5j18&t=9s)

[Actions in GPTs](https://platform.openai.com/docs/actions)

[Creating a GPT](https://help.openai.com/en/articles/8554397-creating-a-gpt)

[GPTs vs Assistants](https://help.openai.com/en/articles/8673914-gpts-vs-assistants)

[GPTs FAQ](https://help.openai.com/en/articles/8554407-gpts-faq)

[How to Make GPTs WITHOUT ChatGPT Plus in Minutes (OpenAI GPTs)](https://www.youtube.com/watch?v=F31fe68q_4Q)

[GPT Actions: How to Integrate APIs Into OpenAI's Custom GPTs](https://www.youtube.com/watch?v=-ceIJx7zaBM)

[Latest Status](https://www.youtube.com/watch?v=KlFVj1OYNJ8)

**Note that APIs and OpenAPI Specifications are extremely important in this new era of Generative AI**

GPT Actions are a way to integrate APIs into OpenAI's custom GPTs, which are tailored versions of ChatGPT that can be created for specific purposes. GPT Actions allow you to connect your GPT to external data sources or services, such as databases, emails, or e-commerce platforms. You can define GPT Actions using an OpenAPI specification, which describes the endpoints, parameters, and responses of your API. You can also set some endpoints as consequential, which means they will require user confirmation before running.

To integrate APIs into OpenAI's custom GPTs, you need to:

- Create a GPT in the ChatGPT UI and give it a name and a description.
- Configure your GPT by adding GPT Actions and filling in your OpenAPI spec or pasting in a URL where it is hosted.
- Test your GPT by interacting with it in the playground and seeing how it responds to different queries and actions.

You can find more information and examples on how to integrate APIs into OpenAI's custom GPTs on these websites:

- [Integrating APIs into OpenAI's Custom GPTs: A Step-by-Step Guide](^1^)
- [Actions - OpenAI API](^2^)
- [Enhance GPTs with Custom Actions and APIs: Full Tutorial](^3^)


(1) Integrating APIs into OpenAI's Custom GPTs: A Step-by-Step Guide. https://eightify.app/summary/artificial-intelligence-and-programming/integrating-apis-into-openai-s-custom-gpts-a-step-by-step-guide.
(2) Actions - OpenAI API. https://platform.openai.com/docs/actions/what-is-a-gpt.
(3) Enhance GPTs with Custom Actions and APIs: Full Tutorial. https://eightify.app/summary/artificial-intelligence-and-technology/enhance-gpts-with-custom-actions-and-apis-full-tutorial.

**Who calls my APIs**

OpenAI calls your APIs in GPT Actions by using the OpenAPI specification that you provide when you create or edit a GPT. The OpenAPI specification defines the endpoints, parameters, and responses of your API, as well as whether they are consequential or not. Consequential endpoints require user confirmation before running, while non-consequential endpoints can be called without user intervention.

**When you interact with a GPT that has Actions, the model can choose to call one or more of your endpoints based on the user query and the description of each function. The model will generate a JSON object that adheres to your custom schema and pass it to your API. Your API should return a response that matches the expected format of your schema. The model will then use the response to generate a reply to the user.**

You can test your GPT Actions by using the playground in the ChatGPT UI. You can also use the API Alchemist GPT¹ to test if your API is correct and compatible with GPT Actions.

You can find more information and examples on how to use GPT Actions on these websites:

- [Actions - OpenAI API](^2^)
- [Integrating APIs into OpenAI's Custom GPTs: A Step-by-Step Guide](^3^)
- [Enhance GPTs with Custom Actions and APIs: Full Tutorial](^4^)

I hope this helps you understand how OpenAI calls your APIs in GPT Actions. 

(1) Actions - OpenAI API. https://platform.openai.com/docs/actions.
(2) Issue with GPT Actions not triggering external API calls. https://community.openai.com/t/issue-with-gpt-actions-not-triggering-external-api-calls/495495.
(3) Function calling - OpenAI API - platform.openai.com. https://platform.openai.com/docs/guides/function-calling.
(4) Function calling - OpenAI API - platform.openai.com. https://platform.openai.com/docs/guides/function-calling?lang=node.js.

**OpenAI GPTs vs Assistants**

OpenAI GPTs and Assistants are two different ways of creating custom chatbots that can leverage the power of ChatGPT and other tools. Here are some of the main differences between them:

- **Creation process**: GPTs can be created by anyone using a simple UI within ChatGPT, while Assistants require coding for integration with the OpenAI API.
- **Operational environment**: GPTs live inside of ChatGPT and can be accessed through its interface, while Assistants can be integrated into any product or service that supports the OpenAI API.
- **Pricing**: GPTs are included in ChatGPT on Plus/Enterprise plans, while Assistants are billed based on the usage of different features.
- **User interface**: GPTs have a built-in UI with ChatGPT that allows users to interact with them, while Assistants are designed for programmatic use and can be visualized using the playground.
- **Shareability**: GPTs have a built-in ability to share them with others, while Assistants do not have a built-in shareability feature.
- **Hosting**: GPTs are hosted by OpenAI, while OpenAI does not host Assistants.
- **Tools**: GPTs have built-in tools like Web Browser, DALL·E, Code Interpreter, Retrieval, and Custom Actions, while Assistants have built-in tools like Code Interpreter, Functions, and File Retrieval.

You can find more information about GPTs and Assistants on these websites:

- [GPTs vs Assistants | OpenAI Help Center](^1^)
- [GPTs vs. Assistants: What's the difference? | Zapier](^2^)
- [API assistant VS GPTs: what's the main difference?](^3^)
- [OpenAI Assistants vs GPTs | how.wtf](^4^)
- [What's the difference between GPTs and AI Assistants](^5^)

I hope this helps you understand the difference between GPTs and Assistants. If you have any other questions, feel free to ask me. 😊

(1) GPTs vs Assistants | OpenAI Help Center. https://help.openai.com/en/articles/8673914-gpts-vs-assistants.
(2) GPTs vs. Assistants: What's the difference? | Zapier. https://zapier.com/blog/gpts-vs-ai-assistants/.
(3) API assistant VS GPTs: what's the main difference?. https://community.openai.com/t/api-assistant-vs-gpts-whats-the-main-difference/499523.
(4) OpenAI Assistants vs GPTs | how.wtf. https://how.wtf/openai-assistants-vs-gpts.html.
(5) What's the difference between GPTs and AI Assistants. https://www.gettingstarted.ai/whats-the-difference-between-gpts-and-ai-assistants/.



## Latest News

[OpenAI’s GPT Store delayed to 2024 following leadership chaos](https://techcrunch.com/2023/12/01/openais-gpt-store-delayed-to-2024-following-leadership-chaos/)

