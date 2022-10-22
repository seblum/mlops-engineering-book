output "upper_names" {
  value = [for name in var.names : upper(name)]
}

output "short_upper_names" {
  value = [for name in var.names : upper(name) if length(name) < 5]
}


# for

output "for_directive" {  
  value = "%{ for name in var.names }${name}, %{ endfor }"  
}