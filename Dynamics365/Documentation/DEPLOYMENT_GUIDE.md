# Sales Order Customs Broker Tracking - Deployment Guide

## Overview
This document provides deployment instructions for the Sales Order Customs Broker Tracking customization for Microsoft Dynamics 365 Finance and Operations.

## Prerequisites

### System Requirements
- Microsoft Dynamics 365 Finance and Operations (Version 10.0 or higher)
- Visual Studio with Dynamics 365 development tools
- Access to Dynamics 365 development environment
- Administrator privileges for deployment

### Required Modules
- Supply Chain Management
- Sales and Marketing
- Transportation Management
- Warehouse Management

## Package Contents

### 1. Extended Data Types (EDTs)
- **TMSBrokerId.xml** - Extended Data Type for Broker ID field

### 2. Table Extensions
- **CustTable_Extension.xml** - Customer table extension
- **SalesTable_Extension.xml** - Sales order table extension
- **SalesAgreementHeader_Extension.xml** - Sales agreement header extension
- **CustPackingSlipJour_Extension.xml** - Packing slip journal extension
- **WHSLoadTable_Extension.xml** - Load table extension

### 3. Form Extensions
- **CustTable_Extension.xml** - Customer form extension
- **SalesTable_Extension.xml** - Sales order form extension
- **SalesAgreement_Extension.xml** - Sales agreement form extension
- **CustPackingSlipJour_Extension.xml** - Packing slip journal form extension
- **WHSLoadTable_Extension.xml** - Load form extension

### 4. Business Logic Classes
- **CustTable_BrokerExtension.xpp** - Customer validation logic
- **SalesTable_BrokerExtension.xpp** - Sales order initialization and validation
- **SalesAgreementHeader_BrokerExtension.xpp** - Sales agreement initialization
- **WHSLoadTable_BrokerExtension.xpp** - Load initialization
- **CustPackingSlipJour_BrokerExtension.xpp** - Packing slip initialization

## Deployment Steps

### Step 1: Import Metadata to Visual Studio

1. Open Visual Studio with Dynamics 365 development tools
2. Create a new Dynamics 365 project:
   - File → New → Project
   - Select "Dynamics 365 for Finance and Operations"
   - Name: "SCM0603_BrokerTracking"

3. Import EDT:
   - Right-click project → Add → Existing Item
   - Navigate to `Dynamics365/Metadata/EDTs/`
   - Add TMSBrokerId.xml

4. Import Table Extensions:
   - Right-click project → Add → Existing Item
   - Navigate to `Dynamics365/Metadata/Tables/`
   - Add all table extension files

5. Import Form Extensions:
   - Right-click project → Add → Existing Item
   - Navigate to `Dynamics365/Metadata/Forms/`
   - Add all form extension files

6. Import Business Logic Classes:
   - Right-click project → Add → Existing Item
   - Navigate to `Dynamics365/Metadata/Classes/`
   - Add all .xpp class files

### Step 2: Build the Project

1. In Visual Studio, right-click on the project
2. Select "Build"
3. Review build output for any errors
4. Fix any compilation errors if they occur

### Step 3: Synchronize Database

1. In Visual Studio, go to Dynamics 365 menu
2. Select "Synchronize database"
3. Select the project or specific elements to synchronize
4. Click "Synchronize"
5. Wait for synchronization to complete
6. Review synchronization log for any errors

### Step 4: Create Deployable Package

1. Right-click on the project in Solution Explorer
2. Select "Create Deployable Package"
3. Choose output location for the package
4. Wait for package creation to complete
5. Package will be created as a .zip file

### Step 5: Deploy to Target Environment

#### For Development Environment:
- The changes are already deployed after synchronization

#### For UAT/Production Environment:
1. Navigate to Lifecycle Services (LCS)
2. Go to Asset Library
3. Upload the deployable package
4. Go to target environment
5. Click "Maintain" → "Apply updates"
6. Select the uploaded package
7. Follow the deployment wizard
8. Monitor deployment progress
9. Verify deployment completion

### Step 6: Post-Deployment Configuration

1. **Setup Customs Brokers:**
   - Navigate to: Transportation management → Setup → General → Shipping carriers
   - Create new records for customs brokers
   - Configure carrier details
   - Set appropriate Mode/Type to distinguish brokers from regular carriers

2. **Verify Security Roles:**
   - Navigate to: System administration → Security → Security configuration
   - Review roles and privileges
   - Ensure appropriate users have access to Broker ID fields

3. **Test Basic Functionality:**
   - Create a test customer with Broker ID
   - Create a test sales order
   - Verify Broker ID defaults from customer
   - Confirm sales order
   - Verify Broker ID appears on load

## Validation Checklist

After deployment, verify the following:

- [ ] EDT TMSBrokerId exists in the system
- [ ] BrokerId field appears on Customer form
- [ ] BrokerId field appears on Sales Order form
- [ ] BrokerId field appears on Sales Agreement form
- [ ] BrokerId field appears on Load form
- [ ] BrokerId field appears on Packing Slip Journal (read-only)
- [ ] Broker ID defaults from Customer to Sales Order
- [ ] Broker ID defaults from Customer to Sales Agreement
- [ ] Broker ID defaults from Sales Agreement to Sales Order
- [ ] Broker ID transfers from Sales Order to Load
- [ ] Broker ID appears on Packing Slip
- [ ] Validation works for invalid Broker IDs
- [ ] List pages display Broker ID column
- [ ] Filtering works on list pages

## Rollback Procedure

If issues occur and rollback is necessary:

### Development Environment:
1. Revert code changes in source control
2. Build and synchronize database
3. Database schema changes may need manual cleanup

### UAT/Production Environment:
1. In LCS, navigate to environment
2. Use environment restore feature
3. Restore from latest backup before deployment
4. Note: This will roll back ALL changes, not just this customization

## Troubleshooting

### Build Errors

**Issue:** EDT not found
- **Solution:** Ensure TMSBrokerId.xml is properly added to project

**Issue:** Table extension compilation errors
- **Solution:** Verify base tables exist in your environment version

**Issue:** Form extension errors
- **Solution:** Check that control names match the target form structure

### Synchronization Errors

**Issue:** Table synchronization fails
- **Solution:** Check for conflicting customizations on the same tables

**Issue:** Missing field after sync
- **Solution:** Re-sync specific table or full database sync

### Runtime Errors

**Issue:** Broker ID not appearing on forms
- **Solution:** Clear browser cache, refresh metadata

**Issue:** Validation errors
- **Solution:** Verify TMSCarrier table has appropriate records

**Issue:** Default logic not working
- **Solution:** Check that initFromCustTable methods are being called

## Support and Maintenance

### Regular Maintenance Tasks
- Monitor error logs for broker-related issues
- Review and update broker records as needed
- Validate data integrity quarterly
- Update documentation for any configuration changes

### Getting Help
For deployment issues:
1. Review deployment logs in LCS
2. Check Dynamics 365 trace logs
3. Contact Microsoft Support if needed
4. Reference FDD SCM0603 V2.0 for business requirements

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024 | Initial deployment |

## References

- FDD SCM0603 - Sales Order Customs Broker Tracking V2.0
- Microsoft Dynamics 365 Deployment Guide
- LCS Deployment Documentation

---

**End of Deployment Guide**
