
data "aws_ami" "ubuntu" {

  most_recent = true

  filter {
    name = "name"
    # The AMI depends on the region you are in
    values = ["ubuntu/images/hvm-ssd/ubuntu-xenial-16.04-amd64-server-*"]
  }
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonial
}

resource "aws_instance" "web-instance" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type
  tags = {
    Name = var.instance_name
  }
}