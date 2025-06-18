## ✅ Sequence Diagram: User Registration

```mermaid
sequenceDiagram
    participant User
    participant API as "API /register"
    participant Service as "UserService"
    participant DB as "Database"

    User->>API: POST /register {name, email, password}
    API->>Service: validateAndCreateUser(data)
    Service->>DB: insertUser(data)
    DB-->>Service: success
    Service-->>API: return 201 + userJSON
    API-->>User: 201 Created (user info)
