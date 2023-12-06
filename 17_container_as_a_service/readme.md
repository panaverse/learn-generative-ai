# Serverless Containers

Serverless CaaS (Container as a Service) is quickly growing in prominence. Datadog’s 2022 “The State of Serverless” report shows that in 2022, Google Cloud Run was the fastest-growing method for deploying serverless applications in Google Cloud. The 2023 report indicates that serverless CaaS adoption has continued to intensify across all major cloud providers.

[How to Run a Docker Container on the Cloud: Top 5 CaaS Solutions](https://bluelight.co/blog/how-to-run-a-docker-container-on-the-cloud)

[Container as a Service (CaaS) Market Projections for 2030: Size, Share, and Growth](https://medium.com/@watsonmac944/container-as-a-service-caas-market-projections-for-2030-size-share-and-growth-e30b663dbcd9)

We will used Google Cloud Run to deploy serverless containers in the cloud. Cloud Run is a managed compute platform that lets you run containers directly on top of Google's scalable infrastructure. You can deploy code written in Python, TypeScript, or any other programming language on Cloud Run if you can build a container image from it. These serverless containers must be stateless.

You can run not only serverless containers but also Cloud Run jobs. A Cloud Run job only runs its tasks and exits when finished. A job does not listen for or serve requests. After you create or update a job, you can: Execute the job as a one-off, on a schedule, or as part of a workflow.

We will be mainly using Cloud Run to develop API's using Python or TypeScript.

Create Account: https://cloud.google.com/run

[What is Google Cloud Run](https://youtu.be/1t94tdyojs0)

Note: All customers get 2 million requests free per month, not charged against your credits or to you.

[Install the gcloud CLI](https://cloud.google.com/sdk/docs/install)


## Follow these Tutorials to Deploy helloword project:

[Deploy a Python service to Cloud Run](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service)

[Flask: A Minimal Application](https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application)

Change directory to helloworld and run the following command:

    gcloud run deploy

My container was deployed at:

https://helloworld-oqgectyvca-wl.a.run.app

Note: In deploying I selected us-west2 as the region


