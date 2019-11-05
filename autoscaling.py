int [] priority_list

for all (vnf in priority_list) do
	for all (instance in vnf) do
	{
		initialize cps_fin = null
		quaery requests for an instance instance
		calculate cps_req for the next interval
		setup the cps_min and cps_threshold for this instance

		if (cps_req > (cps_min + cps_threshold)) then
		{
			wf_core = 1.0
			
			if (machine is virtual) then
			{
				wf_core = 0.8
			}
			
			cps_fin = cps_req/wf_core
		}

		GHz_req = cps_fin * (10)^9
	}

	end for
end for