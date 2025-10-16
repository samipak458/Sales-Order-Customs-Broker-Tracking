# Sales Order Customs Broker Tracking - Implementation

## Overview

This directory contains the complete implementation of the Sales Order Customs Broker Tracking functionality for Microsoft Dynamics 365 Finance and Operations, as specified in FDD SCM0603 V2.0.

## Purpose

This customization enables Leggett & Platt Automotive (LPA) to:
- Assign customs brokers to customer records
- Track broker information through the sales process
- Maintain broker details on sales orders, agreements, loads, and packing slips
- Support efficient customs clearance and shipping operations

## Repository Structure

```
Dynamics365/
├── Metadata/
│   ├── EDTs/
│   │   └── TMSBrokerId.xml
│   ├── Tables/
│   │   ├── CustTable_Extension.xml
│   │   ├── SalesTable_Extension.xml
│   │   ├── SalesAgreementHeader_Extension.xml
│   │   ├── CustPackingSlipJour_Extension.xml
│   │   └── WHSLoadTable_Extension.xml
│   ├── Forms/
│   │   ├── CustTable_Extension.xml
│   │   ├── SalesTable_Extension.xml
│   │   ├── SalesAgreement_Extension.xml
│   │   ├── CustPackingSlipJour_Extension.xml
│   │   └── WHSLoadTable_Extension.xml
│   └── Classes/
│       ├── CustTable_BrokerExtension.xpp
│       ├── SalesTable_BrokerExtension.xpp
│       ├── SalesAgreementHeader_BrokerExtension.xpp
│       ├── WHSLoadTable_BrokerExtension.xpp
│       └── CustPackingSlipJour_BrokerExtension.xpp
└── Documentation/
    ├── DEPLOYMENT_GUIDE.md
    ├── CONFIGURATION_GUIDE.md
    └── TEST_VALIDATION_SCRIPTS.md
```

## Key Components

### 1. Extended Data Type (EDT)
- **TMSBrokerId**: Specialized EDT extending TMSShipCarrierId for customs broker identification

### 2. Table Extensions
- **CustTable**: Adds BrokerId field to customer master
- **SalesTable**: Adds BrokerId field to sales orders with defaulting logic
- **SalesAgreementHeader**: Adds BrokerId field to sales agreements
- **CustPackingSlipJour**: Adds BrokerId field for packing slip tracking
- **WHSLoadTable**: Adds BrokerId field to warehouse loads

### 3. Form Extensions
- **Customer Form**: Broker ID field in Transportation/General FastTab
- **Sales Order Form**: Broker ID field with customer defaulting
- **Sales Agreement Form**: Broker ID field in General FastTab
- **Packing Slip Journal Form**: Read-only Broker ID display
- **Load Form**: Broker ID field populated from sales order

### 4. Business Logic Classes
- **CustTable_BrokerExtension**: Customer validation logic
- **SalesTable_BrokerExtension**: Sales order initialization and validation
- **SalesAgreementHeader_BrokerExtension**: Sales agreement initialization
- **WHSLoadTable_BrokerExtension**: Load initialization and transfer
- **CustPackingSlipJour_BrokerExtension**: Packing slip broker tracking

## Business Flow

```
Customer Master (BrokerId)
    ↓
    ├─→ Sales Agreement (BrokerId defaults from Customer)
    │        ↓
    │   Sales Order (BrokerId defaults from Agreement)
    │
    └─→ Sales Order (BrokerId defaults from Customer)
         ↓
    Load (BrokerId transfers from Sales Order)
         ↓
    Packing Slip (BrokerId displays from Load/Order)
```

## Key Features

### Defaulting Logic
- Customer → Sales Agreement: Broker ID automatically copies
- Customer → Sales Order: Broker ID defaults when order created
- Sales Agreement → Sales Order: Broker ID inherits when releasing order
- Sales Order → Load: Broker ID transfers upon confirmation
- Sales Order → Packing Slip: Broker ID displays on journal

### Validation Rules
- Broker ID must exist in TMSCarrier table
- Broker ID is not mandatory (per business requirements)
- Invalid broker IDs are rejected with error messages
- Data consistency maintained across transaction chain

### List Page Enhancements
- Broker ID column available on Customer list page
- Broker ID column available on Sales Order list page
- Broker ID column available on Load list page
- Filtering and sorting enabled for all list pages

## Prerequisites

### System Requirements
- Microsoft Dynamics 365 Finance and Operations (Version 10.0+)
- Transportation Management module enabled
- Warehouse Management module enabled
- Sales and Marketing module enabled

### Development Tools
- Visual Studio with Dynamics 365 development tools
- Access to development environment
- Appropriate deployment permissions

## Quick Start

### 1. Deploy the Customization
Follow the [Deployment Guide](Documentation/DEPLOYMENT_GUIDE.md) for detailed instructions.

**Quick Steps:**
1. Import metadata into Visual Studio project
2. Build the project
3. Synchronize database
4. Create deployable package
5. Deploy to target environment

