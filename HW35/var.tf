variable "project" {
  default = "my-project-terraform-407409"
}

variable "region" {
  default = "us-central1"
}

variable "zone" {
  type    = list(string)
  default = ["us-central1-a", "us-central1-b", "us-central1-c"]
}

variable "credentials" {
  default = "hw35.json"
}

variable "machine_type" {
  default = "e2-standard-2"
}

variable "image_family" {
  default = "debian-12"
}

variable "image_project" {
  default = "debian-cloud"
}

variable "enable_public_ip" {
  default = "true"
}
