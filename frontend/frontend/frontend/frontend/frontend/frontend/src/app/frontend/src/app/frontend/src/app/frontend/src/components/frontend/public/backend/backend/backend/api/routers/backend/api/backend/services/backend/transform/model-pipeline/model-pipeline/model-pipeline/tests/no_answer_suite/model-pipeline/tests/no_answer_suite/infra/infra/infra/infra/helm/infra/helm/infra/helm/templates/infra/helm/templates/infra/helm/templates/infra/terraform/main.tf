provider "aws" {
  region = var.region
}

resource "aws_eks_cluster" "lazy_ai" {
  name     = "lazy-ai-cluster"
  role_arn = aws_iam_role.eks_role.arn

  vpc_config {
    subnet_ids = var.subnet_ids
  }
}

# TODO: Add S3, RDS (Postgres), Redis, IAM roles
