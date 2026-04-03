## Script Architecture (Mermaid)

```mermaid
flowchart TD

    A([main()]) --> B["Collect System Info<br/>get_system_info()"]
    A --> C["Collect Network Info<br/>get_network_info()"]
    A --> D["Test Internet Speed<br/>test_internet_speed()"]
    A --> E["Get Unique ID<br/>get_unique_id()"]

    B --> F[Merge Data]
    C --> F
    D --> F
    E --> F

    F --> G["Validate Data<br/>validate_data()"]
    G --> H["Sanitise Data<br/>sanitise_data()"]

    H --> I{CSV Exists?}

    I -->|Yes| J["Append to CSV<br/>append_to_csv()"]
    I -->|No| K["Create CSV + Write Header<br/>write_new_csv()"]

    J --> L([End])
    K --> L([End])
```