### 2. Configure the System
Follow the [Configuration Guide](Documentation/CONFIGURATION_GUIDE.md) for setup instructions.

**Quick Steps:**
1. Setup customs brokers in Shipping Carriers
2. Assign brokers to customers
3. Configure security roles
4. Test functionality

### 3. Validate Implementation
Use the [Test Validation Scripts](Documentation/TEST_VALIDATION_SCRIPTS.md) to verify functionality.

**Quick Tests:**
1. Create customer with broker
2. Create sales order - verify defaulting
3. Create load - verify transfer
4. Post packing slip - verify display

## Business Rules

### From FDD SCM0603 V2.0

1. **Broker Assignment:**
   - Broker ID field available on Customer, Sales Agreement, and Sales Order
   - Broker ID is optional (not mandatory)
   - Selected broker must exist in TMSCarrier table

2. **Data Flow:**
   - Customer → Sales Agreement (automatic copy)
   - Customer → Sales Order (automatic default)
   - Sales Agreement → Sales Order (automatic inherit)
   - Sales Order → Load (automatic transfer)
   - Sales Order/Load → Packing Slip (automatic display)

3. **Override Capability:**
   - Users can override default broker on sales orders
   - Users can override default broker on sales agreements
   - Changes are saved and propagated downstream

4. **Transportation Management:**
   - Shipping Carriers table stores customs brokers
   - Mode field distinguishes brokers from regular carriers
   - Brokers are maintained at legal entity level

## Technical Details

### EDT Specifications
```xml
<Name>TMSBrokerId</Name>
<Extends>TMSShipCarrierId</Extends>
<Label>Broker ID</Label>
<ReferenceTable>TMSCarrier</ReferenceTable>
```

### Table Relations
All BrokerId fields relate to TMSCarrier.ShipCarrierId with ZeroOne cardinality.

### Method Implementations

**initFromCustTable():**
- Implemented on SalesTable
- Implemented on SalesAgreementHeader
- Copies broker from customer to order/agreement

**initFromSalesTable():**
- Implemented on WHSLoadTable
- Implemented on CustPackingSlipJour
- Transfers broker from order to load/packing slip

**validateWrite():**
- Implemented on all tables with BrokerId
- Validates broker exists in TMSCarrier
- Provides user-friendly error messages

## Security Considerations

### Role-Based Access
- **Sales Manager**: Full read/write access
- **Sales Representative**: Read customer, write order
- **Transportation Coordinator**: Manage load brokers
- **Warehouse Manager**: Read-only access

### Audit Trail
- Standard Dynamics 365 auditing applies
- Track who modified broker assignments
- Monitor changes for compliance

## Troubleshooting

### Common Issues

**Issue:** Broker ID not defaulting to sales order
- **Solution:** Verify customer has broker assigned
- **Solution:** Check initFromCustTable method execution

**Issue:** Cannot save with broker ID
- **Solution:** Ensure broker exists in TMSCarrier table
- **Solution:** Verify broker record is active

**Issue:** Broker not appearing on packing slip
- **Solution:** Check broker on sales order
- **Solution:** Verify load has broker assigned

### Getting Help
1. Review documentation in this directory
2. Check deployment and configuration guides
3. Review FDD SCM0603 V2.0 for business requirements
4. Contact system administrator or Microsoft Support

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024 | Implementation Team | Initial implementation per FDD SCM0603 V2.0 |

## References

### Related Documentation
- [FDD SCM0603 V2.0](../../FDD_SCM0603_Sales_Order_Customs_Broker_Tracking_V2.0.md)
- [Deployment Guide](Documentation/DEPLOYMENT_GUIDE.md)
- [Configuration Guide](Documentation/CONFIGURATION_GUIDE.md)
- [Test Validation Scripts](Documentation/TEST_VALIDATION_SCRIPTS.md)

### Microsoft Documentation
- [Dynamics 365 Customization Guide](https://docs.microsoft.com/dynamics365)
- [Table Extensions](https://docs.microsoft.com/dynamics365/fin-ops-core/dev-itpro/extensibility/extensibility-home-page)
- [Form Extensions](https://docs.microsoft.com/dynamics365/fin-ops-core/dev-itpro/extensibility/form-extensions)
- [Transportation Management](https://docs.microsoft.com/dynamics365/supply-chain/transportation/transportation-management-overview)

## License

This customization is proprietary to Leggett & Platt Automotive and is provided for internal use only.

## Support

For issues, questions, or support:
- Internal: Contact your Dynamics 365 administrator
- External: Contact Microsoft Support with reference to FDD SCM0603

---

**Implementation Team:**
- Anupam Soni (Microsoft SCM Senior Consultant)
- Lacey Burnette (Microsoft SCM Consultant)
- Andrew Jinks (LPA SCM Business Analyst)

**Prepared for:** Leggett & Platt Automotive
**Project:** E03 - ERP Analysis, Design & Implementation
**Work Stream:** SCM

---

**End of README**
