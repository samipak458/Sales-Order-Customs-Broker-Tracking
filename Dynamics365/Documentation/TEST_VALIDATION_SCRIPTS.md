# Sales Order Customs Broker Tracking - Test Validation Scripts

## Overview
This document provides test scripts to validate the Sales Order Customs Broker Tracking functionality.

## Test Environment Setup

### Prerequisites
- Dynamics 365 environment with customization deployed
- Test user accounts with appropriate permissions
- Sample customs broker records created
- Test customer accounts available

### Test Data Setup

```sql
-- Create test broker in TMSCarrier table
-- This would typically be done through the UI
-- Shipping Carrier: TEST_BROKER_001
-- Name: Test Customs Broker Inc.
-- Mode: Appropriate mode for customs broker

-- Create test customer
-- Customer Account: CUST_TEST_001
-- Name: Test Customer for Broker Validation
```

## Test Case 1: Customer Broker Assignment

### TC001: Create Customer with Broker ID

**Objective:** Verify that a customs broker can be assigned to a customer

**Steps:**
1. Navigate to: Accounts receivable → Customers → All customers
2. Click "New" to create new customer
3. Enter customer details:
   - Account: CUST_TEST_001
   - Name: Test Customer for Broker
4. In General/Transportation FastTab:
   - Set Broker ID: TEST_BROKER_001
5. Click "Save"

**Expected Result:**
- Customer saves successfully
- Broker ID is persisted
- Broker name displays in lookup

**Validation Query:**
```sql
SELECT AccountNum, BrokerId
FROM CustTable
WHERE AccountNum = 'CUST_TEST_001'
-- Expected: BrokerId = 'TEST_BROKER_001'
```

**Pass/Fail:** ___________

---

### TC002: Validate Invalid Broker ID

**Objective:** Verify validation prevents invalid broker assignment

**Steps:**
1. Open customer CUST_TEST_001
2. Manually type invalid broker ID: "INVALID_BROKER"
3. Try to save the record

**Expected Result:**
- Validation error displays
- Error message: "Broker ID does not exist" or similar
- Record cannot be saved

**Pass/Fail:** ___________

---

## Test Case 2: Sales Order Broker Defaulting

### TC003: Broker Defaults from Customer to Sales Order

**Objective:** Verify Broker ID defaults from customer when creating sales order

**Steps:**
1. Navigate to: Sales and marketing → Sales orders → All sales orders
2. Click "New" to create sales order
3. Select customer: CUST_TEST_001
4. Tab out of customer field
5. Check Broker ID field

**Expected Result:**
- Broker ID automatically populates with TEST_BROKER_001
- Value matches customer's broker ID
- User can still override if needed

**Validation Query:**
```sql
SELECT SalesId, CustAccount, BrokerId
FROM SalesTable
WHERE CustAccount = 'CUST_TEST_001'
-- Expected: BrokerId = 'TEST_BROKER_001'
```

**Pass/Fail:** ___________

---

### TC004: Override Broker ID on Sales Order

**Objective:** Verify user can override broker on sales order

**Steps:**
1. Create new sales order for CUST_TEST_001
2. Note defaulted Broker ID: TEST_BROKER_001
3. Change Broker ID to different broker: TEST_BROKER_002
4. Save sales order

**Expected Result:**
- Sales order saves with new broker ID
- Override persists
- No validation errors (assuming TEST_BROKER_002 exists)

**Validation Query:**
```sql
SELECT SalesId, CustAccount, BrokerId
FROM SalesTable
WHERE SalesId = 'SO_TEST_001'
-- Expected: BrokerId = 'TEST_BROKER_002'
```

**Pass/Fail:** ___________

---

## Test Case 3: Sales Agreement Broker Flow

### TC005: Broker Defaults to Sales Agreement

**Objective:** Verify Broker ID defaults from customer to sales agreement

**Steps:**
1. Navigate to: Sales and marketing → Sales agreements → Sales agreements
2. Click "New"
3. Select customer: CUST_TEST_001
4. Check Broker ID in General FastTab

