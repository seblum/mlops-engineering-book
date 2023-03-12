
# Infrastructure Deployment

## Structure

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
│   └── rds
│
└── modules
│   │
│   └── airflow
│   │
│   └── mlflow
│   │
│   └── jupyterhub
│
└── applications
    │
    └── airflow
    │
    └── mlflow
    │
    └── jupyterhub

```

**Infrastructure**

AWS resources for our EKS cluster that serves as the fundament of the mlops platform

**Modules**

Custom modules and tools we deploy on the AWS EKS environment

**Applications**

consists of helm Charts and values.yaml files
will be described and referenced in modules sections

## Infrastructure.VPC

vpc to set up securely

## Infrastructure.EKS

eks
two nodegroups. what are those?
ebs csi
autoscaler

## Infrastructure.RDS

rds for service if needed
attached to vpc
rds password & endpoint
outputs needed for..

## Modules.Airflow

user management
git repo airflow_dag

## Modules.Mlflow

https://pedro-munoz.tech/how-to-setup-mlflow-in-production/

https://kili-technology.com/data-labeling/machine-learning/how-to-manage-your-machine-learning-pipeline-with-mlflow

open endpoint - not very secure

### MLFlow Infrastructure


+ Create a docker image for the MLFlow tracking server.
+ Deploy Postgresql database on Kubernetes.
    + Helm to deploy PostgreSQL
+ Create YAML configurations for deployment, service and configmap to deploy the tracking server to Kubernetes.
    + The first thing we need to do is create the configmap and secrets for the tracking server.



## Modules.Jupyterhub

code-server custom
this is where we need ebs
user management
git repo airflow_dag
