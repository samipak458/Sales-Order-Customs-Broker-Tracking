# Sales Order Customs Broker Tracking - Configuration Guide

## Overview
This guide provides step-by-step instructions for configuring the Sales Order Customs Broker Tracking functionality in Microsoft Dynamics 365 Finance and Operations.

## Configuration Steps

### 1. Setup Customs Brokers in Shipping Carriers

#### Navigation Path
Transportation management → Setup → General → Shipping carriers

#### Steps to Create Customs Broker Records

1. **Open Shipping Carriers Form:**
   - Navigate to: Transportation management → Setup → General → Shipping carriers
   - Click "New" to create a new record

2. **Enter Broker Details:**
   - **Shipping carrier:** Enter unique broker ID (e.g., "CB001", "BROKER1")
   - **Name:** Enter the full name of the customs broker company
   - **Mode:** Select appropriate mode to identify as customs broker
   - **Carrier service:** Optional - specify service level if applicable

3. **Configure Additional Information:**
   - **Contact information:** Add phone, email, address
   - **Operating parameters:** Set up as needed for broker operations
   - **Rating profile:** Configure if using transportation rating

4. **Save the Record:**
   - Click "Save" to create the broker record
   - Repeat for all customs brokers your organization uses

5. **Verify Broker Setup:**
   - Confirm broker appears in lookup lists
   - Test selection on Customer form

#### Example Broker Configuration

| Shipping Carrier | Name | Mode | Contact |
|------------------|------|------|---------|
| CB001 | International Customs Services | Air | customs@ics.com |
| CB002 | Global Freight Brokers | Ocean | info@gfb.com |
| CB003 | Express Border Solutions | Ground | contact@ebs.com |

### 2. Configure Customer Master Records

#### Navigation Path
Accounts receivable → Customers → All customers

#### Steps to Assign Broker to Customer

1. **Open Customer Form:**
   - Navigate to: Accounts receivable → Customers → All customers
   - Select an existing customer or create new

2. **Navigate to General FastTab:**
   - Expand the General FastTab (or Transportation FastTab depending on form layout)

3. **Assign Broker ID:**
   - Locate the "Broker ID" field
   - Click the dropdown/lookup button
   - Select the appropriate customs broker from the list
   - The lookup will display all shipping carriers configured as brokers

4. **Save Customer Record:**
   - Click "Save" to persist the broker assignment

5. **Verify Assignment:**
   - Confirm Broker ID is saved
   - Check that the broker name displays correctly

#### When to Assign Broker to Customer

- **Export Customers:** Assign broker to customers that ship internationally
- **Domestic Customers:** Broker ID is optional for domestic-only customers
- **Special Requirements:** Assign based on customer-specific contractual requirements

### 3. Configure Sales Agreements

#### Navigation Path
Sales and marketing → Sales agreements → Sales agreements

#### Steps to Assign Broker to Sales Agreement

1. **Create or Open Sales Agreement:**
   - Navigate to: Sales and marketing → Sales agreements → Sales agreements
   - Create new agreement or open existing

2. **Locate Broker ID Field:**
   - Go to General FastTab
   - Find "Broker ID" field

3. **Assign Broker:**
   - **Automatic:** If creating from customer, Broker ID defaults from customer
   - **Manual:** Use lookup to select or change broker
   - **Override:** Can override customer default if needed

4. **Complete Agreement Setup:**
   - Configure other agreement parameters
   - Save the agreement

5. **Verify Defaulting:**
   - Create sales order from agreement
   - Verify Broker ID transfers to sales order

### 4. Configure Security Roles and Permissions

#### Navigation Path
System administration → Security → Security configuration

#### Required Privileges

**Sales Manager Role:**
- Read/Write access to Customer.BrokerId
- Read/Write access to SalesTable.BrokerId
- Read/Write access to SalesAgreementHeader.BrokerId

**Sales Representative Role:**
- Read access to Customer.BrokerId
- Read/Write access to SalesTable.BrokerId
- Read access to SalesAgreementHeader.BrokerId

**Transportation Coordinator Role:**
- Read/Write access to WHSLoadTable.BrokerId
- Read access to SalesTable.BrokerId

**Warehouse Manager Role:**
- Read access to all Broker ID fields

#### Steps to Configure Security

1. **Review Existing Roles:**
   - Navigate to: System administration → Security → Security configuration
   - Review roles that need broker access

2. **Assign Privileges:**
   - The extension automatically inherits security from base tables
   - No additional security configuration typically needed

3. **Test Access:**
   - Log in with different user roles
   - Verify appropriate read/write access to Broker ID fields

4. **Document Assignments:**
   - Maintain record of which roles can modify broker information
   - Update security documentation

### 5. List Page Configuration

#### Customer List Page

1. **Navigate to:** Accounts receivable → Customers → All customers
2. **Add Broker ID Column:**
   - Right-click on column header
   - Select "Add columns"
   - Find and add "Broker ID"
