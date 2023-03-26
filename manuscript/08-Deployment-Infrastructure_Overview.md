
# AWS Infrastructure Deployment

## Overview

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
