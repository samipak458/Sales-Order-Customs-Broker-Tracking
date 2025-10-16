# User Training Guide - Sales Order Customs Broker Tracking

## Overview

This guide provides step-by-step instructions for end users on how to use the Sales Order Customs Broker Tracking functionality in Microsoft Dynamics 365.

## Target Audience

- Sales Representatives
- Sales Managers
- Customer Service Representatives
- Transportation Coordinators
- Warehouse Managers

## What is a Customs Broker?

A customs broker is a licensed professional who helps importers and exporters meet Federal requirements governing imports and exports. In LPA's Dynamics 365 system, you can assign a customs broker to customers to track who handles customs clearance for shipments.

## Key Concepts

### Broker Assignment Flow

1. **Customer Level:** Assign a default broker to customers who regularly need customs services
2. **Sales Agreement:** Broker defaults from customer, can be changed if needed
3. **Sales Order:** Broker defaults from customer or agreement, can be overridden
4. **Load:** Broker automatically transfers from sales order
5. **Packing Slip:** Broker information displays for reference

### Why Track Brokers?

- Ensures correct broker handles customs for each shipment
- Maintains compliance with export regulations
- Streamlines communication with customs brokers
- Provides audit trail for customs processes

## Section 1: Working with Customers

### 1.1 Assigning a Broker to a Customer

**When to do this:** Setting up a new export customer or updating existing customer

**Steps:**

1. **Navigate to Customers:**
   - Go to: Accounts receivable → Customers → All customers
   - Or search "All customers" in the navigation bar

2. **Open Customer Record:**
   - Click on existing customer account
   - Or click "New" to create new customer

3. **Locate Broker ID Field:**
   - Find the General or Transportation FastTab
   - Expand the FastTab if collapsed
   - Look for "Broker ID" field

4. **Select Broker:**
   - Click in the Broker ID field
   - Click the dropdown arrow or lookup button
   - Select the appropriate customs broker from the list
   - Example: Select "CB001 - International Customs Services"

5. **Save Customer:**
   - Click "Save" button on toolbar
   - Verify broker ID is saved and displays correctly

**Screenshot Location:** [Customer form with Broker ID field highlighted]

### 1.2 Viewing Customer's Broker

**When to do this:** Checking which broker is assigned to a customer

**Steps:**

1. Open customer record
2. View the Broker ID field
3. The broker code and name will display
4. To see full broker details, click the broker ID to navigate to carrier form

### 1.3 Changing a Customer's Broker

**When to do this:** Customer switches to different customs broker

**Steps:**

1. Open customer record
2. Click in Broker ID field
3. Select new broker from dropdown
4. Click "Save"
5. All future orders will use the new broker

**Important Notes:**
- Changing customer broker does NOT change existing orders
- Only new orders created after the change will use new broker
- You can manually update broker on existing orders if needed

## Section 2: Working with Sales Orders

### 2.1 Creating Sales Order with Broker

**When to do this:** Creating a new sales order for export customer

**Steps:**

1. **Create Sales Order:**
   - Go to: Sales and marketing → Sales orders → All sales orders
   - Click "New" to create new order

2. **Select Customer:**
   - In customer account field, enter or select customer
   - Press Tab or Enter to move to next field

3. **Verify Broker Defaulted:**
   - Check the General FastTab
   - Broker ID field should auto-populate from customer
   - Verify it shows the correct broker

4. **Continue with Order:**
   - Add order lines
   - Complete other order details
   - Save the order

**Screenshot Location:** [Sales order form with Broker ID defaulted]

### 2.2 Overriding Broker on Sales Order

**When to do this:** Customer requests different broker for specific order

**Steps:**

1. Create or open sales order
2. Locate Broker ID field in General FastTab
3. Click in the field
4. Select different broker from dropdown
5. Save the order

**Example Scenario:**
Customer usually uses CB001, but for a special shipment to Canada, they want to use CB002 (Canada specialist). You override the broker on this one order while keeping CB001 as the customer's default.

### 2.3 Creating Order Without Broker

**When to do this:** Domestic shipment that doesn't need customs broker

**Steps:**

1. Create sales order as normal
2. Broker ID field will be empty if customer has no default
3. Leave it empty for domestic shipments
4. Continue processing order normally

