# post-install-test
A set of small tests to ensure your ZeroStack cluster is running properly.

## Dependencies
In order to run the post install tests download the cloud admin RC and certificate files out of the admin.local BU.
1. Zerostack rc file
2. Zerostack key file

### RC File

Use the below example to configure your RC file. <br />
<br />
USER_NAME=billybob <br />
USER_PASSWD=mypassword <br />
USER_DOMAIN=admin.local <br />
PROJECT_DOMAIN=admin.local <br />
USER_PROJECT=zs_default <br />
ZS_CERT_FILE=~/zs_Certificate_ca.bundle <br />
export OS_AUTH_URL=https://console.zerostack.com/os/6366ac07-6c56-5000-991d-b75607d02f32/regions/e333d4a5-4a74-6bfc-9f1f-1bd66da3f9e7/keystone/v3 <br />
export OS_CACERT=$ZS_CERT_FILE <br />
export OS_IDENTITY_API_VERSION=3 <br />
export OS_IMAGE_API_VERSION=1 <br />
export OS_VOLUME_API_VERSION=2 <br />
export OS_USERNAME=$USER_NAME <br />
export OS_USER_DOMAIN_NAME=$USER_DOMAIN <br />
export OS_PASSWORD=$USER_PASSWD <br />
export OS_PROJECT_NAME=$USER_PROJECT <br />
export OS_PROJECT_DOMAIN_NAME=$PROJECT_DOMAIN <br />
export OS_REGION='blah' <br />

## Git
1. git clone https://github.com/Zerostack-open/post-install-test.git

## Run tests
$ source ~/zsrc.txt <br />
$ python zs-post-install.py 
