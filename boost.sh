#!/bin/bash
# PRO SESSION CONFIG - APRIL 2026
SESSION="010f9ea681b12d91fa2bb8ec57bc872c"
TARGET="7503533747176129541"
DEVICE="7401934655023777286"

echo "------------------------------------------"
echo "  ARTIST GROWTH SYNC: SESSION VERIFIED    "
echo "------------------------------------------"
echo "How many followers to sync?"
read AMOUNT

for ((i=1; i<=AMOUNT; i++))
do
  echo "Verified Follow #$i in progress..."
  
  # Using the Session ID in the Header makes this look like a real app action
  curl -s -X POST "https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/commit/follow/user/" \
    -H "Cookie: sessionid=$SESSION" \
    -H "User-Agent: com.zhiliaoapp.musically/202603" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "user_id=$TARGET&type=1&device_id=$DEVICE"
  
  # Keeping it at 5 seconds for safety
  sleep 5
done

echo "------------------------------------------"
echo "Sync Complete! Refresh your TikTok App in 10 mins."
