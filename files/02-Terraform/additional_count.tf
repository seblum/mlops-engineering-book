resource "aws_iam_user" "example" {
  count = 3
  name  = "neo.${count.index}"
}

variable "user_names" {
  description = "Create IAM users with these names"
  type        = list(string)
  default     = ["adam", "eve", "snake", "apple"]
}

resource "aws_iam_user" "example" {
  count = length(var.user_names) # returns the number of items in the given array
  name  = var.user_names[count.index]
}



# delete
variable "user_names" {
  description = "Create IAM users with these names"
  type        = list(string)
  default     = ["adam", "eve", "apple"]
}

resource "aws_iam_user" "example" {
  count = length(var.user_names) # returns the number of items in the given array
  name  = var.user_names[count.index]
}



# conditional
resource "example-1" "example" {
  count = var.enable_autoscaling ? 1 : 0
  name  = var.user_names[count.index]
}