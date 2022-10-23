

output "all_users" {
  value = aws_iam_user.count-example
}

output "upper_names" {
  value = [for name in var.user_names : upper(name)]
}

output "short_upper_names" {
  value = [for name in var.user_names : upper(name) if length(name) < 5]
}

# FOR
output "for_directive" {
  value = "%{for name in var.user_names}${name}, %{endfor}"
}



