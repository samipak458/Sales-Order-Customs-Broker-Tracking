# FDD SCM0603- Sales Order Customs Broker Tracking-V2.0 (1)


<!-- Page 1 -->
Functional Design Document

SCM FDD0603 – Sales Order Customs Broker Tracking



Prepared for
Leggett & Platt Automotive


Project
E03 - ERP Analysis, Design & Implementation

Work Stream
## Scm


Prepared by:
Anupam Soni

Contributors:
Lacey Burnette, Andrew Jinks
Leggett & Platt Automotive

| Leggett & Platt Automotive   |
|:-----------------------------|
| Leggett & Platt Automotive   |

![Image](images/image1.png)

![Image](images/image2.png)

---

<!-- Page 2 -->
Revision History and Signoff Sheet

Change Record:

Date
Author
Version
Change Reference
2019-03-19
Anupam Soni
1.0
First Draft
2019-03-22
Anupam Soni
1.1
### Updated the following sections:
1. Assumptions and Business
Rules
2. Business logic section for
Broker ID on Packing Slip
3. Configuration section
2019-03-28
Anupam Soni
2.0
### Assumption section has been updated


Client Review and Approval:

Name
Version Approved
Position
Date
Luke Bunch
1.0
LPA SCM Workstream Lead
2019-03-21
Luke Bunch
1.1
LPA SCM Workstream Lead
2019-03-22







Related Documents:

Document Name
Version
Date

|            | Date   |    |             | Author   |    |     | Version   |    |                                     | Change Reference   |    |
|:-----------|:-------|:---|:------------|:---------|:---|----:|:----------|:---|:------------------------------------|:-------------------|:---|
| 2019-03-19 |        |    | Anupam Soni |          |    | 1   |           |    | First Draft                         |                    |    |
| 2019-03-22 |        |    | Anupam Soni |          |    | 1.1 |           |    | Updated the following sections:     |                    |    |
|            |        |    |             |          |    |     |           |    | 1. Assumptions and Business         |                    |    |
|            |        |    |             |          |    |     |           |    | Rules                               |                    |    |
|            |        |    |             |          |    |     |           |    | 2. Business logic section for       |                    |    |
|            |        |    |             |          |    |     |           |    | Broker ID on Packing Slip           |                    |    |
|            |        |    |             |          |    |     |           |    | 3. Configuration section            |                    |    |
| 2019-03-28 |        |    | Anupam Soni |          |    | 2   |           |    | Assumption section has been updated |                    |    |

|            | Name   |    |     | Version Approved   |    |                         | Position   |    |            | Date   |    |
|:-----------|:-------|:---|:----|:-------------------|:---|:------------------------|:-----------|:---|:-----------|:-------|:---|
| Luke Bunch |        |    | 1.0 |                    |    | LPA SCM Workstream Lead |            |    | 2019-03-21 |        |    |
| Luke Bunch |        |    | 1.1 |                    |    | LPA SCM Workstream Lead |            |    | 2019-03-22 |        |    |
|            |        |    |     |                    |    |                         |            |    |            |        |    |

|    | Document Name   |    |    | Version   |    |    | Date   |    |
|:---|:----------------|:---|:---|:----------|:---|:---|:-------|:---|
|    |                 |    |    |           |    |    |        |    |
|    |                 |    |    |           |    |    |        |    |

---

<!-- Page 3 -->
Table of Contents

TABLE OF CONTENTS ................................................................................................................................ I
1
INTRODUCTION .................................................................................................................................... 2
1.1
PURPOSE .............................................................................................................................................. 2
1.2
ABBREVIATIONS AND GLOSSARY OF TERMS ........................................................................................ 2
1.3
AUDIENCE / STAKEHOLDERS ................................................................................................................ 3
1.4
FDD / DESIGN CLASSIFICATION ........................................................................................................... 3
2
DESIGN SCOPE ...................................................................................................................................... 4
2.1
GAP REQUIREMENTS ............................................................................................................................ 4
3
DESIGN ASSUMPTIONS & BUSINESS RULES ................................................................................ 5
3.1
DESIGN ASSUMPTIONS ......................................................................................................................... 5
3.2
BUSINESS RULES................................................................................................................................... 5
4
BUSINESS PROCESS ............................................................................................................................. 7
4.1
PROCESS DEFINITION / BUSINESS PROCESS FLOW ................................................................................ 7
5
DESIGN ..................................................................................................................................................... 8
5.1
MODIFICATION TO FORMS .................................................................................................................... 8
5.2
MODIFICATION TO TABLES ................................................................................................................. 10
5.3
MODIFICATION TO BUSINESS LOGIC ................................................................................................... 12
5.4
MODIFICATION TO LIST PAGES ........................................................................................................... 15
6
## Configurations / Parameters / Security Considerations ................................. 17
6.1
SHIPPING CARRIERS FORM ................................................................................................................. 17
6.2
SECURITY ROLE CONSIDERATIONS .................................................................................................... 17
7
ERROR HANDLING ............................................................................................................................. 18
8
TEST CASES .......................................................................................................................................... 19
8.1
TEST CASES ........................................................................................................................................ 19
9
APPENDICES ......................................................................................................................................... 20

