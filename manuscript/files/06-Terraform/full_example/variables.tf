variable "instance_names" {
  type        = list(string)
  default     = ["instance-one", "instance-two", "instance-three", "instance-four"]
  description = "Names of the aws instances to be created"
}
