### MLFlow Infrastructure


+ Create a docker image for the MLFlow tracking server.
+ Deploy Postgresql database on Kubernetes.
    + Helm to deploy PostgreSQL
+ Create YAML configurations for deployment, service and configmap to deploy the tracking server to Kubernetes.
    + The first thing we need to do is create the configmap and secrets for the tracking server.
