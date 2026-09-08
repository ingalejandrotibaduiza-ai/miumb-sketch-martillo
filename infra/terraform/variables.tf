variable "environment" {
  description = "Ambiente de trabajo para el ERP de joyería."
  type        = string
  default     = "dev"

  validation {
    condition     = contains(["dev", "test", "prod"], var.environment)
    error_message = "El ambiente debe ser dev, test o prod."
  }
}

variable "database_engine" {
  description = "Motor de base de datos futuro."
  type        = string
  default     = "mongodb"
}
