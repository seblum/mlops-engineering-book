locals {
  vpc_id = module.network.vpc_id
}
module "network" {
  source = "./network"
}
module "service1" {
  source = "./service1"
  vpc_id = local.vpc_id
}
module "service2" {
  source = "./service2"
  vpc_id = local.vpc_id
}


resource "aws_instance" "awesome-instance" {
  ami           = "ami-0ddbdea833a8d2f0d"
  instance_type = "t2.micro"

  tags = {
    Name = var.instance_name
  }
}


module "network" {
  source           = "./networking"
  create_public_ip = true
  environment      = "prod"
}
