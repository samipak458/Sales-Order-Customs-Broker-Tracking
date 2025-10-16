# Quick Start Guide - Developer Setup

## Overview

This guide will help developers quickly set up and deploy the Sales Order Customs Broker Tracking customization in a Microsoft Dynamics 365 development environment.

## Prerequisites Checklist

Before you begin, ensure you have:

- [ ] Microsoft Dynamics 365 Finance and Operations development environment
- [ ] Visual Studio with Dynamics 365 development tools installed
- [ ] Access to development environment with admin privileges
- [ ] Git repository cloned locally
- [ ] Dynamics 365 license and environment access

## Quick Start (15 Minutes)

### Step 1: Clone Repository (2 minutes)

```bash
git clone https://github.com/samipak458/Sales-Order-Customs-Broker-Tracking.git
cd Sales-Order-Customs-Broker-Tracking
```

### Step 2: Open Visual Studio (1 minute)

1. Launch Visual Studio with Dynamics 365 tools
2. Sign in with your credentials
3. Select File → New → Project

### Step 3: Create D365 Project (2 minutes)

1. Select **Dynamics 365** → **Dynamics 365 for Finance and Operations**
2. Project Name: `SCM0603_BrokerTracking`
3. Location: Your workspace folder
4. Click **Create**

### Step 4: Import Metadata Files (5 minutes)

#### Import EDT
1. Right-click project → **Add** → **Existing Item**
2. Navigate to: `Dynamics365/Metadata/EDTs/`
3. Select `TMSBrokerId.xml`
4. Click **Add**

#### Import Table Extensions
1. Right-click project → **Add** → **Existing Item**
2. Navigate to: `Dynamics365/Metadata/Tables/`
3. Select all XML files (5 files):
   - CustTable_Extension.xml
   - SalesTable_Extension.xml
   - SalesAgreementHeader_Extension.xml
   - WHSLoadTable_Extension.xml
   - CustPackingSlipJour_Extension.xml
4. Click **Add**

#### Import Form Extensions
1. Right-click project → **Add** → **Existing Item**
2. Navigate to: `Dynamics365/Metadata/Forms/`
3. Select all XML files (5 files):
   - CustTable_Extension.xml
   - SalesTable_Extension.xml
   - SalesAgreement_Extension.xml
   - WHSLoadTable_Extension.xml
   - CustPackingSlipJour_Extension.xml
4. Click **Add**

#### Import Business Logic Classes
1. Right-click project → **Add** → **Existing Item**
2. Navigate to: `Dynamics365/Metadata/Classes/`
3. Select all XPP files (5 files):
   - CustTable_BrokerExtension.xpp
   - SalesTable_BrokerExtension.xpp
   - SalesAgreementHeader_BrokerExtension.xpp
   - WHSLoadTable_BrokerExtension.xpp
   - CustPackingSlipJour_BrokerExtension.xpp
4. Click **Add**

### Step 5: Build Project (3 minutes)

1. Right-click project in Solution Explorer
2. Select **Build**
3. Wait for build to complete
4. Review Output window for any errors
5. ✅ **Expected:** 0 Errors, 0 Warnings

### Step 6: Synchronize Database (2 minutes)

1. In Visual Studio menu, select **Dynamics 365**
2. Click **Synchronize database**
3. Select your project or specific elements
4. Click **Synchronize**
5. Wait for completion
6. ✅ **Expected:** Sync successful, new fields added to tables

## Verify Installation

### Quick Verification (5 minutes)

1. **Open D365 Client:**
   - Navigate to your D365 environment URL
   - Log in with admin credentials

2. **Verify Customer Form:**
   - Go to: Accounts receivable → Customers → All customers
   - Open any customer
   - Look for "Broker ID" field in General FastTab
   - ✅ Field should be visible

3. **Verify Sales Order Form:**
   - Go to: Sales and marketing → Sales orders → All sales orders
   - Create new order or open existing
   - Look for "Broker ID" field in General FastTab
   - ✅ Field should be visible

4. **Test Basic Functionality:**
   - Create a test customer
   - Assign a broker (you may need to set up test broker first)
   - Create sales order for that customer
   - ✅ Broker should default to sales order

## Common Issues and Solutions

### Issue 1: Build Errors

**Error:** "Type TMSBrokerId not found"
**Solution:** 
- Ensure TMSBrokerId.xml is in project
- Build EDT first, then other elements
- Clean and rebuild project

### Issue 2: Sync Errors

**Error:** "Cannot synchronize database"
**Solution:**
- Check database connection
- Ensure you have admin rights
- Try sync specific table instead of full sync

### Issue 3: Fields Not Showing

**Error:** "Broker ID field not visible in forms"
**Solution:**
- Clear browser cache
- Refresh metadata: Dynamics 365 → Refresh metadata
- Restart IIS on dev environment

### Issue 4: Form Extension Errors

**Error:** "Control not found on target form"
**Solution:**
- Check that base forms exist in your environment
- Verify control names match your D365 version
- Review form extension XML structure

## Next Steps

After successful installation:

1. **Setup Test Data:**
   - Create test customs broker records
   - Create test customers with brokers
   - Create test sales orders

