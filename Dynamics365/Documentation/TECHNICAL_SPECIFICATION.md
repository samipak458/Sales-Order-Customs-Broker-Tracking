# Technical Specification - Sales Order Customs Broker Tracking

## Document Information

**Document Title:** Technical Specification for SCM0603 - Customs Broker Tracking
**Version:** 1.0
**Date:** 2024
**Prepared for:** Leggett & Platt Automotive

## 1. Technical Architecture

### 1.1 System Components

The implementation consists of the following technical components:

```
┌─────────────────────────────────────────────────────┐
│           Presentation Layer (Forms)                 │
│  - CustTable Form                                   │
│  - SalesTable Form                                  │
│  - SalesAgreement Form                              │
│  - WHSLoadTable Form                                │
│  - CustPackingSlipJour Form                         │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│         Business Logic Layer (Classes)               │
│  - CustTable_BrokerExtension                        │
│  - SalesTable_BrokerExtension                       │
│  - SalesAgreementHeader_BrokerExtension             │
│  - WHSLoadTable_BrokerExtension                     │
│  - CustPackingSlipJour_BrokerExtension              │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│           Data Layer (Tables)                        │
│  - CustTable (Extended)                             │
│  - SalesTable (Extended)                            │
│  - SalesAgreementHeader (Extended)                  │
│  - WHSLoadTable (Extended)                          │
│  - CustPackingSlipJour (Extended)                   │
│  - TMSCarrier (Reference)                           │
└─────────────────────────────────────────────────────┘
```

### 1.2 Extension Model

All customizations use the Dynamics 365 extension model:
- No overlayering of base application
- Table extensions for new fields
- Form extensions for UI modifications
- Class extensions for business logic
- Full upgrade compatibility

## 2. Data Model

### 2.1 Extended Data Type (EDT)

**Name:** TMSBrokerId

```xml
<AxEdt>
  <Name>TMSBrokerId</Name>
  <Extends>TMSShipCarrierId</Extends>
  <Label>Broker ID</Label>
  <HelpText>Customs broker identification</HelpText>
  <FormHelp>Customs broker assigned to handle customs clearance</FormHelp>
  <ReferenceTable>TMSCarrier</ReferenceTable>
</AxEdt>
```

**Properties:**
- Base Type: String
- Extends: TMSShipCarrierId
- Length: Inherited (typically 10-20 characters)
- Label: "Broker ID"
- Help Text: Descriptive help for users

### 2.2 Table Extensions

#### 2.2.1 CustTable Extension

**Purpose:** Add Broker ID to customer master records

**Fields Added:**

| Field Name | Type | EDT | Mandatory | Allow Edit |
|------------|------|-----|-----------|------------|
| BrokerId | String | TMSBrokerId | No | Yes |

**Relations:**
- Relation to TMSCarrier on ShipCarrierId
- Cardinality: ZeroOne
- Validation: Yes

**Methods Extended:**
- validateWrite() - Validates broker exists

#### 2.2.2 SalesTable Extension

**Purpose:** Add Broker ID to sales orders

**Fields Added:**

| Field Name | Type | EDT | Mandatory | Allow Edit |
|------------|------|-----|-----------|------------|
| BrokerId | String | TMSBrokerId | No | Yes |

**Relations:**
- Relation to TMSCarrier on ShipCarrierId
- Cardinality: ZeroOne
- Validation: Yes

**Methods Extended:**
- initFromCustTable() - Defaults from customer
- initFromSalesAgreementHeader() - Defaults from agreement
- validateWrite() - Validates broker exists

#### 2.2.3 SalesAgreementHeader Extension

**Purpose:** Add Broker ID to sales agreements

**Fields Added:**

| Field Name | Type | EDT | Mandatory | Allow Edit |
|------------|------|-----|-----------|------------|
| BrokerId | String | TMSBrokerId | No | Yes |

**Relations:**
- Relation to TMSCarrier on ShipCarrierId
- Cardinality: ZeroOne
- Validation: Yes

**Methods Extended:**
- initFromCustTable() - Defaults from customer
- validateWrite() - Validates broker exists

#### 2.2.4 WHSLoadTable Extension

**Purpose:** Add Broker ID to warehouse loads

**Fields Added:**

| Field Name | Type | EDT | Mandatory | Allow Edit |
|------------|------|-----|-----------|------------|
| BrokerId | String | TMSBrokerId | No | Yes |

**Relations:**
- Relation to TMSCarrier on ShipCarrierId
- Cardinality: ZeroOne
- Validation: Yes

**Methods Extended:**
- initFromSalesTable() - Transfers from sales order
- validateWrite() - Validates broker exists

