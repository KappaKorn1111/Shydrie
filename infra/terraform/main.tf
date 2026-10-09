provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "shydrie_raw" {
  bucket = "shydrie-raw-storage"
  force_destroy = true
}

resource "aws_s3_bucket" "shydrie_processed" {
  bucket = "shydrie-processed-storage"
  force_destroy = true
}

resource "aws_iam_role" "shydrie_worker" {
  name = "shydrie-worker-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = { Service = "ec2.amazonaws.com" }
      Action = "sts:AssumeRole"
    }]
  })
}
