resource "aws_instance" "my-instance" {
  ami           = "ami-0ddbdea833a8d2f0d"
  instance_type = "t2.micro"
  
  tags = {
    Name = "my-instance"
    ManagedBy = "Terraform"
  }
}