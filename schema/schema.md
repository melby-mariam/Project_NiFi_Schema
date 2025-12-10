# File Schema

_Source PDF_: `schema.pdf`


10/12/2025, 10:56 ChoctawBirchstreetOut - Overview
ChoctawBirchstreetOut
Last updated by | Christopher Leva Harrington | 22 Jul 2025 at 00:09 GMT+5:30
File Integration ChoctawBirchstreetOut
Data Analyst @Christopher Leva Harrington
Status Completed
Contents
• Summary
• File Lineage Differences
• Legacy File Overview
• File Schema
Summary
ChoctawBirchstreetOut is an Analytic CSV file extended from the BirchStreetV2 map integrated in
Milestone 10 (See  79587BirchstreetV2 (Alcohol Invoices) Done ).
File Lineage Differences
If R_VENDOR_RETAILER.VENDOR_NAME_RETAILER is > null, then report value under col C as noted in
the file schema.
Else, follow AlternateVendorID
Else, VendorSysID
Legacy File Overview
Map Type: FA
Map ID: 999
Map Name: StandardAnalyticsDelimited
Map Description: Standard Analytics Delimited Datafeed
Map Alias: ChoctawBirchstreetOut
File Schema
https://dev.azure.com/FintechDevOps/Data Engineering/_wiki/wikis/Data-Engineering.wiki/4943/ChoctawBirchstreetOut 1/3



10/12/2025, 10:56 ChoctawBirchstreetOut - Overview
Column Output Header Table Column Name Da
VA
A VendorName r_company NAME
BY
VA
B RetailerName r_company NAME
BY
C RetailerVendorId R_VENDOR_RETAILER VENDOR_NAME_RETAILER NU
VA
D VendorStoreNumber a_edi_summary VENDOR_STORE_NUMBER
BY
VA
E RetailerStoreNumber a_edi_summary STORE_NUMBER
BY
F ProcessDateEFT a_eft_processed PROCESS_DATE DA
G InvoiceDate a_edi_summary INVOICE_DATE DA
H InvoiceDueDate a_edi_summary TERM_NET_DUE_DATE DA
VA
I InvoiceNumber a_edi_summary INVOICE_NUMBER
BY
J InvoiceAmount a_edi_summary INVOICE_TOTAL NU
K InvoiceItemCount a_edi_summary ITEM_COUNT NU
VA
L PONumber a_edi_summary PO_NUMBER
BY
M PODate a_edi_summary PO_DATE DA
VA
N ReferenceInvoiceNumber a_edi_summary REF_INVOICE_NUMBER
BY
VA
O ProductNumber a_edi_data PRODUCT_NUMBER
BY
P Quantity a_edi_data ITEM_QUANTITY NU
Q UnitCost a_edi_data QUANTITY_COST NU
VA
R UnitOfMeasure a_edi_data UNIT_OF_MEASURE
BY
S PacksPerCase master_catalog PACKS_PER_CASE NU
VA
T PackUPC Vendor_item_signature UPC_PACK_CODE
BY
https://dev.azure.com/FintechDevOps/Data Engineering/_wiki/wikis/Data-Engineering.wiki/4943/ChoctawBirchstreetOut 2/3



10/12/2025, 10:56 ChoctawBirchstreetOut - Overview
Column Output Header Table Column Name Da
VA
U CaseUPC Vendor_item_signature UPC_CASE_CODE
BY
VA
V ProductDescription master_catalog DISPLAY_NAME_DEFAULT
BY
W DiscountAdjustment Sac_Data DiscountAdjustment
X DepositAdjustment Sac_Data DepositAdjustment
Y MiscellaneousAdjustment Sac_Data MiscellaneousAdjustment
Z TaxAdjustment Sac_Data TaxAdjustment
AA DeliveryAdjustment Sac_Data DeliveryAdjustment
AB ExtendedPrice a_edi_data TOTAL_COST NU
VA
AC Manufacturer master_catalog MANUFACTURER_NAME
BY
AD UnitSize master_catalog UNIT_SIZE NU
AE UnitsPerCase **
VA
AF Dept retailer_product_catalog RETAILER_ITEM_NUMBER
BY
VA
AG GLCode retailer_product_catalog GL_CODE
BY
**UNITS_PER_CASE = PACKS_PER_CASE (master_catalog) * UNITS_PER_PACK
(Vendor_item_signature)
Dept - Uses the Retailer Item Number field from the Product Catalog.
https://dev.azure.com/FintechDevOps/Data Engineering/_wiki/wikis/Data-Engineering.wiki/4943/ChoctawBirchstreetOut 3/3


