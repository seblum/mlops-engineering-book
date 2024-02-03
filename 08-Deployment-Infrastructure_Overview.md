
# Platform Deployment

The provided directory structure represents the Terraform project for managing the infrastructure of our ML platform. It follows a modular organization to promote reusability and maintainability of the codebase. The full codebase is also available and can be accessed on [github](https://github.com/seblum/mlops-mlplatform-on-eks)

```bash
root
│   main.tf
│   variables.tf
│   outputs.tf
│   providers.tf
│
└── infrastructure
│   │
│   └── vpc
│   │
│   └── eks
│   │
│   └── networking
│   │
│   └── rds
│
└── modules
    │
    └── airflow
    │
    └── mlflow
    │
    └── jupyterhub
```

By structuring the Terraform project this way it becomes easier to manage, scale, and maintain the infrastructure as the project grows. Each module can be independently developed, tested, and reused across different projects, promoting consistency and reducing duplication of code and effort.

### Root  {.unlisted .unnumbered}

The *root* directory of the Terraform project contains the general configuration files related to the overall infrastructure setup.

* The `main.tf` Terraform configuration file, where all major resources are defined and organized into modules.
* The `variables.tf` containing the definition of input variables used throughout the project, allowing users to customize the infrastructure setup.
* The `outputs.tf` defining the output variables that expose relevant information about the deployed infrastructure.
* The `providers.tf` that defining and configuring the providers used in the project, for example, AWS, Kubernetes, Helm.

### Infrastructure {.unlisted .unnumbered}

The *infrastructure* directory holds the individual modules responsible for provisioning specific components of the AWS Cloud and EKS setup.

* `vpc` defines a module that configures resources related to the Virtual Private Cloud (VPC), such as subnets, route tables, and internet gateways.
* The `eks` module is responsible for creating and configuring an Amazon Elastic Kubernetes Service (EKS) cluster, including worker nodes and other related resources like the Cluster Autoscaler, Elastic Block Storage, or Elastic File System.
* `networking` contains networking components that provide access to the cluster using ingresses and DNS records, for example the AWS Application Load Balancer or an External DNS.
* The `rds` module provides resources to deploy and Amazon Relational Database Service (RDS), such as database instances, subnets, and security groups. This module is needed for the specific tools and components of our ML platform.

### Modules {.unlisted .unnumbered}

The *modules* directory contains Terraform modules that are specific for setting up out ML Platform and provides the components to integrate the MLOps Framework, such as tools for model tracking (MLflow), workflow management (Airflow), or a integrated development environment (JupyterHub).

* `airflow` provides the Terraform module to deploy an Apache Airflow instance based on the Helm provider, which enables to orchestrate our ML workflows. The module is highly customized as it sets up necessary connections to other services, sets airflow variables that can be used by Data Scientists, creates an ingress ressource, and enables user management and authentication using Github.
* The `mlflow` module sets up MLflow to managing machine learning experiments and models. As MLflow does not natively provide a solution to deploy on Kubernetes, a custom Helm deployment is integrated that configures the necessary deployment, services, and ingress ressources.
* `jupyterhub` deploys a JupyterHub environment via Helm that enables multi-user notebook environment, suitable for collaborative data science and machine learning work. The Helm chart is highly customized providing user management and authentication via Github, provisioning ingress resources, and cloning a custom Github repository that provides all our Data Science and Machine Learning code.

### Prerequisites & Installation {.unlisted .unnumbered}

The installation and deployment process involves several key steps to ensure a smooth setup of your environment. Before proceeding with the installation, it's crucial to complete the following essential prerequisites: installing the necessary tools, establishing a GitHub organization along with OAuth apps, and obtaining a DNS name to link with your services.
Please adhere to the installation instructions of the repositories' [readme document](https://github.com/seblum/mlops-mlplatform-on-eks/blob/main/Installation.md).
