output "aws_security_group" {
  value       = aws_security_group.tf-tutorial-sg.id
  description = "AWS security group of the given vpc network"
}

output "aws_subnet" {
  value       = aws_subnet.tf-tutorial-subnet.id
  description = "AWS subnet of the given vpc network"
}

output "vpc_id" {
  value       = aws_vpc.tf-tutorial-vpc.id
  description = "AWS ID of the VPC"
}