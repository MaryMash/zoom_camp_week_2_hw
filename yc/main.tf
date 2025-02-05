terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone = "ru-central1-a"
}

resource "yandex_storage_bucket" "s3_bucket" {
  bucket = var.s3_bucket_name

  lifecycle_rule {
    id      = "cleanupoldlogs"
    enabled = true
    expiration {
      days = 1
    }
  }
}