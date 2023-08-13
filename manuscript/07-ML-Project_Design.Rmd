# ML Platform Design

ML platforms can be set up in various ways to apply MLOps practices to the machine learning workflow.
(1) SaaS tools provide an integrated development and management experience, with an aim to offer an end-to-end process. (2) Custom-made platforms offer high flexibility and can be tailored to specific needs. However, integrating multiple different services requires significant engineering effort. (3) Many cloud providers offer a mix of SaaS and custom-tailored platforms, providing a relatively well-integrated experience while remaining open enough to integrate other services.

This project involves building a custom-tailored ML platform focused on MLOps engineering, as the entire infrastructure will be set up from scratch. An exemplary ML platform will be developed using Airflow and MLflow for management during the machine learning lifecycle and JupyterHub to provide an integrated development environment. 

Even though there are workflow tools better designed for machine learning pipelines, for example Kubeflow Pipelines, Airflow and MLflow can leverage and an combine there functionalities to provide similar capabilites. Airflow provides the workflow management for the platform whilst MLflow is used for machine learning tracking. MLflow further allow to register each model effortlessly. As an MLOps plattform should also provide an environment to develop machine learning model code, JupyterHub will be deployed to be able to develop code in the cloud and without the need for a local setup. The coding environment will synchronize with Airflow's DAG repository to seamlessly integrate the defined models within the workflow management.
Airflow and MLflow are very flexible with their running environment and their stack would be very suitable for small scale systems, where there is no need for a setup maintaining a Kubernetes cluster. While it would be possible to run anything on a docker/docker-compose setup, this work will scale the mentioned tools to a Kubernetes cluster in the cloud to fully enable the concept of an MLOps plattform.
The infrastructure will be maintained using the Infrastructure as Code tool *Terraform*, and incorporate best Ops practices such as CI/CD and automation. The project will also incorporate the work done by data and machine learning scientists since basic machine learning models will be implemented and run on the platform.


![](images/01-Introduction/airflow-on-eks-basic.drawio.svg){ width=100% }

The following chapters give an introductory tutorial on each of the previously introduced tools. A machine learning workflow using Airflow is set up on the deployed infrastructure, including data preprocessing, model training, and model deployment, as well as tracking the experiment and deploying the model into production using MLFlow. 

The necessary AWS infrastructure is set up using Terraform. This includes creating an AWS EKS cluster and the associated ressources like a virtual private cloud (VPC), subnets, security groups, IAM roles, as well as further AWS ressources needed to deploy custom modules.  Networking is handled by AWS Application Load Balancing service or Ingress controller to route traffic to the correct service/pod in the cluster.
Once the EKS cluster is set up, Kubernetes can be used to deploy and manage applications on the cluster. Helm, a package manager for Kubernetes, is used to manage the deployment of Airflow and MLflow. The EKS cluster allows for easy scalability and management of the platforms. The code is made public on a Github repository and Github Actions is used for automating the deployment of the infrastructure using CI/CD principles. 

Once the infrastructure is set up, machine learning models can be trained on the EKS cluster as Kubernetes pods, using Airflows scheduling processes. Airflow's ability to scan local directories or Git repositories will be used to import the relevant machine learning code from second Github repository.
Similarly, to building Airflow workflows, the machine learning code will also include using the MLFlow API to allow for model tracking and storage. Github Actions is used as a CI/CD pipeline to automatically build, test, and deploy the machine learning model code to this repository similarly as it is used in the repository for the infrastructure. 

Model serving is done via Seldon, which allows for automatic scalability and seamlessly integrates with MLflow. Monitoring and logging is achieved using Prometheus & Grafana to monitor the health and performance of the EKS cluster and its components, such as worker nodes, Kubernetes pods, etc and similarly for monitoring the deployed models as applications.

Whereas the deployment of the infrastructure would be taken care of by MLOps-, DevOps-, and Data Engineers, the development of the Airflow workflows including MLFlow would be taken care of by Data Scientist and ML Engineers.