2. **Run Test Cases:**
   - Follow [Test Validation Scripts](TEST_VALIDATION_SCRIPTS.md)
   - Verify all 16 test cases pass

3. **Configure Security:**
   - Review security roles
   - Assign appropriate permissions
   - Test with different user roles

4. **Documentation:**
   - Read [Configuration Guide](CONFIGURATION_GUIDE.md)
   - Review [Technical Specification](TECHNICAL_SPECIFICATION.md)
   - Share [User Training Guide](USER_TRAINING_GUIDE.md) with end users

## Development Tips

### Code Organization

```
Project Structure:
SCM0603_BrokerTracking/
├── EDT/
│   └── TMSBrokerId
├── Table Extensions/
│   ├── CustTable_Extension
│   ├── SalesTable_Extension
│   ├── SalesAgreementHeader_Extension
│   ├── WHSLoadTable_Extension
│   └── CustPackingSlipJour_Extension
├── Form Extensions/
│   ├── CustTable_Extension
│   ├── SalesTable_Extension
│   ├── SalesAgreement_Extension
│   ├── WHSLoadTable_Extension
│   └── CustPackingSlipJour_Extension
└── Classes/
    ├── CustTable_BrokerExtension
    ├── SalesTable_BrokerExtension
    ├── SalesAgreementHeader_BrokerExtension
    ├── WHSLoadTable_BrokerExtension
    └── CustPackingSlipJour_BrokerExtension
```

### Debugging Tips

1. **Enable Debugging:**
   - Set breakpoints in X++ code
   - Use Debug → Attach to Process
   - Attach to w3wp.exe

2. **Check Event Log:**
   - Navigate to: System administration → Inquiries → Event log
   - Filter by "Broker" keyword
   - Review errors and warnings

3. **SQL Profiler:**
   - Use SQL Profiler to trace database calls
   - Verify foreign key constraints
   - Check data flow

### Best Practices

✅ **DO:**
- Always build before sync
- Test in dev environment first
- Keep backups before deployment
- Document any customizations
- Follow naming conventions

✗ **DON'T:**
- Don't modify base application code
- Don't skip testing
- Don't deploy without backup
- Don't ignore compiler warnings

## Create Deployable Package

When ready to deploy to UAT/Production:

1. **Create Package:**
   - Right-click project → Create Deployable Package
   - Choose output location
   - Wait for package creation
   - Package saved as .zip file

2. **Upload to LCS:**
   - Go to Lifecycle Services (LCS)
   - Navigate to Asset Library
   - Upload package
   - Add description and version info

3. **Deploy:**
   - Go to target environment
   - Select Maintain → Apply updates
   - Choose your package
   - Follow deployment wizard

## Additional Resources

### Documentation
- [Deployment Guide](DEPLOYMENT_GUIDE.md) - Full deployment instructions
- [Configuration Guide](CONFIGURATION_GUIDE.md) - System configuration
- [Technical Specification](TECHNICAL_SPECIFICATION.md) - Technical details
- [Architecture Diagrams](ARCHITECTURE_DIAGRAMS.md) - Visual architecture

### Microsoft Resources
- [D365 Development Home](https://docs.microsoft.com/dynamics365/fin-ops-core/dev-itpro/dev-tools/developer-home-page)
- [Extension Best Practices](https://docs.microsoft.com/dynamics365/fin-ops-core/dev-itpro/extensibility/extensibility-home-page)
- [Visual Studio Development](https://docs.microsoft.com/dynamics365/fin-ops-core/dev-itpro/dev-tools/development-tools-overview)

### Support
- Review GitHub issues for known problems
- Contact project team for assistance
- Reference FDD SCM0603 V2.0 for requirements

## Checklist

Use this checklist to ensure complete setup:

- [ ] Repository cloned
- [ ] Visual Studio project created
- [ ] EDT imported and built
- [ ] Table extensions imported and built
- [ ] Form extensions imported and built
- [ ] Business logic classes imported and built
- [ ] Database synchronized
- [ ] No build errors
- [ ] Broker ID field visible on Customer form
- [ ] Broker ID field visible on Sales Order form
- [ ] Basic functionality tested
- [ ] Test cases reviewed
- [ ] Documentation read

## Time Estimate

| Task | Estimated Time |
|------|----------------|
| Clone repository | 2 minutes |
| Create project | 2 minutes |
| Import metadata | 5 minutes |
| Build project | 3 minutes |
| Sync database | 2 minutes |
| Verify installation | 5 minutes |
| **Total** | **~20 minutes** |

## Success Criteria

✅ You've successfully set up the customization when:
- All files imported without errors
- Project builds with 0 errors
- Database sync completes successfully
- Broker ID fields visible in forms
- Basic defaulting works (customer to sales order)
- No runtime errors in event log

---

**Ready to Deploy?** 
Proceed to [Deployment Guide](DEPLOYMENT_GUIDE.md) for UAT/Production deployment instructions.

**Need Help?**
Review [Technical Specification](TECHNICAL_SPECIFICATION.md) or contact the development team.

---

**Last Updated:** 2024
**Version:** 1.0
**Status:** Production Ready ✅
