terraform {
  required_version = ">= 1.6.0"

  required_providers {
    random = {
      source  = "hashicorp/random"
      version = "~> 3.6"
    }
  }
}

# Sprint 2 académico: no despliega recursos con costo.
# Modela nombres y estructura base para demostrar IaC sin proveedor cloud real.

resource "random_id" "suffix" {
  byte_length = 4
}

locals {
  project_name = "joyeria-martillo-erp"
  environment  = var.environment
  network_name = "${local.project_name}-${local.environment}-${random_id.suffix.hex}"
}

resource "random_id" "vpc_placeholder" {
  byte_length = 3
}

resource "random_id" "database_placeholder" {
  byte_length = 3
}

output "simulated_vpc_name" {
  value = local.network_name
}

output "simulated_database_name" {
  value = "${local.project_name}-db-${random_id.database_placeholder.hex}"
}
