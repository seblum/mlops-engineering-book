provider "local" {
  version = "~> 1.4"
}
resource "local_file" "hello" {
  content = "Hello, Terraform"
  filename = "hello.txt"
}


# terraform init — Initializes the working directory which consists of all the configuration files
# terraform validate — Validates the configuration files in a directory
# terraform plan — Creates an execution plan to reach a desired state of the infrastructure
# terraform apply — Makes the changes in the infrastructure as defined in the plan
# terraform destroy — Deletes all the old infrastructure resources
