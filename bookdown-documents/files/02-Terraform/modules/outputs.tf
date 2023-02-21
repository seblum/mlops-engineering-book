output "instance_address" {
  value       = aws_instance.awesome-instance.private_ip
  description = "Web server's private IP address"
}
