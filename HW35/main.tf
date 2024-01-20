terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.12.0"
    }
  }
}

provider "google" {
  project     = var.project
  region      = var.region
  zone        = var.zone[1]
  credentials = var.credentials
}

resource "google_storage_bucket" "hwbucket" {
  name          = "hw35-bucket"
  location      = var.region
  storage_class = "STANDARD"
}

resource "google_storage_bucket_object" "file_key" {
  name         = "key_sa"
  source       = var.credentials
  content_type = "text/plain"
  bucket       = google_storage_bucket.hwbucket.name
}

terraform {
  backend "gcs" {
    bucket      = "hw35-bucket"
    prefix      = "terraform/state"
    credentials = "hw35.json"
  }
}

data "google_compute_image" "debian_image" {
  family  = var.image_family
  project = var.image_project
}

data "http" "ip-name" {
  url = "https://icanhazip.com"
}

output "my-ip" {
  # value = google_compute_instance.default.network_interface.0.access_config.0.nat_ip
  value = chomp(data.http.ip-name.response_body)
}

resource "google_compute_instance" "tfinstance" {
  name         = "tf-instance"
  machine_type = var.machine_type
  zone         = var.zone[1]

  tags = ["foo", "bar", "test"]

  boot_disk {
    initialize_params {
      image = data.google_compute_image.debian_image.self_link
      size  = 15
    }
  }

  network_interface {
    network = "default"
    dynamic "access_config" {
      for_each = var.enable_public_ip ? [""] : ["Ephemeral public IP"]
      content {
      }
    }
  }
}

resource "google_compute_firewall" "rules" {
  name     = "my-firewall-rule"
  network  = "default"
  priority = "1111"

  allow {
    protocol = "icmp"
  }

  allow {
    protocol = "udp"
    ports    = ["0-65535"]
  }

  allow {
    protocol = "tcp"
    ports    = ["0-65535"]
  }

  source_ranges = ["0.0.0.0/0"] # ["$chomp(data.http.ip-name.response_body)/32"]
  target_tags   = ["web", "test", "foo"]
}
