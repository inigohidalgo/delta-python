# Delta tables without spark

## Setup

### Storage

99% of the time should use cloud-based storage. MinIO is a good option for local development.

```bash
docker run \
   -p 9000:9000 \
   -p 9001:9001 \
   --user $(id -u):$(id -g) \
   --name minio1 \
   -e "MINIO_ROOT_USER=ROOTUSER" \
   -e "MINIO_ROOT_PASSWORD=CHANGEME123" \
   -v ${HOME}/minio/data:/data \
   quay.io/minio/minio server /data --console-address ":9001"
```

### Requirements

Main dependency is `deltalake` which is a wrapper around `python-rs`

Install using `requirements.txt`