![Image](images/image3.png)

---

<!-- Page 4 -->
2 | 22 | P a g e

## 1 Introduction
1.1
## Purpose
LPA needs the ability to assign a customs broker to every customer record to make sure it can track
shipment related information at a customer level all the way down to a sales orders and resultant
loads

The purpose of this document is to describe the functional implementation of the requirements
identified by Leggett & Platt Automotive and Microsoft.

The Functional Design Document will cover the following design topics:
Design Topics
Description
### Section 5.1
Modifications to Forms to support the functional design
### Section 5.2
Modifications to Tables to support the functional design
### Section 5.3
Modifications to Business Logic to support the functional design
### Section 5.4
Modifications to List Pages to support the functional design
### Section 6
Configurations and Security Considerations
### Section 7
Test Cases to validate the modifications to support the functional design
### Section 8
Appendix for supporting information and templates related to the
functional design

1.2
## Abbreviations And Glossary Of Terms

Abbreviation
Explanation
Forms
The Forms used to enter data to support the process you are designing for.
Fast Tab
A FastTab is a container for data entry controls. A FastTab organizes fields
into related chunks. FastTabs are used primarily on task pages such as
details forms, dialog forms, simple list and details forms.
Tables
The tables that source the forms
Action Pane
An action pane is the part of a form that organizes and displays buttons that
represent the actions the form supports.
List Pages
The list page presents the primary data of the application on a user
interface that is optimized for browsing records, finding the right one, and
then taking an action upon that record. The list page lets the user search,
filter, sort, and preview the data.
Navigation Path
The standard navigation window presents the user with a module
navigation control.  This will indicate where the forms, list pages or periodic
jobs are stored and how to navigate within D365.
String
Text Field

|             | Design Topics   |    |                                                                           | Description                                                      |    |
|:------------|:----------------|:---|:--------------------------------------------------------------------------|:-----------------------------------------------------------------|:---|
|             | Section 5.1     |    |                                                                           | Modifications to Forms to support the functional design          |    |
| Section 5.2 |                 |    | Modifications to Tables to support the functional design                  |                                                                  |    |
|             | Section 5.3     |    |                                                                           | Modifications to Business Logic to support the functional design |    |
| Section 5.4 |                 |    | Modifications to List Pages to support the functional design              |                                                                  |    |
|             | Section 6       |    |                                                                           | Configurations and Security Considerations                       |    |
| Section 7   |                 |    | Test Cases to validate the modifications to support the functional design |                                                                  |    |
| Section 8   |                 |    |                                                                           | Appendix for supporting information and templates related to the |    |
|             |                 |    |                                                                           | functional design                                                |    |

|                 | Abbreviation   |    |                                                                                | Explanation                                                                  |    |
|:----------------|:---------------|:---|:-------------------------------------------------------------------------------|:-----------------------------------------------------------------------------|:---|
|                 | Forms          |    |                                                                                | The Forms used to enter data to support the process you are designing for.   |    |
| Fast Tab        |                |    | A FastTab is a container for data entry controls. A FastTab organizes fields   |                                                                              |    |
|                 |                |    | into related chunks. FastTabs are used primarily on task pages such as         |                                                                              |    |
|                 |                |    | details forms, dialog forms, simple list and details forms.                    |                                                                              |    |
|                 | Tables         |    |                                                                                | The tables that source the forms                                             |    |
| Action Pane     |                |    | An action pane is the part of a form that organizes and displays buttons that  |                                                                              |    |
|                 |                |    | represent the actions the form supports.                                       |                                                                              |    |
| List Pages      |                |    |                                                                                | The list page presents the primary data of the application on a user         |    |
|                 |                |    |                                                                                | interface that is optimized for browsing records, finding the right one, and |    |
|                 |                |    |                                                                                | then taking an action upon that record. The list page lets the user search,  |    |
|                 |                |    |                                                                                | filter, sort, and preview the data.                                          |    |
| Navigation Path |                |    | The standard navigation window presents the user with a module                 |                                                                              |    |
|                 |                |    | navigation control. This will indicate where the forms, list pages or periodic |                                                                              |    |
|                 |                |    | jobs are stored and how to navigate within D365.                               |                                                                              |    |
|                 | String         |    |                                                                                | Text Field                                                                   |    |

---

<!-- Page 5 -->
3 | 22 | P a g e

Data Source
Used for String fields that will point to data reference table, for example the
field Delivery Terms is sourced from the table “DeliveryTerms”.
Boolean
Yes or No value
Real
Used to indicate a Number or Currency field.

