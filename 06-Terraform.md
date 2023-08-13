# Terraform

Terraform is an open-source, declarative programming language developed by HashiCorp and allows to create both on-prem and cloud resources in the form of writing code. This is also know as Infrastructure as Code (IAC). There are several IaC tools in the market today and Terraform is only one of them. Yet it is a well known and established tool and during the course of this project we only focus on this.

[HashiCorp](https://www.terraform.io/docs) describes that:
<blockquote>
Terraform is an infrastructure as code (IaC) tool that allows you to build, change, and version infrastructure safely and efficiently. This includes both low-level components like compute instances, storage, and networking, as well as high-level components like DNS entries and SaaS features. 
</blockquote> 


This means that users are able to manage and provision an entire IT infrastructure using machine-readable definition files and thus allowing faster execution when configuring infrastructure, as well as enableing full traceability of changes. Terraform comes with several hundred different providers that can be used to provision infrastructure, such as Amazon Web Services (AWS), Azure, Google Cloud Platform (GCP), Kubernetes, Helm, GitHub, Splunk, DataDog, etc.

The given chapter introduces the concepts & usage of Terraform which will be needed to create the introduced MLOps Airflow deployment in an automated and tracable way. We will learn how to use Terraform to provision ressources as well as to structure a Terraform Project.


### Prerequisites {.unlisted .unnumbered}

To be able to follow this tutorial, one needs to have the AWS CLI installed as well as the AWS credentials set up. Needles to say an AWS accounts needs to be present. It is also recommended to have basic knowledge of the AWS Cloud as this tutorials used the AWS infrastructure to provision cloud resources. The attached resource definitions are specified to the AWS region `eu-central-1`. It might be necessary to change accordingly if you are set in another region. 
Further, Terraform itself needs to be installed. Please refer to the corresponding sites. The scripts are run under Terraform version `v1.2.4`. Later releases might have breaking changes. One can check its installation via `terraform version`.
