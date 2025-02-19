#!/bin/bash

set -e

DIST_TAG=$1
DIST_VER=$2
SPEC_DIR=$3
STAGE_DIR=$4
PH_BUILDER_TAG=$5
ARCH=x86_64

source common.sh

# Docker image for flannel
fn="${SPEC_DIR}/flannel/flannel.spec"
FLANNEL_VER=$(get_spec_ver "${fn}")
FLANNEL_VER_REL=${FLANNEL_VER}-$(get_spec_rel "${fn}")
FLANNEL_RPM=flannel-${FLANNEL_VER_REL}${DIST_TAG}.${ARCH}.rpm
FLANNEL_RPM_FILE=${STAGE_DIR}/RPMS/$ARCH/${FLANNEL_RPM}
FLANNEL_TAR=flannel-v${FLANNEL_VER_REL}.tar

if [ ! -f ${FLANNEL_RPM_FILE} ]; then
  echo "flannel RPM ${FLANNEL_RPM_FILE} not found. Exiting.."
  exit 1
fi

IMG_NAME=vmware/photon-${DIST_VER}-flannel:v${FLANNEL_VER}

IMG_ID=$(docker images -q ${IMG_NAME} 2> /dev/null)
if [[ ! -z "${IMG_ID}" ]]; then
  echo "Removing image ${IMG_NAME}"
  docker rmi -f ${IMG_NAME}
fi

mkdir -p tmp/flannel
cp ${FLANNEL_RPM_FILE} tmp/flannel/
pushd ./tmp/flannel
cmd="cd '${PWD}' && rpm2cpio '${FLANNEL_RPM}' | cpio -vid"
if ! rpmSupportsZstd; then
  docker run --rm --privileged -v ${PWD}:${PWD} $PH_BUILDER_TAG bash -c "${cmd}"
else
  eval "${cmd}"
fi
popd

start_repo_server

docker build --rm -t ${IMG_NAME} -f Dockerfile.flannel .
docker save -o ${FLANNEL_TAR} ${IMG_NAME}
gzip ${FLANNEL_TAR}
mv -f ${FLANNEL_TAR}.gz ${STAGE_DIR}/docker_images/

rm -rf ./tmp
