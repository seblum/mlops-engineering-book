# Preamble {.unnumbered}

This project started out of an interest in multiple domains. At first, I was working on a Kubeflow platform at the time and haven't had much experience in the realm of MLOps. I was starting with K8s and Terraform and was interested to dig deeper. I did so by teaching myself and I needed a project. What better also to do than to build "my own" MLOps plattform. I used Airflow since it is widely uses for workflow management and I also wanted to use it from the perspective of a data scientist, meaning to actually build some pipelines with it. This idea of extending the project to actually have a running use case expanded this work to include MLFlow for model tracking.

### Topics {.unlisted .unnumbered}

The overall aim is to build and create a MLOps architecture based on Airflow running on AWS EKS. Ideally, this architecture is create using terraform. Model tracking might be done using MLFlow, Data tracking using DVC. Further mentioned might be best practices in software development, CI/CD, Docker, and pipelines. I might also include a small Data Science use case utilizing the Airflow Cluster we built.

The book contains two parts with distinct focuses. The first part comprises Chapters [3: Airflow](#airflow), [4: MLflow](#mlflow), [5: Kubernetes](#kubernetes), and [6: Terraform](#terraform), which consist of tutorials on the specific tools aforementioned. These chapters also serve as prerequisites for the subsequent part. Among these tutorials, the chapters dedicated to *Airflow* and *MLflow* are oriented towards Data Scientists, providing insights into their usage. The chapters centered around *Kubernetes* and *Terraform* target Data- and MLOps Engineers, offering detailed guidance on deploying and managing these tools.

The second part, comprising Chapters [7: ML Platform Design](#ml-platform-design), [8: Platform Deployment](#platform-deployment), and [9: Use Case Development](#use-case-development), delves into an exemplary machine learning Platform. This part of the book demands a strong background in engineering due to its complexity. While these chapters cover the essential tools introduced in the previous part, they may not explore certain intricate aspects used like OAuth authentication and networking details in great depth. Moreover, it is crucial to note that the ML Platform example presented is not intended for production deployment, as there should be significant security concerns considered. Instead, its main purpose is to serve as an informative illustration of ML platforms and MLOps engineering principles.

Chapter [1: Introduction](#introduction) and [2: Ops Tools and Principles](#ops-tools-and-principles) serve as an introduction to the domain of MLOps

### A work in progress {.unlisted .unnumbered}

This project / book / tutorial / whatever this is or will be, startet by explaining the concept of Kubernetes. The plan is to continuously update it by further chapters. Since there is no deadline, there is no timeline, and I am also not sure whether there will exist something final to be honest.

This document is written during my journey in the realm of MLOps. It is therefore in a state of continuous development. 