1.3
## Audience / Stakeholders
Name
Position
Hollie Elliott
LPA Materials Manager
Stephanie Mitchell
LPA Plant Scheduler
Steve Shaften
LPA Logistics Supervisor
Mara Celic
LPA Purchasing Manager
Rolando Aviles
LPA Business Lead
Enrique Aldrete
LPA Solution Architect
Luke Bunch
LPA SCM Workstream Lead
Andrew Jinks
LPA SCM Business Analyst
Joseph Calicott
LPA SCM Business Analyst
Francis Moigula
Microsoft Solution Architect
Claudio Sbardella
Microsoft Delivery Architect
Ausif Hussain
Microsoft Technical Lead
Anupam Soni
Microsoft SCM Senior Consultant
Lacey Burnette
Microsoft SCM Consultant
Bob Fesmire
KPMG Business Architect
Shea Carroll
KPMG SCM Process Lead



1.4
## Fdd / Design Classification
Design Classification
Included in Design? (Yes or No)
Creation or Modification to Dynamics Processes or Logic
## Y
Customizations to Dynamics Forms / Screens
## Y
Integration
## N
Creating or Modifying Dynamics Reports or Inquiries
## N

| Data Source   | None    | None   | Used for String fields that will point to data reference table, for example the   | None            | None   |
|               |         |        | field Delivery Terms is sourced from the table “DeliveryTerms”.                   |                 |        |
|:--------------|:--------|:-------|:----------------------------------------------------------------------------------|:----------------|:-------|
|               | Boolean |        |                                                                                   | Yes or No value |        |
| Real          |         |        | Used to indicate a Number or Currency field.                                      |                 |        |

|                    | Name              |    |                              | Position                        |    |
|:-------------------|:------------------|:---|:-----------------------------|:--------------------------------|:---|
|                    | Hollie Elliott    |    |                              | LPA Materials Manager           |    |
| Stephanie Mitchell |                   |    | LPA Plant Scheduler          |                                 |    |
|                    | Steve Shaften     |    |                              | LPA Logistics Supervisor        |    |
| Mara Celic         |                   |    | LPA Purchasing Manager       |                                 |    |
|                    | Rolando Aviles    |    |                              | LPA Business Lead               |    |
| Enrique Aldrete    |                   |    | LPA Solution Architect       |                                 |    |
|                    | Luke Bunch        |    |                              | LPA SCM Workstream Lead         |    |
| Andrew Jinks       |                   |    | LPA SCM Business Analyst     |                                 |    |
|                    | Joseph Calicott   |    |                              | LPA SCM Business Analyst        |    |
| Francis Moigula    |                   |    | Microsoft Solution Architect |                                 |    |
|                    | Claudio Sbardella |    |                              | Microsoft Delivery Architect    |    |
| Ausif Hussain      |                   |    | Microsoft Technical Lead     |                                 |    |
|                    | Anupam Soni       |    |                              | Microsoft SCM Senior Consultant |    |
| Lacey Burnette     |                   |    | Microsoft SCM Consultant     |                                 |    |
|                    | Bob Fesmire       |    |                              | KPMG Business Architect         |    |
| Shea Carroll       |                   |    | KPMG SCM Process Lead        |                                 |    |

|                                                     | Design Classification                                   |    |    | Included in Design? (Yes or No)   |    |
|:----------------------------------------------------|:--------------------------------------------------------|:---|:---|:----------------------------------|:---|
|                                                     | Creation or Modification to Dynamics Processes or Logic |    |    | Y                                 |    |
| Customizations to Dynamics Forms / Screens          |                                                         |    | Y  |                                   |    |
|                                                     | Integration                                             |    |    | N                                 |    |
| Creating or Modifying Dynamics Reports or Inquiries |                                                         |    | N  |                                   |    |

---

<!-- Page 6 -->
4 | 22 | P a g e

## 2 Design Scope
2.1
## Gap Requirements

List the relevant gap requirements to be discussed in the scope of this FDD.

## Id
Title
4462
Ability to select a customs broker for each customer

|    |   ID |    |    | Title                                                |    |
|:---|-----:|:---|:---|:-----------------------------------------------------|:---|
|    | 4462 |    |    | Ability to select a customs broker for each customer |    |

---

<!-- Page 7 -->
5 | 22 | P a g e

## 3 Design Assumptions & Business Rules

3.1
## Design Assumptions

The following design assumptions have been made as part of this FDD

