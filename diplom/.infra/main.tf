provider "google" {
  project = "my-project-terraform-407409"

  credentials = file("sevice-key.json")
}

resource "google_compute_instance" "vm_instance" {
  name         = "terraform-instance"
  machine_type = "e2-standard-2"
  zone         = "us-central1-c"
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    access_config {
    }
  }
}
