# Pseudocode — Computer Fingerprint Collector

BEGIN
  SET current_time = get current system time
  SET computer_name = get computer name
  SET ip_address = get IP address
  SET mac_address = get MAC address
  SET processor_model = get processor model
  SET operating_system = get OS name and version
  SET internet_speed = test internet download speed
  SET active_ports = get list of open ports
  SET unique_id = get system UUID or serial number

  VALIDATE all collected data
  SANITISE data to remove unwanted characters

  IF CSV file exists THEN
      APPEND new row with collected data
  ELSE
      CREATE new CSV file with headers
      ADD collected data as first row
  ENDIF
END
