
# COUNT
# resource "aws_iam_user" "count-example" {
#   count = 2
#   name  = "neo.${count.index}"
# }

# COUNT INDEX
resource "aws_iam_user" "count-index-example" {
  count = length(var.user_names)
  name  = var.user_names[count.index]
}

# # COUNT CONDITIONAL
# resource "aws_iam_user" "count-conditional-example" {
#   count = var.enable_private_users ? 1 : 0
#   name  = var.user_names[count.index]
# }

# FOR EACH
# resource "aws_iam_user" "for-each-example" {
#   for_each = toset(var.user_names)
#   name     = each.value
# }

# module "users" {  
#   source = "./iam-user"  

#   for_each  = toset(var.user_names)  
#   user_name = each.value  
# }


provider "aws" {
  region = "eu-central-1"
}

terraform {
  backend "s3" {
    bucket = "tutorial-terraform"
    key    = "some-storage-key"
    region = "eu-central-1"
  }
}