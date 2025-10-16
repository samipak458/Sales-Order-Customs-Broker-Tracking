# FDD SCM0603 - Sales Order Customs Broker Tracking V2.0

## Functional Design Document

**Document Title:** SCM FDD0603 – Sales Order Customs Broker Tracking

**Prepared for:** Leggett & Platt Automotive

**Project:** E03 - ERP Analysis, Design & Implementation

**Work Stream:** SCM

**Prepared by:** Anupam Soni

**Contributors:** Lacey Burnette, Andrew Jinks

---

## Revision History and Signoff Sheet

### Change Record

| Date | Author | Version | Change Reference |
|:-----|:-------|:--------|:-----------------|
| 2019-03-19 | Anupam Soni | 1.0 | First Draft |
| 2019-03-22 | Anupam Soni | 1.1 | Updated the following sections:<br/>1. Assumptions and Business Rules<br/>2. Business logic section for Broker ID on Packing Slip<br/>3. Configuration section |
| 2019-03-28 | Anupam Soni | 2.0 | Assumption section has been updated |

### Client Review and Approval

| Name | Version Approved | Position | Date |
|:-----|:----------------|:---------|:-----|
| Luke Bunch | 1.0 | LPA SCM Workstream Lead | 2019-03-21 |
| Luke Bunch | 1.1 | LPA SCM Workstream Lead | 2019-03-22 |

### Related Documents

| Document Name | Version | Date |
|:--------------|:--------|:-----|
| (To be populated) | | |

---

## Table of Contents

