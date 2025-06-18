# holbertonschool-hbnb
# HBnB Evolution - Technical Documentation

##  Project Overview

**HBnB Evolution** is a simplified AirBnB-like application designed to manage users, places, reviews, and amenities. The objective of this phase is to build complete technical documentation that defines the architecture, core business logic, and data interactions within the system. This documentation will serve as a foundation for implementation.

## Team Members

* Munira Alsubaie
* Abdullah Alameeri
* Mohammed Alahmari
  
##  Table of Contents

1. [High-Level Package Diagram](#1-high-level-package-diagram)
2. [Class Diagram: Business Logic Layer](#2-class-diagram-business-logic-layer)
3. [Sequence Diagrams for API Calls](#3-sequence-diagrams-for-api-calls)
4. [Design Rationale and Explanatory Notes](#4-design-rationale-and-explanatory-notes)

---

## 1. High-Level Package Diagram

### Description

Illustrates the 3-tier architecture (Presentation, Business Logic, Persistence) and uses the **Facade Pattern** to decouple layers.

![Package Diagram](https://raw.githubusercontent.com/z502wa/holbertonschool-hbnb/main/part1/hbnb-package-diagram.png)

* **Presentation Layer**: Handles API endpoints, user interface interactions.
* **Business Logic Layer**: Contains core operations and validation logic.
* **Persistence Layer**: Manages database interactions.

---

## 2. Class Diagram: Business Logic Layer

### Description

UML diagram showing entities, attributes, methods, and relationships in the business logic.

```mermaid
classDiagram
    direction LR

    class User {
        -id: int
        -first_name: string
        -last_name: string
        -email: string
        -password: string
        -is_admin: boolean
        -created_at: datetime
        -updated_at: datetime
        +register(): void
        +updateProfile(): void
        +delete(): void
    }

    class Place {
        -id: int
        -title: string
        -description: string
        -price: float
        -latitude: float
        -longitude: float
        -created_at: datetime
        -updated_at: datetime
        +create(): void
        +update(): void
        +delete(): void
    }

    class Review {
        -id: int
        -rating: int
        -comment: string
        -created_at: datetime
        -updated_at: datetime
        +create(): void
        +update(): void
        +delete(): void
    }

    class Amenity {
        -id: int
        -name: string
        -description: string
        -created_at: datetime
        -updated_at: datetime
        +create(): void
        +update(): void
        +delete(): void
    }

    User --> "*" Place : owns
    Place --> "*" Review : has
    User --> "*" Review : writes
    Place --> "*" Amenity : includes
```

---

## 3. Sequence Diagrams for API Calls

### 3.1 User Registration

```mermaid
sequenceDiagram
    participant User
    participant API as "API /register"
    participant Service as "UserService"
    participant DB as "Database"

    User->>API: POST /register
    API->>Service: validateAndCreateUser()
    Service->>DB: insertUser()
    DB-->>Service: success
    Service-->>API: return 201
    API-->>User: User created
```

### 3.2 Place Creation

```mermaid
sequenceDiagram
    participant Owner
    participant API as "API /places"
    participant Service as "PlaceService"
    participant DB as "Database"

    Owner->>API: POST /places
    API->>Service: createPlace()
    Service->>DB: insertPlace()
    DB-->>Service: success
    Service-->>API: return 201
    API-->>Owner: Place created
```

### 3.3 Review Submission

```mermaid
sequenceDiagram
    participant User
    participant API as "API /places/:id/review"
    participant Service as "ReviewService"
    participant DB as "Database"

    User->>API: POST /places/1/review
    API->>Service: validateAndCreateReview()
    Service->>DB: insertReview()
    DB-->>Service: success
    Service-->>API: return 201
    API-->>User: Review added
```

### 3.4 Fetching List of Places

```mermaid
sequenceDiagram
    participant User
    participant API as "GET /places"
    participant Service as "PlaceService"
    participant DB as "Database"

    User->>API: GET /places
    API->>Service: fetchPlaces(filters)
    Service->>DB: queryPlaces()
    DB-->>Service: results
    Service-->>API: return JSON
    API-->>User: display places
```

---

## 4. Design Rationale and Explanatory Notes

### Architecture Choices

* **Facade Pattern**: Used to simplify and standardize interactions between Presentation and Business Logic.
* **3-layered Design**: Promotes maintainability, modularity, and clear responsibility separation.

### Entity Design Decisions

* All entities include `created_at` and `updated_at` for audit.
* Relationships reflect real-world associations (e.g., Users write Reviews, Places have Amenities).

### Sequence Flow Explanation

Each API call goes through:

1. **Presentation Layer** for input/response handling.
2. **Business Logic Layer** for validation and core logic.
3. **Persistence Layer** for DB operations.

---

## Final Notes

* All diagrams were created using [Mermaid.js](https://mermaid.js.org/).
* This document is meant to serve as the primary reference for HBnB’s implementation phase.

> Prepared by Team | June 2025
