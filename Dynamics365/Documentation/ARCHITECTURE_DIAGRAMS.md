# Sales Order Customs Broker Tracking - Architecture Diagram

## System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        PRESENTATION LAYER                            │
│                         (User Interface)                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐              │
│  │   Customer   │  │ Sales Order  │  │    Load      │              │
│  │     Form     │  │     Form     │  │     Form     │              │
│  │              │  │              │  │              │              │
│  │ [BrokerId]   │  │ [BrokerId]   │  │ [BrokerId]   │              │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘              │
│         │                 │                 │                        │
│         │                 │                 │                        │
│  ┌──────┴───────┐  ┌──────┴───────┐  ┌──────┴───────┐              │
│  │    Sales     │  │   Packing    │  │    List      │              │
│  │  Agreement   │  │     Slip     │  │    Pages     │              │
│  │     Form     │  │   Journal    │  │              │              │
│  │              │  │              │  │  (Filtering) │              │
│  │ [BrokerId]   │  │ [BrokerId]   │  │              │              │
│  └──────────────┘  └──────────────┘  └──────────────┘              │
│                                                                       │
└───────────────────────────────┬───────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      BUSINESS LOGIC LAYER                            │
│                      (X++ Class Extensions)                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌──────────────────────────────────────────────────────────┐       │
│  │  CustTable_BrokerExtension                              │       │
│  │  - validateWrite(): Validate broker exists              │       │
│  └──────────────────────────────────────────────────────────┘       │
│                                                                       │
│  ┌──────────────────────────────────────────────────────────┐       │
│  │  SalesTable_BrokerExtension                             │       │
│  │  - initFromCustTable(): Default from customer           │       │
│  │  - initFromSalesAgreementHeader(): Default from agreement│       │
│  │  - validateWrite(): Validate broker exists              │       │
│  └──────────────────────────────────────────────────────────┘       │
│                                                                       │
│  ┌──────────────────────────────────────────────────────────┐       │
│  │  SalesAgreementHeader_BrokerExtension                   │       │
│  │  - initFromCustTable(): Default from customer           │       │
│  │  - validateWrite(): Validate broker exists              │       │
│  └──────────────────────────────────────────────────────────┘       │
│                                                                       │
│  ┌──────────────────────────────────────────────────────────┐       │
│  │  WHSLoadTable_BrokerExtension                           │       │
│  │  - initFromSalesTable(): Transfer from sales order      │       │
│  │  - validateWrite(): Validate broker exists              │       │
│  └──────────────────────────────────────────────────────────┘       │
│                                                                       │
│  ┌──────────────────────────────────────────────────────────┐       │
│  │  CustPackingSlipJour_BrokerExtension                    │       │
│  │  - initFromSalesTable(): Transfer from sales order      │       │
│  │  - initFromWHSLoadTable(): Transfer from load           │       │
│  └──────────────────────────────────────────────────────────┘       │
│                                                                       │
└───────────────────────────────┬───────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         DATA LAYER                                   │
│                    (Table Extensions)                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐              │
│  │  CustTable   │  │ SalesTable   │  │ WHSLoadTable │              │
│  │              │  │              │  │              │              │
│  │ + BrokerId   │  │ + BrokerId   │  │ + BrokerId   │              │
│  │   (string)   │  │   (string)   │  │   (string)   │              │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘              │
│         │                 │                 │                        │
│         │ FK to           │ FK to           │ FK to                  │
│         │ TMSCarrier      │ TMSCarrier      │ TMSCarrier             │
│         │                 │                 │                        │
│  ┌──────┴────────────┐  ┌─┴───────────────┐                        │
│  │ SalesAgreement    │  │ CustPacking     │                        │
│  │ Header            │  │ SlipJour        │                        │
│  │                   │  │                 │                        │
│  │ + BrokerId        │  │ + BrokerId      │                        │
│  │   (string)        │  │   (string)      │                        │
│  └───────┬───────────┘  └────────┬────────┘                        │
│          │                       │                                   │
│          │ FK to                 │ FK to                             │
│          │ TMSCarrier            │ TMSCarrier                        │
│          │                       │                                   │
│          └───────────┬───────────┘                                  │
│                      │                                               │
│                      ▼                                               │
│           ┌──────────────────────┐                                  │
│           │    TMSCarrier        │                                  │
│           │  (Reference Table)   │                                  │
│           │                      │                                  │
│           │  ShipCarrierId (PK)  │◄── All BrokerId fields           │
│           │  Name                │    reference this table          │
│           │  Mode                │                                  │
│           └──────────────────────┘                                  │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

## Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                         BROKER DATA FLOW                             │
└─────────────────────────────────────────────────────────────────────┘

Step 1: Customer Setup
┌────────────────┐
│   CustTable    │
│                │
│ BrokerId =     │
│ "CB001"        │
└────────┬───────┘
         │
         │ User assigns broker
         │
         ▼
┌────────────────────────────────────┐
│  Broker stored in customer master  │
└────────────────────────────────────┘


Step 2A: Sales Agreement Creation (Optional)
         │
         │ initFromCustTable()
         ▼
┌────────────────────────┐
│ SalesAgreementHeader   │
│                        │
│ BrokerId = "CB001"     │  ◄── Defaults from customer
│                        │
└────────┬───────────────┘
         │
         │ User can override
         │
         ▼


