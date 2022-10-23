locals {
  vpc_id = module.networking.vpc_id
}
module "networking" {
  source = "./networking"
}

# module "s3" {
#   source = "./s3"
# }

module "ec2" {
  source        = "./ec2"
  for_each      = toset(var.instance_names)
  instance_name = each.value
  instance_type = "t2.micro"
}


provider "aws" {
  region = "eu-central-1"
}

terraform {
  backend "s3" {
    # The bucket needs to be created manually beforehand
    bucket = "tutorial-terraform"
    key    = "some-storage-key"
    region = "eu-central-1"
  }
}