#### 2.2.5 CustPackingSlipJour Extension

**Purpose:** Add Broker ID to packing slip journal

**Fields Added:**

| Field Name | Type | EDT | Mandatory | Allow Edit |
|------------|------|-----|-----------|------------|
| BrokerId | String | TMSBrokerId | No | No |

**Relations:**
- Relation to TMSCarrier on ShipCarrierId
- Cardinality: ZeroOne
- Validation: No (read-only)

**Methods Extended:**
- initFromSalesTable() - Transfers from sales order
- initFromWHSLoadTable() - Transfers from load

## 3. Business Logic Implementation

### 3.1 Initialization Chain

```
Customer.BrokerId
    ↓ [initFromCustTable()]
SalesAgreement.BrokerId
    ↓ [initFromSalesAgreementHeader()]
SalesOrder.BrokerId
    ↓ [initFromSalesTable()]
Load.BrokerId
    ↓ [initFromWHSLoadTable()]
PackingSlip.BrokerId
```

### 3.2 Method Details

#### 3.2.1 CustTable_BrokerExtension::validateWrite()

```xpp
public boolean validateWrite()
{
    boolean ret = next validateWrite();
    
    if (ret && this.BrokerId)
    {
        TMSCarrier carrier = TMSCarrier::find(this.BrokerId);
        
        if (!carrier)
        {
            error(strFmt("@SCM0603:BrokerNotFound", this.BrokerId));
            ret = false;
        }
    }
    
    return ret;
}
```

**Purpose:** Validates broker exists in carrier table
**Execution:** Before customer record is saved
**Error Handling:** Displays user-friendly error message

#### 3.2.2 SalesTable_BrokerExtension::initFromCustTable()

```xpp
public void initFromCustTable(CustTable _custTable)
{
    next initFromCustTable(_custTable);
    
    if (_custTable.BrokerId)
    {
        this.BrokerId = _custTable.BrokerId;
    }
}
```

**Purpose:** Defaults broker from customer to sales order
**Execution:** When sales order is created from customer
**Override:** User can change after initialization

#### 3.2.3 SalesTable_BrokerExtension::initFromSalesAgreementHeader()

```xpp
public void initFromSalesAgreementHeader(SalesAgreementHeader _salesAgreementHeader)
{
    next initFromSalesAgreementHeader(_salesAgreementHeader);
    
    if (_salesAgreementHeader.BrokerId)
    {
        this.BrokerId = _salesAgreementHeader.BrokerId;
    }
}
```

**Purpose:** Defaults broker from agreement to sales order
**Execution:** When sales order is released from agreement
**Override:** User can change after release

#### 3.2.4 WHSLoadTable_BrokerExtension::initFromSalesTable()

```xpp
public void initFromSalesTable(SalesTable _salesTable)
{
    next initFromSalesTable(_salesTable);
    
    if (_salesTable.BrokerId)
    {
        this.BrokerId = _salesTable.BrokerId;
    }
}
```

**Purpose:** Transfers broker from sales order to load
**Execution:** When load is created from sales order
**Timing:** During order confirmation process

## 4. User Interface Design

### 4.1 Form Extensions

#### 4.1.1 Customer Form (CustTable)

**Form Pattern:** DetailsFormMaster
**FastTab:** General or Transportation
**Control Type:** String with lookup

**XML Structure:**
```xml
<AxFormControl>
  <Name>BrokerId</Name>
  <Type>String</Type>
  <DataSource>CustTable</DataSource>
  <DataField>BrokerId</DataField>
  <Label>Broker ID</Label>
  <LookupButton>Auto</LookupButton>
</AxFormControl>
```

**Behavior:**
- Lookup displays all TMSCarrier records
- User can select or type broker ID
- Validation occurs on save

#### 4.1.2 Sales Order Form (SalesTable)

**Form Pattern:** DetailsFormTransaction
**FastTab:** General (Header)
**Control Type:** String with lookup

**Behavior:**
- Auto-populates from customer
- Can be overridden by user
- Validates on save

#### 4.1.3 Load Form (WHSLoadTable)

**Form Pattern:** DetailsFormMaster
**FastTab:** General
**Control Type:** String with lookup

**Behavior:**
- Auto-populates from sales order
- Can be manually modified
- Used for load planning

#### 4.1.4 Packing Slip Journal (CustPackingSlipJour)

**Form Pattern:** ListPage
**Grid Column:** BrokerId
**Control Type:** String (read-only)

**Behavior:**
- Display only (no editing)
- Shows historical broker information
- Used for tracking and reporting

### 4.2 List Page Modifications

