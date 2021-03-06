## Update instance hostname with Public IP

**Instance ID** - The instance ID is a unique identifier that is found via the EC2 console. 
```
i-XXXXXXX
```

**DNS host zone** - The hostzone is a unique identifier that is found via the Route53 console or via the following command:
```
./public_ip_change.py --lookup
```

**DNS Hostname** - This is the hostname you wish to update with this script:
```
hostname.domain.com.
```

### Run the following:
```
./public_ip_change.py --id i-12345678 --hostzone Z123P456F789Z3 --hostname hostname.domain.com.
```