Step 2B: Sales Order Creation (Direct or from Agreement)
         │
         │ initFromCustTable() OR
         │ initFromSalesAgreementHeader()
         ▼
┌────────────────────────┐
│    SalesTable          │
│                        │
│ BrokerId = "CB001"     │  ◄── Defaults from customer/agreement
│                        │
└────────┬───────────────┘
         │
         │ User can override
         │ Order confirmed
         │
         ▼


Step 3: Load Creation
         │
         │ initFromSalesTable()
         ▼
┌────────────────────────┐
│   WHSLoadTable         │
│                        │
│ BrokerId = "CB001"     │  ◄── Transfers from sales order
│                        │
└────────┬───────────────┘
         │
         │ Load processing
         │
         ▼


Step 4: Packing Slip Generation
         │
         │ initFromSalesTable() OR
         │ initFromWHSLoadTable()
         ▼
┌─────────────────────────┐
│  CustPackingSlipJour    │
│                         │
│ BrokerId = "CB001"      │  ◄── Displays from sales order/load
│ (Read-only)             │
└─────────────────────────┘
```

## Component Interaction Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                    USER INTERACTION FLOW                             │
└─────────────────────────────────────────────────────────────────────┘

1. Sales Rep opens Customer form
            │
            ▼
2. Assigns Broker ID: CB001
            │
            ▼
3. Creates Sales Order for customer
            │
            ▼
4. System calls: SalesTable.initFromCustTable()
            │
            ▼
5. Broker ID "CB001" auto-populates
            │
            ▼
6. Sales Rep can override if needed
            │
            ▼
7. Confirms sales order
            │
            ▼
8. System calls: WHSLoadTable.initFromSalesTable()
            │
            ▼
9. Load created with Broker ID "CB001"
            │
            ▼
10. Warehouse processes and ships
            │
            ▼
11. System calls: CustPackingSlipJour.initFromWHSLoadTable()
            │
            ▼
12. Packing slip shows Broker ID "CB001" (read-only)
            │
            ▼
13. Complete - Broker tracked through entire process
```

## Validation Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                      VALIDATION FLOW                                 │
└─────────────────────────────────────────────────────────────────────┘

User enters Broker ID
         │
         ▼
┌────────────────────────────┐
│ validateWrite() triggered  │
└────────┬───────────────────┘
         │
         ▼
┌─────────────────────────────┐
│ Check if BrokerId is empty  │
└────────┬────────────────────┘
         │
         ├─── Yes ──► Allow save (optional field)
         │
         └─── No ──► Continue validation
                      │
                      ▼
          ┌──────────────────────────────┐
          │ Query TMSCarrier table       │
          │ WHERE ShipCarrierId =        │
          │       entered BrokerId       │
          └──────────┬───────────────────┘
                     │
                     ├─── Found ──► Allow save
                     │
                     └─── Not Found ──► Display error
                                        "Broker ID does not exist"
                                        Block save
```

## Extension Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    EXTENSION PATTERN                                 │
└─────────────────────────────────────────────────────────────────────┘

Base D365 Application
         │
         │ (No overlayering)
         │
         ▼
Extension Framework
         │
         ├─── EDT Extension
         │    └─── TMSBrokerId extends TMSShipCarrierId
         │
         ├─── Table Extensions (5)
         │    ├─── CustTable_Extension
         │    ├─── SalesTable_Extension
         │    ├─── SalesAgreementHeader_Extension
         │    ├─── WHSLoadTable_Extension
         │    └─── CustPackingSlipJour_Extension
         │
         ├─── Form Extensions (5)
         │    ├─── CustTable_Extension
         │    ├─── SalesTable_Extension
         │    ├─── SalesAgreement_Extension
         │    ├─── WHSLoadTable_Extension
         │    └─── CustPackingSlipJour_Extension
         │
         └─── Class Extensions (5)
              ├─── CustTable_BrokerExtension
              ├─── SalesTable_BrokerExtension
              ├─── SalesAgreementHeader_BrokerExtension
              ├─── WHSLoadTable_BrokerExtension
              └─── CustPackingSlipJour_BrokerExtension

All extensions use Chain of Command (CoC)
└─── Upgrade compatible
└─── No code conflicts
└─── Maintainable
```

---

## Deployment Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                   DEPLOYMENT PIPELINE                                │
└─────────────────────────────────────────────────────────────────────┘

Development Environment
         │
         │ 1. Import metadata
         │ 2. Build project
         │ 3. Sync database
         │
         ▼
Create Deployable Package
         │
         │ Package as .zip
         │
         ▼
Upload to LCS Asset Library
         │
         │
         ▼
┌────────────────────────┐
│  UAT Environment       │ ◄── Deploy package
│                        │     Run tests
│  - Testing             │     Validate
│  - Validation          │
└────────┬───────────────┘
         │
         │ Approval
         │
         ▼
┌────────────────────────┐
│ Production Environment │ ◄── Deploy package
│                        │     Go live
│  - Live System         │     Monitor
│  - End Users           │
└────────────────────────┘
```

---

**Legend:**
- `│` `├` `└` `┌` `┐` : Flow connections
- `▼` `►` : Direction of flow
- `FK` : Foreign Key relationship
- `PK` : Primary Key
- `CoC` : Chain of Command

---

This architecture ensures:
- ✅ Clean separation of concerns
- ✅ Maintainable code structure
- ✅ Upgrade compatibility
- ✅ Data integrity
- ✅ User-friendly interface
- ✅ Comprehensive validation