1. [Introduction](#1-introduction)
   - 1.1 [Purpose](#11-purpose)
   - 1.2 [Abbreviations and Glossary of Terms](#12-abbreviations-and-glossary-of-terms)
   - 1.3 [Audience / Stakeholders](#13-audience--stakeholders)
   - 1.4 [FDD / Design Classification](#14-fdd--design-classification)
2. [Design Scope](#2-design-scope)
   - 2.1 [Gap Requirements](#21-gap-requirements)
3. [Design Assumptions & Business Rules](#3-design-assumptions--business-rules)
   - 3.1 [Design Assumptions](#31-design-assumptions)
   - 3.2 [Business Rules](#32-business-rules)
4. [Business Process](#4-business-process)
   - 4.1 [Process Definition / Business Process Flow](#41-process-definition--business-process-flow)
5. [Design](#5-design)
   - 5.1 [Modification to Forms](#51-modification-to-forms)
   - 5.2 [Modification to Tables](#52-modification-to-tables)
   - 5.3 [Modification to Business Logic](#53-modification-to-business-logic)
   - 5.4 [Modification to List Pages](#54-modification-to-list-pages)
6. [Configurations / Parameters / Security Considerations](#6-configurations--parameters--security-considerations)
   - 6.1 [Shipping Carriers Form](#61-shipping-carriers-form)
   - 6.2 [Security Role Considerations](#62-security-role-considerations)
7. [Error Handling](#7-error-handling)
8. [Test Cases](#8-test-cases)
   - 8.1 [Test Cases](#81-test-cases)
9. [Appendices](#9-appendices)

---

## 1 Introduction

### 1.1 Purpose

LPA needs the ability to assign a customs broker to every customer record to make sure it can track shipment related information at a customer level all the way down to a sales orders and resultant loads.

The purpose of this document is to describe the functional implementation of the requirements identified by Leggett & Platt Automotive and Microsoft.

The Functional Design Document will cover the following design topics:

| Design Topics | Description |
|:--------------|:------------|
| Section 5.1 | Modifications to Forms to support the functional design |
| Section 5.2 | Modifications to Tables to support the functional design |
| Section 5.3 | Modifications to Business Logic to support the functional design |
| Section 5.4 | Modifications to List Pages to support the functional design |
| Section 6 | Configurations and Security Considerations |
| Section 7 | Test Cases to validate the modifications to support the functional design |
| Section 8 | Appendix for supporting information and templates related to the functional design |


### 1.2 Abbreviations and Glossary of Terms

| Abbreviation | Full Form | Definition/Description |
|:-------------|:----------|:-----------------------|
| LPA | Leggett & Platt Automotive | Client organization |
| FDD | Functional Design Document | Document type |
| SCM | Supply Chain Management | Work stream focus area |

**Glossary of Terms:**

| Data Type | Description |
|:----------|:------------|
| Action Pane | An action pane is the part of a form that organizes and displays buttons that represent the actions the form supports. |
| List Pages | The list page presents the primary data of the application on a user interface that is optimized for browsing records, finding the right one, and then taking an action upon that record. The list page lets the user search, filter, sort, and preview the data.|
| Navigation Path | The standard navigation window presents the user with a module navigation control.  This will indicate where the forms, list pages or periodic jobs are stored and how to navigate within D365. |
| String | Used for Text fields |
| Data Source | Used for String fields that will point to data reference table, for example the field Delivery Terms is sourced from the table "DeliveryTerms" |
| Boolean | Yes or No value |
| Real | Used to indicate a Number or Currency field |

### 1.3 Audience / Stakeholders

| Name | Position |
|:-----|:---------|
| Hollie Elliott | LPA Materials Manager |
| Stephanie Mitchell | LPA Plant Scheduler |
| Steve Shaften | LPA Logistics Supervisor |
| Mara Celic | LPA Purchasing Manager |
| Rolando Aviles | LPA Business Lead |
| Enrique Aldrete | LPA Solution Architect |
| Luke Bunch | LPA SCM Workstream Lead |
| Andrew Jinks | LPA SCM Business Analyst |
| Joseph Calicott | LPA SCM Business Analyst |
| Francis Moigula | Microsoft Solution Architect |
| Claudio Sbardella | Microsoft Delivery Architect |
| Ausif Hussain | Microsoft Technical Lead |
| Anupam Soni | Microsoft SCM Senior Consultant |
| Lacey Burnette | Microsoft SCM Consultant |
| Bob Fesmire | KPMG Business Architect |
| Shea Carroll | KPMG SCM Process Lead |

### 1.4 FDD / Design Classification

| Design Classification | Included in Design? |
|:---------------------|:-------------------|
| Creation or Modification to Dynamics Processes or Logic | Yes |
| Customizations to Dynamics Forms / Screens | Yes |
| Integration | No |
| Creating or Modifying Dynamics Reports or Inquiries | No |

---

## 2 Design Scope

### 2.1 Gap Requirements

List the relevant gap requirements to be discussed in the scope of this FDD.

| ID | Title |
|:---|:------|
| 4462 | Ability to select a customs broker for each customer |

---

## 3 Design Assumptions & Business Rules

### 3.1 Design Assumptions

The following design assumptions have been made as part of this FDD:

| S. No. | Title |
|:-------|:------|
| 1. | The Broker ID field is a look-up field on the shipping carrier table in Standard D365. It is assumed that Custom Brokers would be set up in the same table as shipping carriers. This assumption has been verified by LPA SME's and the BA. |
| 2. | The Shipping Carriers table will be used for maintaining both the carriers and customs brokers, and this applies to both the sales and purchasing side. |
| 3. | In case of ISV (ATOS), the ISV solution will have to use the additional logic to ensure customs broker field is utilized on relevant EDI transactions. This is outside the scope of this design document, but it needs to be done during the ISV Design/Build phase.  An issue has been logged in VSTS regarding the same. |
| 4. | When a Sales Order is “released to warehouse” and an outbound shipping wave is created, the system requires the user to specify the Broker ID field manually on the outbound load. This is standard D365 functionality, and no change has been proposed to Transportation Management (in case we use loads and shipments in D365). |
| 5. | Customs Brokers and Shipping Carriers will be maintained at each branch level (i.e. at a legal entity level in D365).| 
| 6. | The Broker ID field is not mandatory on the Customer Master, Sales Agreement, or Sales Order forms in D365.  |

### 3.2 Business Rules

| S. No. | Business Rule |
|:-------|:--------------|
| 1. | The Broker ID field should copy over from the Customer form to the Sales Agreement form when a Sales Agreement is created for a Customer. It should then further copy over from the Sales Agreement form to the resultant Sales Order when a release sales order gets created in D365.  |
| 2. | If no sales agreements exist or are not created for a customer, but sales orders are being created directly, the system should still copy the customs broker field from the customer to the sales order. |
| 3. | In D365, the Shipping Carrier table/form is in the Inventory Management Module, so from a data setup perspective the same needs to be configured in the Inventory Management Module. Please refer to the configuration section below in this document. |

---

## 4 Business Process

### 4.1 Process Definition / Business Process Flow

![Image](images/image4.jpeg)

**Business Process Flow Description:**

1. **Customer Setup:** During customer setup, a Broker ID can be assigned to customers marked as Export customers.
2. **Sales Order Creation:** When creating a sales order for an Export customer, the Broker ID defaults from the customer record.
3. **Sales Order Override:** Users can override the Broker ID on the sales order if needed.
4. **Sales Order Confirmation:** Upon confirmation, the Broker ID is transferred to the load record.
5. **Packing Slip Generation:** The Broker ID appears on the packing slip for tracking purposes.

---

## 5 Design

### 5.1 Modification to Forms

#### 5.1.1 Customer Form

**Form Name:** CustTable

**Modifications Required:**

| Field Name | Control Name | Fast Tab | Field Type | Notes |
|:-----------|:-------------|:---------|:-----------|:------|
| Broker ID | CustBrokerId | General | Lookup | Lookup to Shipping Carrier table where Type = 'Customs Broker' |

**Field Properties:**

- **Data Type:** EDT (Extended Data Type)
- **Table Relation:** WHSShipCarrier
- **Mandatory:** Required only when customer is flagged as Export customer
- **Label:** Broker ID

#### 5.1.2 Sales Order Form

**Form Name:** SalesTable

**Modifications Required:**

| Field Name | Control Name | Fast Tab | Field Type | Notes |
|:-----------|:-------------|:---------|:-----------|:------|
| Broker ID | SalesBrokerId | General | Lookup | Defaults from Customer record, can be overridden |

**Field Properties:**

- **Data Type:** EDT (Extended Data Type)
- **Table Relation:** WHSShipCarrier
- **Default Value:** Inherited from Customer record
- **Label:** Broker ID

#### 5.1.3 Load Form

**Form Name:** WHSLoadTable

**Modifications Required:**

| Field Name | Control Name | Fast Tab | Field Type | Notes |
|:-----------|:-------------|:---------|:-----------|:------|
| Broker ID | LoadBrokerId | General | Lookup | Populated from Sales Order upon confirmation |

**Field Properties:**

- **Data Type:** EDT (Extended Data Type)
- **Table Relation:** WHSShipCarrier
- **Source:** Sales Order Broker ID
- **Label:** Broker ID

![Image](images/image5.png)

### 5.2 Modification to Tables

#### 5.2.1 Customer Table (CustTable)

**Table Modifications:**

| Field Name | Data Type | Extended Data Type | Mandatory | Notes |
|:-----------|:----------|:-------------------|:----------|:------|
| BrokerId | String | WHSShipCarrierId | Conditional | Required only for Export customers |

**Table Relations:**

- **Related Table:** WHSShipCarrier
- **Relation Type:** Normal
- **Filter Condition:** CarrierType == CarrierType::CustomsBroker

#### 5.2.2 Sales Order Table (SalesTable)

**Table Modifications:**

| Field Name | Data Type | Extended Data Type | Mandatory | Notes |
|:-----------|:----------|:-------------------|:----------|:------|
| BrokerId | String | WHSShipCarrierId | No | Defaults from Customer, can be overridden |

**Table Relations:**

- **Related Table:** WHSShipCarrier
- **Relation Type:** Normal
- **Filter Condition:** CarrierType == CarrierType::CustomsBroker

#### 5.2.3 Load Table (WHSLoadTable)

**Table Modifications:**

| Field Name | Data Type | Extended Data Type | Mandatory | Notes |
|:-----------|:----------|:-------------------|:----------|:------|
| BrokerId | String | WHSShipCarrierId | No | Populated from Sales Order |

**Table Relations:**

- **Related Table:** WHSShipCarrier
- **Relation Type:** Normal
- **Filter Condition:** CarrierType == CarrierType::CustomsBroker

![Image](images/image6.jpeg)

### 5.3 Modification to Business Logic

#### 5.3.1 Customer Form Business Logic

**Method:** validateWrite()

**Logic Description:**
- Validate that Broker ID is provided when customer is marked as Export customer
- Ensure selected Broker ID is of type 'Customs Broker'

**Pseudocode:**
```
if (this.ExportCustomer == NoYes::Yes)
{
    if (!this.BrokerId)
    {
        error("Broker ID is required for Export customers");
        return false;
    }
}
return true;
```

#### 5.3.2 Sales Order Business Logic

**Method:** initFromCustTable()

**Logic Description:**
- Default Broker ID from Customer record when creating sales order

**Pseudocode:**
```
if (custTable.BrokerId)
{
    this.BrokerId = custTable.BrokerId;
}
```

**Method:** validateWrite()

**Logic Description:**
- Validate Broker ID selection if provided

#### 5.3.3 Load Business Logic

**Method:** initFromSalesTable()

**Logic Description:**
- Populate Broker ID from Sales Order when load is created

**Pseudocode:**
```
if (salesTable.BrokerId)
{
    this.BrokerId = salesTable.BrokerId;
}
```

![Image](images/image7.png)

### 5.4 Modification to List Pages

#### 5.4.1 Customer List Page

**Page Name:** CustTableListPage

**Modifications:**
- Add Broker ID column to the grid
- Enable filtering by Broker ID

#### 5.4.2 Sales Order List Page

**Page Name:** SalesTableListPage

**Modifications:**
- Add Broker ID column to the grid
- Enable filtering by Broker ID

#### 5.4.3 Load List Page

**Page Name:** WHSLoadTableListPage

**Modifications:**
- Add Broker ID column to the grid
- Enable filtering by Broker ID

![Image](images/image8.png)

---

## 6 Configurations / Parameters / Security Considerations

### 6.1 Shipping Carriers Form

**Configuration Requirements:**

The existing Shipping Carriers form will be enhanced to support Customs Brokers:

1. **Type Field Enhancement:** The existing 'Type' field will include a new option for 'Customs Broker'
2. **Customs Broker Setup:** Users can create new records with Type = 'Customs Broker'
3. **Identification:** Customs Brokers will be clearly distinguished from regular shipping carriers

**Setup Process:**
1. Navigate to Transportation management > Setup > General > Shipping carriers
2. Create new records for Customs Brokers
3. Set Type = 'Customs Broker'
4. Configure other relevant fields as needed

### 6.2 Security Role Considerations

**Security Roles Affected:**

| Role | Permissions Required | Justification |
|:-----|:-------------------|:--------------|
| Sales Manager | Read/Write access to Customer and Sales Order Broker ID fields | Need to manage customer broker assignments and sales order overrides |
| Sales Representative | Read access to Customer Broker ID, Write access to Sales Order Broker ID | Need to view customer defaults and override on sales orders |
| Transportation Coordinator | Read/Write access to Load Broker ID | Need to manage load information including broker details |
| System Administrator | Full access to Shipping Carriers configuration | Need to setup and maintain customs broker records |

**Security Considerations:**
- Ensure proper segregation of duties
- Audit trail for broker ID changes
- Data security for broker information

![Image](images/image9.png)

---

## 7 Error Handling

### 7.1 Error Scenarios and Handling

| Error Scenario | Error Message | Resolution |
|:---------------|:--------------|:-----------|
| Export customer without Broker ID | "Broker ID is required for Export customers" | User must select a valid Customs Broker |
| Invalid Broker ID selection | "Selected carrier is not a Customs Broker" | User must select a record with Type = 'Customs Broker' |
| Broker ID not found | "Broker ID does not exist" | User must select from available Customs Brokers |
| Missing Broker ID on packing slip | "Broker information unavailable" | System will display warning, user should verify load configuration |

### 7.2 Validation Rules

1. **Customer Level:** Broker ID validation for Export customers
2. **Sales Order Level:** Broker ID format and existence validation
3. **Load Level:** Data consistency validation
4. **Report Level:** Display formatting validation

![Image](images/image10.png)

---

## 8 Test Cases

### 8.1 Test Cases

#### 8.1.1 Customer Management Test Cases

| Test Case ID | Test Description | Expected Result |
|:-------------|:----------------|:----------------|
| TC001 | Create Export customer without Broker ID | Error message displayed |
| TC002 | Create Export customer with valid Broker ID | Customer created successfully |
| TC003 | Create Non-Export customer without Broker ID | Customer created successfully |
| TC004 | Update customer to Export status without Broker ID | Error message displayed |

#### 8.1.2 Sales Order Test Cases

| Test Case ID | Test Description | Expected Result |
|:-------------|:----------------|:----------------|
| TC005 | Create sales order for customer with Broker ID | Broker ID defaults from customer |
| TC006 | Override Broker ID on sales order | Override accepted and saved |
| TC007 | Create sales order for customer without Broker ID | Sales order created without Broker ID |
| TC008 | Confirm sales order with Broker ID | Broker ID transferred to load |

#### 8.1.3 Load and Reporting Test Cases

| Test Case ID | Test Description | Expected Result |
|:-------------|:----------------|:----------------|
| TC009 | Generate packing slip for load with Broker ID | Broker ID displayed on packing slip |
| TC010 | Generate packing slip for load without Broker ID | Packing slip generated without broker info |
| TC011 | Filter loads by Broker ID | Correct loads displayed |
| TC012 | Export load data including Broker ID | Data exported with broker information |

![Image](images/image11.png)

---

## 9 Appendices

### Appendix A: Technical Specifications

![Image](images/image12.png)

### Appendix B: Business Process Diagrams

![Image](images/image13.png)

### Appendix C: Screen Mockups

![Image](images/image14.jpeg)

### Appendix D: Configuration Guide

![Image](images/image15.png)

### Appendix E: Data Model

![Image](images/image16.png)

### Appendix F: Integration Points

![Image](images/image17.png)

### Appendix G: Security Model

![Image](images/image18.png)

### Appendix H: Test Data

![Image](images/image19.png)

### Appendix I: User Training Materials

![Image](images/image20.png)

### Appendix J: Additional Documentation

![Image](images/image21.png)

![Image](images/image22.png)

![Image](images/image23.png)

![Image](images/image24.png)

---

**End of Document**
