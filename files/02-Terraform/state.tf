terraform {
  backend "s3" {
    bucket = "some-bucket"
    key = "some-storage-key"
    region = "us-east-1"
  }
}