3. **Enable Filtering:**
   - Click filter icon on Broker ID column
   - Verify filtering works correctly
4. **Save Personalization:**
   - Save view for future use

#### Sales Order List Page

1. **Navigate to:** Sales and marketing → Sales orders → All sales orders
2. **Add Broker ID Column:**
   - Right-click on column header
   - Select "Add columns"
   - Find and add "Broker ID"
3. **Configure Sorting:**
   - Click column header to sort by Broker ID
   - Verify sorting works correctly

#### Load List Page

1. **Navigate to:** Warehouse management → Loads → All loads
2. **Add Broker ID Column:**
   - Right-click on column header
   - Select "Add columns"
   - Find and add "Broker ID"
3. **Test Filtering:**
   - Apply filter to show loads for specific broker
   - Verify results are accurate

### 6. Workspace Configuration (Optional)

#### Creating Broker-Specific Tiles

1. **Navigate to Workspace:**
   - Go to Sales or Transportation workspace

2. **Add Tile:**
   - Click "Add tile" or "Personalize"
   - Create new tile with query

3. **Configure Query:**
   - Filter by specific Broker ID
   - Set count or summary as needed

4. **Position Tile:**
   - Arrange tile in workspace
   - Save workspace personalization

### 7. Data Validation Rules

#### Validation Points

1. **Customer Level:**
   - Broker ID must exist in TMSCarrier table
   - Broker record must be active

2. **Sales Order Level:**
   - Inherits from customer or agreement
   - Can be overridden by user
   - Must be valid broker if specified

3. **Load Level:**
   - Populated from sales order
   - Must match sales order broker

#### Testing Validation

1. **Test Invalid Broker:**
   - Try to enter non-existent broker ID
   - Verify error message displays
   - Confirm save is blocked

2. **Test Valid Broker:**
   - Enter valid broker ID
   - Verify save succeeds
   - Check data persists

### 8. Testing Configuration

#### End-to-End Test Scenario

1. **Setup Test Broker:**
   - Create test broker "TEST_BROKER"
   - Configure all required fields

2. **Create Test Customer:**
   - Create customer "CUST_001"
   - Assign "TEST_BROKER" as Broker ID
   - Save customer

3. **Create Sales Order:**
   - Create new sales order for "CUST_001"
   - Verify Broker ID defaults to "TEST_BROKER"
   - Add order lines
   - Save order

4. **Confirm and Create Load:**
   - Confirm sales order
   - Create load
   - Verify Broker ID transfers to load

5. **Generate Packing Slip:**
   - Process packing slip
   - Verify Broker ID appears on packing slip journal

6. **Verify List Pages:**
   - Check customer list page shows broker
   - Check sales order list page shows broker
   - Check load list page shows broker

#### Test with Sales Agreement

1. **Create Sales Agreement:**
   - Create agreement for "CUST_001"
   - Verify Broker ID defaults from customer
   - Save agreement

2. **Release Sales Order:**
   - Create release sales order from agreement
   - Verify Broker ID transfers to order
   - Complete order processing

## Best Practices

### Data Maintenance

1. **Regular Review:**
   - Review broker assignments quarterly
   - Update inactive brokers
   - Maintain accurate contact information

2. **Data Cleanup:**
   - Remove obsolete broker records
   - Update customer assignments as needed
   - Verify data integrity periodically

3. **Documentation:**
   - Maintain list of active brokers
   - Document broker responsibilities
   - Track broker assignment changes

### User Training

1. **Train Users On:**
   - How to assign brokers to customers
   - How to override broker on sales orders
   - How to verify broker information on loads
   - How to use list page filtering

2. **Provide Documentation:**
   - User guides for each role
   - Quick reference cards
   - Process flow diagrams

### Troubleshooting

**Issue:** Broker ID not defaulting to sales order
- **Check:** Verify customer has broker assigned
- **Check:** Verify initFromCustTable method is executing
- **Solution:** Review event log for errors

**Issue:** Cannot save invalid broker
- **Expected:** This is validation working correctly
- **Solution:** Select valid broker from lookup

**Issue:** Broker not appearing on packing slip
- **Check:** Verify broker on sales order
- **Check:** Verify broker on load
- **Solution:** Ensure data flows through confirmation process

## Configuration Checklist

After completing configuration, verify:

- [ ] Customs brokers created in Shipping Carriers
- [ ] Test customer assigned broker ID
- [ ] Broker ID defaults to sales order from customer
- [ ] Broker ID defaults to sales agreement from customer
- [ ] Broker ID defaults to sales order from agreement
- [ ] Broker ID transfers to load from sales order
- [ ] Broker ID appears on packing slip journal
- [ ] List pages show Broker ID column
- [ ] Filtering works on list pages
- [ ] Security roles configured appropriately
- [ ] Users trained on functionality
- [ ] End-to-end testing completed successfully

## Support

For configuration questions or issues:
- Reference FDD SCM0603 V2.0 for business requirements
- Contact system administrator
- Review deployment guide for technical details

---

**End of Configuration Guide**