**Expected Result:**
- Broker ID defaults from customer
- Shows TEST_BROKER_001

**Validation Query:**
```sql
SELECT AgreementHeaderRecId, CustAccount, BrokerId
FROM SalesAgreementHeader
WHERE CustAccount = 'CUST_TEST_001'
-- Expected: BrokerId = 'TEST_BROKER_001'
```

**Pass/Fail:** ___________

---

### TC006: Broker Transfers from Agreement to Sales Order

**Objective:** Verify Broker ID transfers when releasing sales order from agreement

**Steps:**
1. Create sales agreement for CUST_TEST_001 with broker TEST_BROKER_001
2. Add agreement line
3. Confirm agreement
4. Release sales order from agreement
5. Check Broker ID on created sales order

**Expected Result:**
- Sales order inherits broker from agreement
- Broker ID = TEST_BROKER_001

**Pass/Fail:** ___________

---

## Test Case 4: Load Broker Transfer

### TC007: Broker Transfers to Load

**Objective:** Verify Broker ID transfers from sales order to load

**Steps:**
1. Create sales order with Broker ID: TEST_BROKER_001
2. Add order lines (ensure items are warehouse-enabled)
3. Confirm sales order
4. Create load for the order
5. Check Broker ID on load

**Expected Result:**
- Load inherits Broker ID from sales order
- Load.BrokerId = TEST_BROKER_001

**Validation Query:**
```sql
SELECT LoadId, BrokerId
FROM WHSLoadTable
WHERE LoadId = 'LOAD_TEST_001'
-- Expected: BrokerId = 'TEST_BROKER_001'
```

**Pass/Fail:** ___________

---

## Test Case 5: Packing Slip Broker Display

### TC008: Broker Appears on Packing Slip Journal

**Objective:** Verify Broker ID appears on posted packing slip

**Steps:**
1. Create and confirm sales order with Broker ID
2. Pick and ship the order
3. Post packing slip
4. Navigate to packing slip journal
5. Open posted packing slip record
6. Verify Broker ID field

**Expected Result:**
- Broker ID displays on packing slip journal
- Field is read-only
- Value matches sales order broker

**Validation Query:**
```sql
SELECT PackingSlipId, BrokerId
FROM CustPackingSlipJour
WHERE PackingSlipId = 'PS_TEST_001'
-- Expected: BrokerId = 'TEST_BROKER_001'
```

**Pass/Fail:** ___________

---

## Test Case 6: List Page Functionality

### TC009: Customer List Page Shows Broker

**Objective:** Verify Broker ID column appears on customer list page

**Steps:**
1. Navigate to: Accounts receivable → Customers → All customers
2. Add Broker ID column to grid (if not visible)
3. Locate CUST_TEST_001
4. Check Broker ID column value

**Expected Result:**
- Broker ID column displays
- Shows TEST_BROKER_001 for CUST_TEST_001
- Column is sortable and filterable

**Pass/Fail:** ___________

---

### TC010: Filter Sales Orders by Broker

**Objective:** Verify filtering works on sales order list page

**Steps:**
1. Navigate to: Sales and marketing → Sales orders → All sales orders
2. Add Broker ID column to grid
3. Apply filter: Broker ID = TEST_BROKER_001
4. Review filtered results

**Expected Result:**
- Only sales orders with TEST_BROKER_001 display
- Filter functions correctly
- Can clear filter to see all orders

**Pass/Fail:** ___________

---

### TC011: Sort Loads by Broker

**Objective:** Verify sorting works on load list page

**Steps:**
1. Navigate to: Warehouse management → Loads → All loads
2. Add Broker ID column to grid
3. Click Broker ID column header to sort
4. Review sort order

**Expected Result:**
- Loads sort alphabetically by broker ID
- Ascending/descending toggle works
- Null values handled appropriately

**Pass/Fail:** ___________

---

## Test Case 7: Validation Rules

### TC012: Prevent Save with Invalid Broker

