
# OUTPUT COUNT
# output "all_users_count" {
#   value = aws_iam_user.count-example
# }

# OUTPUT COUNT LIST
output "all_users_count_list" {
  value = aws_iam_user.count-index-example
}

# FOR EACH
# output "all_users_for_each" {
#   value = aws_iam_user.for-each-example
# }


# FOR ON LIST
# output "upper_names" {
#   value = [for name in var.user_names : upper(name)]
# }

# output "short_upper_names" {
#   value = [for name in var.user_names : upper(name) if length(name) < 5]
# }

# FOR ON STRING
# output "for_directive" {
#   value = "%{for name in var.user_names}${name}, %{endfor}"
# }



