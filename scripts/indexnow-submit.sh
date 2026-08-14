#!/usr/bin/env bash
set -euo pipefail

HOST="sibe-cad.vercel.app"
KEY_FILE="834b662808ed78415e21e6edd3940f70482296a32e85195392a2573e3a8acf1f.txt"
KEY_LOCATION="https://${HOST}/${KEY_FILE}"
API_ENDPOINT="https://api.indexnow.org/indexnow"

if [[ ! -f "$KEY_FILE" ]]; then
  echo "IndexNow key file not found: $KEY_FILE" >&2
  exit 1
fi

KEY="$(tr -d '\r\n' < "$KEY_FILE")"

for attempt in {1..24}; do
  if curl --silent --fail --max-time 10 "$KEY_LOCATION" | grep -Fxq "$KEY"; then
    break
  fi
  if [[ "$attempt" -eq 24 ]]; then
    echo "IndexNow key file is not live at $KEY_LOCATION" >&2
    exit 1
  fi
  sleep 5
done

URLS=(
  "https://${HOST}/"
  "https://${HOST}/cloud-cad-management/"
  "https://${HOST}/features/cad-file-management/"
  "https://${HOST}/features/solidworks-revision-approval-workflow/"
  "https://${HOST}/features/solidworks-bom-management/"
  "https://${HOST}/features/remote-team-collaboration-for-solidworks-teams/"
  "https://${HOST}/cloud-pdm/solidworks-pdm-migration/"
  "https://${HOST}/sitemap.xml"
  "https://${HOST}/robots.txt"
  "https://${HOST}/llms.txt"
  "https://${HOST}/llms-full.txt"
)

PAYLOAD="$(printf '%s\n' "${URLS[@]}" | sed 's/.*/"&"/' | paste -sd, -)"
PAYLOAD="{\"host\":\"${HOST}\",\"key\":\"${KEY}\",\"keyLocation\":\"${KEY_LOCATION}\",\"urlList\":[${PAYLOAD}]}"

STATUS="$(curl --silent --show-error --output /tmp/indexnow-response.txt --write-out '%{http_code}' \
  -X POST "$API_ENDPOINT" \
  -H 'Content-Type: application/json; charset=utf-8' \
  --data "$PAYLOAD")"

cat /tmp/indexnow-response.txt
printf '\nIndexNow response: HTTP %s\n' "$STATUS"

case "$STATUS" in
  200|202) exit 0 ;;
  *) exit 1 ;;
esac
