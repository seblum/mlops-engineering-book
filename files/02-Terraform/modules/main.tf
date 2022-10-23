locals {
  vpc_id = module.networking.vpc_id
}
module "networking" {
  source = "./networking"
}



resource "aws_instance" "awesome-instance" {
  ami           = "ami-09042b2f6d07d164a"
  instance_type = "t2.micro"

  tags = {
    Name = var.instance_name
  }
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