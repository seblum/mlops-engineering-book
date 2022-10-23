# CORE CONCEPTS - PROVIDERS

provider "aws" {
  region = "eu-central-1"
}

# STATE

terraform {
  backend "s3" {
    # The bucket needs to be created manually beforehand
    bucket = "tutorial-terraform" 
    key = "some-storage-key"
    region = "eu-central-1"
  }
}