variable "user_names" {
  description = "Create IAM users with these names"
  type        = list(string)
  default     = ["adam", "eve", "snake", "apple"]
}

resource "aws_iam_user" "example" {
  for_each = toset(var.user_names)
  name     = each.value
}

output "all_users" {  
  value = aws_iam_user.example  
}



# resource

module "users" {  
  source = "./iam-user"  
  
  for_each  = toset(var.user_names)  
  user_name = each.value  
}