All list pages (Customer, Sales Order, Load) include:
- BrokerId column in grid
- Sorting capability
- Filtering capability
- Personalization support

## 5. Database Schema Changes

### 5.1 Table Schema

**CustTable:**
```sql
ALTER TABLE CustTable
ADD BrokerId NVARCHAR(20) NULL
```

**SalesTable:**
```sql
ALTER TABLE SalesTable
ADD BrokerId NVARCHAR(20) NULL
```

**SalesAgreementHeader:**
```sql
ALTER TABLE SalesAgreementHeader
ADD BrokerId NVARCHAR(20) NULL
```

**WHSLoadTable:**
```sql
ALTER TABLE WHSLoadTable
ADD BrokerId NVARCHAR(20) NULL
```

**CustPackingSlipJour:**
```sql
ALTER TABLE CustPackingSlipJour
ADD BrokerId NVARCHAR(20) NULL
```

### 5.2 Foreign Key Constraints

All BrokerId fields have foreign key relationship to TMSCarrier:

```sql
ALTER TABLE [TableName]
ADD CONSTRAINT FK_[TableName]_TMSCarrier_BrokerId
FOREIGN KEY (BrokerId) REFERENCES TMSCarrier(ShipCarrierId)
```

### 5.3 Indexes

No additional indexes required. Existing indexes on related tables are sufficient.

## 6. Integration Points

### 6.1 Internal Integration

- **Customer Management:** CustTable integration
- **Sales Management:** SalesTable, SalesAgreementHeader integration
- **Warehouse Management:** WHSLoadTable integration
- **Transportation Management:** TMSCarrier reference

### 6.2 External Integration (Future)

Per FDD assumptions, ISV integrations (e.g., ATOS EDI) will need to:
- Include broker ID in EDI transactions
- Map broker field in integration layer
- Validate broker data in translation

## 7. Performance Considerations

### 7.1 Database Performance

- Broker lookups use existing TMSCarrier indexes
- Foreign key relationships ensure referential integrity
- No complex joins introduced
- Minimal impact on existing queries

### 7.2 Form Performance

- Form extensions load with base forms
- Minimal additional controls
- Standard lookup mechanism
- No performance degradation expected

### 7.3 Business Logic Performance

- Extension methods use CoC (Chain of Command)
- Minimal additional processing
- Validation only on save operations
- No batch processing impact

## 8. Error Handling

### 8.1 Validation Errors

**Error Code:** @SCM0603:BrokerNotFound
**Message:** "Broker ID [%1] does not exist"
**Resolution:** Select valid broker from lookup

**Error Code:** @SCM0603:InvalidBrokerType
**Message:** "Selected carrier is not a customs broker"
**Resolution:** Select carrier configured as broker

### 8.2 Error Logging

- Standard Dynamics 365 error logging
- Errors written to event log
- User notified via info bar
- Admin can review via System administration

## 9. Testing Strategy

### 9.1 Unit Testing

- Test each method in isolation
- Mock customer, order, load data
- Verify defaulting logic
- Validate error handling

### 9.2 Integration Testing

- Test complete flow from customer to packing slip
- Verify data consistency across tables
- Test override scenarios
- Validate list page functionality

### 9.3 Performance Testing

- Measure form load times
- Test with large data volumes
- Verify query performance
- Load test concurrent users

## 10. Deployment Architecture

### 10.1 Package Structure

```
SCM0603_BrokerTracking.zip
├── Metadata/
│   ├── TMSBrokerId/
│   ├── CustTable_Extension/
│   ├── SalesTable_Extension/
│   ├── SalesAgreementHeader_Extension/
│   ├── WHSLoadTable_Extension/
│   ├── CustPackingSlipJour_Extension/
│   └── [Extension Classes]/
└── Resources/
    └── Labels/
```

### 10.2 Deployment Process

1. Package created in development
2. Deployed to UAT via LCS
3. Testing and validation
4. Promoted to production
5. Post-deployment verification

## 11. Maintenance and Support

### 11.1 Code Maintenance

- Source code stored in version control
- Extensions allow for easy updates
- No overlayering simplifies upgrades
- Compatibility with future D365 versions

### 11.2 Support Procedures

- Monitor system logs for broker-related errors
- Review data integrity quarterly
- Update documentation as needed
- Provide user training and support

## 12. Compliance and Security

### 12.1 Data Security

- Field-level security via roles
- Audit trail via database log
- Data encryption at rest
- Secure transmission over HTTPS

### 12.2 Compliance

- SOX compliance through audit trail
- GDPR compliance for customer data
- Export control compliance for customs data

---

**End of Technical Specification**