**Important:** Broker ID is NOT mandatory. It's only needed for shipments requiring customs clearance.

### 2.4 Viewing Broker on Existing Order

**When to do this:** Checking broker assignment on placed order

**Steps:**

1. Open sales order
2. View General FastTab
3. Broker ID displays with broker code and name
4. This tells you which broker to contact for this shipment

## Section 3: Working with Sales Agreements

### 3.1 Creating Agreement with Broker

**When to do this:** Setting up blanket order or sales agreement

**Steps:**

1. **Create Sales Agreement:**
   - Go to: Sales and marketing → Sales agreements → Sales agreements
   - Click "New"

2. **Select Customer:**
   - Enter customer account
   - Press Tab to move forward

3. **Verify Broker:**
   - Go to General FastTab
   - Broker ID should default from customer
   - Verify or change if needed

4. **Complete Agreement:**
   - Add agreement lines
   - Set up quantities and prices
   - Confirm and activate agreement

### 3.2 Releasing Orders from Agreement

**When to do this:** Creating sales order from active agreement

**Steps:**

1. Open sales agreement
2. Click "Create release order" button
3. New sales order is created
4. Broker ID automatically copies from agreement to order
5. You can still override broker on the order if needed

## Section 4: Working with Loads

### 4.1 Viewing Broker on Load

**When to do this:** Planning shipments and coordinating with brokers

**Steps:**

1. **Navigate to Loads:**
   - Go to: Warehouse management → Loads → All loads
   - Or Transportation management → Loads → Load planning workbench

2. **Open Load:**
   - Click on load number to open details

3. **View Broker:**
   - Check General FastTab
   - Broker ID shows the broker from sales order
   - This is the broker who will handle customs for this load

4. **Contact Broker:**
   - Use broker information to coordinate shipment
   - Provide load details to broker for customs documentation

### 4.2 Understanding Broker Transfer

**Automatic Transfer:**
- When sales order is confirmed, load is created
- Broker ID automatically transfers from order to load
- You don't need to manually enter it

**Manual Update:**
- If needed, you can change broker on load
- Click in Broker ID field
- Select different broker
- Save the load

## Section 5: Working with Packing Slips

### 5.1 Viewing Broker on Packing Slip

**When to do this:** Reviewing posted shipments and broker assignments

**Steps:**

1. **Navigate to Packing Slips:**
   - Go to: Accounts receivable → Inquiries and reports → Packing slip journal
   - Or from sales order, click Packing slip button

2. **Open Packing Slip:**
   - Click on packing slip number to view details

3. **View Broker:**
   - Check the details section
   - Broker ID displays (read-only)
   - This is historical record of broker for the shipment

**Important:** Broker on packing slip is read-only. It's a permanent record of which broker handled customs for that shipment.

## Section 6: Using List Pages and Filtering

### 6.1 Filtering Customers by Broker

**When to do this:** Finding all customers using specific broker

**Steps:**

1. Go to: Accounts receivable → Customers → All customers
2. Add Broker ID column (if not visible):
   - Right-click column header
   - Select "Add columns"
   - Check "Broker ID"
3. Click filter icon on Broker ID column
4. Select broker to filter by
5. List shows only customers using that broker

### 6.2 Filtering Sales Orders by Broker

**When to do this:** Reviewing all orders for specific broker

**Steps:**

1. Go to: Sales and marketing → Sales orders → All sales orders
2. Add Broker ID column if needed
3. Apply filter on Broker ID column
4. Select broker from filter dropdown
5. View all orders for that broker

### 6.3 Filtering Loads by Broker

**When to do this:** Coordinating multiple shipments with same broker

**Steps:**

1. Go to: Warehouse management → Loads → All loads
2. Add Broker ID column if needed
3. Filter by specific broker
4. View all loads requiring that broker's services

## Section 7: Common Scenarios

### Scenario 1: New Export Customer

**Situation:** Setting up a new customer in Mexico who will need customs broker

**Steps:**
1. Create new customer account
2. Assign Broker ID: CB003 (Mexico specialist)
3. Save customer
4. Create first sales order
5. Verify broker defaults to CB003
6. Process order normally

### Scenario 2: Customer Changes Broker

**Situation:** Customer switches from CB001 to CB002 effective next month

