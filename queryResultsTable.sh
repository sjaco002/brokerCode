curl --silent -H "Accept: application/x-adm" -v -d 'mode=synchronous' --data-urlencode 'statement=use steven;
          select * from EmergencyChannelResults where channelExecutionTime > current_datetime()-day_time_duration("PT10S")
	;
    ' http://promethium.ics.uci.edu:19002/query/service -w %{time_total} >> responses/responses.txt

echo "" >> responses/responses.txt
