# Learn Generative AI Engineering (GenEng)

This course is part of the [GenAI, Web 3, and Metaverse Program](https://docs.google.com/presentation/d/1XVSZhmv4XH14YpyDxJIvYWiUrF1EO9tsUnle17wCLIc/edit?usp=sharing)

Before starting to learn from this repo [Learn Modern Python](https://github.com/panaverse/learn-modern-python)

## All Faculty and Students please Register for Microsoft Azure and Google Cloud Accounts:


1. Microsoft Azure Account
https://azure.microsoft.com/en-us/free/ai-services/

Note: If possible register your account with a company email address.

Once you have a subscription id apply for Azure Open AI Service here:

https://azure.microsoft.com/en-us/products/ai-services/openai-service


2. Google Cloud Account
https://cloud.google.com/free

# The New Era

[The Age of AI has begun](https://www.gatesnotes.com/The-Age-of-AI-Has-Begun)

[Nvidia says generative AI will be bigger than the internet](https://www.theverge.com/2023/11/15/23962497/nvidia-says-generative-ai-will-be-bigger-than-the-internet)

[Generative AI and Its Economic Impact: What You Need to Know](https://www.investopedia.com/economic-impact-of-generative-ai-7976252)

[Must Read: OpenAI DevDay - a pivotal moment for AI](https://www.aitidbits.ai/p/openai-devday)

# Generative Engineering (GenEng)

GenEng revolution being led by developers who build deep proficiency in how to best leverage and integrate generative AI technologies into applications

 There is a clear separation of roles between those that create and train models (Data Scientists and Engineers) and those who use those models (Developers). This was already on the way, and it much clearer with the GenAI revolution - the future of the GenAI will be determined on how it will be driven to adoption - and it will be driven by how developers adopt it.

 GenEng practitioners will need to have many of the same skills of traditional application development, including scalable architecting, integrating enterprise systems, and understanding requirements from the business user. These skills will be augmented with the nuances of building generative AI applications, such as involving the business domain experts in validating aspects of prompt engineering and choosing the right LLM based on price/performance and outcomes

[The rise of GenEng: How AI changes the developer role](https://cloud.google.com/blog/products/ai-machine-learning/the-rise-of-geneng-how-ai-changes-the-developer-role)

[Watch: The Rise of GenEng](https://www.youtube.com/watch?v=RLUrvgfEeUc)

# Latest News

[Google launches its largest and ‘most capable’ AI model, Gemini](https://www.cnbc.com/2023/12/06/google-launches-its-largest-and-most-capable-ai-model-gemini.html)

[Meta, IBM and Intel join alliance for open AI development while Google and Microsoft sit out](https://www.scmp.com/tech/big-tech/article/3244012/meta-ibm-and-intel-join-alliance-open-ai-development-while-google-and-microsoft-sit-out)

[What Elon Musk has said about Ilya Sutskever, the chief scientist at the center of OpenAI’s leadership upheaval](https://finance.yahoo.com/news/elon-musk-said-ilya-sutskever-171726023.html)

[Who is OpenAI chief scientist Ilya Sutskever, and what does he think about the future of AI and ChatGPT?](https://www.fastcompany.com/90985752/ilya-sutskever-openai-chief-scientist)

[Sam Altman to return as CEO of OpenAI](https://www.theverge.com/2023/11/22/23967223/sam-altman-returns-ceo-open-ai)


## Technology from the Business and Top Management Perspective

[The Year in Tech, 2024: The Insights You Need from Harvard Business Review](https://www.hbsp.harvard.edu/product/10673-PDF-ENG)

The Year in Tech 2024: The Insights You Need about Generative AI and Web 3.0 from Harvard Business Review will help you understand what the latest and most important tech innovations mean for your organization and how you can use them to compete and win in today's turbulent business environment. Business is changing. Will you adapt or be left behind? Get up to speed and deepen your understanding of the topics that are shaping your company's future with the Insights You Need from Harvard Business Review series. You can't afford to ignore how these issues will transform the landscape of business and society. The Insights You Need series will help you grasp these critical ideas--and prepare you and your company for the future.

[McKinsey Technology Trends Outlook 2023](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-top-trends-in-tech#new-and-notable)

## Introduction to Generative AI

[Watch Introduction to Generative AI](https://www.youtube.com/watch?v=G2fqAlgmoPo)

![Alt text](genai_fit.jpeg "Where Does GenAI Fit")


## Generative AI and the Economy

1. [McKinsey: The economic potential of generative AI: The next productivity frontier](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier#introduction), McKinsey Digital report, June 2023 

2. [GPTs are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Models](https://arxiv.org/pdf/2303.10130.pdf), Tyna Eloundou, Sam Manning, Pamela Miskin, and Daniel Rock, March 2023 (arXiv:2303.10130)

3. [Goldman Sachs: The Potentially Large Effects of Artificial Intelligence on Economic Growth](https://www.gspublishing.com/content/research/en/reports/2023/03/27/d64e052b-0f6e-45d7-967b-d7be35fabd16.html), Joseph Briggs and Devesh Kodnani, March 2023

## "ChatGPT API" or correctly: OpenAI API

OpenAI API is a collection of APIs

APIs offer access to various Large Language Models (LLMs)

LLM: Program trained to understand human language

ChatGPT is a web service using the Chat completion API
Uses:

1. gpt-3.5-turbo (free tier)
2. gpt-4.0 (paid tier)

## OpenAI API endpoints

1. Chat completion:
Given a series of messages, generate a response

2. Function calling: 
Choose which function to call

3. Image generation:
Given a text description generate an image

4. Speech to text:
Given an audio file and a prompt generate a transcript

5. Fine tuning:
Train a model using input and output examples

## OpenAI Assistants API

The new Assistants API is a stateful evolution of Chat Completions API meant to simplify the creation of assistant-like experiences, and enable developer access to powerful tools like Code Interpreter and Retrieval.

![Alt text](assistants.png "Assistants")

## Chat Completions API vs Assistants API

The primitives of the Chat Completions API are Messages, on which you perform a Completion with a Model (gpt-3.5-turbo, gpt-4, etc). It is lightweight and powerful, but inherently stateless, which means you have to manage conversation state, tool definitions, retrieval documents, and code execution manually.

The primitives of the Assistants API are

1. Assistants, which encapsulate a base model, instructions, tools, and (context) documents,
2. Threads, which represent the state of a conversation, and
3. Runs, which power the execution of an Assistant on a Thread, including textual responses and multi-step tool use.

## What is the OPL stack in AI?

The OPL Stack stands for OpenAI, Pinecone, and Langchain. It's a collection of open-source tools and libraries that make building and deploying LLMs a breeze. 


![Alt text](opl.jpeg "OPL")


## The Future of Generative AI

“AI will be the greatest wealth creator in history because artificial intelligence doesn’t care where you were born, whether you have money, whether you have a PhD,” Higgins tells CNBC Make It. “It’s going to destroy barriers that have prevented people from moving up the ladder, and pursuing their dream of economic freedom.”

It’s already valued at almost $100 billion, and expected to contribute $15.7 trillion to the global economy by 2030.

“It’s not that if you don’t jump on it now, you never can,” Higgins says. “It’s that now is the greatest opportunity for you to capitalize on it.”

[A.I. will be the biggest wealth creator in history](https://www.cnbc.com/2023/07/10/how-to-use-ai-to-make-money-right-now-say-experts.html)

[Generative AI could add up to $4.4 trillion annually to the global economy](https://www.zdnet.com/article/generative-ai-could-add-up-to-4-4-trillion-annually-to-global-economy/)

[Research Report](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier#key-insights)

[Silicon Valley Sees a New Kind of Mobile Device Powered by GenAI](
https://www.bloomberg.com/news/newsletters/2023-10-02/silicon-valley-sees-a-new-kind-of-mobile-device-powered-by-ai)

[Microsoft CEO: AI is "bigger than the PC, bigger than mobile" - but is he right?](https://www.techradar.com/computing/artificial-intelligence/microsoft-ceo-ai-is-bigger-than-the-pc-bigger-than-mobile-but-is-he-right)

[Artificial General Intelligence Is Already Here](https://www.noemamag.com/artificial-general-intelligence-is-already-here/)

[Inside the race to build an ‘operating system’ for generative AI](https://venturebeat.com/ai/inside-the-race-to-build-an-operating-system-for-generative-ai/)

## Generative BI

[Business intelligence in the era of GenAI](https://www.youtube.com/watch?v=m0-ul3O3GwA)

## Convergence of Generative AI and Web 3.0

[The Convergence of AI and Web3: A New Era of Decentralized Intelligence](https://medium.com/@dhruvil7694/the-convergence-of-ai-and-web3-a-new-era-of-decentralized-intelligence-ca86aef481d)

[What is the potential of Generative AI and Web 3.0 when combined?](https://blog.softtek.com/en/what-is-the-potential-of-generative-ai-and-web-3.0-when-combined)

[How Web3 Can Unleash the Power of Generative AI](https://www.linkedin.com/pulse/how-web3-can-unleash-power-generative-ai-iman-sheikhansari/)


## Text Books

1. [Generative AI with LangChain: Build large language model (LLM) apps with Python, ChatGPT and other LLMs](https://www.amazon.com/Generative-AI-LangChain-language-ChatGPT/dp/1835083463/ref=sr_1_3)
2. [LangChain Crash Course: Build OpenAI LLM powered Apps](https://www.amazon.com/LangChain-Crash-Course-powered-building-ebook/dp/B0CHHHX118/ref=sr_1_2)
3. [Build and Learn: AI App Development for Beginners: Unleashing ChatGPT API with LangChain & Streamlit](https://www.amazon.com/Build-Learn-Development-Beginners-Unleashing/dp/B0CDNNC5Z1/ref=sr_1_1)
4. [Generative AI in Healthcare - The ChatGPT Revolution](https://leanpub.com/generative-ai-in-healthcare)
5. [Generative AI in Accounting Guide: Explore the possibilities of generative AI in accounting](https://www.icaew.com/technical/technology/artificial-intelligence/generative-ai-guide)
6. [Using Generative AI in Business Whitepaper](https://resources.multiply.ai/en-gb/multiply-white-paper-chatgpt-and-generative-ai-download)
7. [Generative AI: what accountants need to know in 2023](https://www.amazon.com/Generative-AI-what-accountants-need/dp/B0CCL1P8XP)
8. [100 Practical Applications and Use Cases of Generative AI](https://ai.gov.ae/wp-content/uploads/2023/04/406.-Generative-AI-Guide_ver1-EN.pdf)

## Learn Langchain, Pinecone, and LLMs

[LangChain Explained in 13 Minutes | QuickStart Tutorial for Beginners](https://www.youtube.com/watch?v=aywZrzNaKjs)

[LangChain Crash Course for Beginners](https://www.freecodecamp.org/news/learn-langchain-for-llm-development/) 

[LangChain Crash Course for Beginners Video](https://www.youtube.com/watch?v=lG7Uxts9SXs)

[LangChain for LLM Application Development](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/)

[LangChain: Chat with Your Data](https://www.deeplearning.ai/short-courses/langchain-chat-with-your-data/)

[A Gentle Intro to Chaining LLMs, Agents, and Utils via LangChain](https://towardsdatascience.com/a-gentle-intro-to-chaining-llms-agents-and-utils-via-langchain-16cd385fca81) 

[The LangChain Cookbook - Beginner Guide To 7 Essential Concepts](https://www.youtube.com/watch?v=2xxziIWmaSA&list=PLqZXAkvF1bPNQER9mLmDbntNfSpzdDIU5&index=4&t=1092s)

[Greg Kamradt’s LangChain Youtube Playlist](https://www.youtube.com/playlist?list=PLqZXAkvF1bPNQER9mLmDbntNfSpzdDIU5)

[1littlecoder LangChain Youtube Playlist](https://www.youtube.com/playlist?list=PLpdmBGJ6ELUK-v0MK-t4wZmVEbxM5xk6L)

Pinecone

https://docs.pinecone.io/docs/quickstart

https://python.langchain.com/docs/integrations/vectorstores/pinecone 

LangChain - Vercel AI SDK

https://sdk.vercel.ai/docs/guides/providers/langchain 

Using Python and Flask in Next.js 13 API

https://github.com/wpcodevo/nextjs-flask-framework

https://vercel.com/templates/python/flask-hello-world

https://vercel.com/docs/functions/serverless-functions/runtimes/python 

https://codevoweb.com/how-to-integrate-flask-framework-with-nextjs/#google_vignette 

https://github.com/vercel/examples/tree/main/python 

https://github.com/orgs/vercel/discussions/2732 

https://flask.palletsprojects.com/en/2.3.x/tutorial/

https://flask.palletsprojects.com/en/2.3.x/ 

Reference Material:
	
[LangChain Official Docs](https://python.langchain.com/docs/get_started/introduction)

[LangChain AI Handbook](https://www.pinecone.io/learn/series/langchain/)

[Top 5 Resources to learn LangChain](https://medium.com/@ankity09/top-5-resources-to-learn-langchain-e2bdbbd11702)

[Official LangChain YouTube channel](https://python.langchain.com/docs/additional_resources/youtube)



## Projects

[Building Custom Q&A Applications Using LangChain and Pinecone Vector Database](https://www.analyticsvidhya.com/blog/2023/08/qa-applications/)

[End to End LLM Project Using Langchain | NLP Project End to End](https://www.youtube.com/watch?v=MoqgmWV1fm8)

[Build and Learn: AI App Development for Beginners: Unleashing ChatGPT API with LangChain & Streamlit](https://www.amazon.com/Build-Learn-Development-Beginners-Unleashing/dp/B0CDNNC5Z1/ref=tmm_pap_swatch_0?_encoding=UTF8&qid=1695978776&sr=8-1) 

## Fundamentals of GenAI Quiz

Total Questions: 40

Duration: 60 minutes 



