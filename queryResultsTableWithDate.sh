#!/bin/bash
curl --silent -G -H "Accept: application/x-adm" -v -d 'mode=synchronous' --data-urlencode "aql=use steven;
          select * from EmergencyChannelResults where channelExecutionTime = datetime('$1'); 
    " http://promethium.ics.uci.edu:19002/sqlpp -w %{time_total} >> responses/responses.txt

echo "" >> responses/responses.txt
