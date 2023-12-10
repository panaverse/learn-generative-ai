# Container as a Service (CaaS)

Google Cloud Account

https://cloud.google.com/free

Serverless CaaS (Container as a Service) is quickly growing in prominence. Datadog’s 2022 “The State of Serverless” report shows that in 2022, Google Cloud Run was the fastest-growing method for deploying serverless applications in Google Cloud. The 2023 report indicates that serverless CaaS adoption has continued to intensify across all major cloud providers.

[How to Run a Docker Container on the Cloud: Top 5 CaaS Solutions](https://bluelight.co/blog/how-to-run-a-docker-container-on-the-cloud)

[Container as a Service (CaaS) Market Projections for 2030: Size, Share, and Growth](https://medium.com/@watsonmac944/container-as-a-service-caas-market-projections-for-2030-size-share-and-growth-e30b663dbcd9)

We will use Google Cloud Run to deploy serverless containers in the cloud. Cloud Run is a managed compute platform that lets you run containers directly on top of Google's scalable infrastructure. You can deploy code written in Python, TypeScript, or any other programming language on Cloud Run if you can build a container image from it. These serverless containers must be stateless.

You can run not only serverless containers but also Cloud Run jobs. A Cloud Run job only runs its tasks and exits when finished. A job does not listen for or serve requests. After you create or update a job, you can: Execute the job as a one-off, on a schedule, or as part of a workflow.

We will be mainly using Cloud Run to develop API's using Python or TypeScript.

## Deploy Locally

[Deploy a Cloud Run service with Cloud Code for VS Code](https://cloud.google.com/code/docs/vscode/deploy-cloud-run-app)

[Installing](https://cloud.google.com/code/docs/vscode/install#installing)

https://cloud.google.com/code/docs/vscode/cloud-run-overview

https://cloud.google.com/code/docs/vscode/develop-service

## Deploy on the Cloud

Create Account: https://cloud.google.com/run

[What is Google Cloud Run](https://youtu.be/1t94tdyojs0)

[GCP Cloud Run: What is it? What’s it for?](https://datascientest.com/en/gcp-cloud-run-what-is-it-whats-it-for)

Note: All customers get 2 million requests free per month, not charged against your credits or to you.

[Install the gcloud CLI](https://cloud.google.com/sdk/docs/install)


## Follow these Tutorials to Deploy 00_helloword project:

[Deploy a Python service to Cloud Run](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service)

[Flask: A Minimal Application](https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application)

[Google Hello World Sample](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/run/helloworld)

[Dev to Prod in Three Easy Steps with Cloud Run](https://codelabs.developers.google.com/codelabs/cloud-run-dev2prod#0)

Change directory to helloworld and run the following command:

    gcloud run deploy

My container was deployed at:

https://helloworld-oqgectyvca-wl.a.run.app

Note: In deploying I selected us-west2 as the region

### Container Image will be in Artifact Registary (Container Registry)

Artifact Registry is the recommended service for managing container images

https://console.cloud.google.com/artifacts?project=project_name

### Cloud Run Dashboard

https://console.cloud.google.com/home/dashboard?project=project_name

### Build using a Docker File

    gcloud auth configure-docker
    gcloud components install docker-credential-gcr

https://cloud.google.com/run/docs/building/containers#building_using_a_dockerfile


### Manually Deploy

[Watch: Manually Deploy to Cloud Run - Updated for Artifact Registry](https://www.youtube.com/watch?v=MM4viHa7k4w)

[Work with container images](https://cloud.google.com/artifact-registry/docs/docker)

[Multi-platform images](https://docs.docker.com/build/building/multi-platform/)