**Steps:**
1. Wait until cutoff date
2. Open customer record
3. Change Broker ID from CB001 to CB002
4. Save customer
5. All new orders will use CB002
6. Existing orders keep CB001

### Scenario 3: Special Order Different Broker

**Situation:** Regular customer needs different broker for one specific order

**Steps:**
1. Create sales order for customer
2. Note default broker from customer
3. Override broker on this order only
4. Complete order with special broker
5. Next order will default back to customer's normal broker

### Scenario 4: Urgent Shipment Coordination

**Situation:** Need to contact broker about urgent shipment

**Steps:**
1. Find the sales order or load number
2. Open the order/load
3. Note the Broker ID
4. Navigate to broker record (click Broker ID)
5. View contact information
6. Call or email broker with shipment details

## Section 8: Tips and Best Practices

### For Sales Representatives

✓ **DO:**
- Verify broker defaults correctly when creating export orders
- Confirm with customer if broker needs to be different
- Leave broker blank for domestic-only shipments
- Update customer's default broker when they switch brokers

✗ **DON'T:**
- Don't remove broker from export orders without checking customer
- Don't override broker without reason
- Don't forget to verify broker on rush/special orders

### For Customer Service

✓ **DO:**
- Keep customer broker assignments up to date
- Communicate broker changes to transportation team
- Document reason for any broker overrides

✗ **DON'T:**
- Don't change customer's default broker without approval
- Don't assume all customers need brokers

### For Transportation Coordinators

✓ **DO:**
- Review broker on loads before shipment
- Coordinate with correct broker for each load
- Verify broker information is accurate
- Filter loads by broker for efficient communication

✗ **DON'T:**
- Don't ship without verifying broker on export loads
- Don't change broker on load without checking sales order

## Section 9: Troubleshooting

### Problem: Broker not defaulting to sales order

**Possible Causes:**
- Customer doesn't have broker assigned
- System error

**Solutions:**
1. Check customer record for Broker ID
2. If missing, assign broker to customer
3. If present, manually select on order
4. Contact IT if problem persists

### Problem: Cannot save order with broker

**Possible Cause:**
- Invalid broker ID entered

**Solution:**
1. Use lookup button to select broker
2. Don't type broker ID manually
3. Verify broker exists in system

### Problem: Wrong broker on load

**Possible Cause:**
- Broker was changed on order after load created

**Solution:**
1. Update broker on load to match order
2. Notify transportation team of change
3. Contact correct broker

### Problem: Cannot find Broker ID field

**Possible Cause:**
- Field not visible in your form view

**Solution:**
1. Check General or Transportation FastTab
2. Expand all FastTabs
3. Contact administrator if still not visible
4. You may need security permissions

## Section 10: Getting Help

### Internal Support

**For system issues:**
- Contact IT Help Desk
- Reference: SCM0603 Broker Tracking

**For business questions:**
- Contact your supervisor
- Contact Sales Manager

**For broker-related questions:**
- Contact Transportation Department
- Contact specific broker directly

### Documentation References

- Configuration Guide (for administrators)
- Technical Specification (for IT staff)
- FDD SCM0603 V2.0 (for detailed requirements)

## Quick Reference Card

### Key Fields Location

| Where | Field Location |
|-------|---------------|
| Customer | General FastTab → Broker ID |
| Sales Agreement | General FastTab → Broker ID |
| Sales Order | General FastTab (Header) → Broker ID |
| Load | General FastTab → Broker ID |
| Packing Slip | Details → Broker ID (read-only) |

### Key Navigation Paths

| Function | Path |
|----------|------|
| Customer List | Accounts receivable → Customers → All customers |
| Sales Orders | Sales and marketing → Sales orders → All sales orders |
| Sales Agreements | Sales and marketing → Sales agreements → Sales agreements |
| Loads | Warehouse management → Loads → All loads |
| Packing Slips | Accounts receivable → Inquiries and reports → Packing slip journal |
| Shipping Carriers | Transportation management → Setup → General → Shipping carriers |

### Remember

- Broker ID is OPTIONAL
- Always defaults from customer
- Can be overridden on orders
- Transfers automatically to loads
- Read-only on packing slips

---

**End of User Training Guide**

For questions or clarification, contact your system administrator or supervisor.