S. No.
Title
1.
The Broker ID field is a look-up field on the shipping carrier table in Standard D365. It
is assumed that Custom Brokers would be set up in the same table as shipping
carriers.  This assumption has been verified by LPA SME’s and the BA.
2.
The Shipping Carriers table will be used for maintaining both the carriers and
customs brokers, and this applies to both the sales and purchasing side.
3.
In case of ISV (ATOS), the ISV solution will have to use the additional logic to ensure
customs broker field is utilized on relevant EDI transactions. This is outside the scope
of this design document, but it needs to be done during the ISV Design/Build phase.
An issue has been logged in VSTS regarding the same.
4.
When a Sales Order is “released to warehouse” and an outbound shipping wave is
created, the system requires the user to specify the Broker ID field manually on the
outbound load. This is standard D365 functionality, and no change has been
proposed to Transportation Management (in case we use loads and shipments in
## D365).
5.
Customs Brokers and Shipping Carriers will be maintained at each branch level (i.e.
at a legal entity level in D365).
6.
The Broker ID field is not mandatory on the Customer Master, Sales Agreement, or
Sales Order forms in D365.

3.2
## Business Rules

The following business rules apply to this FDD

S. No.
Title
1.
The Broker ID field should copy over from the Customer form to the Sales Agreement
form when a Sales Agreement is created for a Customer. It should then further copy
over from the Sales Agreement form to the resultant Sales Order when a release sales
order gets created in D365.
If no sales agreements exist or are not created for a customer, but sales orders are
being created directly, the system should still copy the customs broker field from the
customer to the sales order.
2.
In D365, the Shipping Carrier table/form is in the Inventory Management Module, so
from a data setup perspective the same needs to be configured in the Inventory

|    | S. No.   |    |                                                                                      | Title                                                                                     |    |
|:---|:---------|:---|:-------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------|:---|
| 1. | 1.       |    |                                                                                      | The Broker ID field is a look-up field on the shipping carrier table in Standard D365. It |    |
|    |          |    |                                                                                      | is assumed that Custom Brokers would be set up in the same table as shipping              |    |
|    |          |    |                                                                                      | carriers. This assumption has been verified by LPA SME’s and the BA.                      |    |
| 2. |          |    | The Shipping Carriers table will be used for maintaining both the carriers and       |                                                                                           |    |
|    |          |    | customs brokers, and this applies to both the sales and purchasing side.             |                                                                                           |    |
| 3. |          |    |                                                                                      | In case of ISV (ATOS), the ISV solution will have to use the additional logic to ensure   |    |
|    |          |    |                                                                                      | customs broker field is utilized on relevant EDI transactions. This is outside the scope  |    |
|    |          |    |                                                                                      | of this design document, but it needs to be done during the ISV Design/Build phase.       |    |
|    |          |    |                                                                                      | An issue has been logged in VSTS regarding the same.                                      |    |
| 4. |          |    | When a Sales Order is “released to warehouse” and an outbound shipping wave is       |                                                                                           |    |
|    |          |    | created, the system requires the user to specify the Broker ID field manually on the |                                                                                           |    |
|    |          |    | outbound load. This is standard D365 functionality, and no change has been           |                                                                                           |    |
|    |          |    | proposed to Transportation Management (in case we use loads and shipments in         |                                                                                           |    |
|    |          |    | D365).                                                                               |                                                                                           |    |
| 5. |          |    |                                                                                      | Customs Brokers and Shipping Carriers will be maintained at each branch level (i.e.       |    |
|    |          |    |                                                                                      | at a legal entity level in D365).                                                         |    |
| 6. |          |    | The Broker ID field is not mandatory on the Customer Master, Sales Agreement, or     |                                                                                           |    |
|    |          |    | Sales Order forms in D365.                                                           |                                                                                           |    |

|    | S. No.   |    |                                                                                    | Title                                                                                  |    |
|:---|:---------|:---|:-----------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|:---|
| 1. | 1.       |    |                                                                                    | The Broker ID field should copy over from the Customer form to the Sales Agreement     |    |
|    |          |    |                                                                                    | form when a Sales Agreement is created for a Customer. It should then further copy     |    |
|    |          |    |                                                                                    | over from the Sales Agreement form to the resultant Sales Order when a release sales   |    |
|    |          |    |                                                                                    | order gets created in D365.                                                            |    |
|    |          |    |                                                                                    | If no sales agreements exist or are not created for a customer, but sales orders are   |    |
|    |          |    |                                                                                    | being created directly, the system should still copy the customs broker field from the |    |
|    |          |    |                                                                                    | customer to the sales order.                                                           |    |
| 2. |          |    | In D365, the Shipping Carrier table/form is in the Inventory Management Module, so |                                                                                        |    |
|    |          |    | from a data setup perspective the same needs to be configured in the Inventory     |                                                                                        |    |

---

<!-- Page 8 -->
6 | 22 | P a g e

Management Module. Please refer to the configuration section below in this
document.

|    | Management Module. Please refer to the configuration section below in this   |
|    | document.                                                                    |
|----|------------------------------------------------------------------------------|

---

<!-- Page 9 -->
7 | 22 | P a g e

## 4 Business Process
4.1
## Process Definition / Business Process Flow
### This section is not applicable for this FDD.

4.1.1 Business Process Narrative
### This section is not applicable for this FDD.

4.1.2 Business Process Flow
### This section is not applicable for this FDD.

---

<!-- Page 10 -->
8 | 22 | P a g e

## 5 Design
5.1
## Modification To Forms
5.1.1 Customer Master Form
It is proposed to add the Broker ID field (which is present in Standard D365) to the Customer Master
form. This field is present on the “All Sales Orders” form in Sales and Marketing Module as well as on
the “All loads” form in Transportation Management Module.




Existing or New?
Existing
Form Name
CustTable
Form Label
All Customers
Navigation Path
Accounts Receivable > Customers > All Customers

Field
Name
Control Name
Fast Tab
Field
Type
Notes
Broker ID
TMCustTable_BrokerCode
Transportation  Look-
up
Broker ID field, which is
currently on the SO Header
form.
(TMSSalesTable_BrokerCode)

5.1.2 Sales Agreement Form
The Broker ID field should also be added on to the Sales Agreement form as shown below:

|    | Existing or New?   |    | Existing      | None                                            |
|:---|:-------------------|:---|:--------------|:------------------------------------------------|
|    | Form Name          |    |               | CustTable                                       |
|    | Form Label         |    | All Customers |                                                 |
|    | Navigation Path    |    |               | Accounts Receivable > Customers > All Customers |

|           | Field     |    | Control Name           | Fast Tab       |       | Field   |    | Notes   | Notes                      |
|:----------|:----------|:---|:-----------------------|:---------------|:------|:--------|:---|:--------|:---------------------------|
|           | Name      |    |                        |                |       | Type    |    |         |                            |
| Broker ID | Broker ID |    | TMCustTable_BrokerCode | Transportation | Look- | Look-   |    |         | Broker ID field, which is  |
|           |           |    |                        |                | up    |         |    |         |                            |
|           |           |    |                        |                |       | up      |    |         | currently on the SO Header |
|           |           |    |                        |                |       |         |    |         | form.                      |
|           |           |    |                        |                |       |         |    |         | (TMSSalesTable_BrokerCode) |

![Image](images/image4.jpeg)

![Image](images/image5.png)

---

<!-- Page 11 -->
9 | 22 | P a g e



Existing or New?
Existing
Form Name
Sales Agreements Header Form
Form Label
Sales Agreements
Navigation Path
Sales and Marketing > Sales Agreements > Sales Agreements

Field
Name
Control Name
Fast Tab
Field
Type
Notes
Broker
## Id
TMSSalesAgreement_BrokerCode General
Look-
up
Broker ID field, which is
currently on the SO Header
form.
(TMSSalesTable_BrokerCode)


5.1.3 Packing Slip Journal Form
The Broker ID field should also be added on to the Packing Slip Journal form as shown below. This
field will be shown on Posted Packing Slip Journal and will be un-editable on this form. The data on
this field will be shown when the sales order packing slip is posted.

|    | Existing or New?   |    | Existing         | None                                                      |
|:---|:-------------------|:---|:-----------------|:----------------------------------------------------------|
|    | Form Name          |    |                  | Sales Agreements Header Form                              |
|    | Form Label         |    | Sales Agreements |                                                           |
|    | Navigation Path    |    |                  | Sales and Marketing > Sales Agreements > Sales Agreements |

|        | Field   |    | Control Name                 | Fast Tab   |       | Field   |    | Notes   | Notes                      |
|:-------|:--------|:---|:-----------------------------|:-----------|:------|:--------|:---|:--------|:---------------------------|
|        | Name    |    |                              |            |       | Type    |    |         |                            |
| Broker | Broker  |    | TMSSalesAgreement_BrokerCode | General    | Look- | Look-   |    |         | Broker ID field, which is  |
| ID     |         |    |                              |            | up    |         |    |         |                            |
|        | ID      |    |                              |            |       | up      |    |         | currently on the SO Header |
|        |         |    |                              |            |       |         |    |         | form.                      |
|        |         |    |                              |            |       |         |    |         | (TMSSalesTable_BrokerCode) |

![Image](images/image6.jpeg)

![Image](images/image7.png)

---

<!-- Page 12 -->
10 | 22 | P a g e



Existing or New?
Existing
Form Name
Packing Slip Journal Form
Form Label
Packing Slip Journal
Navigation Path
Sales and Marketing > Sales Orders > All Sales Orders

Field Name
Control Name
Fast Tab
Field
Type
Notes
Broker ID
TMSSalesTable_BrokerCode Order Tracking  Look-up
Once Packing Slip is
posted for a SO, Broker
ID field should show on
the Posted Packing Slip
Journal.


5.2
## Modification To Tables
5.2.1 Customer Table

Existing or New?
Existing
Table Name
CustTable

|    | Existing or New?   |    | Existing             | None                                                  |
|:---|:-------------------|:---|:---------------------|:------------------------------------------------------|
|    | Form Name          |    |                      | Packing Slip Journal Form                             |
|    | Form Label         |    | Packing Slip Journal |                                                       |
|    | Navigation Path    |    |                      | Sales and Marketing > Sales Orders > All Sales Orders |

| Field Name   | Control Name             | Fast Tab       |         | Field   |    | Notes   | Notes                   |
|:-------------|:-------------------------|:---------------|:--------|:--------|:---|:--------|:------------------------|
|              |                          |                |         | Type    |    |         |                         |
| Broker ID    | TMSSalesTable_BrokerCode | Order Tracking | Look-up | Look-up |    |         | Once Packing Slip is    |
|              |                          |                |         |         |    |         | posted for a SO, Broker |
|              |                          |                |         |         |    |         | ID field should show on |
|              |                          |                |         |         |    |         | the Posted Packing Slip |
|              |                          |                |         |         |    |         | Journal.                |

|    | Existing or New?   |    | Existing   | None      |
|:---|:-------------------|:---|:-----------|:----------|
|    | Table Name         |    |            | CustTable |

![Image](images/image8.png)

![Image](images/image9.png)

---

<!-- Page 13 -->
11 | 22 | P a g e

Shared Table
No

Field Name
Field Type
Size
Notes
Broker ID
(TMSCustTable_BrokerCode)
Look-up

Broker ID field, which is currently on
the SO Header form.
(TMSSalesTable_BrokerCode)






5.2.2 Sales Agreements

Existing or New?
Existing
Table Name
Sales Agreements
Form Label
Sales Agreements

Field Name
Field Type
Size
Notes
Broker ID
(TMSSalesAgreement_BrokerCode)
Look-up

Broker ID field which is currently
on the SO Header form.
(TMSSalesTable_BrokerCode)


5.2.3 Packing Slip
Existing or New?
Existing
Table Name
CustPackingSlipJour
Form Label
Packing Slip Journal

Field Name
Field Type
Size
Notes
Broker ID
(TMSSalesAgreement_BrokerCode)
Look-up

Broker ID field, which is currently
on the SO Header form.
(TMSSalesTable_BrokerCode)

|    | Shared Table   |    | No   |
|----|----------------|----|------|

|                           | Field Name                |    |         | Field Type   |    |    | Size   |    |    | Notes                                  |
|:--------------------------|:--------------------------|:---|:--------|:-------------|:---|:---|:-------|:---|:---|:---------------------------------------|
| Broker ID                 | Broker ID                 |    | Look-up | Look-up      |    |    |        |    |    | Broker ID field, which is currently on |
| (TMSCustTable_BrokerCode) |                           |    |         |              |    |    |        |    |    |                                        |
|                           | (TMSCustTable_BrokerCode) |    |         |              |    |    |        |    |    | the SO Header form.                    |
|                           |                           |    |         |              |    |    |        |    |    | (TMSSalesTable_BrokerCode)             |

|    | Existing or New?   |    | Existing         | None             |
|:---|:-------------------|:---|:-----------------|:-----------------|
|    | Table Name         |    |                  | Sales Agreements |
|    | Form Label         |    | Sales Agreements |                  |

|                                | Field Name                     |    |         | Field Type   |    |    | Size   |    |    | Notes                              |
|:-------------------------------|:-------------------------------|:---|:--------|:-------------|:---|:---|:-------|:---|:---|:-----------------------------------|
| Broker ID                      | Broker ID                      |    | Look-up | Look-up      |    |    |        |    |    | Broker ID field which is currently |
| (TMSSalesAgreement_BrokerCode) |                                |    |         |              |    |    |        |    |    |                                    |
|                                | (TMSSalesAgreement_BrokerCode) |    |         |              |    |    |        |    |    | on the SO Header form.             |
|                                |                                |    |         |              |    |    |        |    |    | (TMSSalesTable_BrokerCode)         |

|    | Existing or New?   |    | Existing             | None                |
|:---|:-------------------|:---|:---------------------|:--------------------|
|    | Table Name         |    |                      | CustPackingSlipJour |
|    | Form Label         |    | Packing Slip Journal |                     |

|                                | Field Name                     |    |         | Field Type   |    |    | Size   |    |    | Notes                               |
|:-------------------------------|:-------------------------------|:---|:--------|:-------------|:---|:---|:-------|:---|:---|:------------------------------------|
| Broker ID                      | Broker ID                      |    | Look-up | Look-up      |    |    |        |    |    | Broker ID field, which is currently |
| (TMSSalesAgreement_BrokerCode) |                                |    |         |              |    |    |        |    |    |                                     |
|                                | (TMSSalesAgreement_BrokerCode) |    |         |              |    |    |        |    |    | on the SO Header form.              |
|                                |                                |    |         |              |    |    |        |    |    | (TMSSalesTable_BrokerCode)          |

---

<!-- Page 14 -->
12 | 22 | P a g e




5.3
## Modification To Business Logic
In case a Sales Order is being created using a Release Order from a Sales Agreement, the customs
broker field will need to flow down from the Sales Agreement form to the Sales Order form as shown
below:

![Image](images/image10.png)

![Image](images/image11.png)

![Image](images/image12.png)

![Image](images/image13.png)

---

<!-- Page 15 -->
13 | 22 | P a g e


The customs broker field should populate from the Customer Master table/form to the sales order
header form as soon as a sales order is created for a customer in D365. This is applicable for cases in
which a sales order is created directly for a customer and no valid sales agreement exist for customer
in the system:

![Image](images/image14.jpeg)

![Image](images/image15.png)

![Image](images/image16.png)

![Image](images/image17.png)

---

<!-- Page 16 -->
14 | 22 | P a g e

The Broker ID field should also be added to the Posted Packing Slip Journal form. When the sales
order packing slip is posted, the information from the sales order form should go to the order
tracking section of the posted Packing slip journal form as shown below:



Existing or New?
Existing
Table Name
CustPackingSlipJour
Form Label
Packing Slip Journal

Field Name
Control Name
Fast Tab
Field
Type
Notes
Broker ID
TMSSalesTable_BrokerCode Order Tracking  Look-up
Once Packing Slip is
posted for a SO, Broker
ID field should show on
the Posted Packing Slip
Journal.

|    | Existing or New?   |    | Existing             | None                |
|:---|:-------------------|:---|:---------------------|:--------------------|
|    | Table Name         |    |                      | CustPackingSlipJour |
|    | Form Label         |    | Packing Slip Journal |                     |

| Field Name   | Control Name             | Fast Tab       |         | Field   |    | Notes   | Notes                   |
|:-------------|:-------------------------|:---------------|:--------|:--------|:---|:--------|:------------------------|
|              |                          |                |         | Type    |    |         |                         |
| Broker ID    | TMSSalesTable_BrokerCode | Order Tracking | Look-up | Look-up |    |         | Once Packing Slip is    |
|              |                          |                |         |         |    |         | posted for a SO, Broker |
|              |                          |                |         |         |    |         | ID field should show on |
|              |                          |                |         |         |    |         | the Posted Packing Slip |
|              |                          |                |         |         |    |         | Journal.                |

![Image](images/image18.png)

![Image](images/image19.png)

---

<!-- Page 17 -->
15 | 22 | P a g e

5.4
## Modification To List Pages
It should be possible to add the Broker ID field on the list pages of Sales Agreements and Sales
Orders. This is required to ensure that data can be filtered in different ways by using Broker ID field.

The list pages would then subsequently be used to create Tiles and should be able to be placed on
different workspaces in D365 by individual users.

5.4.1 Sales Agreement List Page
The Broker ID field should be added to the Sales Agreements List Page. It should be possible to use
this field to filter and sort data in this form. It should also be possible to use this field for the
purpose of creating a Tile and place it on any appropriate workspace in D365 by the user:



Existing or New?
Existing
List Page Name
Sales Agreements
Navigation Path
Sales and Marketing > Sales Agreements > Sales Agreements

Field Name
Control Name
Field
Type
Notes
SalesAgreementListPage TMSSalesAgreement_BrokerCode Look-
up
Broker ID field, which is
currently on the SO Header
form.
(TMSSalesTable_BrokerCode)

5.4.2 Sales Orders List Page
The Broker ID field should be added to the Sales Orders List Page. It should be possible to use this
field to filter and sort data in this form. It should also be possible to use this field for the purpose of
creating a Tile and place it on any appropriate workspace in D365 by the user:

|    | Existing or New?   |    | Existing                                                  | None             | None   |
|:---|:-------------------|:---|:----------------------------------------------------------|:-----------------|:-------|
|    | List Page Name     |    |                                                           | Sales Agreements |        |
|    | Navigation Path    |    | Sales and Marketing > Sales Agreements > Sales Agreements |                  |        |

| Field Name             | Control Name                 |       | Field   |    | Notes   | None                       | None   |
|:-----------------------|:-----------------------------|:------|:--------|:---|:--------|:---------------------------|:-------|
|                        |                              |       | Type    |    |         |                            |        |
| SalesAgreementListPage | TMSSalesAgreement_BrokerCode | Look- | Look-   |    |         | Broker ID field, which is  |        |
|                        |                              | up    |         |    |         |                            |        |
|                        |                              |       | up      |    |         | currently on the SO Header |        |
|                        |                              |       |         |    |         | form.                      |        |
|                        |                              |       |         |    |         | (TMSSalesTable_BrokerCode) |        |

![Image](images/image20.png)

![Image](images/image21.png)

---

<!-- Page 18 -->
16 | 22 | P a g e



Existing or New?
Existing
List Page Name
All Sales Orders
Navigation Path
Sales and Marketing > Sales Orders > All Sales Orders

Field Name
Control Name
Field Type Notes
SalesTableListPage TMSSalesTable_BrokerCode Look-up
Broker ID field, which is currently
on the SO Header form.
(TMSSalesTable_BrokerCode)

|    | Existing or New?   |    | Existing                                              | None             |
|:---|:-------------------|:---|:------------------------------------------------------|:-----------------|
|    | List Page Name     |    |                                                       | All Sales Orders |
|    | Navigation Path    |    | Sales and Marketing > Sales Orders > All Sales Orders |                  |

|                    | Field Name         |    |                          | Control Name             |    |         | Field Type   |    |    | Notes                               |
|:-------------------|:-------------------|:---|:-------------------------|:-------------------------|:---|:--------|:-------------|:---|:---|:------------------------------------|
| SalesTableListPage | SalesTableListPage |    | TMSSalesTable_BrokerCode | TMSSalesTable_BrokerCode |    | Look-up | Look-up      |    |    | Broker ID field, which is currently |
|                    |                    |    |                          |                          |    |         |              |    |    | on the SO Header form.              |
|                    |                    |    |                          |                          |    |         |              |    |    | (TMSSalesTable_BrokerCode)          |

![Image](images/image22.png)

![Image](images/image23.png)

---

<!-- Page 19 -->
17 | 22 | P a g e

## 6 Configurations / Parameters / Security Considerations
6.1
## Shipping Carriers Form
The screenshot below shows the shipping carrier form and table. This is the same table where we will
be setting up Brokers as well. Just as in the example shown below, the
‘Mode’ field will be utilized to specify if the record in the table is a Broker or not:




Existing or New?
Existing
Form Name
TMSCarrier
Form Label
Shipping Carriers
Navigation Path
Inventory Management > Set up > Shipping Carriers > Shipping Carriers




6.1.1 Modifications to Parameter Forms
### This section is not applicable for this FDD.

6.1.2 Modifications to Parameter Table
### This section is not applicable for this FDD.

6.2
## Security Role Considerations
### This section is not applicable for this FDD.

|    | Existing or New?   |    | Existing          | None                                                                  | None   |
|:---|:-------------------|:---|:------------------|:----------------------------------------------------------------------|:-------|
|    | Form Name          |    |                   | TMSCarrier                                                            |        |
|    | Form Label         |    | Shipping Carriers |                                                                       |        |
|    | Navigation Path    |    |                   | Inventory Management > Set up > Shipping Carriers > Shipping Carriers |        |

![Image](images/image24.png)

---

<!-- Page 20 -->
18 | 22 | P a g e

## 7 Error Handling

### This section is not applicable for this FDD.

Error #
Error Description
Infolog Error Message

|    | Error #   |    |    | Error Description   |    |    | Infolog Error Message   |    |
|:---|:----------|:---|:---|:--------------------|:---|:---|:------------------------|:---|
|    |           |    |    |                     |    |    |                         |    |

---

<!-- Page 21 -->
19 | 22 | P a g e

## 8 Test Cases

Given below are the Test Cases that are applicable for this FDD.

8.1
## Test Cases
## Vsts Id
Test Case Title
13860
Create a stand-alone sales order and enter a customs broker on the sales order
13863
Create SA with customs broker selected then create an SO off the SA then change the
customs broker on the SA and ensure that the existing SO doesn't change and that any
new SOs created have the updated customs broker value
13861
Edit the customs broker value on a sales agreement and a sales order and ensure it can
be edited or changed
13862
Ensure the customs broker field can be queried against and tiles created using a filter on
this field
13859
Enter a customs broker on an SA and then create an SO off of the SA to ensure the
customs broker defaults onto the SO

|       | VSTS ID   |    |                                                                                            | Test Case Title                                                                        |    |
|:------|:----------|:---|:-------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|:---|
|       | 13860     |    |                                                                                            | Create a stand-alone sales order and enter a customs broker on the sales order         |    |
| 13863 |           |    | Create SA with customs broker selected then create an SO off the SA then change the        |                                                                                        |    |
|       |           |    | customs broker on the SA and ensure that the existing SO doesn't change and that any       |                                                                                        |    |
|       |           |    | new SOs created have the updated customs broker value                                      |                                                                                        |    |
| 13861 |           |    |                                                                                            | Edit the customs broker value on a sales agreement and a sales order and ensure it can |    |
|       |           |    |                                                                                            | be edited or changed                                                                   |    |
| 13862 |           |    | Ensure the customs broker field can be queried against and tiles created using a filter on |                                                                                        |    |
|       |           |    | this field                                                                                 |                                                                                        |    |
| 13859 |           |    |                                                                                            | Enter a customs broker on an SA and then create an SO off of the SA to ensure the      |    |
|       |           |    |                                                                                            | customs broker defaults onto the SO                                                    |    |

---

<!-- Page 22 -->
20 | 22 | P a g e

## 9 Appendices

### This section is not applicable for this FDD.
