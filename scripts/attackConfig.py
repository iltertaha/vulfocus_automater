CWE_ID = "CWE-78"
CVE_ID = "CVE-2019-15107"
IP_ADDR = ""
PORT_NO = "8082"

IMAGE_NAME    = "vulhub/webmin:1.910"
IMAGE_SRC     = "https://github.com/vulhub/vulhub/tree/master/webmin/CVE-2019-15107"
IMAGE_RUN_CMD = "sudo docker run -it -p 10000:10000 -d  vulhub/webmin:1.910"

MAIN_ATTACK_PATH = "~/TEST_ATTACKS/ATTACK_YAMLS/CWE-78_OS-Command-Injection/CVE-2019-15107_Payload.yaml"
MAIN_YAML_AUTHOR = "~/nuclei-templates/cves/2019/CVE-2019-15107.yaml (Original) is rewritten by HALE, referencing the MAIN_YAML_SOURCE"
MAIN_YAML_SOURCE = "https://github.com/jas502n/CVE-2019-15107"

