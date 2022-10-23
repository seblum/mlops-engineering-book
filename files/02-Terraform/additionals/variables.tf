
variable "user_names" {
  description = "Create IAM users with these names"
  type        = list(string)
  default     = ["adam", "eve", "snake", "apple"]
}

variable "enable_private_users" {
  description = "Boolean to enable private users in conditional count"
  type = bool 
  default = true
}
