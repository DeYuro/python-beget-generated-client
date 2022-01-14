#!/bin/bash

prg=$0
if [ ! -e "$prg" ]; then
  case $prg in
    (*/*) exit 1;;
    (*) prg=$(command -v -- "$prg") || exit;;
  esac
fi
dir=$(
  cd -P -- "$(dirname -- "$prg")" && pwd -P
) || exit
prg=$dir/$(basename -- "$prg") || exit

dr=$(dirname "$prg")

rm -rf $dr/../internal/apiclient/vps
rm -rf $dr/../internal/apiclient/auth
mkdir -p $dr/../internal/apiclient/vps
mkdir -p $dr/../internal/apiclient/auth

docker run \
 --rm \
  -v $dr/../api/vps:/source \
  -v $dr/../internal/apiclient/vps:/local \
  --user $(id -u):$(id -g) \
  openapitools/openapi-generator-cli generate -g python -i /source/openapi.yaml \
  --additional-properties=packageName=vps_generated \
  --additional-properties=generateSourceCodeOnly=true  \
  -o /local \

mv $dr/../internal/apiclient/vps/vps_generated $dr/../vps_generated

docker run \
 --rm \
  -v $dr/../api/auth:/source \
  -v $dr/../internal/apiclient/auth:/local \
  --user $(id -u):$(id -g) \
  openapitools/openapi-generator-cli generate -g python -i /source/openapi.yaml \
  --additional-properties=packageName=auth_generated \
  --additional-properties=generateSourceCodeOnly=true  \
  -o /local

mv $dr/../internal/apiclient/auth/auth_generated $dr/../auth_generated
