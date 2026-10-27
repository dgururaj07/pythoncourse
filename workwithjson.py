from pathlib import Path
import json

file_path = Path("data/invoice.json")
def load_invoices():
    with open(file_path, "r") as f:
        invoices = json.load(f)
    return invoices

invoices = load_invoices()

check_inv_id = 101

for index, existing_invoice in enumerate(invoices):
    print(index, existing_invoice["invoice_id"], existing_invoice["vendor"], existing_invoice["amount"], existing_invoice["status"])
    if existing_invoice["invoice_id"] == check_inv_id:
        print(f"Invoice ID {check_inv_id} exists. at index {index}.")
        break


print("Invoices loaded:",invoices)


# check_inv_id = 101

# found = False
# for invoice in invoices:
#     if invoice["invoice_id"] == check_inv_id:
#         found = True

# if found:
#     print(f"Invoice ID {check_inv_id} exists.")
# else:
#     print(f"Invoice ID {check_inv_id} not found.")




# invoice_id = 101


# for index, existing_invoice in enumerate(invoices):
#     print(index, existing_invoice["invoice_id"], existing_invoice["vendor"], existing_invoice["amount"], existing_invoice["status"])





    