**Objective:** Verify validation prevents saving invalid broker reference

**Steps:**
1. Open customer form
2. Enter Broker ID: FAKE_BROKER_999 (non-existent)
3. Try to save

**Expected Result:**
- Validation error occurs
- Error message displayed
- Save is blocked

**Pass/Fail:** ___________

---

### TC013: Allow Save with Empty Broker

**Objective:** Verify broker is not mandatory (per FDD assumptions)

**Steps:**
1. Create new customer
2. Leave Broker ID blank
3. Save customer

**Expected Result:**
- Customer saves successfully
- Broker ID remains blank
- No validation errors

**Pass/Fail:** ___________

---

## Test Case 8: Data Flow Integration

### TC014: End-to-End Data Flow

**Objective:** Verify complete broker tracking from customer through packing slip

**Steps:**
1. Create customer with broker: TEST_BROKER_001
2. Create sales order - verify broker defaults
3. Confirm sales order
4. Create and confirm load - verify broker transfers
5. Pick items
6. Post packing slip - verify broker appears

**Expected Result:**
- Broker ID flows through entire process
- Data consistency maintained
- All lookups and displays work correctly

**Validation Queries:**
```sql
-- Verify customer
SELECT AccountNum, BrokerId FROM CustTable WHERE AccountNum = 'CUST_TEST_001'

-- Verify sales order
SELECT SalesId, BrokerId FROM SalesTable WHERE CustAccount = 'CUST_TEST_001'

-- Verify load
SELECT LoadId, BrokerId FROM WHSLoadTable 
WHERE LoadId IN (SELECT LoadId FROM WHSLoadLine WHERE SalesId = 'SO_TEST_001')

-- Verify packing slip
SELECT PackingSlipId, BrokerId FROM CustPackingSlipJour WHERE SalesId = 'SO_TEST_001'
```

**Pass/Fail:** ___________

---

## Test Case 9: Security and Permissions

### TC015: Read-Only Access

**Objective:** Verify users with read-only access cannot modify broker

**Steps:**
1. Login as user with read-only permissions
2. Open customer with broker ID
3. Try to change broker ID
4. Try to save

**Expected Result:**
- Field is read-only or save is blocked
- Appropriate permission error if attempted
- Data protection enforced

**Pass/Fail:** ___________

---

### TC016: Write Access

**Objective:** Verify users with write access can modify broker

**Steps:**
1. Login as sales manager or similar role
2. Open customer
3. Change broker ID
4. Save customer

**Expected Result:**
- Change is allowed
- Save succeeds
- Audit trail captured (if enabled)

**Pass/Fail:** ___________

---

## Test Summary

### Test Execution Summary

| Test Case | Description | Status | Notes |
|-----------|-------------|--------|-------|
| TC001 | Create Customer with Broker | | |
| TC002 | Validate Invalid Broker | | |
| TC003 | Broker Defaults to Sales Order | | |
| TC004 | Override Broker on Sales Order | | |
| TC005 | Broker Defaults to Agreement | | |
| TC006 | Broker from Agreement to Order | | |
| TC007 | Broker Transfers to Load | | |
| TC008 | Broker on Packing Slip | | |
| TC009 | Customer List Page Display | | |
| TC010 | Filter Sales Orders by Broker | | |
| TC011 | Sort Loads by Broker | | |
| TC012 | Prevent Invalid Broker Save | | |
| TC013 | Allow Empty Broker | | |
| TC014 | End-to-End Data Flow | | |
| TC015 | Read-Only Access | | |
| TC016 | Write Access | | |

### Overall Test Result

**Total Tests:** 16
**Passed:** ___________
**Failed:** ___________
**Blocked:** ___________

### Issues Identified

| Issue # | Description | Severity | Status |
|---------|-------------|----------|--------|
| | | | |

### Sign-Off

**Tested By:** _____________________ **Date:** __________

**Reviewed By:** ___________________ **Date:** __________

**Approved By:** ___________________ **Date:** __________

---

**End of Test Validation Scripts**
